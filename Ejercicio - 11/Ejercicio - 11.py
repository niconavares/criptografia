from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

# Texto cifrado que me dan 
texto_cifrado_hex = "b72e6fd48155f565dd2684df3ffa8746d649b11f0ed4637fc4c99d18283b32e1709b30c96b4a8a20d5dbc639e9d83a53681e6d96f76a0e4c279f0dffa76a329d04e3d3d4ad629793eb00cc76d10fc00475eb76bfbc1273303882609957c4c0ae2c4f5ba670a4126f2f14a9f4b6f41aa2edba01b4bd586624659fca82f5b4970186502de8624071be78ccef573d896b8eac86f5d43ca7b10b59be4acf8f8e0498a455da04f67d3f98b4cd907f27639f4b1df3c50e05d5bf63768088226e2a9177485c54f72407fdf358fe64479677d8296ad38c6f177ea7cb74927651cf24b01dee27895d4f05fb5c161957845cd1b5848ed64ed3b03722b21a526a6e447cb8ee"

# Paso el texto a bytes
datos_cifrados = bytes.fromhex(texto_cifrado_hex)

# Clave Privada (la copio tal cual me la has pasado)
clave_privada_pem = """-----BEGIN PRIVATE KEY-----
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

# Clave Publica
clave_publica_pem = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv2m7Ky3+/U+3M7c47f4R
xifti0wa2fdJialU8ArS1OcQnfYXpXzolUPmRWR+WtXsCN0OYTwNekfwHYOt3Jal
mOIkaeCWbfOBhsNl3i1EUOtFTcZbn0LdWgvaFNEItWJLCNfi6jWusuSjsB6mRZKK
vtuRBpHbjYfcwD3r8tZFZ3v5X1CbMb7YI7jRTflongratzOX7M43gTNnsOR3xzyy
DSq+WKWE0ZFPNE5qzdEdInsEppbqWgJP4Ui9gA1HZs62lai86rye+t0e/XDvkpro
KBBAxCpcSvsQhONr7vVtNHfZtmUhCYIlXlecgwqDisxciZ5oS+nSmBTLg1FNSuDs
bQIDAQAB
-----END PUBLIC KEY-----"""

# Cargo la clave privada
clave_privada = RSA.import_key(clave_privada_pem)

# Preparo el descifrador
cipher = PKCS1_OAEP.new(clave_privada, hashAlgo=SHA256)

# Descifro
mensaje_claro = cipher.decrypt(datos_cifrados)
print("La clave descifrada es:", mensaje_claro.hex())

# Ahora voy a cifrarlo otra vez
# Cargo la clave publica
clave_publica = RSA.import_key(clave_publica_pem)

# Preparo el cifrador
cipher2 = PKCS1_OAEP.new(clave_publica, hashAlgo=SHA256)

# Cifro
nuevo_cifrado = cipher2.encrypt(mensaje_claro)
print("El nuevo cifrado es:", nuevo_cifrado.hex())

print("Son distintos porque RSA mete cosas aleatorias al cifrar.")