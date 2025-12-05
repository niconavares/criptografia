from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Clave que saque de la KeyStorePractica
clave_hex = "A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"
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
