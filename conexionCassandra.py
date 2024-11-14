from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Si Cassandra está protegido por contraseña, agrega la autenticación
# auth_provider = PlainTextAuthProvider(username='your_username', password='your_password')

cluster = Cluster(['127.0.0.1'], port=9042)  # Asegúrate de usar el puerto correcto
session = cluster.connect()

# Crear un keyspace o trabajar con el keyspace por defecto
session.set_keyspace('system')

print("Conexión exitosa a Cassandra")
