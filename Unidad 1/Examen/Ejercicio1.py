# Ejercicio 1
# Equipo 4: 19100195 y 18100149

n = int(input("Numero n: "));
m = int(input("Numero m: "));
lista = [n];

if m == 1 or n == 0 or m == 0:
    print("Secuencia invalida");
else :
    while n > 1 :
        res = n / m;
        lista.append(res);
        n = res;

    if n == 1 :
        print(lista)
    else :
        print("Secuencia invalida");