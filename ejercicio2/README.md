# Ejercicio 2 – Descifrado AES/CBC/PKCS7

Este ejercicio forma parte del Proyecto Final del módulo de **Criptografía** del Bootcamp de Ciberseguridad Full Stack de KeepCoding.

El objetivo es descifrar un texto cifrado con **AES en modo CBC** usando padding **PKCS7**, obtener el texto en claro y analizar cuánto padding se añadió. Además, se comprueba qué ocurre si intentamos usar padding **X923**.

---

## 🔹 Enunciado del ejercicio

Se nos proporciona:

- Una clave hexadecinal del keystore.  
- Un IV compuesto por 16 bytes a cero (`00`).  
- Un texto cifrado en Base64:

TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=


El cifrado utilizado es **AES/CBC/PKCS7**.

---

## 🔹 Código utilizado

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Clave obtenida del keystore
clave_hex = "A2CFB8599E495FA94C945ACB94A8A5EB8448C3AEF877152B3F1AFC40148FB3A4260DB72"

# IV compuesto por ceros
iv_hex = "00" * 16

# Texto cifrado en base64
texto_cifrado_b64 = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="
texto_cifrado = base64.b64decode(texto_cifrado_b64)

# Paso todo a bytes
clave = bytes.fromhex(clave_hex)
iv = bytes.fromhex(iv_hex)

# Descifrado AES/CBC
cipher = AES.new(clave, AES.MODE_CBC, iv)
datos_descifrados_con_padding = cipher.decrypt(texto_cifrado)

# Elimino el padding PKCS7
datos_limpios = unpad(datos_descifrados_con_padding, AES.block_size, style='pkcs7')

print("Texto descifrado:", datos_limpios.decode('utf-8'))

# Cálculo del padding añadido
total_bytes = len(datos_descifrados_con_padding)
bytes_utiles = len(datos_limpios)
padding_extra = total_bytes - bytes_utiles

print("Padding añadido:", padding_extra)

## 🔹 Resultado del descifrado

Texto descifrado: 20553975C31055ED
Padding añadido: 5

🔹 ¿Qué ocurre si usamos padding X923?

❌ Da error porque el padding encontrado no coincide.

PKCS7 usa: 05 05 05 05 05

X923 usa: 00 00 00 00 05

## 📌 Captura del ejercicio
![Captura del ejercicio](https://github.com/niconavares/criptografia/blob/main/ejercicio2/captura-ejercicio2.png)

