import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('contact/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find form handling script
scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', text, re.DOTALL)
print(f"Total script tags in contact/index.html: {len(scripts)}")

for i, s in enumerate(scripts):
    if 'form' in s.lower() or 'submit' in s.lower() or 'lead' in s.lower() or 'supabase' in s.lower():
        print(f"\n--- Script {i+1} ---")
        lines = [l for l in s.splitlines() if any(k in l.lower() for k in ['submit', 'fetch', 'post', 'rate', 'spam', 'honeypot', 'supabase', 'cal', 'email', 'lead'])]
        for l in lines[:30]:
            print("  ", l.strip()[:120])
