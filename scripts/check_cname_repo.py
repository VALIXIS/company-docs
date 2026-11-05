import requests, base64

for r in ['VALIXIS/company-docs', 'metspy9069/metspy9069.github.io']:
    url = f"https://api.github.com/repos/{r}/contents/CNAME"
    resp = requests.get(url, headers={'User-Agent': 'ValixisAuditor'})
    if resp.status_code == 200:
        cname = base64.b64decode(resp.json()['content']).decode('utf-8').strip()
        print(f"{r} CNAME: {cname}")
    else:
        print(f"{r} has no CNAME (status {resp.status_code})")
