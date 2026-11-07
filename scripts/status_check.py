import sqlite3

conn = sqlite3.connect('ai_agents/data/leads.db')
c = conn.cursor()
c.execute("SELECT status, count(id) FROM leads GROUP BY status")
print("Leads Status Breakdown:")
for row in c.fetchall():
    print(f"  {row[0]}: {row[1]}")

c.execute("SELECT count(id) FROM email_dispatch_log WHERE strftime('%Y-%m-%d', created_at) = strftime('%Y-%m-%d', 'now') AND dispatch_channel = 'RESEND_API'")
today_resend = c.fetchone()[0]
print(f"\nResend emails dispatched today (UTC): {today_resend}")
print(f"Remaining quota on Resend (out of 100): {100 - today_resend}")

conn.close()
