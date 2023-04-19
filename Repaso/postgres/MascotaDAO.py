from Mascota import Mascota
from cursorDelPool import CursorDelPool

class MascotaDAO:
    _SELECCIONAR= "SELECT * FROM mascota ORDER BY idMascota"
    _INSERTAR = "INSERT INTO mascota(nombre,raza,edad) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE mascota SET nombre = %s, raza = %s, edad = %s WHERE idMascota = %s"
    _ELIMINAR = "DELETE FROM mascota WHERE idMascota = %s"
    _Buscar = "SELECT * FROM mascota WHERE edad > 10"
    _raza = "SELECT * FROM mascota WHERE raza = %s"
    

