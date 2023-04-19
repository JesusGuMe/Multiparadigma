# Ejercicio 6 (Extra)
# Equipo 4: 19100195 y 18100199

def recibirListas(l1,l2): 
    a = set(l1)
    b = set(l2)
    return [list(a & b), list(a ^ b)]

# Usando la entrada del Ejemplo 1
lista1 = ['a', 'b', 2, 3]
lista2 = ['c', 'd', 3, 4]
print(recibirListas(lista1, lista2)) 

