with open('contact/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(700, min(850, len(lines))):
    if lines[i].strip():
        print(f"L{i+1}: {lines[i].strip()[:70]}")
