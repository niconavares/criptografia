# Ejercicio 1 – Disociación de claves mediante XOR

### 📌 Captura del ejercicio
![Captura del ejercicio](https://github.com/niconavares/criptografia/blob/main/ejercicio1/captura-ejercicio1.png)

Este ejercicio forma parte del Proyecto Final del módulo de **Criptografía** del Bootcamp de Ciberseguridad Full Stack de KeepCoding.

El objetivo es comprender cómo se genera una clave final en memoria utilizando dos partes:
- una clave fija embebida en el código  
- una clave dinámica proporcionada por el Key Manager  

La clave final se obtiene aplicando una operación **XOR** entre ambas.

---

## 🔹 Enunciado del ejercicio

Tenemos un sistema que usa claves de 16 bytes. Para evitar que ninguna persona tenga acceso directo a la clave final, se divide en:

- **Clave fija en el código:** `B1EF2ACFE2BAEEFF`  
- **Clave dinámica (properties)** proporcionada por el Key Manager

La clave final es:

clave_codigo XOR clave_properties




### ▶️ Parte 1 — Desarrollo

Sabemos que la clave final generada en memoria es:

91BA13BA21AABB12




**Pregunta:**  
¿Qué valor ha puesto el Key Manager para obtener esa clave final?

---

### ▶️ Parte 2 — Producción

En producción el Key Manager entrega este valor:

B98A15BA31AEBB3F




**Pregunta:**  
¿Qué clave final resultará en memoria?

---

## 📌 Código en Python

Archivo: `Ejercicio-1.py`

```python
#XOR de datos binarios
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])

#Desarrollo
# clave_codigo = B1EF2ACFE2BAEEFF
# clave_final_memoria = 91BA13BA21AABB12
# Buscamos: Key Manager 

m = bytes.fromhex("B1EF2ACFE2BAEEFF")
k = bytes.fromhex("91BA13BA21AABB12")
print("Desarrollo (Key Manager):", xor_data(m,k).hex().upper())

#Produccion
# clave_codigo = B1EF2ACFE2BAEEFF
# Key Manager (Properties) =  B98A15BA31AEBB3F
# Buscamos: Clave Final (Memoria)
m = bytes.fromhex("B1EF2ACFE2BAEEFF")
k = bytes.fromhex("B98A15BA31AEBB3F")
print("Produccion (Clave Final):", xor_data(m,k).hex().upper())
✔️ Resultados
Valor del Key Manager en desarrollo: 20553975C31055ED

Clave final en memoria (producción): 08653F75D31455C0
