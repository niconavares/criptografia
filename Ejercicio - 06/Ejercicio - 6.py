from Crypto.Hash import HMAC, SHA256

#HMAC clave y datos --- hmac=17938c1b46db10b099e3d0ccc96b685b82a793481b20a931f6e1df7711b8e785
clave_bytes = bytes.fromhex('A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB')
datos = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.", "utf8")
hmac256 = HMAC.new(clave_bytes, msg=datos, digestmod=SHA256)
print(hmac256.hexdigest())

