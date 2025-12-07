# Ejercicio 15 – Bloques de Claves TR-31

Este ha sido el último reto y, sinceramente, el que más "miedo" me daba al principio. Nos han enviado un **Key Block TR-31**.

Por lo que he leído, esto es un estándar que usan los bancos para enviar claves de forma segura. No envían la clave "a pelo", sino que la envuelven en un bloque que tiene una cabecera (información) y la clave cifrada dentro.

El bloque que nos han dado es este "chorizo" de caracteres:
`D0144D0AB00S000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B`

---

## 🧐 Análisis del Bloque (Las Respuestas)

Para entender qué significa ese bloque, he usado un script en Python y una herramienta online. Analizando la cabecera (los primeros caracteres), he podido responder a las preguntas del profesor:

1.  **¿Con qué algoritmo se ha protegido el bloque?**
    * **Respuesta:** TDES (Triple DES) o AES Key Derivation (según la versión D). La cabecera empieza por `D`, lo que indica la versión del bloque.

2.  **¿Para qué algoritmo se ha definido la clave de dentro?**
    * **Respuesta:** AES. Lo sé porque en la cabecera aparece una `A` en la posición del algoritmo.

3.  **¿Para qué modo de uso se ha generado?**
    * **Respuesta:** `B` (Both). Significa que sirve tanto para cifrar como para descifrar.

4.  **¿Es exportable?**
    * **Respuesta:** Sí. Aparece la letra `S` (Sensitive), que indica que se puede exportar pero con cuidado (bajo otra clave de confianza).

5.  **¿Para qué se puede usar la clave?**
    * **Respuesta:** `D0` (Data Encryption). Es una clave genérica para cifrar datos.

---

## 🔓 Descubriendo la Clave Oculta

Lo más importante era "desenvolver" (unwrap) el bloque para ver la clave real que había dentro. Para eso necesitaba la **Clave de Transporte** (`A1A1...`) que nos dio el enunciado.

**¡Lo he conseguido!** El valor de la clave secreta es:
`C1C1C1C1C1C1C1C1C1C1C1C1C1C1C1C1`

---

### 📌 Mis Evidencias

Aquí muestro el script de Python haciendo el trabajo sucio y el análisis con una herramienta visual:

**1. Ejecución del script Python:**
![Script Python TR31](Ejercicio%20-%2015.png)

**2. Comprobación con herramienta online:**
![Decodificador TR31](Ejercicio%20-%2015-2.png)

---

## 💻 El código Python

He usado la librería `psec` que facilita mucho trabajar con estos bloques bancarios.

```python
from psec import tr31

def importar():
    """Importa y muestra información de un Key Block TR-31"""
    
    # Clave de transporte para desenvolver (unwrap) el bloque
    kbpk_b = bytes.fromhex("A1A10101010101010101010101010102")
    
    # El Bloque TR31 que nos han enviado
    kb_string = "D0144D0AB00S000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B"
    
    # Crear KeyBlock con la clave de transporte
    kb = tr31.KeyBlock(kbpk_b)
    
    # Cargar la cabecera para leer la info
    kb.header.load(kb_string)
    
    # Unwrappear (desenvolver) para sacar la clave real
    clave_unwrapped = kb.unwrap(kb_string)
    
    print("=" * 60)
    print("INFORMACIÓN DEL KEY BLOCK TR-31")
    print("=" * 60)
    print(f"Clave importada (hex):  {clave_unwrapped.hex().upper()}")
    print(f"Versión:                {kb.header.version_id}")
    print(f"Uso de clave:           {kb.header.key_usage}")
    print(f"Algoritmo:              {kb.header.algorithm}")
    print(f"Modo de uso:            {kb.header.mode_of_use}")
    print(f"Exportabilidad:         {kb.header.exportability}")
    print("=" * 60)

if __name__ == "__main__":
    importar()
