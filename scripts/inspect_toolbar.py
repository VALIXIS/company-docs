with open('client-sites/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(908, min(945, len(lines))):
    print(f"L{i+1}: {lines[i].rstrip()}")
