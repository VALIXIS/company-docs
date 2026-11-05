import os
import sys
import time
import json
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

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
REPO = "VALIXIS/company-docs"

print("Waiting for GitHub Pages build on latest commit...")
url = f"https://api.github.com/repos/{REPO}/pages/builds/latest"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "VALIXIS-Deployer"
}

for attempt in range(15):
    time.sleep(6)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            status = data.get('status')
            commit = data.get('commit', '')[:7]
            print(f"  Attempt {attempt+1}: Status = {status} (Commit: {commit})")
            if status == 'built':
                print("GitHub Pages build SUCCEEDED!")
                break
            elif status == 'errored':
                print("GitHub Pages build ERRORED:", data.get('error'))
                break
    except Exception as e:
        print(f"  Check error: {e}")

print("\nVerifying live asset headers and responses on https://valixis.tech ...")
urls_to_test = [
    "https://valixis.tech/",
    "https://valixis.tech/assets/valixis-logo-transparent.png?v=6",
    "https://valixis.tech/assets/valixis-logo-full.jpg",
    "https://valixis.tech/assets/valixis-horizontal-lockup.png?v=4",
    "https://valixis.tech/assets/favicon-32x32.png",
    "https://valixis.tech/about/",
    "https://valixis.tech/leadership/",
    "https://valixis.tech/contact/"
]

headers_client = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}

for u in urls_to_test:
    try:
        req = urllib.request.Request(u, headers=headers_client)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content_type = resp.headers.get('Content-Type')
            content_length = resp.headers.get('Content-Length')
            print(f"  [200 OK] {u} (Type: {content_type}, Size: {content_length} bytes)")
    except urllib.error.HTTPError as e:
        print(f"  [FAIL {e.code}] {u}")
    except Exception as e:
        print(f"  [ERR] {u} - {e}")

print("\nVerification complete!")
