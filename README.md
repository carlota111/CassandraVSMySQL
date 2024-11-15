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
conda env create --file env_mysql.yml
````
Ese comando es lo mismo que esto de aquí:

```bash
conda create --name MySQL
conda activate MySQL
conda install pip
pip install mysql-connector-python
pip install pandas
````
Esto instalará la librería de Python necesaria para interactuar con MySQL.

### 4. Configuración del Entorno para Cassandra
Para trabajar con Cassandra, crea un entorno conda, actívalo e instala las dependencias necesarias:

```bash
conda env create --file env_Cassandra.yml
````
Si prefieres crear el entorno e instalar tu mismo las librerias sin el yml:

Para que cassandra-diver funcione la versión de python debe ser 3.9

```bash
conda create --name cassandra
conda activate cassandra
conda install -c conda-forge faker
conda install -c conda-forge cassandra-driver
pip install cassandra-driver pandas 
````
Esto instalará la librería de Python necesaria para interactuar con Cassandra en los scripts creados.

### 5. Ejecutar los Scripts de Comparación
Una vez que todo esté configurado, puedes ejecutar los scripts de Python para realizar las pruebas de rendimiento. Para ejecutar un script, usa el siguiente comando:

```bash
python3 nombreScript
````
Reemplaza nombreScript por el nombre del script que deseas ejecutar, ya sea para realizar operaciones en MySQL o Cassandra.

### 6. Preguntas a responder
- **Cal é máis rápida?**

  Inserción de datos:
  MySQL ha sido más rápido que Cassandra.
  
  Consultas:
  Cassandra ha sido más rápida que MySQL.


- **Son os resultados os esperados?**

  No, nosotras esperábamos que fuese más rápida una sola base de datos en ambos campos.


- **Como xustificas os resultados?**

  Inserción de datos:
  Cassandra, al ser una base de datos distribuida, necesita replicar datos entre nodos, lo que introduce latencia durante      las operaciones de escritura.
  MySQL utiliza índices y un modelo relacional optimizado para inserciones rápidas en un entorno transaccional. 

  Consultas:
  Cassandra está optimizada para operaciones de lectura y escritura rápidas en grandes volúmenes de datos gracias a la         ausencia de relaciones complejas y a su almacenamiento distribuido. 
