import pandas as pd
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from datetime import datetime

# Configura la dirección IP del nodo Cassandra
CASSANDRA_HOST = '127.0.0.1'  
CASSANDRA_PORT = 9042  

# Nombre del Keyspace y la tabla
KEYSPACE = 'mykeyspace'
TABLE = 'mytable'

# Cargar los datos desde un archivo CSV (ajusta la ruta del archivo)
CSV_FILE = 'dataset_extracto.csv' 

def connect_to_cassandra():
    """Conectar a Cassandra y retornar la sesión."""
    cluster = Cluster([CASSANDRA_HOST], port=CASSANDRA_PORT)
    session = cluster.connect()
    return session

def create_keyspace_and_table(session):
    """Crear un Keyspace y una tabla en Cassandra."""
    # Crear Keyspace si no existe
    session.execute(f"""
        CREATE KEYSPACE IF NOT EXISTS {KEYSPACE} 
        WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 1}};
    """)

    # Usar el Keyspace creado
    session.set_keyspace(KEYSPACE)

    # Crear la tabla
    session.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE} (
            id INT PRIMARY KEY, 
            nombre TEXT,
            edad INT,
            email TEXT,
            fecha_registro TIMESTAMP
        );
    """)

def insert_data_from_csv(session):
    """Leer datos de CSV y cargarlos en Cassandra."""
    # Leer el archivo CSV con pandas
    df = pd.read_csv(CSV_FILE)

    # Convertir 'fecha_registro' al formato de timestamp
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'], errors='coerce')

    # Crear la sentencia de inserción
    insert_stmt = session.prepare(f"""
        INSERT INTO {TABLE} (id, nombre, edad, email, fecha_registro) 
        VALUES (?, ?, ?, ?, ?)
    """)

    # Insertar cada fila del CSV en la tabla
    for index, row in df.iterrows():
        # Convertir el ID a int 
        id_value = int(row['id']) 

        # Ejecutar la inserción de datos
        session.execute(insert_stmt, (id_value, row['nombre'], row['edad'], row['email'], row['fecha_registro']))

def main():
    # Conectar a Cassandra
    session = connect_to_cassandra()

    # Crear el Keyspace y la tabla (si no existen)
    create_keyspace_and_table(session)

    # Insertar datos desde el CSV
    insert_data_from_csv(session)

    print("Datos cargados exitosamente desde el CSV a Cassandra.")

if __name__ == "__main__":
    main()
