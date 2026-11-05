with open('estimate/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[740:820], 741):
    print(f"L{i}: {l.rstrip()}")
