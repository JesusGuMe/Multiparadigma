from logger_base import log

class Persona:
    def __init__(self, idpersona = None, nombre=None, apellido=None, email=None, edad=None) -> None:
        self._idpersona = idpersona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._edad = edad
    
    def __str__(self) -> str:
        
        return f"""
        Id Persona: {self._idpersona}, Nombre: {self._nombre}
        Apellido: {self._apellido}, Email: {self._email}, Edad: {str(self._edad)}
        """
    
    @property
    def idPersona(self):
        return self._idpersona
    @idPersona.setter
    def idPersona(self, idpersona):
        self._idpersona = idpersona

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def Email(self):
        return self._email
    @Email.setter
    def Email(self, email):
        self._email = email

    @property
    def Apellido(self):
        return self._apellido
    @Apellido.setter
    def Apellido(self, apellido):
        self._apellido = apellido

    @property
    def Edad(self):
        return self._edad
    @Edad.setter
    def Edad(self, edad):
        self._edad = edad

if __name__ == "__main__":
    persona1 = Persona(1,"Juan", "Perez", "Jperez@gmail.com", 20)
    log.debug(persona1)