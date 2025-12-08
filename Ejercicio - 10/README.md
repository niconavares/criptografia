Hola, aquí entrego los archivos resultantes del Ejercicio 10. Es la primera vez que hago una práctica completa de criptografía en la terminal, así que he ido paso a paso y sacando capturas de todo para documentarlo (incluso de cuando me equivocaba).

Aquí explico lo que he hecho y qué captura corresponde a cada paso:

1. Preparación de las claves
Lo primero fue importar las claves públicas y privadas de Pedro y RRHH.

He ejecutado los 4 comandos de importación.

Todo ha salido bien, ponía "sin cambios" o "leídas".

📸 Evidencia: Se puede ver en la imagen 1.png.

2. Verificación de la firma (Paso 1)
Tenía que comprobar que el mensaje de Pedro era auténtico.

Aquí tuve un pequeño fallo al principio: escribí el nombre del archivo acabado en .txt.sig y me dio error porque no existía.

Luego me di cuenta, lo corregí quitando el .txt y ya me salió el mensaje de "Firma correcta" (Good signature).

📸 Evidencia: En la imagen 2.png se ven mis dos intentos y el resultado correcto al final.

3. Firmar la respuesta de RRHH (Paso 2)
Este paso me costó un poco más. Tenía que firmar mi respuesta simulando ser RRHH.

Como se ve en las capturas, al principio me salía un error de "signing failed" o "operación cancelada". Me puse un poco nervioso porque no sabía qué clave estaba cogiendo.

Al final, insistiendo y usando el comando correcto, se generó bien el archivo respuesta_rrhh.txt.sig.

📸 Evidencia: En 3.jpg y el principio de 4.jpg se ven esos intentos hasta que funcionó.

4. Cifrado del mensaje final (Paso 3)
Por último, cifré el mensaje de confirmación para que lo leamos solo Pedro y yo.

Al ejecutar el comando, la terminal me lanzó unas advertencias en plan "No hay seguridad de que esta clave pertenezca al usuario...".

Me asusté un poco, pero leí que tenía que confirmar la confianza, así que escribí "s" (sí) dos veces para aceptar las claves de Pedro y RRHH.

Al final hice un ls para comprobar que el archivo .gpg estaba ahí.

📸 Evidencia: Todo el proceso de las preguntas de seguridad está en 4.jpg y el resultado final en 5.jpg.

Resumen de archivos entregados:
En esta carpeta adjunto tanto los resultados como las pruebas:

Archivos del ejercicio:

respuesta_rrhh.txt.sig (Firma generada en el paso 2).

confirmacion.gpg (Archivo cifrado generado en el paso 3).

Capturas de pantalla del proceso:

1.png, 2.png, 3.jpg, 4.jpg, 5.jpg.

Espero que esté todo bien, ¡un saludo!
