import struct

def decimal_a_ieee754(numero):
    packed = struct.pack('!f', numero)
    integers = [c for c in packed]
    binaries = [format(i, '08b') for i in integers]
    secuencia = ''.join(binaries)
    return secuencia

numero_decimal = float(input("Introduce un número decimal: "))
secuencia_ieee754 = decimal_a_ieee754(numero_decimal)
print("Secuencia en formato IEEE 754 de 32 bits:", secuencia_ieee754)