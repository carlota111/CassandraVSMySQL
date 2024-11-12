import mysql.connector
import csv
from mysql.connector import Error

def insertar_datos_csv():
    try:
        # Conexión a la base de datos MySQL
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
   
          # Crear la tabla 'usuarios' si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL,
                    edad INT,
                    email VARCHAR(50),
                    fecha_registro DATE
                )
            """)
            print("Tabla 'usuarios' creada o ya existía.")

	    # Borrar todos los registros de la tabla 'usuarios' para evitar duplicados
            cursor.execute("DELETE FROM usuarios")
            conexion.commit()
            print("Registros anteriores eliminados exitosamente.")

            # Leer los datos del archivo CSV
            with open('dataset_extracto.csv', mode='r') as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                next(lector_csv)  # Para saltar la primera línea (encabezados)

                # Insertar los datos en la base de datos
                for fila in lector_csv:
                    cursor.execute("""
                        INSERT INTO usuarios (id, nombre, edad, email, fecha_registro)
                        VALUES (%s, %s, %s, %s, %s)
                    """, fila)

            # Confirmar los cambios en la base de datos
            conexion.commit()
            print(f"Se han insertado los  registros en la base de datos.")

    except Error as e:
        print("Error al conectar a la base de datos o al insertar los datos:", e)

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

# Llamar a la función para insertar los datos
insertar_datos_csv()
