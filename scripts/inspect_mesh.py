import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('ai_agents/run_mesh_247.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("ai_agents/run_mesh_247.py lines:", len(text.splitlines()))
for line in text.splitlines()[:35]:
    print(line)
