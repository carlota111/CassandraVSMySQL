import csv
from faker import Faker
import random
from datetime import datetime, timedelta

# Inicializar Faker
fake = Faker()

# Función para generar un conjunto de datos
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'id': random.randint(1, 10000),
            'nombre': fake.name(),
            'edad': random.randint(18, 99),
            'email': fake.email(),
            'fecha_registro': fake.date_this_decade().strftime('%Y-%m-%d')
        }
        data.append(record)
    return data

# Función para escribir el archivo CSV
def write_csv(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()  # Escribir los nombres de las columnas
        writer.writerows(data)  # Escribir los datos

# Generar 100 registros de ejemplo
num_records = 10
data = generate_data(num_records)

# Escribir los datos al archivo CSV
write_csv('dataset_extracto.csv', data)

print("Archivo 'dataset_extracto.csv' creado exitosamente.")
