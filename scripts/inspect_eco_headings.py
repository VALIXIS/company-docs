with open('ecosystem/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, 1):
    if any(k in l for k in ['<h2', '<h3', 'class="product-', 'class="status-', 'class="badge']):
        print(f"L{i}: {l.strip()[:100]}")
