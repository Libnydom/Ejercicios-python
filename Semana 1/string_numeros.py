# 1 | Strings y números | Crea un programa que pida tu nombre y edad, y calcule en qué año naciste 

año_actual = 2026
nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))
calculo = año_actual - edad

print ("Hola " + nombre + ", tienes " + str(edad) + ", por lo tanto, naciste el: " + str(calculo))
