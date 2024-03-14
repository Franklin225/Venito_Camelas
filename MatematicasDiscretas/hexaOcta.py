def hexadecimal_a_octal(hexadecimal):
    partes = hexadecimal.split('.')
    parte_entera = partes[0]
    parte_decimal = partes[1] if len(partes) > 1 else ''

    decimal_entera = int(parte_entera, 16)
    octal_entera = oct(decimal_entera)[2:]

    decimal_decimal = int(parte_decimal, 16) if parte_decimal else 0
    octal_decimal = oct(decimal_decimal)[2:] if parte_decimal else ''

    return octal_entera + ('.' + octal_decimal if octal_decimal else '')

hexadecimal = input("Introduce un número hexadecimal: ")
octal = hexadecimal_a_octal(hexadecimal)
print("Número en base octal:", octal)