# Ejercicio 12 – El peligro de reutilizar el Nonce (AES-GCM)

En este ejercicio tenemos que comunicarnos con una empresa usando el algoritmo **AES-GCM**. Nos dan una clave y un "Nonce" fijo y nos preguntan qué estamos haciendo mal.

Además, he tenido que cifrar la frase: *"He descubierto el error y no volveré a hacerlo mal"*.

---

### 📌 Así me ha quedado
Aquí está el script funcionando. He cifrado la frase y me devuelve el texto en Hexadecimal, en Base64 y el MAC (la firma de seguridad).

![Resultado del ejercicio 12](Ejercicio%20-%2012.png)

---

## 🧐 ¿Qué estamos haciendo mal?

El enunciado nos da un Nonce fijo: `9Yccn/f5nJJhAt2S`.

Al principio no entendía cuál era el problema, pero investigando un poco sobre **AES-GCM**, he descubierto algo vital:

* **El error:** Estamos usando un **Nonce fijo** para todas las comunicaciones.
* **Por qué es grave:** El "Nonce" significa *Number used ONCE* (número usado una sola vez). Si usamos la misma clave y el mismo Nonce para cifrar dos mensajes distintos, un atacante podría romper el cifrado y recuperar los mensajes.

**Conclusión:** Nunca se debe dejar el Nonce "hardcodeado" (fijo) en el código. Hay que generar uno aleatorio nuevo para cada mensaje.

---

## 💻 El código Python

En mi script he usado la librería `Crypto` para cifrar el mensaje. 

*Nota:* Aunque el ejercicio daba un Nonce fijo, en mi código he usado `get_random_bytes(8)` para generar uno aleatorio, porque he entendido que es la forma segura de hacerlo (y así evito el error del que hablaba antes).

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode

# AES-GCM --> (Datos Asociados + Datos a cifrar) + key + nonce

texto_gcm_bytes = bytes("He descubierto el error y no volveré a hacerlo mal", "utf-8")
key_bytes  = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')

# Genero un Nonce aleatorio (8 bytes) para que sea seguro
nonce_bytes = get_random_bytes(8)
print("Nonce hex=", nonce_bytes.hex())

datos_asociados_bytes = bytes("Id usuario","utf-8")

# Configuro el cifrador
cifrador = AES.new(key_bytes, AES.MODE_GCM, nonce=nonce_bytes)
cifrador.update(datos_asociados_bytes)

# Cifro y obtengo el MAC (tag)
texto_cifrado_bytes, mac_bytes = cifrador.encrypt_and_digest(texto_gcm_bytes)

print("Texto cifrado (HEX):", texto_cifrado_bytes.hex())
print("Texto cifrado (Base64):", b64encode(texto_cifrado_bytes).decode('utf-8'))
print("MAC:", mac_bytes.hex())
