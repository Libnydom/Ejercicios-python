#| 2   | elif | Clasificador de edades: niño (0-12), adolescente (13-17), adulto (18-64), adulto mayor (65+)

edad = int(input("Escribe tu edad y diré qué clasificación tienes: "))

if edad >= 0 and edad < 13:
    print("Clasificación: niño.")
elif edad >= 13 and edad < 18:
    print("Clasificación: adolescente.")
elif edad >= 18 and edad < 65:
    print("Clasificación: adulto.")
else:
    print("Adulto Mayor")