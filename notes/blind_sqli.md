# Blind SQL Injection (Boolean-Based y Time-Based)

Blind SQLi ocurre cuando la aplicación no muestra errores, pero su comportamiento permite inferir datos.

## Boolean-Based

El atacante envía condiciones que devuelven TRUE o FALSE.

Ejemplo:

1' AND 1=1--
1' AND 1=2--

Si la respuesta cambia, hay SQLi.

Extracción carácter por carácter:

1' AND SUBSTRING((SELECT password FROM users LIMIT 1),1,1)='a'--

## Time-Based

El atacante usa funciones de retraso:

1' AND IF(1=1, SLEEP(5), 0)--

Si la respuesta tarda más → condición verdadera.

## Indicadores SOC

- patrones repetitivos
- tiempos de respuesta anómalos
- consultas con `SLEEP()`, `WAITFOR DELAY`, `BENCHMARK()`
