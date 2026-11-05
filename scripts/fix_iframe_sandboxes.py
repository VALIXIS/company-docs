import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

iframe_pattern = re.compile(r'<iframe\b([^>]*?)>', re.IGNORECASE)

files_updated = 0

for dirpath, dirnames, filenames in os.walk(repo_root):
    if any(p in dirpath for p in ['.git', 'node_modules', '.gemini']):
        continue
    for f in filenames:
        if f.endswith('.html'):
            fp = os.path.join(dirpath, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as infile:
                content = infile.read()

            if '<iframe' in content:
                state = {'modified': False}

                def replace_iframe(match):
                    attrs = match.group(1)
                    if 'sandbox=' not in attrs:
                        state['modified'] = True
                        return f'<iframe{attrs} sandbox="allow-scripts allow-same-origin allow-forms allow-popups">'
                    return match.group(0)

                new_content = iframe_pattern.sub(replace_iframe, content)
                if state['modified']:
                    with open(fp, 'w', encoding='utf-8') as outfile:
                        outfile.write(new_content)
                    files_updated += 1
                    rel = os.path.relpath(fp, repo_root)
                    print(f"Added sandbox attribute to iframes in: {rel}")

print(f"Total HTML files updated with iframe sandbox: {files_updated}")
