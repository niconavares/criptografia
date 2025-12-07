# Ejercicio 9 – Calcular el KCV (Key Check Value)

En este ejercicio nos han pedido calcular el **KCV** de una clave.

Por lo que he entendido en clase, el KCV es una especie de "resumen" o huella de la clave. Sirve para comprobar si tenemos la clave correcta sin necesidad de enseñarla a nadie.

El profesor nos ha pedido sacarlo de dos formas: usando un hash SHA-256 y cifrando con AES.

---

### 📌 Así me ha quedado
Aquí se ve el script funcionando y los resultados que me da:

![Captura del ejercicio 9](Ejercicio%20-%209.png)

---

## 💻 El código Python

Es muy básico. Solo importa las librerías, define la clave y hace las dos operaciones.

```python
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
🧐 Mis notas personales (Cómo lo hice)
La verdad es que cuando leí el enunciado me asusté un poco con lo de "KCV", "SHA-256" y "bloques de ceros". Pero al ponerme a hacerlo, me di cuenta de que es más simple de lo que parece.

Básicamente, lo que he hecho ha sido seguir la receta paso a paso:

Copiar la clave: Lo primero fue copiar la clave larga que nos daban y pasársela a Python.

Para el primer método (SHA): Simplemente le dije al programa "calcúlame el hash de esto". Me salió un número gigante, así que cogí solo los primeros 6 numeritos (que son los 3 bytes que pedían).

Para el segundo método (AES): Aquí el truco era cifrar "nada" (ceros). Creé una fila de ceros, la cifré con la clave y, otra vez, cogí los primeros numeritos del resultado.

Al final, resulta que el KCV es solo eso: coger un trocito del resultado para ver si coincide y confirmar que la clave está bien. ¡Mucho más fácil de lo que pensaba!
