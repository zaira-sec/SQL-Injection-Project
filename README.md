🚀 SQL Injection Analysis & Detection Project
Proyecto personal basado en el laboratorio SQL Injection Introduction de TryHackMe.
El objetivo es entender, explotar y detectar SQL Injection como lo haría un analista SOC o un pentester junior.

🔥 Resumen del Proyecto
Este repositorio incluye:

análisis técnico de SQL Injection

ejemplos reales de payloads

explicación de técnicas: en banda, ciegas y fuera de banda

notas defensivas y mitigación

un script propio para detectar parámetros vulnerables

documentación clara y profesional

Este repositorio NO contiene contenido del laboratorio original.  
Todo el material es creado por mí a partir de lo aprendido.

🎯 Objetivos Aprendidos
✔ Sintaxis usada en ataques SQLi
UNION

LIKE

comentarios (--, #)

consultas a information_schema

✔ Cómo ocurre la vulnerabilidad
concatenación insegura de entrada del usuario

falta de validación

ausencia de prepared statements

✔ Detección de puntos de inyección
pruebas con caracteres especiales

observación de errores SQL

comportamiento anómalo en respuestas

✔ Explotación en banda
SQLi basada en errores

SQLi basada en UNION

extracción de credenciales y tablas

✔ Explotación ciega (Blind SQLi)
bypass de autenticación

boolean-based

time-based

extracción carácter por carácter

✔ SQLi fuera de banda (OOB)
exfiltración vía DNS/HTTP

cuándo se usa y por qué

✔ Defensa y mitigación
declaraciones preparadas

validación de entrada

principio de mínimo privilegio
🛠️ Script de Detección de SQL Injection (Python)
```python
import requests

url = "http://example.com/product?id="
payloads = ["1'", "1'--", "1' OR '1'='1", "1' UNION SELECT null,null--"]

for p in payloads:
    r = requests.get(url + p)
    if "error" in r.text.lower() or "sql" in r.text.lower():
        print(f"[!] Posible SQLi detectada con payload: {p}")
    else:
        print(f"[-] Sin indicios con payload: {p}")
```

Este script demuestra:

automatización

comprensión de payloads

análisis de respuestas

pensamiento ofensivo

📁 Estructura del Repositorio
SQL-Injection-Project/
│
├── README.md
├── sqli_detector.py
└── notes/
    ├── sqli_basics.md
    ├── error_based.md
    ├── union_based.md
    ├── blind_sqli.md
    ├── oob_sqli.md
    └── mitigation.md
🧠 Qué aprendí (reflexión personal)
Cómo identificar y explotar SQL Injection en diferentes escenarios

Cómo automatizar pruebas con Python

Cómo documentar un ataque de forma profesional

Cómo aplicar medidas defensivas reales

Cómo pensar como atacante y como defensor

🛡️ Aplicación en un entorno SOC
Un analista SOC debe:

reconocer patrones de SQLi en logs

detectar payloads sospechosos

correlacionar intentos repetidos

entender cómo se extraen datos

recomendar mitigaciones

Este proyecto me ayuda a desarrollar esas habilidades.
