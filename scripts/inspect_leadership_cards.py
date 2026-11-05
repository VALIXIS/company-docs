with open('leadership/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(605, 645):
    if i < len(lines):
        print(f"{i+1}: {repr(lines[i])}")
