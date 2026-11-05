import re

with open('estimate/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

for i, line in enumerate(content.splitlines(), 1):
    if 'contact' in line.lower() or 'consultation' in line.lower() or 'book' in line.lower():
        print(f"L{i}: {line.strip()[:110]}")
