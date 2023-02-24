"""
    Una jugueteria vende 2 tipos de productos: payasos y muñecas.
    Hace su venta por correo y la logistica les cobra por peso del paquete.
    Se debe calcular el peso de los payasos y muñecas que se dan en cada paquete de manda.
    - Payaso 112g
    - Muñeca 75g
    Escribir un programa en el cual capture el numero de payasos y muñecas, 
    calcule el peso total del paquete y precio total envio si:
    - Por cada 100g de Payaso se cobra $2.5
    - Por cada 100g de Muñeca se cobra $2
"""

payasos = int(input("Cantidad de payasos: "));
munecas = int(input("Cantidad de muniecas: "));

pesoTotalPayasos = 112 * payasos;
pesoTotalMunecas = 75 * munecas;

costoTotalPayasos = pesoTotalPayasos * 2.5 / 100;
costoTotalMunecas = pesoTotalMunecas * 2 / 100;

print("El peso total es de:", pesoTotalPayasos + pesoTotalMunecas);
print("El costo total sera de: ${0:,.2f}".format(costoTotalMunecas + costoTotalPayasos));
