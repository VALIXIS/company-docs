import os
import sys
import base64
import json
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPO = "VALIXIS/company-docs"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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


# Files and directories to deploy
CANONICAL_PAGES = [
    'index.html',
    'sitemap.xml',
    'robots.txt',
    '_headers',
    'about/index.html',
    'leadership/index.html',
    'leadership/subhash-annam/index.html',
    'leadership/jyothsna-sri/index.html',
    'services/index.html',
    'services/ai-automation/index.html',
    'services/software-mobile/index.html',
    'services/web-platforms/index.html',
    'services/3d-gaming-interactive/index.html',
    'work/index.html',
    'work/rose-cafe/index.html',
    'work/novel-hotel/index.html',
    'work/hiyya-dino-mandi/index.html',
    'client-sites/index.html',
    'estimate/index.html',
    'ecosystem/index.html',
    'projects/index.html',
    'contact/index.html',
]

def get_remote_sha(remote_path):
    url = f"https://api.github.com/repos/{REPO}/contents/{remote_path}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "VALIXIS-Deployer"
    })
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get("sha")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise e

def upload_file(local_path, remote_path):
    if not os.path.exists(local_path):
        print(f"Skipping missing file: {local_path}")
        return False

    with open(local_path, 'rb') as f:
        content_bytes = f.read()

    sha = get_remote_sha(remote_path)
    content_b64 = base64.b64encode(content_bytes).decode('utf-8')

    url = f"https://api.github.com/repos/{REPO}/contents/{remote_path}"
    payload = {
        "message": f"Deploy VALIXIS Website 2.0: {remote_path}",
        "content": content_b64
    }
    if sha:
        payload["sha"] = sha

    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
        "User-Agent": "VALIXIS-Deployer"
    }, method="PUT")

    try:
        with urllib.request.urlopen(req) as resp:
            status = "Updated" if sha else "Created"
            print(f"[{status}] {remote_path}")
            return True
    except urllib.error.HTTPError as e:
        print(f"[Error] Failed to upload {remote_path}: {e.code} - {e.read().decode('utf-8')[:100]}")
        return False

def deploy_all():
    print(f"Starting deployment to https://github.com/{REPO} (GitHub Pages: https://valixis.tech/)...")
    success_count = 0

    # 1. Deploy canonical HTML and root files
    for rel in CANONICAL_PAGES:
        local_p = os.path.join(BASE_DIR, rel)
        remote_p = rel.replace('\\', '/')
        if upload_file(local_p, remote_p):
            success_count += 1

    # 2. Deploy assets folder
    assets_dir = os.path.join(BASE_DIR, 'assets')
    for root, dirs, files in os.walk(assets_dir):
        for f in files:
            local_p = os.path.join(root, f)
            rel_p = os.path.relpath(local_p, BASE_DIR).replace('\\', '/')
            # skip large video file to avoid GitHub REST API 100MB limit; preview reel is 1.6MB which is fine
            if f.endswith('.mp4') and os.path.getsize(local_p) > 25 * 1024 * 1024:
                print(f"Skipping large binary: {rel_p}")
                continue
            if upload_file(local_p, rel_p):
                success_count += 1

    # 3. Deploy client-sites subfolders (rose-cafe, novel-hotel, hiyya-dino-mandi)
    cs_dir = os.path.join(BASE_DIR, 'client-sites')
    for root, dirs, files in os.walk(cs_dir):
        for f in files:
            local_p = os.path.join(root, f)
            rel_p = os.path.relpath(local_p, BASE_DIR).replace('\\', '/')
            if rel_p == 'client-sites/index.html':
                continue # already uploaded
            if upload_file(local_p, rel_p):
                success_count += 1

    print(f"\nDeployment complete! Successfully deployed {success_count} files to {REPO}.")

if __name__ == '__main__':
    deploy_all()
