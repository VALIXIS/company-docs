with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, 1):
    if any(k in l for k in ['function lenisRaf', 'function animate()', 'function renderCursor', 'requestAnimationFrame']):
        print(f"L{i}: {l.strip()[:100]}")
