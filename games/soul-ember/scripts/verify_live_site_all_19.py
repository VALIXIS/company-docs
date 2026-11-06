import requests
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CANONICAL_URLS = [
    'https://valixis.tech/',
    'https://valixis.tech/about/',
    'https://valixis.tech/leadership/',
    'https://valixis.tech/leadership/subhash-annam/',
    'https://valixis.tech/leadership/jyothsna-sri/',
    'https://valixis.tech/services/',
    'https://valixis.tech/services/ai-automation/',
    'https://valixis.tech/services/software-mobile/',
    'https://valixis.tech/services/web-platforms/',
    'https://valixis.tech/services/3d-gaming-interactive/',
    'https://valixis.tech/work/',
    'https://valixis.tech/work/rose-cafe/',
    'https://valixis.tech/work/novel-hotel/',
    'https://valixis.tech/work/hiyya-dino-mandi/',
    'https://valixis.tech/client-sites/',
    'https://valixis.tech/estimate/',
    'https://valixis.tech/ecosystem/',
    'https://valixis.tech/projects/',
    'https://valixis.tech/contact/',
    'https://valixis.tech/sitemap.xml',
    'https://valixis.tech/robots.txt'
]

print("=" * 80)
print("LIVE VERIFICATION: TESTING ALL 19 CANONICAL PAGES ON VALIXIS.TECH")
print("=" * 80)

results = []
for url in CANONICAL_URLS:
    try:
        r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0 ValixisLiveCheck'})
        status = r.status_code
        length = len(r.content)
        ok = status == 200
        results.append((url, status, length, ok))
        mark = "[200 OK]" if ok else f"[{status} FAIL]"
        print(f"{mark:12s} | {length:7d} bytes | {url}")
    except Exception as e:
        results.append((url, 'Error', 0, False))
        print(f"[ERROR]      | {url} -> {e}")

passed = sum(1 for r in results if r[3])
total = len(results)
print("=" * 80)
print(f"LIVE TEST SUMMARY: {passed}/{total} URLs returning 200 OK on https://valixis.tech/")
print("=" * 80)

if passed == total:
    print("ALL 19 CANONICAL ROUTES + SITEMAP + ROBOTS ARE LIVE AND OPERATIONAL!")
else:
    sys.exit(1)
