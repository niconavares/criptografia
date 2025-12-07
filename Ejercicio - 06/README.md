# Ejercicio 6 – Cálculo de HMAC-SHA256

Este ejercicio consiste en verificar la integridad y autenticidad de un mensaje utilizando un **HMAC** (Hash-based Message Authentication Code).

Se nos pide calcular el HMAC-SHA256 de una frase concreta utilizando una clave secreta que hemos extraído de un Keystore.

---

## 🔹 1. Obtención de la Clave (Keystore)

La clave secreta para la firma se encuentra almacenada en un Keystore bajo el alias `hmac-sha256`.

### 📌 Evidencia del Keystore
Aquí podemos verificar el valor hexadecimal de la clave utilizada:
![Captura del Keystore](Keystore.png)

* **Clave Hexadecimal:** `A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB`

---

## 🔹 2. Ejecución del Código

Para resolver el ejercicio, utilizamos la librería `Crypto.Hash` con el algoritmo SHA-256 y la clave extraída anteriormente.

### 📌 Captura del script funcionando
![Ejecución del ejercicio 6](Ejercicio%20-%206.png)

### 💻 Código Python

```python
from Crypto.Hash import HMAC, SHA256

# Clave obtenida del KeyStore (en formato bytes)
clave_bytes = bytes.fromhex('A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB')

# Mensaje que queremos autenticar
datos = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.", "utf8")

# Cálculo del HMAC-SHA256
hmac256 = HMAC.new(clave_bytes, msg=datos, digestmod=SHA256)

# Mostramos el resultado en hexadecimal
print(hmac256.hexdigest())
🔹 Resultado Final
El hash HMAC obtenido es: 857d5ab916789620f35bcfe6a1a5f4ce98200180cc8549e6ec83f408e8ca0550
