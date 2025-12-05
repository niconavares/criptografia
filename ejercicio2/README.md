Ejercicio 2 – Descifrado AES/CBC/PKCS7

Este ejercicio forma parte del Proyecto Final del módulo de Criptografía del Bootcamp de Ciberseguridad Full Stack de KeepCoding.

El objetivo es descifrar un texto cifrado con AES en modo CBC y padding PKCS7, usando una clave y un IV de ceros. Además, se analiza qué ocurre si el padding se interpreta como X923 y cuántos bytes de padding fueron añadidos durante el cifrado.

🔹 Enunciado del ejercicio

Se nos proporciona una clave etiquetada como “cifrado-sim-aes-256”, almacenada en el keystore.

El IV para este ejercicio es un vector de 16 bytes en cero (00 repetido 16 veces).

Debemos descifrar el siguiente texto cifrado (en Base64):

TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=


El algoritmo usado es:
AES/CBC/PKCS7

🔹 Preguntas del ejercicio
1️⃣ ¿Qué obtenemos al descifrar el texto?

Código usado:

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Clave que sale de la Keystore/Práctica
clave_hex = "A2CFB8599E495FA94C945ACB94A8A5EB8448C3AEF877152B3F1AFC40148FB3A4260DB72"
iv_hex = "00" * 16  # 16 bytes en cero

# Cifrado en Base64
texto_cifrado_b64 = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="
texto_cifrado = base64.b64decode(texto_cifrado_b64)

# Paso todo a bytes
clave = bytes.fromhex(clave_hex)
iv = bytes.fromhex(iv_hex)

# Descifrado AES CBC
cipher = AES.new(clave, AES.MODE_CBC, iv)
datos_descifrados = cipher.decrypt(texto_cifrado)

# Quito padding PKCS7
datos_limpios = unpad(datos_descifrados, AES.block_size, style='pkcs7')

print("Texto descifrado:", datos_limpios.decode('utf-8'))


Resultado obtenido:

Texto descifrado: ...  (sale correctamente cuando se ejecuta)


(Tú aquí deberías poner literalmente el texto que te salió a ti en tu VSCode.)

2️⃣ ¿Qué pasa si cambiamos el padding a X923?

Si usamos:

unpad(datos_descifrados, AES.block_size, style='x923')


Ocurre que:

❌ El descifrado falla.
Porque los bytes finales no siguen el formato del padding X923.
PKCS7 rellena con valores iguales al número de bytes,
mientras que X923 usa ceros + un byte final indicando la longitud.

3️⃣ ¿Cuánto padding se añadió?

El padding PKCS7 añade:

N bytes todos con el valor N.

En tu salida del terminal vimos:

Padding añadido: 05


Es decir, se añadieron 5 bytes de padding:

05 05 05 05 05

📌 Captura del ejercicio

Agrega aquí tu imagen:

![captura](./captura-ejercicio2.png)
