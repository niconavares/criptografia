# Ejercicio 5 – Algoritmos de Hashing y Efecto Avalancha

Este ejercicio tiene como objetivo identificar los algoritmos de hash utilizados para generar ciertos resúmenes criptográficos y observar el comportamiento de estos algoritmos ante pequeños cambios en la entrada (Efecto Avalancha).

---

### 📌 Captura de ejecución
![Captura del ejercicio 5](Ejercicio%20-%205.png)

---

## 🔹 Enunciado

Se proporciona el siguiente texto base:
> *"En KeepCoding aprendemos cómo protegernos con criptografía"*

Y dos hashes obtenidos a partir de él que debemos identificar:
1.  `bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe`
2.  `4cec5a9f85dcc5c4...` (cadena de longitud extensa).

Finalmente, se solicita generar un nuevo hash SHA3-256 añadiendo un punto final al texto y comparar el resultado.

---

## 🔹 Código de la solución

Se ha utilizado la librería `hashlib` de Python para comprobar diferentes algoritmos hasta encontrar las coincidencias.

```python
import hashlib

# Texto del ejercicio
texto = "En KeepCoding aprendemos cómo protegernos con criptografía"

print("--- Texto original ---")
print(texto)

# 1. Buscamos el algoritmo del primer hash (bced1be9...)
# Probamos con SHA3-256
h1 = hashlib.sha3_256()
h1.update(bytes(texto, "utf-8"))
res1 = h1.hexdigest()
print("\nSHA3-256:", res1)
# Coincide con el enunciado: Es SHA3-256

# 2. Buscamos el algoritmo del segundo hash (4cec5a9f...)
# Al ser una cadena muy larga, probamos con SHA-512
h2 = hashlib.sha512()
h2.update(bytes(texto, "utf-8"))
res2 = h2.hexdigest()
print("\nSHA-512:", res2)
# Coincide con el enunciado: Es SHA-512

# 3. Generamos SHA3-256 con el punto al final
texto_con_punto = "En KeepCoding aprendemos cómo protegernos con criptografía."
print("\n--- Texto con punto al final ---")
print(texto_con_punto)

h3 = hashlib.sha3_256()
h3.update(bytes(texto_con_punto, "utf-8"))
res3 = h3.hexdigest()
print("SHA3-256 (con punto):", res3)

print("\n--- Conclusión ---")
print("Al cambiar solo un carácter (el punto), el hash cambia completamente.")
print("Esto se conoce como 'Efecto Avalancha'.")
🔹 Análisis de Resultados
Tras la ejecución del script, se han obtenido las siguientes conclusiones:

Identificación de algoritmos:

El primer hash corresponde a un SHA3-256.

El segundo hash, debido a su mayor longitud, corresponde a un SHA-512 (familia SHA-2).

Efecto Avalancha: Al añadir únicamente un punto (".") al final de la frase original, el hash resultante cambia por completo:

Original: bced1be9...

Modificado: 302be507...

Esto demuestra la propiedad de Efecto Avalancha, donde una mínima modificación en la entrada produce un cambio drástico en la salida, garantizando que no se pueda deducir el mensaje original por similitud.
