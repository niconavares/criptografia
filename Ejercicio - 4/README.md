# Ejercicio 4 – Análisis y Manipulación de JWT

Este ejercicio se centra en la seguridad de los **JSON Web Tokens (JWT)**. Analizamos un token firmado, identificamos su contenido y observamos qué ocurre cuando un atacante intenta modificar los privilegios (Escalada de Privilegios) sin conocer la clave secreta.

---

## 🔹 1. Análisis del Token Original

Se nos proporciona un JWT firmado con la clave secreta: `"Con KeepCoding aprendemos"`.

### 📌 Captura: Token Legítimo
![Token Original](token-original.png)

### 🔎 Detalles Técnicos
Al decodificar el token en `jwt.io`, observamos:

1.  **Algoritmo de Firma:**
    * En el header aparece `"alg": "HS256"`.
    * Esto indica **HMAC con SHA-256**.

2.  **Payload (Carga útil):**
    ```json
    {
      "usuario": "Don Pepito de los palotes",
      "rol": "isNormal",
      "iat": 1667933533
    }
    ```
    * El usuario tiene el rol **"isNormal"**, es decir, sin privilegios administrativos.

---

## 🔹 2. Intento de Ataque (Escalada de Privilegios)

Un atacante intercepta el token e intenta modificar el payload para convertirse en administrador.

### 📌 Captura: Token Manipulado
![Token Manipulado](token-atacante.png)

### 🕵️‍♂️ Análisis del Ataque
El atacante modifica el cuerpo del JWT cambiando el rol:
```json
{
  "usuario": "Don Pepito de los palotes",
  "rol": "isAdmin",  <--- CAMBIO ILEGÍTIMO
  "iat": 1667933533
}
El objetivo es hacerse pasar por administrador ("isAdmin") manipulando el payload.

🔹 Conclusión: ¿Por qué falla el ataque?
Al intentar validar el token modificado, el sistema arroja el error:

❌ Invalid signature / signature verification failed

Explicación
La firma de un JWT se genera usando el Header, el Payload y la Clave Secreta.

El hacker ha modificado el Payload.

Al cambiar el contenido, la firma matemática debería cambiar.

Como el hacker NO conoce la clave secreta ("Con KeepCoding aprendemos"), no puede calcular la nueva firma válida.

Por lo tanto, el servidor recalcula la firma con los datos manipulados y su clave; al ver que no coincide con la firma que trae el token, rechaza la petición.
