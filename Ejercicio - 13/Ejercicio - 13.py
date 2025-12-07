from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
import ed25519
import hashlib

# Ejercicio de Firmas

# PASO 1: DEFINIR EL MENSAJE
# Este es el texto que tenemos que firmar
mensaje = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos."
# Lo convierto a bytes porque si no da error
mensaje_bytes = bytes(mensaje, "utf-8")

# PASO 2: PONER LAS CLAVES (RSA)
# Copio y pego las claves del archivo aqui

clave_privada_rsa = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/absrLf79T7cz
tzjt/hHGJ+2LTBrZ90mJqVTwCtLU5xCd9helfOiVQ+ZFZH5a1ewI3Q5hPA16R/Ad
g63clqWY4iRp4JZt84GGw2XeLURQ60VNxlufQt1aC9oU0Qi1YksI1+LqNa6y5KOw
HqZFkoq+25EGkduNh9zAPevy1kVne/lfUJsxvtgjuNFN+WieCtq3M5fszjeBM2ew
5HfHPLINKr5YpYTRkU80TmrN0R0iewSmlupaAk/hSL2ADUdmzraVqLzqvJ763R79
cO+SmugoEEDEKlxK+xCE42vu9W00d9m2ZSEJgiVeV5yDCoOKzFyJnmhL6dKYFMuD
UU1K4OxtAgMBAAECggEAPqkQGoyOIsKLyKQ8QLyheOrtOmKJj70CF8yU/5ereQLD
T9KV3xjK0sJNiX3iVz4cbLJg2Lfd+Z+/HQpUShgO0cOGBBr/Y7MJPeKNYHQVHyBF
qbY7nCE5cRbcJ2Bep3Ir+hMiN2WncOykIS2HZNMaFGywRyRMaUKGo3Ah43b9dWhx
RYhLee8CD1c9IllkRZ2UycmeJdgWe+CmUOiFWH87r0FBcqVI+6zlKMk2IRh/HfVp
v646kOwKBF3XPT4YFjX+t2JSeLSaQbRQ+aVq3Twyz354GvPvaVsON91FsToQbj+1
fOJRzleWz/CU1XlbhnTvd8TCMv8+hPzf3weyOeTcgQKBgQDdm6wdu54/B/pfQlUX
T3cyYHFKxDj5S/s96HlLcuUR89Sn7LQwwkkZYwki/osm9B5e54/rbSop/1+beCoO
OxKpSozc8/xms3ulbwpDxR3+xTMj9vAGjjp2hw5vylTH6o7Kyq8kYyPjmGnqNpCf
ANv7mfDl8Jvw/kIAEpWxEo6+HQKBgQDdHm4jLWek8PZbBUmZajzzf1MddXMKX50u
dzhKOF2W57WutJpYRbg4/sz3Ty6qtulDexuWnw+feEkroq8cMfBB7FQaQPtq3nac
coWkTSEUG7Tz1RQ318kslVVJ3Y93iSaoMtrThcaa18+FmVG3SwBefl0uEX8SpAVg
1iP0+pfWkQKBgQCTDDwuUpOT4ZhaY2qRGDLQ47vpT8E6cxeYoczyqp+jxPcEIoYC
oLjetp+Wb+8n/u60LNWL85j52zG2uQq2/K3KVeSYrPF7uHdAdCkMhRz9NB9WKwJk
ZzYV9lI3DbwqF9N+bvW+oGZtHHKTbneSeoB+OEzoVzsys5RZ9fsMT3MWZQKBgAye
W/Kt+Kg1CBoRpy2WHnxW28tmlHYXFsU8EH5L0St3darOq7A16ll2UQQcBLHBVnZ/
ZAeodB/JoYNX+V5Gi0t3zSTiaHak02gCMRY7QJQBMMZpdonpSpW8v+1DM5jCvu4C
WPKRQ9A6WKFrKnqnURITbAXhAbtymMv57HtigZ/BAoGAdpmMRDQNKqai7aGbmbmF
Wy1GbLITkxWAOFScQQUYrFs8cuOGu79aB7PHwzeOIHk/5ESj/gz7hoKJtOgi4ikx
zG2lYqqe11/Gg6wHendR1qR8VrbLBkpqylFTGusmLBuq7y4E/z9y2b4rMciU3OY2
X230g/Q6y6kMprauaCuxNSk=
-----END PRIVATE KEY-----"""

clave_publica_rsa = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv2m7Ky3+/U+3M7c47f4R
xifti0wa2fdJialU8ArS1OcQnfYXpXzolUPmRWR+WtXsCN0OYTwNekfwHYOt3Jal
mOIkaeCWbfOBhsNl3i1EUOtFTcZbn0LdWgvaFNEItWJLCNfi6jWusuSjsB6mRZKK
vtuRBpHbjYfcwD3r8tZFZ3v5X1CbMb7YI7jRTflongratzOX7M43gTNnsOR3xzyy
DSq+WKWE0ZFPNE5qzdEdInsEppbqWgJP4Ui9gA1HZs62lai86rye+t0e/XDvkpro
KBBAxCpcSvsQhONr7vVtNHfZtmUhCYIlXlecgwqDisxciZ5oS+nSmBTLg1FNSuDs
bQIDAQAB
-----END PUBLIC KEY-----"""

# PASO 3: FIRMAR CON RSA
print("--- Firma 1: RSA ---")

# cargo la clave
mi_clave = RSA.importKey(clave_privada_rsa)

# hago el hash
mi_hash = SHA256.new(mensaje_bytes)

# preparo para firmar
firmador = PKCS115_SigScheme(mi_clave)

# firmo
firma = firmador.sign(mi_hash)

# imprimo el resultado en hex
print("Resultado RSA:", firma.hex())


# PASO 4: PONER LAS CLAVES (Ed25519)
# Estas son mas cortas
clave_privada_ed_hex = "c4225628eb2fc184e90bcadec9bf6d8596f372473b1bb9fb62cc975aacf34cbc7cbd8471d56e8aef76809d025e19df3b17f7127e6d440f91c1fe643ac1eba961"
clave_publica_ed_hex = "7cbd8471d56e8aef76809d025e19df3b17f7127e6d440f91c1fe643ac1eba961"

# PASO 5: FIRMAR CON Ed25519
print("\n--- Firma 2: Ed25519 ---")

# convierto la clave de hex a normal
clave_bytes = binascii.unhexlify(clave_privada_ed_hex)
clave_para_firmar = ed25519.SigningKey(clave_bytes)

# hago otro hash diferente
hash2 = hashlib.sha256()
hash2.update(mensaje_bytes)
hash_listo = hash2.digest()

# firmo
firma2 = clave_para_firmar.sign(hash_listo, encoding='hex')

# imprimo
print("Resultado Ed25519:", firma2.decode("utf-8"))
