#| 2   | Modificar listas | Lista de compras: agrega 3 items, elimina 1, muestra la lista final    |

lista_compras = ["Huevo"]
nueva_compra = ["Leche", "Frutas", "Chettos"]
lista_compras.extend(nueva_compra)
print(lista_compras)

lista_compras.remove("Leche") #Aquí especifico el texto

print(lista_compras)

lista_compras.pop(2) #Aquí especifico el lugar
print(lista_compras)