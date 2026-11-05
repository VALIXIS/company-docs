with open('contact/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")
print("First 20 lines:")
for l in lines[:20]:
    print(l.rstrip())
print("...")
print("Last 20 lines:")
for l in lines[-20:]:
    print(l.rstrip())
