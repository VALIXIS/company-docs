with open('about/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[465:515], 466):
    print(f"{i}: {l}", end='')
