Ejercicio 2 – Descifrado AES/CBC/PKCS7

Este ejercicio forma parte del Proyecto Final del módulo de Criptografía del Bootcamp de Ciberseguridad Full Stack de KeepCoding.

El objetivo es descifrar un texto cifrado usando AES en modo CBC con padding PKCS7, analizar el texto en claro y comparar el resultado si se usa padding X923.

🔹 Enunciado del ejercicio

Se nos proporciona:

Una clave hex con etiqueta “cifrado-sim-aes-256”

Un IV compuesto por 16 bytes a cero (00…00)

El texto cifrado (Base64):

TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=


El cifrado usado fue AES / CBC / PKCS7.

🔹 Código utilizado (con botón de copiar)
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Clave que sale de la Keystore/Práctica
clave_hex = "A2CFB8599E495FA94C945ACB94A8A5EB8448C3AEF877152B3F1AFC40148FB3A4260DB72"

# El IV son todo ceros
iv_hex = "00" * 16

# El texto cifrado en base64
texto_cifrado_b64 = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="
texto_cifrado = base64.b64decode(texto_cifrado_b64)

# Paso todo a bytes para poder usarlo
clave = bytes.fromhex(clave_hex)
iv = bytes.fromhex(iv_hex)

print("\n--- Empezando a descifrar ---\n")

# Configuro el descifrador AES en modo CBC
cipher = AES.new(clave, AES.MODE_CBC, iv)

# Descifro los datos
datos_descifrados_con_padding = cipher.decrypt(texto_cifrado)

# Le quito el padding (PKCS7)
datos_limpios = unpad(datos_descifrados_con_padding, AES.block_size, style='pkcs7')

print("Texto descifrado:", datos_limpios.decode('utf-8'))

# Calculo cuánto padding había
total_bytes = len(datos_descifrados_con_padding)
bytes_utiles = len(datos_limpios)
padding_extra = total_bytes - bytes_utiles
print("\nPadding añadido:", padding_extra)

print("\nSobre el padding x923:")
print("Si cambiamos a x923 daría error al descifrar.")
print("Porque PKCS7 rellena con el número de bytes (ej: 05 05 05 05 05)")
print("y x923 rellena con ceros y solo el último es el número (ej: 00 00 00 00 05)")

🔹 Resultado del descifrado

En la ejecución:

Texto descifrado: 20553975C31055ED
Padding añadido: 5

🔹 ¿Qué ocurre si usamos padding X923?

❌ Produce error.
Porque el padding PKCS7 usa:

05 05 05 05 05


Y X923 espera:

00 00 00 00 05

lll
