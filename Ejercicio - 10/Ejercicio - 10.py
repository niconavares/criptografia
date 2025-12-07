import os
import subprocess
import tempfile
import shutil

# --- EJERCICIO 10: PGP ---
# Como no hay libreria de python para PGP instalada, usamos el comando 'gpg' del sistema.
# Es lo mas facil y "novato" para automatizar esto sin instalar cosas raras.

def run_gpg(args, input_data=None, homedir=None):
    # Funcion para ejecutar gpg
    cmd = ["gpg", "--batch", "--yes"]
    if homedir:
        cmd.extend(["--homedir", homedir])
    cmd.extend(args)
    
    result = subprocess.run(
        cmd, 
        input=input_data if input_data else None,
        capture_output=True,
        text=True
    )
    return result

# 1. DATOS (Hardcoded)

# Claves de Pedro
pedro_pub = """-----BEGIN PGP PUBLIC KEY BLOCK-----

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

pedro_priv = """-----BEGIN PGP PRIVATE KEY BLOCK-----

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

# Claves de RRHH
rrhh_pub = """-----BEGIN PGP PUBLIC KEY BLOCK-----

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

rrhh_priv = """-----BEGIN PGP PRIVATE KEY BLOCK-----

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

# Mensaje firmado original
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

# Mensajes nuevos
msg_para_firmar = "Viendo su perfil en el mercado, hemos decidido ascenderle y mejorarle un 25% su salario.\nSaludos."
msg_para_cifrar = "Estamos todos de acuerdo, el ascenso será el mes que viene, agosto, si no hay sorpresas."

# Crea una carpeta temporal para el anillo de claves (para no ensuciar el pc)
temp_dir = tempfile.mkdtemp()
print(f"Usando directorio temporal GPG: {temp_dir}")

try:
    # 2. IMPORTAR CLAVES
    print("\n--- Importando claves ---")
    run_gpg(["--import"], pedro_pub, temp_dir)
    run_gpg(["--import"], rrhh_priv, temp_dir)

    # PARAMETROS COMUNES
    # Las claves estan caducadas (son de 2022). Usamos fake-time para que funcionen.
    # Fecha: 2022-07-01
    fake_time_arg = "--faked-system-time=20220701T000000"

    # 3. VERIFICAR FIRMA
    # Guardamos el mensaje firmado en un archivo temp
    f_sig_path = os.path.join(temp_dir, "mensaje.sig")
    with open(f_sig_path, "w") as f:
        f.write(mensaje_firmado_pedro)
        
    print("\n--- Verificando firma de Pedro ---")
    # gpg --verify mensaje.sig
    res_verify = run_gpg(["--verify", fake_time_arg, f_sig_path], None, temp_dir)
    print(res_verify.stderr)
    
    # 4. FIRMAR MENSAJE (Como RRHH)
    print("\n--- Firmando mensaje como RRHH ---")
    res_sign = run_gpg(["--clearsign", fake_time_arg, "--local-user", "RRHH"], msg_para_firmar, temp_dir)
    print("Mensaje Firmado:")
    print(res_sign.stdout)
    
    # 5. CIFRAR MENSAJE (Para Pedro y RRHH)
    print("\n--- Cifrando mensaje ---")
    
    # Usamos UIDs parciales "Pedro" y "RRHH"
    res_enc = run_gpg(["--encrypt", fake_time_arg, "--recipient", "Pedro", "--recipient", "RRHH", "--armor", "--trust-model", "always"], msg_para_cifrar, temp_dir)
    
    print("Mensaje Cifrado:")
    print(res_enc.stdout)
    
finally:
    # Borramos carpeta temporal
    shutil.rmtree(temp_dir)
    print("\nLimpieza completada.")
