"""
    Escribir un programa en el cual se pide una frase y una letra, escribir o
    imprimir en pantalla el numero de veces que se repite la letra.
"""

frase = input("Palabra en la que se va a buscar: ");
letra = input("Letra a contar: ");
contador = 0;

for i in frase:
    if i == letra:
        contador += 1;
print("La letra " + letra + " aparece " + str(contador) + " vez/veces en la palabra " + frase)
print(contador);