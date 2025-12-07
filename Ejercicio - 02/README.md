# Ejercicio 2 – Descifrado AES/CBC/PKCS7

Este ejercicio forma parte del Proyecto Final del módulo de **Criptografía** del Bootcamp de Ciberseguridad Full Stack de KeepCoding.

El objetivo es descifrar un texto cifrado con **AES en modo CBC** usando padding **PKCS7**, obtener el texto en claro y analizar cuánto padding se añadió.

---

### 📌 Captura del ejercicio
![Captura del ejercicio](captura-ejercicio2.png)

---

## 🔹 Enunciado

Se nos proporciona:
- Una clave hexadecimal del keystore.
- Un IV compuesto por 16 bytes a cero (`00`).
- Un texto cifrado en Base64.

El cifrado utilizado es **AES/CBC/PKCS7**.

---

## 🔹 Código utilizado

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Clave que saque de la KeyStorePractica
clave_hex = "A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A4260DB72"
# El IV son todo ceros
iv_hex = "00000000000000000000000000000000"
# El texto cifrado en base64
texto_cifrado_b64 = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="

# Paso todo a bytes para poder usarlo
clave = bytes.fromhex(clave_hex)
iv = bytes.fromhex(iv_hex)
texto_cifrado = base64.b64decode(texto_cifrado_b64)

print("--- Empezando a descifrar ---")

# Configuro el descifrador AES en modo CBC
cipher = AES.new(clave, AES.MODE_CBC, iv)

# Descifro los datos
datos_descifrados_con_padding = cipher.decrypt(texto_cifrado)

# Le quito el padding (PKCS7)
datos_limpios = unpad(datos_descifrados_con_padding, AES.block_size, style='pkcs7')

# Muestro el resultado
print("Texto descifrado:", datos_limpios.decode('utf-8'))

# Calculo cuanto padding habia
total_bytes = len(datos_descifrados_con_padding)
bytes_utiles = len(datos_limpios)
padding_extra = total_bytes - bytes_utiles
print("Padding añadido:", padding_extra, "bytes")

# Respuesta a la pregunta del x923
print("\nSobre el padding x923:")
print("Si cambiamos a x923 daría error al descifrar.")
print("Porque PKCS7 rellena con el número de bytes (ej: 05 05 05 05 05)")
print("Y x923 rellena con ceros y solo el último es el número (ej: 00 00 00 00 05)")

🔹 Resultado del descifrado
Texto descifrado: Esto es un cifrado en bloque típico. Recuerda, vas por el buen camino. Ánimo.

Padding añadido: 1 bytes

🔹 ¿Qué ocurre si usamos padding X923?
❌ Daría error al descifrar porque el padding encontrado no coincide con el esperado.

PKCS7 rellena con el valor del número de bytes (ej: 05 05 05 05 05).

X923 rellena con ceros y solo el último byte indica la longitud (ej: 00 00 00 00 05).
