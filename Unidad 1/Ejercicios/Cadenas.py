"""
    Escribir un programa que pregunte el nombre de un producto, su precio y su numero de unidades.
    Mostrar en pantalla el nombre del producto, seguido de su precio unitario con 
    seis digitos enteros y dos decimales, el numero de unidades con 3 digitos y el 
    costo total con 8 digitos y 2 decimales.
"""

import string

nombre = input("Nombre del producto: ");
precio = float(input("Precio: "));
cantidad = int(input("Cantidad: "));

print("\nResultados:");
print(" - {0} | ${1:,.2f} costo unitario | {2} unidades | ${3:,.2f} costo total.".format(nombre, precio, cantidad, precio * cantidad));