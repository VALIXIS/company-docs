import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, 1):
    if 'ecosystem' in l.lower() or 'showcase' in l.lower() or 'fitora' in l.lower() or 'portal' in l.lower():
        if any(tag in l for tag in ['<section', '<h2', '<h3', '<a href="ecosystem']):
            print(f"L{i}: {l.strip()[:100]}")
