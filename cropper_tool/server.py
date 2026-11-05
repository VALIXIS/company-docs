import http.server
import socketserver
import json
import base64
import os
import sys
import time
import urllib.request
import urllib.error
import threading

sys.stdout.reconfigure(encoding='utf-8')

PORT = 8500
DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(DIR)

TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO = "VALIXIS/company-docs"

def get_remote_file_sha(remote_path):
    url = f"https://api.github.com/repos/{REPO}/contents/{remote_path}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "VALIXIS-Deployer"
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return data.get("sha")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise e

def push_file_to_github(bytes_data, remote_path, commit_msg):
    local_b64 = base64.b64encode(bytes_data).decode('ascii')
    remote_sha = get_remote_file_sha(remote_path)

    url = f"https://api.github.com/repos/{REPO}/contents/{remote_path}"
    payload = {
        "message": commit_msg,
        "content": local_b64,
        "branch": "main"
    }
    if remote_sha:
        payload["sha"] = remote_sha

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "VALIXIS-Deployer",
        "Content-Type": "application/json"
    }, method="PUT")

    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.status in (200, 201)

def background_deploy_worker(subhash_bytes, jyothsna_bytes):
    print("[DEPLOY] Background worker started...")
    try:
        # Push Subhash
        push_file_to_github(subhash_bytes, "assets/subhash-annam.jpg", "fix(portraits): update manual cropped headshot (Subhash Annam)")
        print("[DEPLOY] Pushed assets/subhash-annam.jpg")
        time.sleep(1)

        # Push Jyothsna
        push_file_to_github(jyothsna_bytes, "assets/jyothsna-sri.jpg", "fix(portraits): update manual cropped headshot (Jyothsna Sri)")
        print("[DEPLOY] Pushed assets/jyothsna-sri.jpg")
        time.sleep(1)

        # Push homepage
        hp_path = os.path.join(ROOT_DIR, "valixis_company_homepage.html")
        if os.path.exists(hp_path):
            with open(hp_path, "rb") as f:
                push_file_to_github(f.read(), "index.html", "fix(portraits): bump cache buster on homepage")
            print("[DEPLOY] Pushed index.html")
            time.sleep(1)

        # Push leadership portal
        lp_path = os.path.join(ROOT_DIR, "leadership", "index.html")
        if os.path.exists(lp_path):
            with open(lp_path, "rb") as f:
                push_file_to_github(f.read(), "leadership/index.html", "fix(portraits): bump cache buster on leadership portal")
            print("[DEPLOY] Pushed leadership/index.html")

        print("[DEPLOY] Background deploy completed successfully!")
    except Exception as e:
        print(f"[DEPLOY ERROR] {e}")

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_POST(self):
        if self.path == '/api/save_and_deploy':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data.decode('utf-8'))
                subhash_b64 = data['subhash_b64'].split(',', 1)[1]
                jyothsna_b64 = data['jyothsna_b64'].split(',', 1)[1]
                subhash_bytes = base64.b64decode(subhash_b64)
                jyothsna_bytes = base64.b64decode(jyothsna_b64)

                # Save locally immediately
                assets_dir = os.path.join(ROOT_DIR, "assets")
                os.makedirs(assets_dir, exist_ok=True)

                p_subhash_local = os.path.join(assets_dir, "subhash-annam.jpg")
                p_jyothsna_local = os.path.join(assets_dir, "jyothsna-sri.jpg")

                with open(p_subhash_local, "wb") as f:
                    f.write(subhash_bytes)
                with open(p_jyothsna_local, "wb") as f:
                    f.write(jyothsna_bytes)
                with open(os.path.join(ROOT_DIR, "subhash_portrait.jpg"), "wb") as f:
                    f.write(subhash_bytes)
                with open(os.path.join(ROOT_DIR, "jyothsna_portrait.jpg"), "wb") as f:
                    f.write(jyothsna_bytes)

                # Bump cache buster in HTML files
                v_tag = f"?v={int(time.time())}"
                import re
                for fn in ["valixis_company_homepage.html", "index.html", "leadership/index.html"]:
                    fpath = os.path.join(ROOT_DIR, fn)
                    if os.path.exists(fpath):
                        with open(fpath, "r", encoding="utf-8") as f:
                            c = f.read()
                        c = re.sub(r'subhash-annam\.jpg\?v=[^\s"\'<>]+', f'subhash-annam.jpg{v_tag}', c)
                        c = re.sub(r'jyothsna-sri\.jpg\?v=[^\s"\'<>]+', f'jyothsna-sri.jpg{v_tag}', c)
                        with open(fpath, "w", encoding="utf-8") as f:
                            f.write(c)

                # Launch async deploy thread to avoid client timeout
                t = threading.Thread(target=background_deploy_worker, args=(subhash_bytes, jyothsna_bytes))
                t.daemon = True
                t.start()

                response = json.dumps({"status": "success", "message": "Saved successfully! Pushing updates to valixis.tech..."}).encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(response)))
                self.end_headers()
                self.wfile.write(response)
                print("[API] Successfully saved local portraits and initiated GitHub deploy thread.")

            except Exception as e:
                response = json.dumps({"status": "error", "message": str(e)}).encode('utf-8')
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(response)))
                self.end_headers()
                self.wfile.write(response)
                print(f"[API ERROR] {e}")
        else:
            self.send_response(404)
            self.end_headers()

class ThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

if __name__ == '__main__':
    with ThreadingServer(("", PORT), CustomHandler) as httpd:
        print(f"VALIXIS Portrait Studio running at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down portrait studio server.")
