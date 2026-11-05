import requests

repos_to_check = [
    'VALIXIS/company-docs',
    'VALIXIS/valixis.github.io',
    'VALIXIS/VALIXIS.github.io',
    'metspy9069/metspy9069.github.io',
    'metspy9069/valixis',
    'metspy9069/valixis.tech',
    'VALIXIS/valixis.tech',
    'metspy9069/VALIXIS_AI_AGENTS'
]

for r in repos_to_check:
    url = f"https://api.github.com/repos/{r}"
    resp = requests.get(url, headers={'User-Agent': 'ValixisAuditor'})
    if resp.status_code == 200:
        d = resp.json()
        print(f"FOUND: {r} (default_branch: {d.get('default_branch')}, has_pages: {d.get('has_pages')})")
    else:
        print(f"{r} -> {resp.status_code}")
