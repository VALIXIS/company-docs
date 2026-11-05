import urllib.request
import urllib.error
import json
import base64
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO = "VALIXIS/company-docs"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAFE_DIR = os.path.join(BASE_DIR, "cafe_portfolio_html")

# Mapping local files to remote paths in showcase
FILE_MAP = {
    os.path.join(CAFE_DIR, "Valixis_Cafe_Showcase_Directory_index.html"): "showcase/index.html",
    os.path.join(CAFE_DIR, "Roastery_Coffee_House_index.html"): "showcase/roastery-coffee-house/index.html",
    os.path.join(CAFE_DIR, "Subko_Specialty_Coffee_index.html"): "showcase/subko-coffee/index.html",
    os.path.join(CAFE_DIR, "Blue_Tokai_Coffee_Roasters_index.html"): "showcase/blue-tokai/index.html",
    os.path.join(CAFE_DIR, "Novel_Hotel_Dining_index.html"): "showcase/novel-hotel/index.html",
}

def get_remote_file_sha(remote_path):
    url = f"https://api.github.com/repos/{REPO}/contents/{remote_path}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "VALIXIS-Showcase-Sync"
    })
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            return data.get("sha"), data.get("content", "").replace("\n", "")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, None
        raise e

def push_file(local_path, remote_path):
    if not os.path.exists(local_path):
        print(f"[SKIP] Local file not found: {local_path}")
        return False

    with open(local_path, "rb") as f:
        local_bytes = f.read()
    
    local_b64 = base64.b64encode(local_bytes).decode('ascii')
    remote_sha, remote_content = get_remote_file_sha(remote_path)

    if remote_content and remote_content == local_b64:
        print(f"[NO CHANGE] {remote_path} is already up to date.")
        return True

    url = f"https://api.github.com/repos/{REPO}/contents/{remote_path}"
    payload = {
        "message": f"sync(showcase): update {remote_path} with latest client demo build",
        "content": local_b64,
        "branch": "main"
    }
    if remote_sha:
        payload["sha"] = remote_sha

    put_req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "VALIXIS-Showcase-Sync",
        "Content-Type": "application/json"
    }, method="PUT")

    try:
        with urllib.request.urlopen(put_req) as resp:
            result = json.loads(resp.read().decode())
            print(f"[UPDATED] {remote_path} -> commit: {result.get('commit', {}).get('sha')[:7]}")
            return True
    except urllib.error.HTTPError as e:
        print(f"[ERROR] Failed to push {remote_path}: {e.code} - {e.read().decode()}")
        return False

def main():
    print("=== Starting VALIXIS Client Showcase Synchronization ===")
    success_count = 0
    for local_path, remote_path in FILE_MAP.items():
        if push_file(local_path, remote_path):
            success_count += 1
    print(f"=== Sync complete: {success_count}/{len(FILE_MAP)} paths processed ===")

if __name__ == "__main__":
    main()
