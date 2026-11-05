with open('client-sites/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines, 1):
    if any(k in l for k in ['turnoverSlider', 'previewIframe', '<header', '<main', 'class="hero', 'class="brand', 'class="page-title']):
        print(f"L{i}: {l.strip()[:100]}")
