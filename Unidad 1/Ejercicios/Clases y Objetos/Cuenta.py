class Cuenta:
    def __init__(self,titular= '',cant=0.0) -> None:
        self.__titular = titular
        self.__cantidad = cant
    
    @property
    def Titular(self):
        return self.__titular
    @Titular.setter
    def Titular(self,a):
        self.__titular = a
    
    @property
    def Cant(self):
        return self.__cantidad

    def Mostrar(self):
        print("El titular es: " + self.__titular)
        print("Su saldo es de: " + str(self.__cantidad))
    
    def Retirar(self,cantidad):
        self.__cantidad = self.__cantidad - cantidad
        
    def Ingresar(self,cantidad):
        self.__cantidad = self.__cantidad + cantidad

class Joven(Cuenta):
    def __init__(self, titular='', cant=0.0, edad=0,bono=0.0) -> None:
        super().__init__(titular, cant)
        self.__edad = edad
        self.__bono = bono
    @property
    def edad(self):
        return self.__edad

    
    @edad.setter
    def edad(self,edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad = 0
        else:
            self.__edad = edad


    @property
    def bono(self):
        return self.__bono
    @bono.setter
    def bono(self,a):
        self.__bono = a
    
    def esMayorEdad(self):
        return self.edad >  17
    
    def Retirar(self, cantidad):
        if not self.esMayorEdad() or self.Cant <= 0:
            print ("No es posible realizar la operacion de retirar el dinero")
        elif self.Cant > 0:
            print("Cuenta Joven: " + self.Titular)
            print("El bono es de %" + str(self.__bono))
            super().Retirar(cantidad)
        
        