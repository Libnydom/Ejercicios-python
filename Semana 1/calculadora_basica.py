#| 3   | Inputs y conversiones   | Calculadora que pida 2 números y muestre suma, resta, multiplicación y división |

numero_uno = int(input ("Dame el primer número: "))
numero_dos = int(input("Dame el segundo número: "))

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
multiplicacion = numero_uno * numero_dos
division = numero_uno / numero_dos

print("Resultados: \n Suma: "+ str(suma)+".\n Resta: " + str(resta) + ". \n Multiplicación: " + str(multiplicacion)+
      ". \n División: "+str(division)+ ".")

