import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    try:
        # Establecer la conexión
        conexion = mysql.connector.connect(
            host='localhost',        # Dirección del servidor MySQL (localhost si está en el mismo equipo)
            port=3306,               # Puerto de MySQL (por defecto es 3306)
            user='mysql',             # Usuario de MySQL (debe coincidir con tu configuración de docker-compose)
            password='pw',    	     # Contraseña de MySQL
            database='dbMySQL'       # Nombre de la base de datos
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")

            # Crear un cursor para ejecutar consultas
            cursor = conexion.cursor()
            
            # Ejecutar una consulta de prueba (opcional)
            cursor.execute("SELECT dbMySQL();")
            registro = cursor.fetchone()
            print(f"Conectado a la base de datos: {registro}")

            # Aquí podrías ejecutar otras consultas, si es necesario

            # Cerrar el cursor
            cursor.close()

    except Error as e:
        print("Error al conectar a la base de datos:", e)

    finally:
        # Cerrar la conexión si estaba abierta
        if conexion.is_connected():
            conexion.close()
            print("La conexión a la base de datos ha sido cerrada")

# Ejecutar la función para conectarse a MySQL
conectar_mysql()
