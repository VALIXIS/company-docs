import os
import re

files_with_token = []
pattern = r'gho_[a-zA-Z0-9]{30,}'

for root, dirs, files in os.walk('.'):
    if any(k in root for k in ['.git', 'node_modules', 'brain', 'scripts']):
        continue
    for f in files:
        if f.endswith(('.py', '.js', '.ts', '.html', '.md', '.json', '.env', '.txt')):
            path = os.path.normpath(os.path.join(root, f))
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as fl:
                    content = fl.read()
                if re.search(pattern, content):
                    files_with_token.append(path)
            except Exception:
                pass

print(f"Files found containing gho_ token: {len(files_with_token)}")
for f in files_with_token:
    print(" ", f)
