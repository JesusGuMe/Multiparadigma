# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla
# Preguntar al usuario por una fruta y el numero de kilos y muestre en pantalla el precio 
# de ese numero de kilos, si la fruta no esta en el diccionario, debe mostrar un mensaje 
# en base a eso
# Platano 1.35
# Manzana 0.80
# Pera 0.85
# Naranja 0.70
# n = 0
# DFrutas = { 
#     "Fruta": "Platano",
#     "Fruta2": "Manzana", 
#     "Fruta3": "Pera",
#     "Fruta4": "Naranja",
#     "Precio": "1.35",
#     "Precio2": "0.80",
#     "Precio3": "0.85",
#     "Precio4": "0.70"
# }

# f = input("Teclee la fruta: ")
# if f in DFrutas:
#     k = input("Teclee los kilos: ")
    


# print(DFrutas)


diccionario = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}


frutaElegida = input("Ingrese la fruta deseada: ")

kilos = int(input("Ingrese los kilos deseados: "))


print(diccionario.get(frutaElegida, "No existe!!"))


precioFrutaSeleccionada = diccionario[frutaElegida]

precioTotal = (kilos) * precioFrutaSeleccionada


print("El precio total es " + str(precioTotal) +
      " y " + "los kilos fueron " + str(kilos))
