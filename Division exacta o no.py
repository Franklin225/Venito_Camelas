numero1 = int (input ("escribe el primer numero:" ))
numero2 = int (input ("escribe el segundo numero:" ))

division = numero1 / numero2
residuo = numero1 % numero2

if residuo == 0: 
  mensaje = "es exacta"

else:
    mensaje = "no es exacta"

print ("El resultado de", numero1, "y", numero2, "es: ", division, "y su division", mensaje)