from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import time

def conectar_cassandra():
    try:
        # Conectar a Cassandra
        cluster = Cluster(['127.0.0.1']) 
        session = cluster.connect('mykeyspace')

        # Medir el tiempo de inicio
        start_time = time.time()

        # Ejecutar la consulta
        query = "select * from mykeyspace.mytable ;"  
        stmt = SimpleStatement(query)
        resultados = session.execute(stmt)

        # Medir el tiempo final
        end_time = time.time()

        # Calcular el tiempo de ejecución
        tiempo_ejecucion = end_time - start_time
        print(f"La consulta tardó {tiempo_ejecucion:.4f} segundos en ejecutarse.")

        # Imprimir los resultados
        for registro in resultados:
            print(registro)

    except Exception as e:
        print("Error al conectar o ejecutar la consulta:", e)

    finally:
        # Cerrar la conexión
        if session:
            session.shutdown()  
            print("La conexión a Cassandra ha sido cerrada")

# Llamar a la función para conectar y ejecutar la consulta
conectar_cassandra()
