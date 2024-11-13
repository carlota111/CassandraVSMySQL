from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Configuración de la conexión
def connect_to_cassandra():
    try:
        # Crear un objeto de autenticación si usas autenticación (opcional)
        # Crear el clúster y la sesión de Cassandra
        cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider)  # IP de tu nodo Cassandra
        session = cluster.connect()

        # Conectarse a la base de datos específica
        session.set_keyspace('mi_keyspace')

        print("Conexión exitosa a Cassandra!")
        return session
    except Exception as e:
        print(f"Error al conectar a Cassandra: {e}")

# Llamar a la función de conexión
session = connect_to_cassandra()

# Si la conexión fue exitosa, puedes comenzar a ejecutar consultas
if session:
    rows = session.execute("SELECT * FROM tu_tabla")
    for row in rows:
        print(row)

# Cerrar la sesión y la conexión
if session:
    session.shutdown()
