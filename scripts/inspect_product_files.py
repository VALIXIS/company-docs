import os

matches = []
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'brain' in root:
        continue
    for d in dirs:
        if 'portal' in d.lower() or 'fitora' in d.lower() or 'desk' in d.lower() or 'pulse' in d.lower():
            matches.append(os.path.join(root, d))
    for f in files:
        if any(k in f.lower() for k in ['portal', 'fitora', 'desk_ai', 'pulse', 'flow', 'pubspec.yaml']):
            matches.append(os.path.join(root, f))

print(f"Total matching dirs/files: {len(matches)}")
for m in matches[:30]:
    print(" ", m)
