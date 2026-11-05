with open('contact/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx in [50, 100, 200, 400, 600, 800, 1000, 1200, 1400, 1500]:
    if idx < len(lines):
        print(f"L{idx}: {lines[idx].strip()[:80]}")
