# PARTE 1
# Crear una clase llamada cuenta con los atributos titular(obligatorio) y cantidad(opcional), la clase
# debe contener lo siguiente: constructor donde los datos pueden estar vacios (self)
# los setters y getters de cada atributo pero el atributo de cantidad no se puede modificar utilizando
# el setter, un metodo mostrar que muestre los datos del objeto, un metodo ingresar y un metodo retirar 

# PARTE 2 
# Definir una clase llamada Cuenta Joven derivada de la anterior, a esta se le va a agregar un atributo
# bonificacion expresada en porcentaje
# En el constructor los setters y getters del nuevo atributo, los titulares de la cuenta tienen que
# ser mayores de edad, la retirada se podra realizar si es mayor de edad y cuenta con dinero en su 
# cuenta (No tenga numeros negativos)
# El metodo Mostrar debe de regresar el mensaje de cuenta joven y la bonificacion de la cuenta

import Cuenta as c

miCuenta = c.Cuenta("Jesus Meza",2000.0)
miCuenta.Mostrar()
miCuenta.Retirar(1000.0)
miCuenta.Mostrar()
miCuenta.Ingresar(6000)
miCuenta.Mostrar()

miJoven = c.Joven("Jesus Joven",710.0)
miJoven.edad = 19
miJoven.bono = 60
miJoven.Mostrar()
miJoven.Retirar(700.0)
miJoven.Mostrar()