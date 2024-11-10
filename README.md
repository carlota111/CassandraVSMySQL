# Comparación de Rendimiento: MySQL vs Cassandra

Este proyecto realiza una comparación de rendimiento entre las bases de datos **MySQL** y **Cassandra** utilizando Docker para la configuración de los entornos y Python para ejecutar los scripts de comparación.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- **Docker**: Puedes descargar e instalar Docker Desktop desde [aquí](https://www.docker.com/products/docker-desktop/).
- **Conda**: Para gestionar entornos virtuales con `conda`. Si no lo tienes instalado, sigue las instrucciones [aquí](https://bigdatawirtz.github.io/basic-tools/python/).

También asegúrate de añadir tu usuario al grupo de Docker para evitar tener que usar `sudo` al ejecutar comandos de Docker.

## Pasos para Ejecutar el Proyecto

### 1. Clonar el Proyecto desde GitHub

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/carlota111/CassandraVSMySQL.git
````

### 2. Configurar Docker
Entra en la carpeta del proyecto y levanta los contenedores de MySQL y Cassandra con docker-compose:

```bash
cd CassandraVSMySQL
ls
docker compose up -d
````

### 3. Configuración del Entorno para MySQL
Para trabajar con MySQL, crea un entorno conda, actívalo e instala las dependencias necesarias:

```bash
conda create --name MySQL
conda activate MySQL
conda install pip
pip install mysql-connector-python
````
Esto instalará la librería de Python necesaria para interactuar con MySQL.

### 4. Ejecutar los Scripts de Comparación
Una vez que todo esté configurado, puedes ejecutar los scripts de Python para realizar las pruebas de rendimiento. Para ejecutar un script, usa el siguiente comando:

```bash
python3 nombreScript
````
Reemplaza nombreScript por el nombre del script que deseas ejecutar, ya sea para realizar operaciones en MySQL o Cassandra.
