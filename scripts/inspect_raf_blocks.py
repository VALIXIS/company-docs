with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- renderCursor (4030-4060) ---")
for i in range(4030, min(4065, len(lines))):
    print(f"L{i+1}: {lines[i].rstrip()}")

print("\n--- animate (4370-4400) ---")
for i in range(4370, min(4400, len(lines))):
    print(f"L{i+1}: {lines[i].rstrip()}")

print("\n--- lenisRaf (4530-4555) ---")
for i in range(4530, min(4555, len(lines))):
    print(f"L{i+1}: {lines[i].rstrip()}")
