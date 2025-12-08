import os
import subprocess
import tempfile
import shutil

# Trabajo de Criptografía - Ejercicio 10
# Me ha costado muchisimo hacer que esto funcione con Python :S
# Al final he tenido que usar 'subprocess' para llamar a los comandos de gpg del PDF

# ==========================================
# DATOS
# ==========================================

# Copio y pego las claves aquí porque si no se me pierden los archivos
clave_pedro_publica = """-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEYrhG/BYJKwYBBAHaRw8BAQdADXLwl3iCWWDNmKoBmZ+/rKdz+8ulKz4cK7Pj
PdZu8Fy0NVBlZHJvIFBlZHJpdG8gUGVkcm8gPHBlZHJvLnBlZHJpdG8ucGVkcm9A
ZW1wcmVzYS5jb20+iJkEExYKAEEWIQQb3mNeTq5uaN+tL3zXML4ZbkZhAQUCYrhG
/AIbAwUJA8JnAAULCQgHAgIiAgYVCgkICwIEFgIDAQIeBwIXgAAKCRDXML4ZbkZh
AYAfAP4xudXYKg3d59Doa3eswATu+r1dfqXk6xbPHd7rTD5bbwEAjar0HIi7Xi3M
0m7LMRGEx5CKcSZYbkCXYwaAyUWm5w+4OARiuEb8EgorBgEEAZdVAQUBAQdANwkF
l/zIRjpNCCwhe6c4NDaEcdmegYUrsahIf+/6MmsDAQgHiH4EGBYKACYWIQQb3mNe
Tq5uaN+tL3zXML4ZbkZhAQUCYrhG/AIbDAUJA8JnAAAKCRDXML4ZbkZhAVusAQD3
PRwejqYh8WLV1sWPlDKkaU+vnfUaRYkpesu7ZSklbAD9EnmAr+dVK2VOW9e3f8h0
5VxGZQQMnBylOKKilTQM7gw=
=O3za
-----END PGP PUBLIC KEY BLOCK-----"""

clave_pedro_privada = """-----BEGIN PGP PRIVATE KEY BLOCK-----

lIYEYrhG/BYJKwYBBAHaRw8BAQdADXLwl3iCWWDNmKoBmZ+/rKdz+8ulKz4cK7Pj
PdZu8Fz+BwMCrqURvfXP1kn7E+b6ReWgTiyEZb+/Y3ltTX1JxW4ms+uwWv/ZeyqN
pyb38GvcqjH65shub28SdT+Rt31dmfiZvyQ9/zceoReLv4wuau3xIbQ1UGVkcm8g
UGVkcml0byBQZWRybyA8cGVkcm8ucGVkcml0by5wZWRyb0BlbXByZXNhLmNvbT6I
mQQTFgoAQRYhBBveY15Orm5o360vfNcwvhluRmEBBQJiuEb8AhsDBQkDwmcABQsJ
CAcCAiICBhUKCQgLAgQWAgMBAh4HAheAAAoJENcwvhluRmEBgB8A/jG51dgqDd3n
0Ohrd6zABO76vV1+peTrFs8d3utMPltvAQCNqvQciLteLczSbssxEYTHkIpxJlhu
QJdjBoDJRabnD5yLBGK4RvwSCisGAQQBl1UBBQEBB0A3CQWX/MhGOk0ILCF7pzg0
NoRx2Z6BhSuxqEh/7/oyawMBCAf+BwMCbCCJhCFLXyn7hpKe4dHwM3UmoQJ2J7Pf
8DbmdQ6gANww3TTuVyNZns4TJIK1yc8OOUEJM+OiiU1S7Wu2SxB1N8qiolT6IW74
W/ZERyJpHoh+BBgWCgAmFiEEG95jXk6ubmjfrS981zC+GW5GYQEFAmK4RvwCGwwF
CQPCZwAACgkQ1zC+GW5GYQFbrAEA9z0cHo6mIfFi1dbFj5QypGlPr531GkWJKXrL
u2UpJWwA/RJ5gK/nVStlTlvXt3/IdOVcRmUEDJwcpTiiopU0DO4M
=TwUq
-----END PGP PRIVATE KEY BLOCK-----"""

