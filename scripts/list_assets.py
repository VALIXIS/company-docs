import os

print("--- assets/ directory contents ---")
for f in os.listdir('assets'):
    path = os.path.join('assets', f)
    print(f"  {f} ({os.path.getsize(path)} bytes)")
