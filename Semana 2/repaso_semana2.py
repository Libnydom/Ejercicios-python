#| 4   | Repaso  | Piedra, papel o tijeras contra la computadora (usa `import random`)                          |

import random

play = ["Piedra","Papel","Tijera"]
maquina = random.choice(play)

jugador = input("Rápido, piedra, papel o tijera: ")

print("La máquina puso: " +maquina)
if jugador == maquina:
    print ("Intenta de nuevo") 
elif jugador == "Piedra" and maquina == "Tijera":
    print("Ganaste")
elif jugador == "Piedra" and maquina == "Papel":
    print("Perdiste")
elif jugador == "Papel" and maquina == "Piedra":
    print("Ganaste")
elif jugador == "Papel" and maquina == "Tijera":
    print("Perdiste")
elif jugador == "Tijera" and maquina == "Pepel":
    print("Ganaste")
elif jugador == "Tijera" and maquina == "Piedra":
    print("Perdiste")
else:
    print("Intenta de nuevo, alguna palabra no es compatible")