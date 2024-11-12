import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Definir el número de registros
num_records = 10

# Generar datos aleatorios para cada columna
data = {
    'id': np.arange(1, num_records + 1),
    'nombre': np.random.choice(['Carlos', 'Ana', 'Luis', 'Maria', 'José', 'Laura'], num_records),
    'edad': np.random.randint(18, 70, num_records),
    'email': [f"user{num}@example.com" for num in range(num_records)],
    'fecha_registro': [datetime.today() - timedelta(days=np.random.randint(1, 365)) for _ in range(num_records)]
}

# Crear DataFrame con los datos
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('dataset_extracto.csv', index=False)

print("Archivo CSV 'dataset_extracto.csv' creado con éxito.")
