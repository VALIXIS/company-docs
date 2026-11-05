import dns.resolver
import sys

resolver = dns.resolver.Resolver()
resolver.timeout = 2.0
resolver.lifetime = 2.0

domains = [
    'ggroasting.com', 
    'mozartscoffee.com', 
    'flattrackcoffee.com', 
    'cuveecoffee.com', 
    'meritcoffee.com', 
    'radiocoffeeandbeer.com', 
    'civilgoats.com', 
    'mediciroasting.com', 
    'barrettscoffee.com', 
    'cosmiccoffeebeer.com', 
    'haihospitality.com', 
    'mmlcatering.com', 
    'emmerandrye.com', 
    'newwaterloo.com', 
    'westlakedermatology.com', 
    'vivadayspa.com', 
    'hsuoffice.com', 
    'claytonkorte.com', 
    'lakeflato.com', 
    'mirorivera.com', 
    'dcarch.com', 
    'alterstudio.net', 
    'mfarchitecture.com', 
    'escobedogroup.com', 
    'data.world'
]

passed = 0
failed = 0

for d in domains:
    try:
        answers = resolver.resolve(d, 'MX')
        mx = str(answers[0].exchange).rstrip('.')
        print(f"[OK] {d} -> {mx}", flush=True)
        passed += 1
    except Exception as e:
        print(f"[FAIL] {d} -> {e}", flush=True)
        failed += 1

print(f"\nTotal: {passed} passed, {failed} failed", flush=True)
