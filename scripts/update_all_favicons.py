import glob
import re

new_favicon_block = """  <!-- Favicon Suite & Search Engine Identity Icons -->
  <link rel="shortcut icon" href="https://valixis.tech/favicon.ico?v=20261104">
  <link rel="icon" type="image/x-icon" href="https://valixis.tech/favicon.ico?v=20261104">
  <link rel="icon" type="image/png" sizes="48x48" href="https://valixis.tech/assets/favicon-48x48.png?v=20261104">
  <link rel="icon" type="image/png" sizes="96x96" href="https://valixis.tech/assets/favicon-96x96.png?v=20261104">
  <link rel="icon" type="image/png" sizes="32x32" href="https://valixis.tech/assets/favicon-32x32.png?v=20261104">
  <link rel="icon" type="image/png" sizes="16x16" href="https://valixis.tech/assets/favicon-16x16.png?v=20261104">
  <link rel="apple-touch-icon" sizes="180x180" href="https://valixis.tech/assets/apple-touch-icon.png?v=20261104">
  <link rel="icon" type="image/png" sizes="192x192" href="https://valixis.tech/assets/android-chrome-192x192.png?v=20261104">
  <link rel="icon" type="image/png" sizes="512x512" href="https://valixis.tech/assets/android-chrome-512x512.png?v=20261104">"""

pattern = re.compile(
    r'(?:<!--\s*Favicon[^\n]*-->\s*)?(?:<link\s+rel=["\'](?:shortcut\s+icon|icon|apple-touch-icon)["\'][^>]*>\s*)+',
    re.IGNORECASE
)

count = 0
for fpath in glob.glob('./**/*.html', recursive=True):
    if any(x in fpath for x in ['.git', 'node_modules', 'scratch']):
        continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    if '<head>' not in content.lower():
        continue
        
    m = pattern.search(content)
    if m:
        new_content = content[:m.start()] + new_favicon_block + '\n' + content[m.end():]
        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        count += 1
        print(f"Updated favicon block in: {fpath}")

print(f"\nTotal HTML files updated with new canonical Google-Search-compliant favicon block: {count}")
