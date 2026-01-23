# Programa que pida precio y porcentaje de descuento, muestre precio final

precio = float(input("Dame el precio (puedes usar decimales): "))
descuento = int(input("Dame el porcentaje de descuento: "))

descuento_aplicar = descuento /100

descuento = precio * descuento_aplicar

total = precio - descuento

print("El total a pagar es de: $" + str(total))



