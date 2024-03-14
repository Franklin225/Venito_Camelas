from decimal import getcontext, Decimal

def base37_a_decimal(numero):
    getcontext().prec = 10  # Establecer la precisión deseada
    base37_chars = "0123456789abcdefghijklmnñopqrstuvwxyz"
    valor_decimal = Decimal(0)
    partes = numero.split('.')
    parte_entera = partes[0]
    parte_decimal = partes[1] if len(partes) > 1 else ''

    # Convertir la parte entera
    potencia = len(parte_entera) - 1
    for char in parte_entera:
        valor_decimal += Decimal(base37_chars.index(char)) * (Decimal(37) ** Decimal(potencia))
        potencia -= 1

    # Convertir la parte decimal
    potencia = -1
    for char in parte_decimal:
        valor_decimal += Decimal(base37_chars.index(char)) * (Decimal(37) ** Decimal(potencia))
        potencia -= 1

    return valor_decimal

def decimal_a_base37(decimal):
    base37_chars = "0123456789abcdefghijklmnñopqrstuvwxyz"
    base37_string = ""
    parte_entera = int(decimal)
    parte_decimal = decimal - parte_entera

    # Convertir la parte entera
    while parte_entera > 0:
        parte_entera, rem = divmod(parte_entera, 37)
        base37_string = base37_chars[rem] + base37_string

    base37_string += '.'

    # Convertir la parte decimal
    while parte_decimal > 0:
        parte_decimal *= 37
        digit = int(parte_decimal)
        base37_string += base37_chars[digit]
        parte_decimal -= digit
        if len(base37_string) > 10:  # Limitar la longitud de la cadena base37
            break

    return base37_string

# Convertir los números a base decimal
num1 = base37_a_decimal("f8ñahtxz")
num2 = base37_a_decimal("map")

# Realizar la división
resultado_decimal = num1 / num2

# Convertir el resultado a base 37
resultado_base37 = decimal_a_base37(resultado_decimal)

print("Resultado de la división en base 37:", resultado_base37)