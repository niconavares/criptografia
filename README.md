# 🔐 Práctica Final - Criptografía

![Status](https://img.shields.io/badge/Estado-En%20Progreso-orange?style=for-the-badge)
![Bootcamp](https://img.shields.io/badge/KeepCoding-Ciberseguridad-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge&logo=python&logoColor=white)

Hola 👋. Soy **Nicolas Navares** y este repositorio recoge mi trabajo final para el módulo de Criptografía del Bootcamp Full Stack de Ciberseguridad en **KeepCoding**.

Este proyecto está siendo un reto muy intenso. Aquí no solo subo las soluciones, sino que intento documentar el "porqué" de las cosas, peleándome con algoritmos de cifrado, firmas digitales, curvas elípticas y entendiendo cómo proteger la información (y cómo romperla si no se hace bien).

---

## 📂 Índice de Ejercicios

El proyecto consta de 15 retos que cubren todo lo visto en el módulo. Aquí está mi progreso actual:

### ✅ Ejercicios Realizados

| Carpeta | Temática | Lo que he aprendido |
| :--- | :--- | :--- |
| **[📂 Ejercicio 1](./Ejercicio%20-%201)** | **Disociación de Claves** | [cite_start]Cómo proteger claves usando XOR entre código fijo y variables dinámicas [cite: 111-114]. |
| **[📂 Ejercicio 2](./ejercicio2)** | **Descifrado AES-CBC** | [cite_start]Descifrar mensajes, manejo de IVs y entender por qué el padding PKCS7 es vital [cite: 119-125]. |
| **[📂 Ejercicio 3](./ejercicio3)** | **ChaCha20 + Poly1305** | [cite_start]Cifrado de flujo moderno y cómo garantizar la integridad del mensaje (AEAD) [cite: 127-130]. |
| **[📂 Ejercicio 4](./ejercicio4)** | **Seguridad en JWT** | [cite_start]Análisis de tokens, firmas HMAC y cómo evitar escaladas de privilegios [cite: 139-147]. |
| **[📂 Ejercicio 5](./ejercicio5)** | **Hashing & Avalancha** | Diferencias entre SHA-2 y SHA-3. [cite_start]Demostración práctica del "Efecto Avalancha" [cite: 149-163]. |
| **[📂 Ejercicio 6](./ejercicio6)** | **Cálculo HMAC** | [cite_start]Verificar la autenticidad de una frase usando una clave secreta de un Keystore[cite: 164]. |

### ⏳ Próximos Ejercicios (En proceso)

| Carpeta | Temática | Descripción del reto |
| :--- | :--- | :--- |
| **[📂 ejercicio7](./ejercicio7)** | **Almacenamiento Passwords** | [cite_start]Análisis de SHA-1 vs SHA-256 y estrategias de salting para bases de datos [cite: 166-173]. |
| **[📂 ejercicio8](./ejercicio8)** | **Seguridad API REST** | [cite_start]Cómo asegurar campos confidenciales (JSON) sin usar TLS [cite: 174-205]. |
| **[📂 ejercicio9](./ejercicio9)** | **KCV (Key Check Value)** | [cite_start]Calcular valores de control para verificar claves AES y SHA [cite: 212-217]. |
| **[📂 ejercicio10](./ejercicio10)** | **PGP & GPG** | [cite_start]Firmado y cifrado de correos/archivos en un escenario corporativo (RRHH) [cite: 218-230]. |
| **[📂 ejercicio11](./ejercicio11)** | **RSA-OAEP** | [cite_start]Cifrado asimétrico para proteger claves de sesión en videollamadas [cite: 239-252]. |
| **[📂 ejercicio12](./ejercicio12)** | **AES-GCM & Nonces** | [cite_start]Análisis de vulnerabilidades por reutilización de nonces en GCM [cite: 253-266]. |
| **[📂 ejercicio13](./ejercicio13)** | **Firmas Digitales** | [cite_start]Comparativa entre firmas clásicas (RSA PKCS#1) y Curvas Elípticas (Ed25519) [cite: 267-270]. |
| **[📂 ejercicio14](./ejercicio14)** | **Derivación de Claves** | [cite_start]Uso de HKDF-SHA512 para generar claves maestras únicas por dispositivo [cite: 271-279]. |
| **[📂 ejercicio15](./ejercicio15)** | **Bloques TR31** | [cite_start]Análisis de seguridad en bloques de claves bancarias (Key Blocks) [cite: 280-295]. |

---

## 🛠️ Librerías y Herramientas

Para resolver estos retos he tenido que investigar y trabajar con varias librerías específicas de Python. Estas son las dependencias principales del proyecto:

* `pycryptodome` (La base para casi todo: AES, ChaCha20, RSA...)
* `cryptography`
* `pyjks` (Para leer los ficheros `.jks` y `.jceks` del Keystore)
* `psec`
* `argon2-cffi` (Para hashing de contraseñas seguro)
* `ed25519` (Para firmas con curvas elípticas)

Para instalarlas todas de golpe:

```bash
pip install pycryptodome cryptography pyjks psec argon2-cffi ed25519