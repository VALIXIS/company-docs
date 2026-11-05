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

bounces_today = []
if typ == 'OK' and data[0]:
    ids = data[0].split()
    for mid in ids[-30:]:
        res, msg_data = mail.fetch(mid, '(RFC822)')
        for part in msg_data:
            if isinstance(part, tuple):
                msg = email.message_from_bytes(part[1])
                subj = msg.get('Subject', '')
                dt = msg.get('Date', '')
                from_addr = msg.get('From', '')
                if '05 Nov 2026' in str(dt) or 'Delivery' in subj or 'Failure' in subj:
                    body = ""
                    for p in msg.walk():
                        if p.get_content_type() == 'text/plain':
                            try:
                                body = p.get_payload(decode=True).decode('utf-8', errors='ignore')
                            except Exception:
                                pass
                            break
                    bounces_today.append({
                        'date': dt,
                        'from': from_addr,
                        'subject': subj,
                        'body': body
                    })

mail.close()
mail.logout()

print(f"Total bounce notifications from Trash today/recent: {len(bounces_today)}")
for b in bounces_today[-8:]:
    print("=" * 60)
    print(f"Date: {b['date']}")
    print(f"From: {b['from']}")
    print(f"Subject: {b['subject']}")
    print("BODY:")
    print(b['body'])
