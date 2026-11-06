import sqlite3

bounced_emails = [
    'coffee@monmouthcoffee.co.uk',
    'enquiries@thehawksmoor.com',
    'mail@industrybeans.com',
    'mail@fosterandpartners.com',
    'mail@heatherwick.com',
    'support@skinceuticals.com'
]

conn = sqlite3.connect('ai_agents/data/leads.db')
c = conn.cursor()
for em in bounced_emails:
    c.execute("UPDATE leads SET status = 'BOUNCED', updated_at = CURRENT_TIMESTAMP WHERE email = ?", (em,))
    c.execute("UPDATE email_dispatch_log SET status = 'BOUNCED', reason = 'Bounced / Inbound Security Filter' WHERE email = ?", (em,))
conn.commit()

c.execute("SELECT status, count(*) FROM leads GROUP BY status")
print("Current status distribution in leads.db:")
for r in c.fetchall():
    print(f"  {r[0]}: {r[1]}")
conn.close()
