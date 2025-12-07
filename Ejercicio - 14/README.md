# Ejercicio 14 – Derivación de Claves (HKDF con SHA-512)

En este ejercicio vamos a practicar la **Derivación de Claves**.

Según he entendido, esto sirve para no usar siempre la misma "Clave Maestra" para todo. Lo que hacemos es coger esa clave maestra, mezclarla con un identificador único (Salt) y generar una **nueva clave derivada** específica para cada dispositivo.

[cite_start]Para ello usamos un algoritmo llamado **HKDF** (HMAC-based Key Derivation Function) junto con **SHA-512** [cite: 612-613].

---

## 🔹 Paso 1: Obtener la Clave Maestra

El enunciado nos dice que la clave maestra está guardada en un Keystore bajo la etiqueta `cifrado-sim-aes-256`. He abierto el Keystore para comprobar su valor.

### 📌 Evidencia del Keystore
![Captura del Keystore](Ejercicio%20-%2014.png)

* **Master Key (Hex):** `A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72`

---

## 🔹 Paso 2: Generar la Clave Derivada

Ahora que tengo la clave maestra, tengo que mezclarla con el "Salt" (que es el identificador del dispositivo) usando el algoritmo HKDF.

* [cite_start]**Salt (ID Dispositivo):** `e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3`[cite: 617].

### 📌 Ejecución del Script
Aquí se ve el programa funcionando y generando la nueva clave:

![Resultado de la ejecución](Ejercicio%20-%2014-2.png)

---

## 💻 El código Python

He utilizado la librería `Crypto.Protocol.KDF` que ya trae la función `HKDF` lista para usar.

```python
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import binascii

# Ejercicio 14: HKDF SHA-512

# 1. CLAVE MAESTRA (MASTER KEY)
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
# Usamos la master_key y el salt con SHA512 para generar una clave de 32 bytes
key_derived = HKDF(master_key, 32, salt, SHA512, 1)

print("CLAVE DIVERSIFICADA")
print(key_derived.hex())
🔹 Resultado Final
La clave única obtenida para este dispositivo es: e716754c67614c53bd9bab176022c952a08e56f07744d6c9edb8c934f52e448a
