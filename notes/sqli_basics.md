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

