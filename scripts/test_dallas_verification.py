import json
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("ai_agents"))
from email_verifier import verify_email_deliverability

with open("ai_agents/data/dallas_leads_staged.json", "r", encoding="utf-8") as f:
    leads = json.load(f)

print(f"Testing deliverability for {len(leads)} staged Dallas leads...\n")

deliverable_count = 0
flagged_count = 0

for l in leads:
    email = l["primary_email"]
    company = l["company"]
    is_deliv, reason = verify_email_deliverability(email)
    if is_deliv:
        deliverable_count += 1
        print(f"✅ [OK] {company[:25]:25} | {email:32} | {reason}")
    else:
        flagged_count += 1
        print(f"⚠️ [FLAGGED] {company[:25]:25} | {email:32} | {reason}")

print(f"\nSummary: {deliverable_count} Deliverable, {flagged_count} Flagged")
