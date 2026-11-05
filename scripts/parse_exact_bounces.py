import imaplib
import email
import os
import sys
from dotenv import load_dotenv

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv('ai_agents/.env')
user = os.getenv('GMAIL_USER')
pwd = os.getenv('GMAIL_APP_PASSWORD')

mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
mail.login(user, pwd)

status, _ = mail.select('"[Gmail]/Trash"')
typ, data = mail.search(None, 'ALL')

if typ == 'OK' and data[0]:
    ids = data[0].split()
    print(f"Total in Trash: {len(ids)}", flush=True)
    # Check the last 15 items in Trash
    for mid in ids[-15:]:
        res, msg_data = mail.fetch(mid, '(RFC822)')
        for part in msg_data:
            if isinstance(part, tuple):
                msg = email.message_from_bytes(part[1])
                subj = msg.get('Subject', '')
                dt = msg.get('Date', '')
                frm = msg.get('From', '')
                
                # Check if it's from today (Nov 05) and is a delivery failure
                if '05 Nov 2026' in str(dt) and ('mailer-daemon' in str(frm).lower() or 'delivery' in str(subj).lower()):
                    print("=" * 60, flush=True)
                    print(f"Msg ID: {mid.decode()} | Date: {dt}", flush=True)
                    print(f"Subject: {subj}", flush=True)
                    
                    # Print relevant lines
                    body_str = ""
                    for p in msg.walk():
                        if p.get_content_type() == 'text/plain':
                            try:
                                body_str = p.get_payload(decode=True).decode('utf-8', errors='ignore')
                            except Exception:
                                pass
                            break
                    for line in body_str.splitlines():
                        line_stripped = line.strip()
                        if any(kw in line_stripped.lower() for kw in [
                            'blocked', '550', '554', 'diagnostic', 'remote server', 'error', 
                            'message to', 'learn more', 'rejected', 'spam', 'dmarc', 'spf', 
                            'policy', 'address not found', 'temporary problem'
                        ]):
                            print(f"  > {line_stripped}", flush=True)

mail.close()
mail.logout()
