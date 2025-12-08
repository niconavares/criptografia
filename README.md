# 🔐 Práctica Final - Criptografía

![Status](https://img.shields.io/badge/Estado-Terminado-green?style=for-the-badge)
![Bootcamp](https://img.shields.io/badge/KeepCoding-Ciberseguridad-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge&logo=python&logoColor=white)

Hola 👋. Soy **Nicolas Navares** y este repositorio recoge mi trabajo final para el módulo de Criptografía del Bootcamp Full Stack de Ciberseguridad en **KeepCoding**.

Este proyecto ha sido un reto muy intenso. Aquí he documentado las 15 prácticas solicitadas, peleándome con algoritmos de cifrado, firmas digitales y entendiendo cómo proteger la información (y cómo romperla si no se hace bien).

---

## 📂 Índice de Ejercicios

Aquí están los 15 retos resueltos. He intentado explicar cada uno de forma sencilla en su propia carpeta:

| Carpeta | Temática | Lo que he aprendido / Qué he hecho |
| :--- | :--- | :--- |
| **[📂 Ejercicio 01](./Ejercicio%20-%201)** | **Disociación de Claves** | Cómo proteger claves usando XOR entre una parte fija en código y otra variable. |
| **[📂 Ejercicio 02](./ejercicio2)** | **Descifrado AES-CBC** | Descifrar mensajes, manejo de IVs y entender por qué el padding PKCS7 es vital. |
| **[📂 Ejercicio 03](./ejercicio3)** | **ChaCha20 + Poly1305** | Cifrado de flujo moderno y cómo garantizar la integridad del mensaje (AEAD). |
| **[📂 Ejercicio 04](./ejercicio4)** | **Seguridad en JWT** | Análisis de tokens, firmas HMAC y cómo evitar escaladas de privilegios. |
| **[📂 Ejercicio 05](./ejercicio5)** | **Hashing & Avalancha** | Diferencias entre SHA-2 y SHA-3 y demostración práctica del "Efecto Avalancha". |
| **[📂 Ejercicio 06](./ejercicio6)** | **Cálculo HMAC** | Verificar la autenticidad de una frase usando una clave secreta extraída de un Keystore. |
| **[📂 Ejercicio 07](./ejercicio7)** | **Passwords** | Análisis teórico: por qué no usar SHA-1 y cómo Argon2 protege mejor las contraseñas. |
| **[📂 Ejercicio 08](./ejercicio8)** | **Seguridad API REST** | Diseño teórico de un JSON seguro usando AES-GCM para proteger datos bancarios. |
| **[📂 Ejercicio 09](./ejercicio9)** | **KCV (Check Value)** | Calcular la "huella" de una clave AES usando tanto SHA-256 como cifrado de ceros. |
| **[📂 Ejercicio 10](./ejercicio10)** | **PGP & GPG** | Firmado y cifrado de correos/archivos en un escenario corporativo (RRHH vs Pedro). |
| **[📂 Ejercicio 11](./ejercicio11)** | **RSA-OAEP** | Descifrar una clave de sesión con RSA y entender por qué el cifrado cambia cada vez. |
| **[📂 Ejercicio 12](./ejercicio12)** | **AES-GCM & Nonces** | El peligro de reutilizar el "Nonce" y cómo cifrar correctamente un mensaje. |
| **[📂 Ejercicio 13](./ejercicio13)** | **Firmas Digitales** | Comparativa visual entre firmas clásicas (RSA) y Curvas Elípticas (Ed25519). |
| **[📂 Ejercicio 14](./ejercicio14)** | **Derivación (HKDF)** | Cómo generar claves únicas por dispositivo usando una clave maestra y un Salt. |
| **[📂 Ejercicio 15](./ejercicio15)** | **Bloques TR-31** | Análisis y decodificación de bloques de claves usados en entornos bancarios. |

---

## 🛠️ Librerías y Herramientas

Para resolver estos retos he tenido que investigar y trabajar con varias librerías de Python. Estas son las principales que he usado:

* `pycryptodome` (La base para casi todo: AES, ChaCha20, RSA...)
* `cryptography`
* `pyjks` (Para leer los ficheros del Keystore)
* `psec` (Para los bloques TR-31)
* `argon2-cffi` (Para hashing de contraseñas seguro)
* `ed25519` (Para firmas con curvas elípticas)

Para instalarlas todas de golpe:

```bash
pip install pycryptodome cryptography pyjks psec argon2-cffi ed25519
También he usado herramientas externas como KeyStore Explorer (para ver las claves gráficamente), CyberChef y GPG en la terminal.

💡 Nota: Soy principiante en el mundo de la criptografía. Es probable que mi código no sea perfecto, pero funciona y me ha servido para entender de verdad cómo funciona la seguridad por debajo.

Hecho por Nicolas Navares. 🚀
