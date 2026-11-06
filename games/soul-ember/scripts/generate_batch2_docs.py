import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

resend_path = "ai_agents/data/batch2_resend_100_staged.json"
gmail_path = "ai_agents/data/batch2_gmail_100_staged.json"

with open(resend_path, "r", encoding="utf-8") as f:
    resend_leads = json.load(f)

with open(gmail_path, "r", encoding="utf-8") as f:
    gmail_leads = json.load(f)

all_leads = resend_leads + gmail_leads

# 1. Generate BATCH_2_200_LEADS_QUEUE.md
queue_md = """# 📋 Batch 2 — 200 Verified High-Ticket Global Outreach Queue

> **Total Queue:** **200 Verified Global Targets**  
> **Channel Split:** **100 via Resend API (`subhash@valixis.tech`)** & **100 via Direct Gmail (`official.valixis@gmail.com`)**  
> **Deliverability:** **100% Pre-Flight DNS MX Verified** (Google Workspace, M365, Proofpoint, Barracuda)  
> **Target Regions:** United States, United Kingdom, Canada, Australia, Europe, Japan  
> **Agencies & Blueprints:** [VALIXIS Technologies](https://valixis.tech) | [Architecture Docs](https://valixis.github.io/company-docs/)  

---

## 🎯 Channel & Vertical Breakdown

```mermaid
flowchart TD
    A["200 High-Ticket Targets (Batch 2)"]
    
    A --> B["100 Dispatched via Resend API (subhash@valixis.tech)"]
    B --> B1["50 AI, DevTools & Cloud Infrastructure<br>Offer: 30-Day Senior Full-Stack Sprint Pods ($5k-$15k/mo)"]
    B --> B2["50 Specialty Coffee Roasters & Artisan DTC<br>Offer: Sub-Second (0.8s) Next.js Storefront & 3D Roast Map"]
    
    A --> C["100 Dispatched via Direct Gmail (official.valixis@gmail.com)"]
    C --> C1["40 Premier Hospitality & Dining Groups<br>Offer: 3D Private Room Buyout Visualizer & VIP Event Engine"]
    C --> C2["30 Luxury Architecture & Spatial Design Studios<br>Offer: 3D WebGL Spatial Portfolios & Client Milestone Hubs"]
    C --> C3["30 High-End DTC, Design & Lifestyle Brands<br>Offer: 3D WebGL Configurator & Sub-Second Mobile Checkout"]
```

---

## 📋 Complete Master Directory (All 200 Targets)

### Part 1: Resend Queue (100 Targets — AI/DevTools & Specialty Coffee)

| # | Company | Country / Region | Key Decision-Maker | Verified Deliverable Email | Channel |
|:---:|:---|:---|:---|:---|:---:|
"""

for idx, lead in enumerate(resend_leads, 1):
    queue_md += f"| **{idx}** | **{lead['company']}** | {lead['country']} | {lead['decision_maker']} | `{lead['email']}` | `RESEND` |\n"

queue_md += """
---

### Part 2: Gmail Queue (100 Targets — Hospitality, Architecture & Luxury DTC)

| # | Company | Country / Region | Key Decision-Maker | Verified Deliverable Email | Channel |
|:---:|:---|:---|:---|:---|:---:|
"""

for idx, lead in enumerate(gmail_leads, 101):
    queue_md += f"| **{idx}** | **{lead['company']}** | {lead['country']} | {lead['decision_maker']} | `{lead['email']}` | `GMAIL` |\n"

with open("BATCH_2_200_LEADS_QUEUE.md", "w", encoding="utf-8") as f:
    f.write(queue_md)

print("Created: BATCH_2_200_LEADS_QUEUE.md")

# 2. Generate BATCH_2_200_BESPOKE_EMAILS.md
emails_md = """# ✉️ Batch 2 — 200 Tailored Bespoke Cold Emails

> Every pitch is individually researched, tailored to the prospect's exact product/architecture, and highlights bespoke technical solutions by VALIXIS Studio.  
> Official links included: [https://valixis.tech](https://valixis.tech) & [https://valixis.github.io/company-docs/](https://valixis.github.io/company-docs/)  

---

"""

for idx, lead in enumerate(all_leads, 1):
    emails_md += f"""## [{idx}/200] {lead['company']} ({lead['country']}) — Via {lead['dispatch_channel']}

* **Recipient:** `{lead['email']}`
* **Decision-Maker:** {lead['decision_maker']}
* **Channel:** `{lead['dispatch_channel']}`
* **Subject:** `{lead['subject']}`

```text
{lead['pitch']}
```

---

"""

with open("BATCH_2_200_BESPOKE_EMAILS.md", "w", encoding="utf-8") as f:
    f.write(emails_md)

print("Created: BATCH_2_200_BESPOKE_EMAILS.md")
