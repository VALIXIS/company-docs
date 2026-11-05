import os

print("--- ai_agents/ directory structure ---")
for root, dirs, files in os.walk('ai_agents'):
    for f in files:
        full = os.path.join(root, f)
        print(f"  {full} ({os.path.getsize(full)} bytes)")
