def ieee754_a_decimal(secuencia):
    signo = int(secuencia[0])
    exponente = int(secuencia[1:9], 2) - 127
    mantisa = 1 + sum([int(bit) * 2**(-i) for i, bit in enumerate(secuencia[9:], start=1)])

    numero_decimal = (-1)**signo * 2**exponente * mantisa
    return round(numero_decimal, 10)

secuencia_ieee754 = input("Introduce una secuencia en formato IEEE 754 de 32 bits: ")
numero_decimal = ieee754_a_decimal(secuencia_ieee754)
print("Número decimal:", numero_decimal)