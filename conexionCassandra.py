from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Configuración de conexión
CASSANDRA_HOSTS = ['localhost']
CASSANDRA_PORT = 9042

# Crear un cluster de Cassandra y establecer la conexión
cluster = Cluster(CASSANDRA_HOSTS, port=CASSANDRA_PORT)
session = cluster.connect()

# Seleccionar el keyspace
session.set_keyspace(KEYSPACE)

# Hacer una consulta simple para probar la conexión
try:
    # Realiza una consulta simple (por ejemplo, ver las tablas disponibles)
    rows = session.execute("SELECT table_name FROM system_schema.tables WHERE keyspace_name = %s", (KEYSPACE,))
    print(f"Tablas en el keyspace '{KEYSPACE}':")
    for row in rows:
        print(row.table_name)
except Exception as e:
    print(f"Error en la consulta: {e}")

# Cerrar la sesión y la conexión
cluster.shutdown()
