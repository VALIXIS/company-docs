import os
import sys
import json
import urllib.request
import re
from dotenv import load_dotenv

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv('ai_agents/.env')
api_key = os.getenv('RESEND_API_KEY')

if not api_key:
    print("No RESEND_API_KEY found in ai_agents/.env")
    sys.exit(1)

# Extract the 37 email IDs and recipients from dallas_email_campaign.log
log_path = os.path.join("ai_agents", "data", "dallas_email_campaign.log")
dispatched = []

if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        log_content = f.read()
    
    matches = re.findall(r"to (.*?) \((.*?)\) \[ID: (.*?)\]", log_content)
    for m in matches:
        dispatched.append({
            "company": m[0],
            "email": m[1],
            "id": m[2]
        })

print(f"Checking live Resend delivery events for {len(dispatched)} dispatched campaign emails...\n")

status_counts = {}
bounced_list = []
delivered_list = []
sent_list = []
other_list = []

for idx, item in enumerate(dispatched, 1):
    email_id = item["id"]
    req = urllib.request.Request(
        f"https://api.resend.com/emails/{email_id}",
        headers={"Authorization": f"Bearer {api_key}"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            last_event = data.get("last_event", "unknown")
            status_counts[last_event] = status_counts.get(last_event, 0) + 1
            
            if last_event == "bounced":
                bounced_list.append((item, data))
                print(f"[{idx:02d}/37] ❌ BOUNCED  | {item['company'][:25]:25} | {item['email']}")
            elif last_event == "delivered":
                delivered_list.append((item, data))
                print(f"[{idx:02d}/37] ✅ DELIVERED| {item['company'][:25]:25} | {item['email']}")
            elif last_event in ("sent", "delivery_delayed"):
                sent_list.append((item, data))
                print(f"[{idx:02d}/37] ⏳ {last_event.upper():9} | {item['company'][:25]:25} | {item['email']}")
            else:
                other_list.append((item, data))
                print(f"[{idx:02d}/37] ℹ️ {last_event.upper():9} | {item['company'][:25]:25} | {item['email']}")
    except Exception as e:
        print(f"[{idx:02d}/37] ⚠️ API Error on {email_id}: {e}")

total = len(dispatched) if dispatched else 1
bounced_pct = (len(bounced_list) / total) * 100
delivered_pct = (len(delivered_list) / total) * 100

print("\n" + "="*50)
print(f"📊 LIVE CAMPAIGN DELIVERABILITY AUDIT RESULTS")
print("="*50)
print(f"Total Emails Checked: {len(dispatched)}")
for event, count in status_counts.items():
    pct = (count / total) * 100
    print(f"• {event.capitalize()}: {count} ({pct:.1f}%)")

print(f"\nExact Bounce Percentage: {bounced_pct:.1f}%")
print("="*50)