clave_rrhh_publica = """-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEYrf4FBYJKwYBBAHaRw8BAQdAzE225Rvjhfdfj9KUhNzZC1irOgGgGeb5Ll1j
dHNp0jS0EFJSSEggPFJSSEhAUlJISD6ImQQTFgoAQRYhBPKx0OiVjfLTvbahBThp
gDxoTSh7BQJit/gUAhsDBQkDwmcABQsJCAcCAiICBhUKCQgLAgQWAgMBAh4HAheA
AAoJEDhpgDxoTSh7bxABALBTqforDq/psjs0slYi4nu49FhC/l7Hgg5MAWycHzfn
AP0ZjBN/kreafHhyeG+D5EwVJIGvJGEQDr+rbuRQc8CgC7g4BGK3+BQSCisGAQQB
l1UBBQEBB0DtQMlHTj+mOs7dB+btDBReycmBKDYjpKYRv9HetaE1HgMBCAeIfgQY
FgoAJhYhBPKx0OiVjfLTvbahBThpgDxoTSh7BQJit/gUAhsMBQkDwmcAAAoJEDhp
gDxoTSh79sMA/Ag83Kr69fMUFsmadW3FVjBKYY0VsgMIV5ELAelGMl4OAP0VwoMM
Uctb/HgCdUxK0xkIPyZ6X2sOCoTsGZUnlE5jBQ==
=i2AB
-----END PGP PUBLIC KEY BLOCK-----"""

clave_rrhh_privada = """-----BEGIN PGP PRIVATE KEY BLOCK-----

lIYEYrf4FBYJKwYBBAHaRw8BAQdAzE225Rvjhfdfj9KUhNzZC1irOgGgGeb5Ll1j
dHNp0jT+BwMCevp8FHb+LPr2E3iSpdOuf+XcZNQKHQHngA7Qd9BJQy5WuUNz636w
WAgJ9X0nCXgzymGgLD2wDGX7KhTMPsJeasqgvAtvs2OCvBg3PR/3c7QQUlJISCA8
UlJISEBSUkhIPoiZBBMWCgBBFiEE8rHQ6JWN8tO9tqEFOGmAPGhNKHsFAmK3+BQC
GwMFCQPCZwAFCwkIBwICIgIGFQoJCAsCBBYCAwECHgcCF4AACgkQOGmAPGhNKHtv
EAEAsFOp+isOr+myOzSyViLie7j0WEL+XseCDkwBbJwfN+cA/RmME3+St5p8eHJ4
b4PkTBUkga8kYRAOv6tu5FBzwKALnIsEYrf4FBIKKwYBBAGXVQEFAQEHQO1AyUdO
P6Y6zt0H5u0MFF7JyYEoNiOkphG/0d61oTUeAwEIB/4HAwKdPLew5SLUHPZtTt41
PPer4naM2o0VU31Wu/XOYO41x7tbtsgUQmuD9Ovc4Zio9boLGIm0bKRv0eDJyRQw
KDbaJmTSkM9frKEZNzPjFYJjiH4EGBYKACYWIQTysdDolY3y0722oQU4aYA8aE0o
ewUCYrf4FAIbDAUJA8JnAAAKCRA4aYA8aE0oe/bDAPwIPNyq+vXzFBbJmnVtxVYw
SmGNFbIDCFeRCwHpRjJeDgD9FcKDDFHLW/x4AnVMStMZCD8mel9rDgqE7BmVJ5RO
YwU=
=+1CU
-----END PGP PRIVATE KEY BLOCK-----"""

mensaje_firmado_pedro = """-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Se debe ascender inmediatamente a Raúl. Es necesario mejorarle sus condiciones económicas un 20% para que se quede con nosotros.
-----BEGIN PGP SIGNATURE-----

iJYEARYKAD4WIQQb3mNeTq5uaN+tL3zXML4ZbkZhAQUCYrhHNSAccGVkcm8ucGVk
cml0by5wZWRyb0BlbXByZXNhLmNvbQAKCRDXML4ZbkZhAcUcAP9G6wAIZDFlR1Q9
TCIJuLEHj6LTRTNkATS4smub+/+88gD+JlAZHDMhx3wThhfJq07TBmD+EBJNgv76
AEBhvVWvKgw=
=e8AU
-----END PGP SIGNATURE-----"""

