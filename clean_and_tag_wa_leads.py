import sqlite3

conn = sqlite3.connect('ai_agents/data/leads.db')
c = conn.cursor()

c.execute("SELECT id, company, phone, status FROM leads")
rows = c.fetchall()

ready_count = 0
invalid_count = 0

for lead_id, company, raw_phone, status in rows:
    if status == 'CONTACTED_WA':
        continue
    
    if not raw_phone:
        continue
    
    digits = ''.join(filter(str.isdigit, raw_phone))
    
    # Strip 91 if 12 digits
    if digits.startswith('91') and len(digits) == 12:
        local_num = digits[2:]
    elif len(digits) == 10:
        local_num = digits
    else:
        c.execute("UPDATE leads SET status = 'NO_WHATSAPP' WHERE id = ?", (lead_id,))
        invalid_count += 1
        continue
    
    # Exclude Subhash's personal phone
    if local_num == '9603416707':
        c.execute("UPDATE leads SET status = 'ON_HOLD' WHERE id = ?", (lead_id,))
        continue
    
    # Filter out known landlines (STD code 804, 802, 806)
    if local_num.startswith('804') or local_num.startswith('802') or local_num.startswith('806'):
        c.execute("UPDATE leads SET status = 'NO_WHATSAPP' WHERE id = ?", (lead_id,))
        invalid_count += 1
        continue
    
    # Indian mobile numbers start with 6, 7, 8, or 9
    if local_num[0] in '6789':
        clean_phone = '+91' + local_num
        c.execute("UPDATE leads SET phone = ?, status = 'READY_WHATSAPP' WHERE id = ?", (clean_phone, lead_id))
        ready_count += 1
    else:
        c.execute("UPDATE leads SET status = 'NO_WHATSAPP' WHERE id = ?", (lead_id,))
        invalid_count += 1

conn.commit()
print(f"DB Cleaned! Valid Mobile Targets tagged READY_WHATSAPP: {ready_count}")
print(f"Landlines/Fictional tagged NO_WHATSAPP: {invalid_count}")
conn.close()
