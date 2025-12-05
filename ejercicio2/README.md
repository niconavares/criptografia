Ejercicio 2 – Descifrado AES/CBC/PKCS7

Este ejercicio forma parte del Proyecto Final del módulo de Criptografía del Bootcamp de Ciberseguridad Full Stack de KeepCoding.

El objetivo es descifrar un texto cifrado usando AES en modo CBC con padding PKCS7, analizar cómo se obtiene el texto en claro y qué sucede si se intenta descifrar usando padding X923.

🔹 Enunciado del ejercicio

Se nos da:

Una clave extraída del keystore con etiqueta “cifrado-sim-aes-256”

Un IV compuesto por 16 bytes a cero (00 * 16)

Un texto cifrado en Base64:

TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=


El algoritmo utilizado para el cifrado ha sido:

AES / CBC / PKCS7

🔹 Código Python utilizado

Este es el código completo del ejercicio, listo para copiar:

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

🔹 Resultado obtenido

En tu ejecución del ejercicio (VSCode):

Texto descifrado: 20553975C31055ED
Padding añadido: 5


🔍 El padding fueron 5 bytes:

05 05 05 05 05

🔹 ¿Qué ocurre si cambiamos a padding X923?

Si hacemos:

unpad(datos_descifrados_con_padding, AES.block_size, style='x923')


➡ Da error.
Porque los bytes finales no coinciden con el formato de padding X923.

📌 Captura del ejercicio

Añade tu captura con VSCode aquí:

![captura](./captura-ejercicio2.png)
