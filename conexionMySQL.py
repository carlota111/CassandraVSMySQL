import mysql.connector
from mysql.connector import Error

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

    except Error as e:
        print("Error al conectar a la base de datos:", e)

    finally:
        if conexion.is_connected():
            conexion.close()
            print("La conexión a la base de datos ha sido cerrada")

conectar_mysql()
