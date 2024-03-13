print ("Convertidor de pies y pulgadas a centimetros")
print ("")

pies= int(input("Escriba la cantidad de pies: "))
pulgadas= int(input("Escriba la cantidad de pulgadas: "))

operacion1= 30.48*pies
operacion2= 2.54*pulgadas
operacion3= operacion1+operacion2

print (f"{pies} pies con {pulgadas} pulgadas es igual a {operacion3} centimetros")