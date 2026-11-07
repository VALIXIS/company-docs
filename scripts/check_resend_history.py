import sqlite3

conn = sqlite3.connect('ai_agents/data/leads.db')
c = conn.cursor()
c.execute("SELECT created_at, email, company, dispatch_channel FROM email_dispatch_log WHERE dispatch_channel = 'RESEND_API' ORDER BY created_at")
rows = c.fetchall()
print(f"Total Resend emails in dispatch log: {len(rows)}")

nov5 = [r for r in rows if '2026-11-05' in str(r[0])]
nov6 = [r for r in rows if '2026-11-06' in str(r[0])]
nov7 = [r for r in rows if '2026-11-07' in str(r[0])]

print(f"Sent on Nov 5: {len(nov5)}")
print(f"Sent on Nov 6: {len(nov6)}")
print(f"Sent on Nov 7 (Today): {len(nov7)}")

if nov7:
    print(f"First on Nov 7: {nov7[0][0]} -> {nov7[0][1]}")
    print(f"Last on Nov 7: {nov7[-1][0]} -> {nov7[-1][1]}")

conn.close()
