from decimal import Decimal, getcontext

def base37_a_decimal(numero):
    getcontext().prec = 10
    base37_chars = "0123456789abcdefghijklmnñopqrstuvwxyz"
    valor_decimal = Decimal(0)
    partes = numero.split('.')
    parte_entera = partes[0]
    parte_decimal = partes[1] if len(partes) > 1 else ''

    potencia = len(parte_entera) - 1
    for char in parte_entera:
        valor_decimal += Decimal(base37_chars.index(char)) * (Decimal(37) ** Decimal(potencia))
        potencia -= 1

    potencia = -1
    for char in parte_decimal:
        valor_decimal += Decimal(base37_chars.index(char)) * (Decimal(37) ** Decimal(potencia))
        potencia -= 1

    return valor_decimal

numero_base37 = "f8ññ.htxz"
valor_decimal = base37_a_decimal(numero_base37)
print("Número en base decimal:", valor_decimal)

def decimal_a_hexadecimal(decimal):
    hex_chars = "0123456789ABCDEF"
    hex_string = ""
    parte_entera = int(decimal)
    parte_decimal = decimal - parte_entera

    while parte_entera > 0:
        parte_entera, rem = divmod(parte_entera, 16)
        hex_string = hex_chars[rem] + hex_string

    hex_string += '.'

    while parte_decimal > 0:
        parte_decimal *= 16
        digit = int(parte_decimal)
        hex_string += hex_chars[digit]
        parte_decimal -= digit
        if len(hex_string) > 10:
            break

    return hex_string

valor_hexadecimal = decimal_a_hexadecimal(valor_decimal)
print("Número en base hexadecimal:", valor_hexadecimal)

def decimal_a_octal(decimal):
    octal_string = ""
    parte_entera = int(decimal)
    parte_decimal = decimal - parte_entera

    # Convertir la parte entera
    while parte_entera > 0:
        parte_entera, rem = divmod(parte_entera, 8)
        octal_string = str(rem) + octal_string

    octal_string += '.'

    while parte_decimal > 0:
        parte_decimal *= 8
        digit = int(parte_decimal)
        octal_string += str(digit)
        parte_decimal -= digit
        if len(octal_string) > 10:
            break

    return octal_string

valor_octal = decimal_a_octal(valor_decimal)
print("Número en base octal:", valor_octal)

def decimal_a_binario(decimal):
    binario_string = ""
    parte_entera = int(decimal)
    parte_decimal = decimal - parte_entera

    while parte_entera > 0:
        parte_entera, rem = divmod(parte_entera, 2)
        binario_string = str(rem) + binario_string

    binario_string += '.'

    while parte_decimal > 0:
        parte_decimal *= 2
        digit = int(parte_decimal)
        binario_string += str(digit)
        parte_decimal -= digit
        if len(binario_string) > 10:
            break

    return binario_string

valor_binario = decimal_a_binario(valor_decimal)
print("Número en base binaria:", valor_binario)