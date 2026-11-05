import os

for path in ['work/index.html', 'VALIXIS WEBSITE/work/index.html']:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        fixed = content.replace('../../client-sites/', '../client-sites/')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f"Fixed client-sites paths in {path}")
