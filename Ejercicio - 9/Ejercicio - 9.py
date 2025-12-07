from Crypto.Cipher import AES
import hashlib

# 2. La clave del ejercicio
clave = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

print("--- DATOS ---")
print("Clave usada:", clave.hex().upper())

# --- PARTE 1: KCV con SHA-256 ---
# Hacemos el hash
hash_completo = hashlib.sha256(clave).hexdigest()

# El KCV son los 3 primeros bytes (que son 6 letras/numeros)
# Usamos [0:6] para recortar
kcv_sha = hash_completo[0:6].upper()

print("\n--- RESULTADO 1: KCV (SHA-256) ---")
print(kcv_sha)


# --- PARTE 2: KCV con AES ---
# Creamos el bloque de ceros y el IV de ceros
ceros = bytes.fromhex("00" * 16) # Esto crea 16 bytes de ceros

# Preparamos el cifrador
cifrador = AES.new(clave, AES.MODE_CBC, ceros)

# Ciframos
resultado_completo = cifrador.encrypt(ceros).hex()

# Igual que antes, recortamos los primeros 6 caracteres
kcv_aes = resultado_completo[0:6].upper()

print("\n--- RESULTADO 2: KCV (AES) ---")
print(kcv_aes)