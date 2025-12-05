#XOR de datos binarios
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])

#Desarrollo
# clave_codigo = B1EF2ACFE2BAEEFF
# clave_final_memoria = 91BA13BA21AABB12
# Buscamos: Key Manager 

m = bytes.fromhex("B1EF2ACFE2BAEEFF")
k = bytes.fromhex("91BA13BA21AABB12")
print("Desarrollo (Key Manager):", xor_data(m,k).hex().upper())

# B1EF2ACFE2BAEEFF XOR 91BA13BA21AABB12 = 20553975C31055ED

#Produccion
# clave_codigo = B1EF2ACFE2BAEEFF
# Key Manager (Properties) =  B98A15BA31AEBB3F
# Buscamos: Clave Final (Memoria)
# B1EF2ACFE2BAEEFF XOR B98A15BA31AEBB3F = 08653F75D31455C0
m = bytes.fromhex("B1EF2ACFE2BAEEFF")
k = bytes.fromhex("B98A15BA31AEBB3F")
print("Produccion (Clave Final):", xor_data(m,k).hex().upper())


""" print(xor_data(m,k).hex())

num1=0xAE12FF2235BC015F
num2=0x1E12BC2135BD016D
num3=(hex(num1^num2))
print(num3[2:]) """


