from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Si Cassandra está protegido por contraseña, agrega la autenticación
# auth_provider = PlainTextAuthProvider(username='your_username', password='your_password')

cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()

session.set_keyspace('system')

print("Conexión exitosa a Cassandra")
