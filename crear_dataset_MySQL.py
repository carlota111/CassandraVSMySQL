import mysql.connector
from mysql.connector import Error

def crear_dataset():
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,       
            user='root', 
            password='pw',
            database='dbMySQL'
        )

        if conexion.is_connected():
            cursor = conexion.cursor()

            # Crear tabla si no existe
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                edad INT,
                email VARCHAR(50),
                fecha_registro DATE
            )
            """)
            print("Tabla 'usuarios' creada o ya existe.")

            # Insertar datos de ejemplo
            datos_usuarios = [
                ("Juan Pérez", 28, "juan.perez@example.com", "2023-01-15"),
                ("María López", 34, "maria.lopez@example.com", "2023-02-20"),
                ("Carlos Sánchez", 22, "carlos.sanchez@example.com", "2023-03-10"),
                ("Ana Gómez", 30, "ana.gomez@example.com", "2023-04-05"),
                ("Pedro Rodríguez", 25, "pedro.rodriguez@example.com", "2023-05-18"),
                ("Lucía Fernández", 27, "lucia.fernandez@example.com", "2023-06-21"),
                ("Miguel Torres", 29, "miguel.torres@example.com", "2023-07-11"),
                ("Sandra Martín", 26, "sandra.martin@example.com", "2023-08-15"),
                ("David González", 31, "david.gonzalez@example.com", "2023-09-05"),
                ("Laura Ruiz", 24, "laura.ruiz@example.com", "2023-10-10")
            ]

            cursor.executemany("""
            INSERT INTO usuarios (nombre, edad, email, fecha_registro)
            VALUES (%s, %s, %s, %s)
            """, datos_usuarios)
            conexion.commit()
            print(f"{cursor.rowcount} registros insertados en la tabla 'usuarios'.")

    except Error as e:
        print("Error al conectar a la base de datos:", e)

    finally:
        # Cerrar la conexión
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("La conexión a la base de datos ha sido cerrada.")

# Ejecutar la función para crear el dataset
crear_dataset()
