import subprocess
import re

res = subprocess.run(['git', '-C', 'audit_recent_commits', 'show', 'dbc07a1:index.html'], capture_output=True, text=True, errors='ignore')
html = res.stdout

m = re.search(r'textureLoader\.load\(.*?\);', html, re.DOTALL)
if m:
    print('Three.js texture load in dbc07a1:')
    print(m.group(0)[:1000])

lockup_refs = re.findall(r'valixis-horizontal-lockup\.png[^"\']*', html)
print('Lockup refs in dbc07a1:', set(lockup_refs))
