import Rectangulo as rec
# Si se quiere traer solo alguna clase del modulo se usa lo siguiente:
# from Rectangulo import Cuadrado
# from Rectangulo import *
miRectangulo = rec.Rectangulo(5,10)
miRectangulo._ancho = 16
miRectangulo._largo = 10
print(miRectangulo._ancho)
print(miRectangulo._largo)
print(miRectangulo._area)
miRectangulo.CalcularArea()
print(miRectangulo._area)
print(miRectangulo.Perimetro())

miCuadrado = rec.Cuadrado(6)
print(miCuadrado.Area())
print(miCuadrado.Perimetro())

# 1. Bucles
# 2. Cadenas
# 3. Condicionales
# 4. Diccionarios
# 5. Listas y Tuplas
# 6. Funciones
# 7. Tipos de datos
# 8. Clases y Objetos (Nuestro Equipo hara ejercicio sobre este tema)

# cadena = convertirADiccionario("ZZ ZZ ZZ ZZ Program Hola Cadena1 Cadena2 Mundo Mundo Programa");