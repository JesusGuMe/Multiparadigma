#Estructuras de control

#El if

# a = 4
# b = 0
# if b!=0:
#     print(a/b)
# print(b)

# a=10
# if a > 5 and a < 15:
#     print("A es mayor que 5 pero menor que 15")

# if a > 5: print("es > 5"); print("Dentro del if");print(a+b)

# x = 5
# if x==5 :
#     print("Es 5")
# else:
#     print("No es 5")

# x = 8
# if x == 5:
#     print("Es 5")
# elif x == 6:
#     print("Es 6")
# elif x==7:
#     print("Es 7")
# else:
#     print(x)

# print("Es 8" if x == 8 else "No es 5")

# a = 10
# b = 0
# c = a/b if b!=0 else -1
# print(c)

#El for

# for i in "python":
#     print(i)

# lista = [
#     [56,34,2], 
#     [12,4,5], 
#     [9,3,2]
#     ]
# for i in lista:
#     for j in i:
#         print(j)


# funciones range

# r = range(6)
# print(r)

# for r in range(3):
#     print(r)

# for i in range(5,22,2):
#     print(i)

# cadena = "pythonypt"
# for letra in cadena:
#     if letra == "y":
#         print(letra)
#         break

# for letra in cadena:
#     if letra == "t":
#         print(letra)
#         continue
    
# for letra in cadena:
#     if letra == "p":
#         continue
#     print(letra)

# El while

# x = 5 
# while x > 0:
#     x -=1
#     print(x)

# x= 5
# while x>0: x-=1;print(x)

# x= 5
# while x>0:
#     x -=1
#     print(x)
# else:
#     print("Bucle finalizado")
#     x=5

# while x>0:
#     x-=1
#     print(x)
#     if x==4:
#         break
# else:
#     print("Fin del bucle")

# z = 7
# x = 1
# while z > 0:
#     print(' ' *z + '*' *x + ' ' *z)
#     z-=1
#     x+=2