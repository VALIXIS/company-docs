import os

for path in ['ecosystem/index.html', 'VALIXIS WEBSITE/ecosystem/index.html']:
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'id="valixisPlayer"' in c and 'controls' not in c[c.find('id="valixisPlayer"'):c.find('id="valixisPlayer"')+300]:
        c = c.replace('playsinline', 'playsinline\n          controls')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Added controls to {path}")
