# Ejercicio 8 – Seguridad en la API (Teórico)

Este ejercicio es diferente a los demás porque no hay que programar, sino pensar cómo arreglar un problema de seguridad.

Nos piden asegurar una API que envía datos bancarios (tarjetas, saldos...) "a pelo", sin usar HTTPS. [cite_start]Cualquiera podría leerlos o cambiarlos [cite: 452-455].

---

## 🧐 Mi solución propuesta

La verdad es que al principio me quedé un poco bloqueado porque no veía código, pero luego me acordé de **lo que le explicaste a Sergio en clase** sobre cómo proteger datos cuando el canal no es seguro.

Creo que la clave es no enviar los datos tal cual, sino cifrarlos nosotros mismos antes de enviarlos.

### ¿Qué algoritmo usaría?

[cite_start]Yo usaría **AES-256 en modo GCM**[cite: 3718].
* **¿Por qué?** Porque según entendí, este modo es el mejor porque hace dos cosas a la vez:
    1.  Cifra los datos para que nadie vea el número de la tarjeta (**Confidencialidad**).
    2.  Firma los datos para que, si alguien intenta cambiar el saldo o el destinatario, nos demos cuenta (**Integridad**).

---

## 📝 ¿Cómo quedaría el JSON?

Básicamente, la API ya no puede mandar los campos `usuario` o `tarjeta` a la vista. Tiene que mandar un "paquete cerrado".

Yo propongo cambiar el JSON para que sea así:

**1. Petición (Lo que enviamos):**
```json
{
  "idUsuario": 1,
  "iv": "a1b2c3d4...", 
  "ciphertext": "k8jhGs/92js...(aquí dentro van el usuario y la tarjeta cifrados)", 
  "tag": "f8a9b2..."
}
El idUsuario lo dejo fuera para que sepan quién soy, pero lo importante va oculto.

2. Respuesta (Lo que recibimos):

JSON

{
  "idUsuario": 1,
  "iv": "x9y8z7...",
  "ciphertext": "m1n2o3p4...(aquí dentro va el saldo y los movimientos)", 
  "tag": "c4d5e6..."
}
Creo que haciéndolo así cumplimos con lo que pide el ejercicio: que nadie lo lea y que nadie lo modifique sin que nos enteremos.
