# x = 10.0
# print(x,end=', ')
# print(id(x),end=', ')
# print(type(x))

# lista = [1,4,5,6,3,2,7]
# lista.sort(reverse=True)
# print(lista)
# for elemento in lista:
#     print(elemento)

# se = {2,3,3,4,5,1,8,7}
# print(se)

# s = {0}
# d = {}
# print(type(s))
# print(type(d))

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

# s = set([5,4,3,2,1,1,8])
# print(s)

# s = {5,4,6,8,8,1}
# print(s)

# """
#     Ejercicio 1
# """

# n = int(input("Numero n: "));
# m = int(input("Numero m: "));
# lista = [n];

# if m == 1 or n == 0 or m == 0:
#     print("Secuencia invalida");
# else :
#     while n > 1 :
#         res = n / m;
#         lista.append(res);
#         n = res;

#     if n == 1 :
#         print(lista)
#     else :
#         print("Secuencia invalida");

# """
#     EJERCICIO 2
# """

# n1 = int(input('N1: ')[::-1])
# n2 = int(input('N2: ')[::-1])
# print(n1 if n1 > n2 else n2)

# """
#     EJERCICIO 3
# """

# def potencia2 (x) :
#     return (x and (not (x & (x - 1))));

# k = int(input("Ingresa k: "));

# quebradas = 0;
# segmentos = 1; # si es impar, empiezo desde 1
# if k % 2 == 0 : #si es par, empiezo en 2
#     segmentos = 2;

# while (segmentos < k) :
#     quebradas += 1;
#     segmentos *= 2;

# # Si es impar y es una potencia de 2, suma una quebrada y multiplicar barra
# if k % 2 != 0 and potencia2(k + 1):
#     segmentos *= 2;
#     quebradas += 1;

# print(segmentos, quebradas)

# """
#     EJERCICIO 4
# """

# def convertirADiccionario(palabras) :
#     list = palabras.split()
#     dic = {}
#     for item in list :
#         if(dic.get(item) == None) : #if item in dic
#             dic[item] = 1
#         else :
#             dic[item] = dic[item] + 1;

#     return dic

# def obtenerValorMayor(diccionario) :
#     mayor = 0;
#     for i,x in diccionario.items() :
#         if x > mayor :
#             mayor = x;
#     return mayor;

# def palabrasMasRepetidas(diccionario, mayor) :
#     lista = list();
#     for i, x in diccionario.items() :
#         if x == mayor :
#             lista.append(i);
#             lista.append(x);
    
#     return tuple(lista);

# # Como quieres que el te quiera si el que quiero que el quiera no me quiere como quiero que el quiera
# dicc = convertirADiccionario(input("Ingrese una oracion: "));
# mayor = obtenerValorMayor(dicc);
# print(palabrasMasRepetidas(dicc, mayor));

# """
#     EJERCICIO 5
# """

# def generarLista(n) :
#     lista = list();
#     for x in range(n - 10, n) :
#         lista.append(x);

#     return lista;

# listas = list(); mul = 11;
# for x in range(0, 10) :
#     aux = generarLista(mul);
#     mul += 10;
#     listas.append(aux);

# inicio = int(input("Ingrese un numero entre 0 y 9: "));
# res = 0;
# for lista in listas :
#     res += lista[inicio];

# print(res);

"""
    EJERCICIO 6
"""

def fun(a,b):
    a = set(a);
    b = set(b);
    return [list(a&b),list(a^b)];
    
# Prueba
a = ['a', 'b', 2, 2, 3];
b = ['c','d',2, 'a', 4];
print(fun(a,b));

# """
#     EXTRA
# """
# def fun(a,b):
#     a = set(a)
#     b = set(b)
#     return [list(a&b),list(a^b)]
# # Prueba
# a = ['a', 'b', 2, 2, 3]
# b = ['c','d',2, 'a', 4]
# print(fun(a,b))

# def sumando(n):
#     superLista = [[],[],[],[],[],[],[],[],[],[]]
#     cubeta = 0
#     inicio = 1
#     fin = 10
#     suma = 0
#     while cubeta < 10:
#         current = -1
#         for k,i in enumerate(range(inicio,fin+1)):
#             superLista[cubeta].append(i)
#             suma+= i if k == n else 0
#             current = i
#         inicio = current + 1
#         fin = inicio + 9
#         print(superLista[cubeta])
#         cubeta += 1
#     return suma

# n = int(input('Dame N: '))
# print(sumando(n))