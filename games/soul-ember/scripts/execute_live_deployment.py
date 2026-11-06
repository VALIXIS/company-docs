import os
import sys
import stat
import shutil
import subprocess

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPO_DIR = 'temp_deploy_repo'
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_github_token():
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        return token
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('GITHUB_TOKEN='):
                    return line.strip().split('=', 1)[1]
    return ''

TOKEN = get_github_token()

def force_remove_dir(path):
    if not os.path.exists(path):
        return
    def on_rm_error(func, p, excinfo):
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except Exception:
            pass
    shutil.rmtree(path, onerror=on_rm_error)

force_remove_dir(REPO_DIR)

print("Cloning remote repository...")
remote_url = f"https://metspy9069:{TOKEN}@github.com/VALIXIS/company-docs.git"
res = subprocess.run(['git', 'clone', '--depth', '1', remote_url, REPO_DIR], capture_output=True, text=True)
if res.returncode != 0:
    print("Failed to clone:", res.stderr.replace(TOKEN, '[TOKEN]'))
    sys.exit(1)

# Purge decommissioned items in cloned repo
DECOMMISSIONED_ITEMS = [
    'client-sites',
    os.path.join('work', 'rose-cafe'),
    os.path.join('work', 'novel-hotel'),
    os.path.join('work', 'hiyya-dino-mandi'),
]
for item in DECOMMISSIONED_ITEMS:
    target = os.path.join(REPO_DIR, item)
    if os.path.exists(target):
        force_remove_dir(target)
        print(f"Purged decommissioned directory from deploy repo: {item}")

# List of items to copy from root to REPO_DIR
ITEMS_TO_COPY = [
    'CNAME',
    'favicon.ico',
    'favicon-48x48.png',
    'favicon-32x32.png',
    'favicon-16x16.png',
    'apple-touch-icon.png',
    'index.html',
    'sitemap.xml',
    'robots.txt',
    '_headers',
    'vercel.json',
    'about',
    'leadership',
    'services',
    'work',
    'estimate',
    'ecosystem',
    'projects',
    'contact',
    'assets'
]

print("Copying files into deployment repository...")
for item in ITEMS_TO_COPY:
    src_path = os.path.join(SRC_DIR, item)
    dst_path = os.path.join(REPO_DIR, item)

    if not os.path.exists(src_path):
        print(f"WARNING: Source item {item} does not exist at {src_path}!")
        continue

    if os.path.isdir(src_path):
        force_remove_dir(dst_path)
        shutil.copytree(src_path, dst_path)
        print(f"Copied directory: {item}/")
    else:
        shutil.copy2(src_path, dst_path)
        print(f"Copied file: {item}")

# Ensure .nojekyll exists
with open(os.path.join(REPO_DIR, '.nojekyll'), 'w') as f:
    pass
print("Created .nojekyll")

# Configure git committer in the temp repo
subprocess.run(['git', '-C', REPO_DIR, 'config', 'user.name', 'VALIXIS Deployer'], check=True)
subprocess.run(['git', '-C', REPO_DIR, 'config', 'user.email', 'official.valixis@gmail.com'], check=True)

# Git stage, commit, push
print("Staging all changes...")
subprocess.run(['git', '-C', REPO_DIR, 'add', '-A'], check=True)

status_res = subprocess.run(['git', '-C', REPO_DIR, 'status', '--porcelain'], capture_output=True, text=True, check=True)
print("Git Status Summary:")
lines = status_res.stdout.strip().splitlines()
print(f"Total files staged for deployment: {len(lines)}")
for l in lines[:15]:
    print("  ", l)
if len(lines) > 15:
    print(f"   ... and {len(lines) - 15} more files.")

if not lines:
    print("No changes to commit. Repository is already up to date.")
else:
    print("Committing changes...")
    commit_msg = 'release: VALIXIS Website 2.1 — design system unification, technical blueprints, and architecture estimator'
    subprocess.run(['git', '-C', REPO_DIR, 'commit', '-m', commit_msg], check=True)

    print("Pushing to GitHub Pages remote (origin main)...")
    push_res = subprocess.run(['git', '-C', REPO_DIR, 'push', 'origin', 'main'], capture_output=True, text=True)
    if push_res.returncode == 0:
        print("PUSH SUCCESSFUL! Deployed to origin main.")
    else:
        print("Push error:", push_res.stderr.replace(TOKEN, '[TOKEN]'))
        sys.exit(1)

# Cleanup temp folder to remove credentials from disk
print("Cleaning up temporary deployment repository...")
force_remove_dir(REPO_DIR)
print("Deployment complete and verified!")
