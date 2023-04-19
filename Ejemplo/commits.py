import psycopg2
from logger_base import log
conexion = psycopg2.connect(user="postgres",
                            password="Jm123423",
                            host="localhost",
                            port= 5432,
                            database="clase_db")
try:
    conexion.autocommit=False
    cursor = conexion.cursor()
    # sentencia = "INSERT INTO cliente(nombre) Values(%s)"
    # nombre = "Daniel"
    # valores = (nombre,)
    # cursor.execute(sentencia,valores)
    # log.debug("Insert")
    sentencia = "UPDATE cliente SET nombre = %s WHERE idCliente = %s"
    valores = ("Jaime", 1)
    cursor.execute(sentencia,valores)
    log.debug("Sentencia Update")
    conexion.commit()

except Exception as e:
    conexion.rollback()
    log.error(e)