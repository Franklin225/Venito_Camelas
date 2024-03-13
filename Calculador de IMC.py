print ("Calculador de IMC")
print ("")
Peso= int (input ("Escribe tu peso: "))
Altura= float (input ("Escribe tu altura: "))

imc= Peso / Altura ** 2

print (f"Tu indice de masa corporal es: {round (imc, 1)}")