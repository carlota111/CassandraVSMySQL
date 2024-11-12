import mysql.connector
from mysql.connector import Error
import time

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='pw',
            database='dbMySQL'
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
           
            cursor = conexion.cursor()

            # Medir el tiempo de inicio
            start_time = time.time()

            # Ejecutar la consulta
            cursor.execute("SELECT * FROM usuarios")
            resultados = cursor.fetchall()

            # Medir el tiempo final
            end_time = time.time()

            # Calcular el tiempo de ejecución
            tiempo_ejecucion = end_time - start_time
            print(f"La consulta tardó {tiempo_ejecucion:.4f} segundos en ejecutarse.")

            # Imprimir los resultados
            for registro in resultados:
                print(registro)

    except Error as e:
        print("Error al conectar a la base de datos:", e)

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("La conexión a la base de datos ha sido cerrada")

conectar_mysql()
