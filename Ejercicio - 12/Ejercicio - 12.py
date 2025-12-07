from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode

# AES-GCM --> (Datos Asociados + Datos a cifrar) + key + nonce

texto_gcm_bytes = bytes("He descubierto el error y no volveré a hacerlo mal", "utf-8")
key_bytes  = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')
nonce_bytes = get_random_bytes(8)
print("Nonce hex=", nonce_bytes.hex())


datos_asociados_bytes = bytes("Id usuario","utf-8")
cifrador = AES.new(key_bytes,AES.MODE_GCM,nonce=nonce_bytes)
cifrador.update(datos_asociados_bytes)
texto_cifrado_bytes,mac_bytes = cifrador.encrypt_and_digest(texto_gcm_bytes)


print("Texto cifrado (HEX):", texto_cifrado_bytes.hex())
print("Texto cifrado (Base64):", b64encode(texto_cifrado_bytes).decode('utf-8'))
print("MAC:", mac_bytes.hex())

# Lo que estamos haciendo mal al principio es utilizar el mismo nonce para el cifrado y el descifrado.