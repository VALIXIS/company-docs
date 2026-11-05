import sqlite3
import sys

def main():
    conn = sqlite3.connect('ai_agents/data/leads.db')
    c = conn.cursor()
    tables = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print("Tables in leads.db:")
    for t in tables:
        count = c.execute(f"SELECT count(*) FROM {t[0]}").fetchone()[0]
        print(f"  {t[0]}: {count} rows")
    
    # Show columns of leads table
    for t in tables:
        schema = c.execute(f"PRAGMA table_info({t[0]});").fetchall()
        print(f"\nSchema for {t[0]}:")
        for col in schema:
            print(f"  {col[1]} ({col[2]})")
            
    conn.close()

if __name__ == "__main__":
    main()
