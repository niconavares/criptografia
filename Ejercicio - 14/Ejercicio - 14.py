from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import binascii

# Ejercicio 14: HKDF SHA-512

# 1. CLAVE MAESTRA (MASTER KEY)
# El profesor podria no tener el keystore, asi que pongo la clave directamente aqui.
# Clave extraida del keystore etiqueta "cifrado-sim-aes-256"
master_key_hex = "A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"
master_key = binascii.unhexlify(master_key_hex)

print("MASTER KEY")
print(master_key.hex())

# 2. SALT (Identificador de dispositivo)
identifier_hex = "e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3"
salt = binascii.unhexlify(identifier_hex)

print("SALT")
print(salt.hex())

# 3. DERIVAR CLAVE (HKDF)
print("HKDF-SHA512")
# Usamos la master_key y el salt con SHA512
key_derived = HKDF(master_key, 32, salt, SHA512, 1)

print("CLAVE DIVERSIFICADA")
print(key_derived.hex())
