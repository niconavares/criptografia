# Ejercicio 2 – Descifrado AES/CBC/PKCS7

Este ejercicio consiste en descifrar un texto cifrado con **AES en modo CBC** usando padding **PKCS7**. [cite_start]El objetivo es obtener el texto en claro y analizar cuánto padding se añadió[cite: 1, 2, 7].

---

### 📌 Captura del ejercicio
![Captura del ejercicio 2](captura-ejercicio2.png)

---

## 🔹 Enunciado

Se nos proporciona:
- [cite_start]Una clave hexadecimal del keystore etiqueta “cifrado-sim-aes-256”[cite: 2].
- [cite_start]Un IV compuesto por 16 bytes a cero (`00`)[cite: 2, 3].
- [cite_start]Un texto cifrado en Base64: `TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=`[cite: 5, 6].

También se plantean las preguntas:
1. [cite_start]Si lo desciframos, ¿qué obtenemos? [cite: 7, 8]
2. [cite_start]¿Qué ocurre si decidimos cambiar el padding a x923? [cite: 9]
3. [cite_start]¿Cuánto padding se ha añadido? [cite: 10]

---

## 🔹 Código Solución

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Clave que saque de la KeyStorePractica
clave_hex = "A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"
# El IV son todo ceros
iv_hex = "00000000000000000000000000000000"
# El texto cifrado en base64
texto_cifrado_b64 = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="

# Paso todo a bytes para poder usarlo
clave = bytes.fromhex(clave_hex)
iv = bytes.fromhex(iv_hex)
texto_cifrado = base64.b64decode(texto_cifrado_b64)

print("--- Empezando a descifrar ---")

# Configuro el descifrador AES en modo CBC
cipher = AES.new(clave, AES.MODE_CBC, iv)

# Descifro los datos
datos_descifrados_con_padding = cipher.decrypt(texto_cifrado)

# Le quito el padding (PKCS7)
datos_limpios = unpad(datos_descifrados_con_padding, AES.block_size, style='pkcs7')

# Muestro el resultado
print("Texto descifrado:", datos_limpios.decode('utf-8'))

# Calculo cuanto padding habia
total_bytes = len(datos_descifrados_con_padding)
bytes_utiles = len(datos_limpios)
padding_extra = total_bytes - bytes_utiles
print("Padding añadido:", padding_extra, "bytes")

# Respuesta a la pregunta del x923
print("\nSobre el padding x923:")
print("Si cambiamos a x923 daría error al descifrar.")
print("Porque PKCS7 rellena con el número de bytes (ej: 05 05 05 05 05)")
print("Y x923 rellena con ceros y solo el último es el número (ej: 00 00 00 00 05)")
🔹 Resultado del descifrado
Según la ejecución del script:

Texto descifrado: Esto es un cifrado en bloque típico. Recuerda, vas por el buen camino. Ánimo.

Padding añadido: 1 bytes

Sobre el padding X923: Si cambiamos a X923 daría error al descifrar porque PKCS7 rellena con el valor del byte repetido (ej: 05 05 05 05 05), mientras que X923 rellena con ceros y solo el último byte indica la longitud (ej: 00 00 00 00 05).
