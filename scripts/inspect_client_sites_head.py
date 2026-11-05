with open('client-sites/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- client-sites/index.html Head (1-60) ---")
for i in range(min(60, len(lines))):
    print(f"L{i+1}: {lines[i].rstrip()}")
