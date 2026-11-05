import imaplib
import email
import re
import os
import sys
import sqlite3
from dotenv import load_dotenv

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv('ai_agents/.env')
user = os.getenv('GMAIL_USER')
pwd = os.getenv('GMAIL_APP_PASSWORD')

mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
mail.login(user, pwd)

bounce_records = []
seen_emails = set()

# In Gmail, bounces can land in Trash or Inbox
for folder_name in ['"[Gmail]/Trash"', 'INBOX']:
    try:
        status, _ = mail.select(folder_name)
        if status != 'OK':
            continue
        
        # Search specifically for messages since today 05-Nov-2026
        # Or search FROM mailer-daemon
        typ, data = mail.search(None, '(SINCE "05-Nov-2026" FROM "mailer-daemon")')
        if typ != 'OK' or not data[0]:
            # fallback: check last 20 messages in folder
            typ2, data2 = mail.search(None, 'ALL')
            ids = data2[0].split()[-25:] if (typ2 == 'OK' and data2[0]) else []
        else:
            ids = data[0].split()

        print(f"Checking {len(ids)} candidate messages in {folder_name}...", flush=True)

        for mid in ids:
            res, msg_data = mail.fetch(mid, '(BODY.PEEK[])')
            for part in msg_data:
                if isinstance(part, tuple):
                    msg = email.message_from_bytes(part[1])
                    date_str = str(msg.get('Date', ''))
                    subj = str(msg.get('Subject', ''))
                    from_str = str(msg.get('From', '')).lower()
                    
                    if '05 nov 2026' in date_str.lower() and ('mailer-daemon' in from_str or 'delivery' in subj.lower() or 'failure' in subj.lower() or 'blocked' in subj.lower()):
                        body = ""
                        for p in msg.walk():
                            if p.get_content_type() == 'text/plain':
                                try:
                                    body = p.get_payload(decode=True).decode('utf-8', errors='ignore')
                                except Exception:
                                    pass
                                break
                        
                        recipient = None
                        m1 = re.search(r'(?:message to|delivered to|recipient:?|to:\s*<*)\s*<*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)>*', body, re.IGNORECASE)
                        if m1:
                            recipient = m1.group(1).lower()
                        else:
                            all_emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', body)
                            for em in all_emails:
                                em_l = em.lower()
                                if 'valixis' not in em_l and 'google' not in em_l and 'gmail' not in em_l:
                                    recipient = em_l
                                    break
                                    
                        if recipient and recipient not in seen_emails:
                            seen_emails.add(recipient)
                            err_reason = "Recipient blocked / rejected"
                            for line in body.splitlines():
                                line_clean = line.strip()
                                if any(code in line_clean for code in ['550', '554', '451', 'DNS Error', 'Access denied', 'blocked', 'rejected']):
                                    err_reason = line_clean[:140]
                                    break
                                    
                            bounce_records.append({
                                'recipient': recipient,
                                'date': date_str,
                                'subject': subj,
                                'reason': err_reason
                            })
    except Exception as e:
        print(f"Error checking {folder_name}: {e}", flush=True)

mail.close()
mail.logout()

# Query DB
conn = sqlite3.connect('ai_agents/data/leads.db')
c = conn.cursor()
c.execute("SELECT count(*) FROM leads WHERE status = 'CONTACTED_GMAIL'")
total_gmail_dispatched = c.fetchone()[0]
conn.close()

print(f"\n=======================================================", flush=True)
print(f"📊 LIVE GMAIL OUTREACH DELIVERABILITY AUDIT", flush=True)
print(f"=======================================================", flush=True)
print(f"Total Emails Dispatched via Gmail so far: {total_gmail_dispatched}", flush=True)
print(f"Total Hard Bounces Detected: {len(bounce_records)}", flush=True)

if total_gmail_dispatched > 0:
    successful_deliveries = total_gmail_dispatched - len(bounce_records)
    bounce_pct = (len(bounce_records) / total_gmail_dispatched) * 100
    deliverability_rate = 100.0 - bounce_pct
    print(f"Successfully Delivered (Inbox/Target): {successful_deliveries} ({deliverability_rate:.1f}%)", flush=True)
    print(f"Bounce Rate: {bounce_pct:.1f}%", flush=True)

print(f"\n--- List of Bounced Inboxes & Reasons ---", flush=True)
if bounce_records:
    for idx, b in enumerate(bounce_records, 1):
        print(f"{idx}. {b['recipient']}", flush=True)
        print(f"   Reason: {b['reason']}", flush=True)
else:
    print("None detected.", flush=True)
