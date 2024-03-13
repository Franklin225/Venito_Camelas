#Crear un Programa en python que lea dos números enteros (n1 y n2). El programa debe calcular:
#La suma de n1 y n2
#La diferencia entre n1 y n2
#El producto de n1 y n2
#El cociente cuando es dividido n1 por n2
#El residuo cuando es divido n1 por n2

numero1 = int(input ("escribe el primer numero: "))
numero2 = int(input ("escribe el segundo numero "))
suma = numero1 + numero2
diferencia = numero1 - numero2
producto = numero1 * numero2
cociente = numero1 // numero2
residuo = numero1 % numero2
print("la suma de ", numero1, "y", numero2, "es: ", suma)
print("la diferencia de ", numero1, "y", numero2, "es: ", diferencia)
print("el producto de ", numero1, "y", numero2, "es: ", producto)
print("el cociente de ", numero1, "y", numero2, "es: ", cociente)
print("el residuo de ", numero1, "y", numero2, "es: ", residuo)