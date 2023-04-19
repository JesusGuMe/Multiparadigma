from psycopg2 import pool
from logger_base import log

class Conexion:
    _DATABASE = "clase_db"
    _USERNAME = 'postgres'
    _PASSWORD = "Jm123423"
    _DBPORT = '5432'
    _HOST = "localhost"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def ObtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host = cls._HOST,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    port = cls._DBPORT,
                    database = cls._DATABASE
                )
                log.debug(f"Creacion del pool {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error("Error en el pool",e)
        else:
            return cls._pool

    @classmethod
    def ObtenerConexion(cls):
        conexion = cls.ObtenerPool().getconn()
        log.debug(f"Conexion obtenida {conexion}")
        return conexion

    @classmethod
    def LiberarConexion(cls,conexion):
        cls.ObtenerPool().putconn(conexion)
        log.debug(f"Conexion regresada: {conexion}")

    @classmethod
    def cerrarConexiones(cls):
        cls.ObtenerPool().closeall()

if __name__ == "__main__":
    conexion1=Conexion.ObtenerConexion()
    conexion2=Conexion.ObtenerConexion()
    conexion3=Conexion.ObtenerConexion()
    conexion4=Conexion.ObtenerConexion()
    conexion5=Conexion.ObtenerConexion()
    Conexion.LiberarConexion(conexion1)
    conexion6=Conexion.ObtenerConexion()
    log.debug(conexion1)
    log.debug(conexion2)
    log.debug(conexion3)
    log.debug(conexion4)
    