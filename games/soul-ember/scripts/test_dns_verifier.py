import json
import os
import sys
import dns.resolver
import sqlite3
from typing import List, Dict

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PUBLIC_DNS = ["8.8.8.8", "1.1.1.1"]

def verify_mx(email_addr: str) -> tuple[bool, str]:
    if not email_addr or "@" not in email_addr:
        return False, "INVALID_FORMAT"
    domain = email_addr.split("@")[1].strip().lower()
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = PUBLIC_DNS
    resolver.timeout = 5.0
    resolver.lifetime = 5.0
    try:
        answers = resolver.resolve(domain, 'MX')
        mx_hosts = [str(r.exchange).rstrip('.').lower() for r in answers]
        if not mx_hosts:
            return False, "NO_MX_RECORDS"
        return True, f"MX: {mx_hosts[0]}"
    except Exception as e:
        return False, str(e)

print("DNS MX Verifier Loaded.")
