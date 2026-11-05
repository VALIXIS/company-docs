import json
import os

with open("ai_agents/data/austin_multi_leads_50_staged.json", "r", encoding="utf-8") as f:
    leads = json.load(f)

# 1. Generate AUSTIN_50_HIGH_TICKET_LEADS_QUEUE.md
lines_queue = []
lines_queue.append("# 🤠 50 High-Ticket Clients Queue (Austin, Texas & Multi-State Tech Hubs)\n")
lines_queue.append("> **Total Leads:** 50 Verified High-Ticket Targets across Cafes, Specialty Roasters, Luxury Hospitality, Architecture, MedSpas & AI Startups  \n")
lines_queue.append("> **Deliverability Status:** 100% DNS MX Pre-Verified (Google Workspace, M365, Mimecast, Proofpoint, Barracuda)  \n")
lines_queue.append("> **Agency:** VALIXIS Technologies (`subhash@valixis.tech`) | [Company Docs](https://valixis.github.io/company-docs/)\n\n---\n")

lines_queue.append("## 📋 Master Lead Directory (50 Targets)\n\n")
lines_queue.append("| # | Company | Decision-Maker | Email Address | City / Region | Vertical | Pitch Angle / Offer |\n")
lines_queue.append("|:---:|:---|:---|:---|:---|:---|:---|\n")

for i, l in enumerate(leads, start=1):
    lines_queue.append(f"| **{i}** | **{l['company']}** | {l['decision_maker']} | `{l['email']}` | {l['city']} | {l['vertical']} | {l['offer']} |\n")

with open("AUSTIN_50_HIGH_TICKET_LEADS_QUEUE.md", "w", encoding="utf-8") as f:
    f.writelines(lines_queue)

# 2. Generate AUSTIN_50_BESPOKE_EMAILS.md
lines_emails = []
lines_emails.append("# 📨 50 Bespoke High-Ticket Cold Emails (Austin, Texas & Multi-State)\n\n")
lines_emails.append("> **Sender:** Subhash <subhash@valixis.tech> | VALIXIS Technologies  \n")
lines_emails.append("> **Reply-To:** official.valixis@gmail.com  \n")
lines_emails.append("> **Documentation:** [https://valixis.github.io/company-docs/](https://valixis.github.io/company-docs/)\n\n---\n")

for i, l in enumerate(leads, start=1):
    lines_emails.append(f"## [{i}/50] {l['company']} ({l['city']})\n\n")
    lines_emails.append(f"**To:** `{l['email']}`  \n")
    lines_emails.append(f"**Decision-Maker:** {l['decision_maker']}  \n")
    lines_emails.append(f"**Vertical:** {l['vertical']}  \n")
    lines_emails.append(f"**Subject:** {l['subject']}\n\n")
    lines_emails.append("```text\n")
    lines_emails.append(l['body'] + "\n")
    lines_emails.append("```\n\n---\n\n")

with open("AUSTIN_50_BESPOKE_EMAILS.md", "w", encoding="utf-8") as f:
    f.writelines(lines_emails)

print("Generated AUSTIN_50_HIGH_TICKET_LEADS_QUEUE.md and AUSTIN_50_BESPOKE_EMAILS.md successfully!")
