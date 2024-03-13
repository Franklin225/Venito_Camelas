print ("Convertidor de segundos a horas, minutos y segundos.")
print ("")

segundos= int(input("Escriba la cantidad de segundos: "))

operación1= segundos//3600
operación2= segundos%3600
operación3= operación2//60
operación4= operación2%60

print (f"{segundos} segundos es igual a {operación1} horas con {operación3} minutos y {operación4} segundos")