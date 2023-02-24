#Tipos de Datos de Python
#numericos
#entero
#integer = 1
#IntegerNegative = -1
#zero = 0
#print(type(integer), integer, id(integer))
#print(type(IntegerNegative), IntegerNegative,id(IntegerNegative))
#print(type(zero),zero,id(zero))

#float
#floatNum= 3.5
#floatNegative = -3.5
#floatZero = 3.0
#print(type(floatNum), floatNum, id(floatNum))
#print(type(floatNegative), floatNegative, id(floatNegative))
#print(type(floatZero), floatZero, id(floatZero))

#complejos
#complexNum= 5j
#complexNum2 = 2 + 4j
#print(type(complexNum), complexNum)
#print(type(complexNum2), complexNum2)

#intToFloat = float(integer)
#floatToInt = int(floatNum)
#floatToComplex = complex(floatNegative)
#print(type(intToFloat),intToFloat)
#print(type(floatToInt),floatToInt)
#print(type(floatToComplex),floatToComplex)

#BOOLEANO

#y = 5
#x= 10
#print(bool(x==y))
#x= None
#print(bool(x))
#x=()
#print(bool(x))
#x={}
#print(bool(x))
#x=0.0
#print(bool(x))
#x= ''
#print(bool(x))

#Cadenas

#print(type("Hello"),"Hello")
#saludo = "Saludo"
#despedida= "Adios"
#print(saludo)
#print(saludo,end=',')
#Interpolacion
#print(f"Saludo: { saludo} , Despedida: {despedida}")
#print("""
#Esto 
#Es 
#Un Texto
#Multilinea
#""")

#print(f"""Saludo
#{saludo}
#Despedida
#{despedida}
#""")

#for letra in saludo:
    #print(letra)

#Revertir cadenas

# print(saludo[::-1])
# print(saludo)
# print(''.join(reversed(saludo)))

# Tuplas
# tupla = (1,2,3)
# print(tupla)
# tupla = 1,2,3
# print(type(tupla))
# print(tupla)
# # tupla[0] = 5
# tupla = 1,2,('a','b'),3
# print(tupla)
# print(tupla[2][0])
# tupla = 1,2,3
# x, y, z = tupla
# print(x,y,z)
# #Conversion de lista a tupla
# lista=[1,3,2]
# tupla = tuple(lista)

# for t in tupla:
#     print(t)
# # Tupla de un 1 elemento
# # tupla=(2,)
# tupla = (2,2,2,2,2,2,2,5,3,6)
# print(tupla.count(2))
# print(tupla.index(3))
# print(tupla.index(5,5))

# Listas
# lista = [1,2,3,5]
# lista = list("1234")
# print(lista)
# lista = [1, "Hola",3.67,[1,2,3]]
# print(lista)
# print(lista[0])
# print(lista[-2])
# print(lista[3][2])
# lista[3][2] = 100
# print(lista[3][2])

# l = [1,3,4,5,6,7,8,9]
# l2 = l[0:4]
# l3= [0,20,10]
# # l[0:3]=l3
# l+=l3

# print(l)

# x,y,z = l3
# print(x,y,z)

# lista = [1,2,3,4]
# for elemento in lista:
#     print(elemento)

# for index,l in enumerate(lista):
#     print(index,l)

# lista2 = ["c","z","a"]

# for l1,l2 in zip(lista,lista2):
#     print(l1,l2)

# for i in range(0,len(lista)):
#     print(lista[i])

# # Agregar elementos a la lista
# l =[2,3]
# l.append(3)
# print(l)
# l.extend([1,2,3,4])
# print(l)
# l.insert(0,100)
# print(l)

# # Remover elementos de la lista

# l.remove(100)
# print(l)
# l.pop()
# print(l)

# # La lista en reversa
# l.reverse()
# print(l)

# # Ordenar la lista, sort lo hace de menor a mayor
# l.sort()
# print(l)
# # Ordena la lista de mayor a menor
# l.sort(reverse=True)
# print(l)

# SETS
# No permiten datos duplicados.
# Son una lista mutable e inmatuble a la vez

# s = set([5,4,3,2,1,1,8])
# print(s)

# s = {5,4,6,8,8,1}
# print(s)

# s = {0}
# d = {}
# print(type(s))
# print(type(d))

# lista = ["Mexico", "España"]
# s = set(["USA", "Tlaxcala", "Mexico", "España"])
# print(s)

# s = {2,3}
# # Discard no marca error si se intenta con un elemento que no existe, remove si marca error sino existe
# s.discard(5)
# print(s)
# s.add(5)
# print(s)
# s.remove(3)
# print(s)

# s = {2,5,7,8,9,3,'a'}
# s.pop()
# print(s)
# s.clear()
# print(s)

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}

# print (s1.union(s2))

# print(s1.intersection(s2))

# Diccionario
# d1 = {
#     "Nombre": "Rocio",
#     "Edad": 24,
#     "Documento": 23233
# }
# print(d1)

# d2 = dict([('Nombre','Rocio'),('Edad', 24),('Documento', 2345)])
# print(d2)

# d3 = dict(Nombre = 'Rocio', Edad = 24, Documento = 332323)
# print(d3)

# print(d1["Nombre"])
# print(d1.get("Edad"))

# d1["Nombre"] = "Juan"
# print(d1)
# d1["Direccion"] = "Calle123"
# print(d1)
# d1["obj"] = {"Curp":1212}
# for x in d1:
#     print(d1[x])

# for x,y in d1.items():
#     print(x,y)
#     if x == 'obj':
#         print(d1[x]["Curp"])

# d1 = {"a":1, "b":2}
# d2 = {"c":3, "d":4 }
# d = {
#     "d1":d1,
#     "d2":d2
# }
# print(d)

# d.clear()
# print(d)

# d = {"a":1, "b":2}
# print(d.get("c"))

# it = d.items()
# print(it)
# print(list(it))
# print(list(it)[0][1])

# k = d.keys()
# print(k)
# print(list(k)[1])

# d.pop('a')
# print(d)
# pop = d.pop('c', -1)
# print(pop)

# d.popitem()
# print(d)

# d1 = {"a":1, "b":2}
# d2 = {"a":233, "d":122 }
# d1.update(d2)
# d2.update(d1)
# print(d2)

# try:
#     pass
# except KeyError as e:
#     e.__cause__