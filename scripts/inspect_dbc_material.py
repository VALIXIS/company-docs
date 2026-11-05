import subprocess
import re

res = subprocess.run(['git', '-C', 'audit_recent_commits', 'show', 'dbc07a1:index.html'], capture_output=True, text=True, errors='ignore')
html = res.stdout

m = re.search(r'// Razor-Sharp High-Res V Monolith Texture.*?vGroup\.add\(vMeshBack\);', html, re.DOTALL)
if m:
    print('Material & Geometry in dbc07a1:')
    print(m.group(0))
