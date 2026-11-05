with open('estimate/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[640:740], 641):
    print(f"L{i}: {l.rstrip()}")
