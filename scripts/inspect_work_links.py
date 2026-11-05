with open('work/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, 1):
    if '../../client-sites' in l:
        print(f"L{i}: {l.strip()}")
