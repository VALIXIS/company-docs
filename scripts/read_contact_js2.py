import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('contact/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[1410:1465], 1411):
    print(f"{i}: {l}", end='')
