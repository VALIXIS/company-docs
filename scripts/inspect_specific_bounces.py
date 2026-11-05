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

for target in ['monmouthcoffee.co.uk', 'thehawksmoor.com', 'industrybeans.com']:
    typ, data = mail.search(None, f'BODY "{target}"')
    if typ == 'OK' and data[0]:
        ids = data[0].split()
        print(f"\n=================== FOUND TARGET: {target} (IDs: {ids}) ===================")
        for mid in ids:
            res, msg_data = mail.fetch(mid, '(RFC822)')
            for part in msg_data:
                if isinstance(part, tuple):
                    msg = email.message_from_bytes(part[1])
                    print(f"Date: {msg.get('Date')}")
                    print(f"Subject: {msg.get('Subject')}")
                    print(f"From: {msg.get('From')}")
                    print("--- BODY EXCERPT ---")
                    body = ""
                    for p in msg.walk():
                        if p.get_content_type() == 'text/plain':
                            try:
                                body = p.get_payload(decode=True).decode('utf-8', errors='ignore')
                            except Exception:
                                pass
                            break
                    print(body[:1500])

mail.close()
mail.logout()
