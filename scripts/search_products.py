import os
import re

search_terms = [
    'portal', 'flow', 'cloud', 'desk_ai', 'pulse', 'fitora', 'gaming studio'
]

results = {term: [] for term in search_terms}

for root, dirs, files in os.walk('.'):
    # ignore .git
    if '.git' in root or 'node_modules' in root or 'brain' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.js', '.json', '.md', '.ts')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().lower()
                    for term in search_terms:
                        if term in content:
                            results[term].append(path)
            except Exception as e:
                pass

print("=== Search Results across codebase ===")
for term, paths in results.items():
    print(f"\nTerm '{term}': {len(paths)} files")
    for p in paths[:8]:
        print(f"  - {p}")
    if len(paths) > 8:
        print(f"  ... and {len(paths)-8} more")
