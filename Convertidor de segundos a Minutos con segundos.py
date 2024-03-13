print ("convertidor de segundos")
print ("")

segundos= int(input("Escriba la cantidad de segundos: "))

operación1= segundos//60
operacion2= segundos%60

print (f"{segundos} segundos es igual a {operación1} minutos y {operacion2} segundos")