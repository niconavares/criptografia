import hashlib

# Texto del ejercicio
texto = "En KeepCoding aprendemos cómo protegernos con criptografía"

print("--- Texto original ---")
print(texto)

# 1. Buscamos el SHA3 que da bced1be9...
# Probamos con SHA3-256
h1 = hashlib.sha3_256()
h1.update(bytes(texto, "utf-8"))
res1 = h1.hexdigest()
print("\nSHA3-256:", res1)
# Si coincide con bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe
# Entonces es SHA3-256

# 2. Buscamos el SHA2 que da 4cec5a9f...
# Como es muy largo, probamos con SHA-512
h2 = hashlib.sha512()
h2.update(bytes(texto, "utf-8"))
res2 = h2.hexdigest()
print("\nSHA-512:", res2)
# Si coincide con el del enunciado, es SHA-512

# 3. Generamos SHA3-256 con el punto al final
texto_con_punto = "En KeepCoding aprendemos cómo protegernos con criptografía."
print("\n--- Texto con punto al final ---")
print(texto_con_punto)

h3 = hashlib.sha3_256()
h3.update(bytes(texto_con_punto, "utf-8"))
res3 = h3.hexdigest()
print("SHA3-256 (con punto):", res3)

print("\n--- Conclusión ---")
print("Al cambiar solo un caracter (el punto), el hash cambia completamente.")
print("Esto se llama 'Efecto Avalancha'.")