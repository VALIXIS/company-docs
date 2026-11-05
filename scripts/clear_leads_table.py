import sqlite3
import os

db_path = os.path.abspath("ai_agents/data/leads.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("DELETE FROM leads;")
c.execute("DELETE FROM email_dispatch_log;")
conn.commit()

count_leads = c.execute("SELECT count(*) FROM leads;").fetchone()[0]
count_logs = c.execute("SELECT count(*) FROM email_dispatch_log;").fetchone()[0]
conn.close()

print(f"Cleared database! leads count: {count_leads}, email_dispatch_log count: {count_logs}")
