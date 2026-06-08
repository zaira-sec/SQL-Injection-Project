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

Si la columna no existe, la base de datos devuelve un error útil.

## Ejemplo de extracción

1' AND (SELECT 1 FROM information_schema.tables LIMIT 1)=1--

Si la aplicación muestra el error, el atacante puede reconstruir la estructura de la base de datos.

## Indicadores en logs (SOC)

- errores SQL repetidos
- parámetros con `'`, `"`, `--`, `#`
- intentos de `information_schema`

