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

print(f"Connecting to IMAP for {user}...")
mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
mail.login(user, pwd)

status, mailboxes = mail.list()
print("Mailboxes found:")
for mb in mailboxes:
    print("  ", mb.decode())

folders_to_check = ['INBOX', '[Gmail]/All Mail', '[Gmail]/Spam', '[Gmail]/Trash']

print("\n--- Searching for bounce / delivery notifications ---")
found_bounces = []

for folder in folders_to_check:
    try:
        status, _ = mail.select(f'"{folder}"')
        if status != 'OK':
            continue
        
        # Search criteria
        queries = [
            'FROM "mailer-daemon"',
            'FROM "Mail Delivery Subsystem"',
            'SUBJECT "Delivery Status Notification"',
            'SUBJECT "Undelivered Mail Returned to Sender"',
            'SUBJECT "failure"'
        ]
        
        all_matched_ids = set()
        for q in queries:
            try:
                typ, data = mail.search(None, q)
                if typ == 'OK' and data[0]:
                    for mid in data[0].split():
                        all_matched_ids.add(mid)
            except Exception as e:
                pass
        
        if all_matched_ids:
            print(f"Folder '{folder}': Found {len(all_matched_ids)} matching messages.")
            for mid in sorted(list(all_matched_ids), key=lambda x: int(x))[-15:]:
                res, msg_data = mail.fetch(mid, '(RFC822)')
                for part in msg_data:
                    if isinstance(part, tuple):
                        msg = email.message_from_bytes(part[1])
                        subj = msg.get("Subject", "")
                        from_addr = msg.get("From", "")
                        to_addr = msg.get("To", "")
                        date_str = msg.get("Date", "")
                        
                        # Extract body snippet
                        body_snippet = ""
                        if msg.is_multipart():
                            for p in msg.walk():
                                ctype = p.get_content_type()
                                if ctype == "text/plain":
                                    try:
                                        body_snippet = p.get_payload(decode=True).decode('utf-8', errors='ignore')[:300]
                                    except Exception:
                                        pass
                                    break
                        else:
                            try:
                                body_snippet = msg.get_payload(decode=True).decode('utf-8', errors='ignore')[:300]
                            except Exception:
                                pass
                                
                        found_bounces.append({
                            "folder": folder,
                            "id": mid.decode(),
                            "date": date_str,
                            "from": from_addr,
                            "to": to_addr,
                            "subject": subj,
                            "snippet": body_snippet.replace('\n', ' ')
                        })
    except Exception as e:
        print(f"Error checking folder {folder}: {e}")

mail.close()
mail.logout()

print(f"\nTotal potential bounce messages detected: {len(found_bounces)}")
for b in found_bounces[-20:]:
    print(f"\n[{b['folder']}] Date: {b['date']}")
    print(f"  From: {b['from']}")
    print(f"  To: {b['to']}")
    print(f"  Subject: {b['subject']}")
    print(f"  Snippet: {b['snippet'][:200]}...")
