# Ejercicio 7 – ¿Cómo guardar las contraseñas?

En este ejercicio nos han planteado un problema teórico sobre cómo deberíamos guardar las contraseñas en la base de datos de la empresa.

He estado analizando las propuestas (SHA-1 y SHA-256) y esta es mi conclusión sobre cuál es la mejor forma de hacerlo.

---

## 1. Sobre el SHA-1 (La mala opción)
**Pregunta:** El analista propuso SHA-1 y el responsable dijo que no. ¿Por qué?

**Mi respuesta:**
Creo que el responsable tiene razón. Por lo que he podido leer, el **SHA-1** ya no se considera seguro desde hace bastantes años (creo que desde 2005).

El problema principal es que ya se han conseguido **colisiones** (es decir, encontrar dos ficheros distintos que dan el mismo hash). Además, genera claves muy cortitas (160 bits) y hoy en día se quedan pequeñas. Vamos, que usar esto ahora mismo sería un riesgo.

---

## 2. Sobre el SHA-256 (La opción intermedia)
**Pregunta:** Si usamos SHA-256, ¿es suficiente? ¿Cómo lo mejoramos?

**Mi respuesta:**
El SHA-256 es seguro (no está roto como el anterior), pero tiene un problema para las contraseñas: **es demasiado rápido**.

Si un hacker roba la base de datos, podría probar millones de contraseñas por segundo para adivinar las nuestras (usando tablas Rainbow). Para evitar esto, se me ocurren dos cosas:

* **Ponerle un "Salt":** Es básicamente añadir unos caracteres aleatorios a la contraseña antes de guardarla. Así, aunque dos usuarios tengan la misma clave ("123456"), en la base de datos se verán diferentes.
* **Usar un "Pepper":** Es parecido al Salt, pero es un código secreto que guardamos nosotros en el servidor, no en la base de datos.

---

## 3. Mi propuesta final (Lo ideal)
**Pregunta:** ¿Cuál sería la mejor opción de todas?

**Mi respuesta:**
Aunque el truco del Salt está bien, lo ideal sería no usar algoritmos de hash normales (como los SHA), porque están hechos para ser rápidos.

Según he entendido, lo mejor es usar funciones específicas para contraseñas (**KDF**). Yo propondría usar **Argon2** (o Argon2id).
* **¿Por qué?** Porque este algoritmo es **lento a propósito**.
* Obliga al ordenador a trabajar un poco más para comprobar la contraseña. Para el usuario es inapreciable (tarda milisegundos), pero para un atacante hace que sea imposible probar millones de claves a la fuerza bruta.

Si no pudiéramos usar Argon2, también he visto que **bcrypt** es una buena alternativa.
