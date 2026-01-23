#| 3   | Condiciones compuestas (and, or) | Validador: pide usuario y contraseña, solo deja pasar si ambos son correctos                 |

user = input("Usuario: ")
password = input("Contraseña: ")

if user ==  "Juan" and password == "Contra123":
    print("Adelante")
elif user != "Juan" or password != "Contra123":
    print("Un dato es incorrecto, intenta de nuevo.")