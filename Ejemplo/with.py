import psycopg2
from logger_base import log

conexion = psycopg2.connect(user="postgres",
                            password="Jm123423",
                            host="localhost",
                            port= 5432,
                            database="clase_db")
log.debug(conexion)

# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = " INSERT INTO cliente(idcliente, nombre) Values(%s, %s)"
#             valores = (
#                 (5, "Juan"),
#                 (6, "Maria")
#             )
#             cursor.executemany(sentencia,valores)
#             registrosInsert = cursor.rowcount
#             log.debug(f"Registros insertados: {registrosInsert}")
# except Exception as e:
#     log.error(e)
# finally:
#     conexion.close()

# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = " UPDATE cliente SET nombre = %s WHERE idcliente = %s"
#             values = (
#                 ("Pedro", 1),
#                 ("Daniela",2)
#             )
#             cursor.executemany(sentencia,values)
#             registrosActualizados = cursor.rowcount
#             log.debug(f"Registros actualizados: {registrosActualizados}")
# except Exception as e:
#     log.error(e)
# finally:
#     conexion.close()

# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = " DELETE FROM cliente WHERE idcliente = %s"
#             valores = (
#                 ("1")
#             )
#             cursor.execute(sentencia,valores)
#             registrosEliminados = cursor.rowcount
#             log.debug(f"Registros eliminados: {registrosEliminados}")
# except Exception as e:
#     log.error(e)
# finally:
#     conexion.close()

# conexion = psycopg2.connect(user="postgres",
#                             password="Jm123423",
#                             host="localhost",
#                             port= 5432,
#                             database="clase_db")
# log.debug(conexion)
# cursor = conexion.cursor()
# cursor.execute("SELECT * FROM cliente")
# resultados = cursor.fetchall()
# log.debug(resultados)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = " DELETE FROM cliente WHERE idcliente IN %s"
            entrada = input ("ID A ELIMINAR: ")
            valores = (tuple(entrada.split(",")),)
            cursor.execute(sentencia,valores)
            registrosEliminados = cursor.rowcount
            log.debug(f"Registros eliminados: {registrosEliminados}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()