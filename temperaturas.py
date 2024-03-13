print ("Convertidor de temperaturas")
while True:
    print ()
    print ("1.Convertir de Celsius a Kelvin y Farenheit")
    print ("2.Convertir de Farenheit a Celsius y Kelvin")
    print ("3.Convertir de Kelvin a Celsius y farenheit")
    print ("4.Salir")
    opcion= int (input ("Elige una opción: "))
    if opcion == 1:
        celsius= int (input ("Escriba la cantidad de grados celisus: "))
        kelvin= celsius + 273
        farenheit= (1.8 * celsius) + 32
        print (f"{celsius} Grados celsius equivalen a {kelvin} grados kelvin y {farenheit} grados farenheit")
    elif opcion == 2:
        farenheit= int (input ("Escriba la cantidad de grados Farenheit: "))
        celsius= (farenheit - 32) / 1.8
        kelvin= ((farenheit - 32) / 1.8) + 273.15
        print (f"{farenheit} Grados farenheit equivalen a {round(celsius, 1)} grados celsius y {round (kelvin, 1)} grados kelvin")
    elif opcion == 3:
         kelvin= int (input ("Escriba la cantidad de grados kelvin: "))
         celsius= kelvin - 273
         farenheit= 1.8 * (kelvin - 273.15) + 32
         print (f"{kelvin} Grados kelvin equivalen a {round(celsius, 1)} grados celsius y {round (farenheit, 1)} grados farenheit")
    elif opcion== 4:
        break
print ("")
print ("Gracias Alfredo :3")