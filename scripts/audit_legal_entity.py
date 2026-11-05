import glob
import re
import json

html_files = sorted(glob.glob('./**/*.html', recursive=True))

legal_terms = ['incorporated', 'incorporation', 'inc.', 'ltd.', 'llc', 'pvt ltd', 'private limited', 'registered company', 'corporation']

print("=== CHECKING LEGAL STATUS CLAIMS ===")
found_claims = []
for f in html_files:
    if any(x in f for x in ['.git', 'node_modules', 'scratch']):
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        for line_num, line in enumerate(fp, 1):
            for term in legal_terms:
                if re.search(r'\b' + re.escape(term) + r'\b', line, re.IGNORECASE):
                    found_claims.append((f, line_num, term, line.strip()))

print(f"Total legal claims found: {len(found_claims)}")
for f, l, term, text in found_claims[:20]:
    print(f"{f}:{l} [{term}] -> {text[:100]}")

print("\n=== CHECKING VENTURE DESCRIPTIONS ===")
for f in ['index.html', 'about/index.html', 'leadership/index.html', 'contact/index.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    # Find Organization schema description
    scripts = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', content, re.DOTALL)
    for s in scripts:
        try:
            data = json.loads(s.strip())
            graph = data.get('@graph', [data])
            for node in graph:
                if node.get('@type') == 'Organization':
                    print(f"{f} Org Schema: name={node.get('name')}, foundingDate={node.get('foundingDate')}")
                    print(f"   @id: {node.get('@id')}")
                    print(f"   description: {node.get('description')}")
                    founders = node.get('founder', [])
                    print(f"   founders: {[f.get('name') if isinstance(f, dict) else f for f in founders]}")
        except Exception as e:
            print(f"Error parsing schema in {f}: {e}")
