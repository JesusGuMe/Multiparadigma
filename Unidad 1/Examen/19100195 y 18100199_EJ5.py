# Ejercicio 5
# Equipo 4: 19100195 y 18100199

numero = int (input("Introducir un numero entre 0 y 9: ")) 
resultado = 0
listas = list()
def funcionListas(n): #Generamos las 10 listas de 10 elementos.
    lista = list()
    for x in range(n - 10, n) :
        lista.append(x)
    return lista

pos = 11
for x in range(0, 10) :
    sig = funcionListas(pos)
    pos += 10
    listas.append(sig)

for index in listas:
    resultado += index[numero]

print(resultado)