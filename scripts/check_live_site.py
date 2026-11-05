import requests

urls = [
    'https://valixis.tech/',
    'https://valixis.tech/about/',
    'https://valixis.tech/leadership/',
    'https://valixis.tech/estimate/',
    'https://valixis.tech/work/',
    'https://valixis.tech/contact/',
    'https://valixis.tech/sitemap.xml'
]

for u in urls:
    try:
        r = requests.get(u, timeout=10)
        print(f"{u} -> Status: {r.status_code}, Server: {r.headers.get('server', 'unknown')}")
    except Exception as e:
        print(f"{u} -> Error: {e}")
