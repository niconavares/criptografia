# Ejercicio 11 – Cifrado Asimétrico (RSA-OAEP)

En este ejercicio nos ponemos en la piel de una empresa de videollamadas. Nos han pasado una **clave simétrica** que estaba cifrada, y nuestro trabajo es recuperarla usando criptografía asimétrica (RSA).

Lo curioso de este ejercicio es ver cómo funciona el cifrado RSA con el estándar **OAEP** y qué pasa cuando ciframos dos veces lo mismo.

---

### 📌 Así me ha quedado
Aquí se ve el programa descifrando la clave y volviendo a cifrarla:

![Resultado del ejercicio 11](Ejercicio%20-%2011.jpg)

---

## 🔹 ¿Qué he tenido que hacer?

El profesor nos dio:
1.  Un texto cifrado en hexadecimal (un churro enorme de números y letras).
2.  Una **Clave Privada** y una **Clave Pública**.

**Mis pasos han sido:**

1.  **Descifrar:** He usado la **Clave Privada** para abrir el mensaje. Ahí apareció la clave de sesión original.
2.  **Volver a Cifrar:** He cogido esa clave que recuperé y la he vuelto a cifrar usando la **Clave Pública**.

---

## 🧐 La pregunta del millón: ¿Por qué son distintos?

Me di cuenta de algo raro: el texto cifrado que me dieron al principio **NO coincide** con el texto que yo he cifrado después, aunque la clave original es la misma.

**Mi conclusión:**
Al principio pensé que había hecho algo mal, pero he descubierto que es normal.
El algoritmo **RSA con OAEP** mete "ruido" aleatorio (padding) cada vez que cifra.
* Esto se hace por seguridad, para que si envías el mismo mensaje dos veces, los hackers no sepan que es el mismo porque el cifrado se ve diferente cada vez.

---

## 💻 El código Python

Aquí está el script. He usado la librería `Crypto.PublicKey.RSA` y `PKCS1_OAEP`.

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

# Texto cifrado que me dan (Hexadecimal)
texto_cifrado_hex = "b72e6fd48155f565dd2684df3ffa8746d649b11f0ed4637fc4c99d18283b32e1709b30c96b4a8a20d5dbc639e9d83a53681e6d96f76a0e4c279f0dffa76a329d04e3d3d4ad629793eb00cc76d10fc00475eb76bfbc1273303882609957c4c0ae2c4f5ba670a4126f2f14a9f4b6f41aa2edba01b4bd586624659fca82f5b4970186502de8624071be78ccef573d896b8eac86f5d43ca7b10b59be4acf8f8e0498a455da04f67d3f98b4cd907f27639f4b1df3c50e05d5bf63768088226e2a9177485c54f72407fdf358fe64479677d8296ad38c6f177ea7cb74927651cf24b01dee27895d4f05fb5c161957845cd1b5848ed64ed3b03722b21a526a6e447cb8ee"

# Paso el texto a bytes
datos_cifrados = bytes.fromhex(texto_cifrado_hex)

# --- 1. DESCIFRADO (Usando Clave Privada) ---
clave_privada_pem = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/absrLf79T7cz
tzjt/hHGJ+2LTBrZ90mJqVTwCtLU5xCd9helfOiVQ+ZFZH5a1ewI3Q5hPA16R/Ad
... (He acortado esto para que no ocupe tanto en el readme) ...
-----END PRIVATE KEY-----"""

clave_privada = RSA.import_key(clave_privada_pem)
cipher = PKCS1_OAEP.new(clave_privada, hashAlgo=SHA256)

mensaje_claro = cipher.decrypt(datos_cifrados)
print("La clave descifrada es:", mensaje_claro.hex())

# --- 2. RE-CIFRADO (Usando Clave Pública) ---
clave_publica_pem = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv2m7Ky3+/U+3M7c47f4R
...
-----END PUBLIC KEY-----"""

clave_publica = RSA.import_key(clave_publica_pem)
cipher2 = PKCS1_OAEP.new(clave_publica, hashAlgo=SHA256)

nuevo_cifrado = cipher2.encrypt(mensaje_claro)
print("El nuevo cifrado es:", nuevo_cifrado.hex())
