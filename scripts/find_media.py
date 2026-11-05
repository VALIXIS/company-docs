import os

video_files = []
image_files = []

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'brain' in root:
        continue
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        full_path = os.path.join(root, f)
        if ext in ['.mp4', '.webm', '.ogg', '.mov', '.mkv']:
            video_files.append((full_path, os.path.getsize(full_path)))
        elif ext in ['.png', '.jpg', '.jpeg', '.webp', '.svg']:
            image_files.append((full_path, os.path.getsize(full_path)))

print(f"Video files found: {len(video_files)}")
for v, s in video_files:
    print(f"  - {v} ({s} bytes)")

print(f"\nImage files found: {len(image_files)}")
for img, s in image_files[:15]:
    print(f"  - {img} ({s} bytes)")
if len(image_files) > 15:
    print(f"  ... and {len(image_files)-15} more")
