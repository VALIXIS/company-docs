import re

for path in ['work/index.html', 'client-sites/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"=== {path} ===")
    # Find headers and descriptions
    intro = re.findall(r'<p class=["\'](?:page-subtitle|hero-desc|hero-subtitle|section-desc|lead)["\'][^>]*>(.*?)</p>', text, re.DOTALL)
    for p in intro:
        print("Intro:", re.sub(r'\s+', ' ', p).strip()[:200])
    
    # Check for words like "demonstration", "pilot", "speculative", "client", "case study"
    for w in ['demonstration', 'illustrative', 'pilot', 'case study', 'concept']:
        matches = len(re.findall(r'\b' + w + r'\b', text, re.IGNORECASE))
        print(f"  Count of '{w}': {matches}")
