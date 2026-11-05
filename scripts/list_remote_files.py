import requests

url = "https://api.github.com/repos/VALIXIS/company-docs/contents"
resp = requests.get(url, headers={'User-Agent': 'ValixisAuditor'})
if resp.status_code == 200:
    items = [item['name'] for item in resp.json()]
    print("Files currently deployed in VALIXIS/company-docs on GitHub:")
    for it in items:
        print("  -", it)
else:
    print(f"Error fetching contents: {resp.status_code}")
