# Ejercicio 3 (Extra)
# Equipo 4: 19100195 y 18100199

def potenciade2(x):
    return(x and (not (x & (x - 1))))

k = int(input("Introducir K: "))
quebra = 0
segm = 1       # Si es impar, se comienza desde 1.
if k % 2 == 0: # Si es par, se inicializa en 2.
    segm = 2

while (segm < k):
    segm *= 2
    quebra += 1
    
# En caso de ser impar y una potencia de 2, se suma una quebrada y se multiplica la barra
if k % 2 != 0 and potenciade2(k + 1):
    segm *= 2
    quebra += 1
print(segm, quebra)