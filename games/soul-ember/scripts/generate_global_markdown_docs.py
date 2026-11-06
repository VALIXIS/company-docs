import json
import os

with open("ai_agents/data/global_100_leads_staged.json", "r", encoding="utf-8") as f:
    leads = json.load(f)

# 1. Generate GLOBAL_100_HIGH_TICKET_LEADS_QUEUE.md
lines_queue = []
lines_queue.append("# 🌍 100 High-Ticket Global Outreach Queue (US, UK, Canada, Australia, Europe)\n\n")
lines_queue.append("> **Target Universe:** 100 High-Ticket Prospects actively hiring or scaling across AI/DevTools, Specialty Cafes, Luxury Hospitality, Architecture & Aesthetics  \n")
lines_queue.append("> **Dispatch Channel:** Direct Human-to-Human Gmail (`official.valixis@gmail.com`) via Authenticated SSL SMTP  \n")
lines_queue.append("> **Deliverability Health:** 100% Pre-Flight DNS MX Verified  \n")
lines_queue.append("> **Documentation:** [https://valixis.github.io/company-docs/](https://valixis.github.io/company-docs/) | [https://valixis.tech](https://valixis.tech)\n\n---\n\n")

lines_queue.append("## 📋 Master Directory (100 Leads)\n\n")
lines_queue.append("| # | Company | Country / City | Decision-Maker | Deliverable Email | Vertical | Pitch Angle / Offer |\n")
lines_queue.append("|:---:|:---|:---|:---|:---|:---|:---|\n")

for i, l in enumerate(leads, start=1):
    country_city = f"{l['country']} ({l['city']})"
    lines_queue.append(f"| **{i}** | **{l['company']}** | {country_city} | {l['decision_maker']} | `{l['email']}` | {l['vertical']} | {l['offer']} |\n")

with open("GLOBAL_100_HIGH_TICKET_LEADS_QUEUE.md", "w", encoding="utf-8") as f:
    f.writelines(lines_queue)

# 2. Generate GLOBAL_100_BESPOKE_EMAILS.md
lines_emails = []
lines_emails.append("# 📨 100 Bespoke Global Cold Emails (Gmail Dispatch Queue)\n\n")
lines_emails.append("> **Sender:** Subhash (VALIXIS Studio) <official.valixis@gmail.com>  \n")
lines_emails.append("> **Direct Mobile / WhatsApp:** +91 9603416707  \n")
lines_emails.append("> **Documentation:** [https://valixis.github.io/company-docs/](https://valixis.github.io/company-docs/)  \n")
lines_emails.append("> **Live Agency:** [https://valixis.tech](https://valixis.tech)\n\n---\n\n")

for i, l in enumerate(leads, start=1):
    lines_emails.append(f"## [{i}/100] {l['company']} — {l['country']} ({l['city']})\n\n")
    lines_emails.append(f"**To:** `{l['email']}`  \n")
    lines_emails.append(f"**Decision-Maker:** {l['decision_maker']}  \n")
    lines_emails.append(f"**Vertical:** {l['vertical']}  \n")
    lines_emails.append(f"**Subject:** {l['subject']}\n\n")
    lines_emails.append("```text\n")
    lines_emails.append(l['pitch'] + "\n")
    lines_emails.append("```\n\n---\n\n")

with open("GLOBAL_100_BESPOKE_EMAILS.md", "w", encoding="utf-8") as f:
    f.writelines(lines_emails)

print("Generated GLOBAL_100_HIGH_TICKET_LEADS_QUEUE.md and GLOBAL_100_BESPOKE_EMAILS.md successfully!")
