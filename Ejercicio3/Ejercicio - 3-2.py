from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes


textoPlano = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
#Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')

#Importante NUNCA debe fijarse el nonce
nonce_mensaje = get_random_bytes(12)
#Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
datos_asociados = bytes('', 'utf-8')
cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
cipher.update(datos_asociados)
texto_cifrado, tag = cipher.encrypt_and_digest(textoPlano)

print("nonce:", b64encode(nonce_mensaje).decode())
print("Datos asociados", b64encode(datos_asociados).decode())
print("Texto cifrado:",b64encode(texto_cifrado).decode())
print("MAC/Tag:",b64encode(tag).decode() )