with open('contact/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[1330:1440], 1331):
    print(f"{i}: {l}", end='')
