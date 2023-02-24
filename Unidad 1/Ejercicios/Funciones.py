# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia
# Escribir otra funcion que reciba el diccionario y devuelva una tupla con la palabra mas repetida y su frecuencia

def convertirADiccionario(palabras) :
    list = palabras.split()
    dic = {}
    for item in list :
        if(dic.get(item) == None) : 
            dic[item] = 1
        else :
            dic[item] = dic[item] + 1
    print(dic)
    return dic
    

def palabraMasRepetida(diccionario) :
    mayor = 0
    keyMayor = ""
    for i, x in diccionario.items() :
        if(x > mayor) :
            mayor = x
            keyMayor = i
    return (keyMayor, mayor)

 
cadena = convertirADiccionario(input("Insertar cadena de palabras: "))
tupla = palabraMasRepetida(cadena)

for i,x in cadena.items() :
    print("La palabra", i, "se repite", x, "veces.")
print(tupla[0], tupla[1])