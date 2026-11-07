import sqlite3

conn = sqlite3.connect('ai_agents/data/leads.db')
c = conn.cursor()
c.execute("""
SELECT id, company, phone, niche, location, status, whatsapp_copy
FROM leads 
WHERE phone IS NOT NULL AND phone != '' AND status != 'CONTACTED_WA'
""")

valid_mobile_leads = []
for row in c.fetchall():
    raw_phone = row[2]
    digits = ''.join(filter(str.isdigit, raw_phone))
    
    if digits.startswith('91') and len(digits) == 12:
        local_num = digits[2:]
    elif len(digits) == 10:
        local_num = digits
    else:
        continue
    
    # Must be 10-digit mobile starting with 6, 7, 8, or 9
    if local_num[0] in '6789' and len(local_num) == 10:
        if local_num == '9603416707':
            continue
        valid_mobile_leads.append({
            'id': row[0],
            'company': row[1],
            'phone': '+91' + local_num,
            'niche': row[3],
            'location': row[4],
            'status': row[5],
            'whatsapp_copy': row[6]
        })

print(f"Total valid Indian mobile leads found: {len(valid_mobile_leads)}")
for l in valid_mobile_leads[:20]:
    print(f"ID {l['id']}: {l['company']} -> {l['phone']} ({l['location']})")
conn.close()
