import sqlite3
import re

conn = sqlite3.connect('ai_agents/data/leads.db')
c = conn.cursor()

c.execute("SELECT id, phone, company FROM leads WHERE status = 'READY_WHATSAPP'")
for row in c.fetchall():
    if not re.match(r'^\+91[6-9]\d{9}$', row[1]):
        print(f"Filtering non-mobile ID {row[0]}: {row[2]} ({row[1]})")
        c.execute("UPDATE leads SET status = 'NO_WHATSAPP' WHERE id = ?", (row[0],))

conn.commit()
c.execute("SELECT count(*) FROM leads WHERE status = 'READY_WHATSAPP'")
print(f"Strict verified +91 mobile leads: {c.fetchone()[0]}")
conn.close()
