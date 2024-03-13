print ("Calculador de gruesas, docenas y unidades.")
print ("")

Cantidad= int(input("Escriba una cantidad entera: "))

operación1 = Cantidad // 144
operación2 = Cantidad % 144
operación3 = operación2 // 12
operación4 = operación2 % 12

print (f"{Cantidad} Unidades son {operación1} gruesas, {operación3} docenas y {operación4} unidades.")