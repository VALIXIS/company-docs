import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<section[^>]*id=["\']hero["\'].*?</section>', text, re.DOTALL)
if m:
    print('Hero HTML snippet:')
    print(m.group(0)[:1200])

for match in re.finditer(r'(\.hero-3d-viewport|#hero-canvas|#hero)\s*\{([^}]+)\}', text):
    print(match.group(1), '-->', match.group(2).replace('\n', ' '))
