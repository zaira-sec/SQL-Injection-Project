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
"SELECT * FROM users WHERE user = '" + user + "'"
5. Monitorización (SOC)
alertas por UNION, SLEEP, information_schema

detección de patrones repetitivos

correlación de intentos fallidos