# Mensajes que tengo que procesar
txt_firma = "Viendo su perfil en el mercado, hemos decidido ascenderle y mejorarle un 25% su salario.\nSaludos."
txt_cifrar = "Estamos todos de acuerdo, el ascenso será el mes que viene, agosto, si no hay sorpresas."

# --------------------------------------------------------------------------------
# EMPIEZA LO DIFICIL
# --------------------------------------------------------------------------------

# Creo una carpeta temporal para que no se me llene el escritorio de basura de gpg
carpeta_tmp = tempfile.mkdtemp()
print("He creado esta carpeta temporal:", carpeta_tmp)


# 1. IMPORTAR CLAVES 
print("\n[+] Importando las claves al anillo temporal...")

# Importo la publica de Pedro
# Tuve que mirar en internet como pasar el string por input
subprocess.run(["gpg", "--homedir", carpeta_tmp, "--import"], input=clave_pedro_publica, capture_output=True, text=True)

# Importo la privada de Pedro
subprocess.run(["gpg", "--homedir", carpeta_tmp, "--import"], input=clave_pedro_privada, capture_output=True, text=True)

# Importo la publica de RRHH
subprocess.run(["gpg", "--homedir", carpeta_tmp, "--import"], input=clave_rrhh_publica, capture_output=True, text=True)

# Importo la privada de RRHH
subprocess.run(["gpg", "--homedir", carpeta_tmp, "--import"], input=clave_rrhh_privada, capture_output=True, text=True)


# IMPORTANTE: Las claves son viejas (2022) y me daban error todo el rato.
# Encontré este parametro --faked-system-time para engañar a GPG y que piense que estamos en 2022
truco_fecha = "--faked-system-time=20220701T000000"


# 2. VERIFICAR FIRMA
# El PDF dice: gpg --verify doc.sig doc
print("\n[+] Voy a VERIFICAR la firma de Pedro...")

# Primero tengo que guardar el mensaje en un fichero porque gpg lo pide asi
fichero_mens = os.path.join(carpeta_tmp, "mensaje_pedro.sig")
with open(fichero_mens, "w") as f:
    f.write(mensaje_firmado_pedro)

cmd_verificar = [
    "gpg",
    "--homedir", carpeta_tmp,
    "--verify",
    truco_fecha, # Sin esto fallaba
    fichero_mens
]
# Ejecuto y rezo
res = subprocess.run(cmd_verificar, capture_output=True, text=True)
# La salida de verify sale por stderr, a saber por que
print(res.stderr)


# 3. FIRMAR
# El PDF dice: gpg --clearsign doc
print("\n[+] Voy a FIRMAR el mensaje de RRHH...")

cmd_firmar = [
    "gpg",
    "--homedir", carpeta_tmp,
    "--clearsign", # firmo en claro
    truco_fecha,
    "--local-user", "RRHH" # Le digo que soy RRHH
]

res = subprocess.run(cmd_firmar, input=txt_firma, capture_output=True, text=True)
print("Resultado de la firma:")
print(res.stdout)


# 4. CIFRAR
# El PDF dice: gpg --encrypt --recipient <id> ...
print("\n[+] Voy a CIFRAR para Pedro y RRHH...")

cmd_cifrar = [
    "gpg",
    "--homedir", carpeta_tmp,
    "--encrypt",
    truco_fecha,
    "--armor", # para que sea ascii
    "--recipient", "Pedro", # Para Pedro
    "--recipient", "RRHH",  # Para mi mismo (RRHH)
    "--trust-model", "always" # Esto lo puse porque me pedia confirmar confianza
]

res = subprocess.run(cmd_cifrar, input=txt_cifrar, capture_output=True, text=True)
print("Mensaje cifrado final:")
print(res.stdout)


# Borro todo al acabar
shutil.rmtree(carpeta_tmp)

