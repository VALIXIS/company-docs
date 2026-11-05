import re
import json
import os

with open("DALLAS_CAMPAIGN_37_EMAILS.md", "r", encoding="utf-8") as f:
    text = f.read()

# Pattern matching sections:
# ### 1. SpendRule
# - **To:** `joseph@spendrule.com`, `chris@spendrule.com`
# - **Subject:** `SpendRule / 30-day engineering pod for hospital ERP integrations?`
# ```text
# body
# ```

sections = text.split("### ")
staged_leads = []

for s in sections[1:]:
    lines = s.strip().split("\n")
    header_line = lines[0].strip()
    match_header = re.match(r"^(\d+)\.\s*(.*)", header_line)
    if not match_header:
        continue
    lead_id = int(match_header.group(1))
    company_name = match_header.group(2).strip()

    # Find To:
    to_match = re.search(r"-\s*\*\*To:\*\*\s*(.*)", s)
    to_str = to_match.group(1).strip() if to_match else ""
    raw_emails = re.findall(r"`([^`]+)`", to_str)
    if not raw_emails:
        raw_emails = [e.strip() for e in to_str.split(",") if "@" in e]

    # Find Subject:
    subj_match = re.search(r"-\s*\*\*Subject:\*\*\s*`([^`]+)`", s)
    subject = subj_match.group(1).strip() if subj_match else f"VALIXIS / Modern Web Platform for {company_name}"

    # Find text block
    body_match = re.search(r"```text\s*\n(.*?)\n```", s, re.DOTALL)
    body = body_match.group(1).strip() if body_match else ""

    # Primary email
    primary_email = raw_emails[0] if raw_emails else ""

    staged_leads.append({
        "id": lead_id,
        "company": company_name,
        "primary_email": primary_email,
        "all_emails": raw_emails,
        "subject": subject,
        "pitch": body
    })

out_path = os.path.join("ai_agents", "data", "dallas_leads_staged.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(staged_leads, f, indent=2, ensure_ascii=False)

print(f"Successfully parsed and staged {len(staged_leads)} leads to {out_path}!")
for l in staged_leads[:5]:
    print(f"[{l['id']}] {l['company']} -> {l['primary_email']} | Subj: {l['subject'][:40]}...")
