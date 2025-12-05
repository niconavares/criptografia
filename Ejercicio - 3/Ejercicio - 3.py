from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode

# Datos del ejercicio
textoPlano = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
clave_hex = 'AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120'
nonce_b64 = '9Yccn/f5nJJhAt2S'

# Preparo los datos
clave = bytes.fromhex(clave_hex)
nonce_mensaje = b64decode(nonce_b64)

print('nonce (hex) = ', nonce_mensaje.hex())

# Configuro el cifrador ChaCha20
cipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)

# Cifro el mensaje
texto_cifrado = cipher.encrypt(textoPlano)

# Muestro los resultados
print('Mensaje cifrado en HEX = ', texto_cifrado.hex())
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado).decode())