import os
import sys
import smtplib
from dotenv import load_dotenv

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv("ai_agents/.env")

gmail_user = os.getenv("GMAIL_USER")
gmail_pass = os.getenv("GMAIL_APP_PASSWORD")

print(f"Testing Gmail SMTP connection for {gmail_user}...")

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
        server.login(gmail_user, gmail_pass)
        print("[SUCCESS] Gmail SMTP authentication SUCCESSFUL!")
except Exception as e:
    print(f"[FAILED] Gmail SMTP authentication FAILED: {e}")
