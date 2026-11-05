import os

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'brain' in root:
        continue
    for f in files:
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.svg', '.mp4')):
            name = f.lower()
            if any(k in name for k in ['portal', 'flow', 'cloud', 'desk', 'pulse', 'fitora', 'game', 'gaming', 'reel', 'video', 'demo', 'screen', 'shot', 'preview']):
                full = os.path.join(root, f)
                print(f"{full} ({os.path.getsize(full)} bytes)")
