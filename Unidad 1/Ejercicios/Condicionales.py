# Una pizzeria ofrece pizzas vegetarianas y no vegetarianas a sus clientes con un listado de
# ingredientes para cada tipo de pizza que aparecen a continuacion:
# Ingredientes vegetarianos: Pimiento y tofu
# Ingredientes no vegetarianos: Peperoni, jamon, y salmon

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no 
# en función a su respuesta desplegar el menu con los ingredientes disponibles
# solo se puede elegir 2 ingredientes maximo, ademas la mozzarela y el tomate 
# estan en todas las pizzas yal final debe mostrar en pantalla si la pizza es vegetariana o no, y 
# todos los ingredientes de la pizza.


from tkinter import Menu


print("Escriba V si quiere Vegetariana o NV si no quiere vegetariana")
eleccion = input("Que pizza quiere?: ")
pizzaFinal = "MOZZARELA , TOMATE"
menuV = "PIMIENTA O TOFU "
menuNV = "PEPPERONI O JAMON O SALMON"

if eleccion == "V":
    print(menuV)
    ingredienteExtra= input("ESCRIBA EL INGREDIENTE DESEADO: ")
    print("La orden final sera una pizza VEGETERIANA con: " + str(pizzaFinal) + " y " + str(ingredienteExtra) )
elif eleccion == "NV":
    print(menuNV)
    ingredienteExtra= input("ESCRIBA EL INGREDIENTE DESEADO: ")
    print("La orden final sera una pizza NO VEGETARIANA con: " + str(pizzaFinal) + " y " + str(ingredienteExtra) )