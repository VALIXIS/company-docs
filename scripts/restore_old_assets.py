import subprocess
import os

repo_dir = 'audit_recent_commits'

files_to_restore = [
    'assets/valixis-logo-transparent.png',
    'assets/valixis-horizontal-lockup.png'
]

targets = ['.', 'VALIXIS WEBSITE']

for rel_path in files_to_restore:
    # Get content from dbc07a1
    cmd = ['git', '-C', repo_dir, 'show', f'dbc07a1:{rel_path}']
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode != 0:
        print(f"Error fetching {rel_path}: {res.stderr}")
        continue
    content = res.stdout
    print(f"Fetched {rel_path} from dbc07a1: {len(content)} bytes")
    
    for t in targets:
        dst = os.path.join(t, rel_path)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as f:
            f.write(content)
        print(f"Restored to {dst} ({len(content)} bytes)")

print("Successfully restored old transparent logo and old horizontal lockup!")
