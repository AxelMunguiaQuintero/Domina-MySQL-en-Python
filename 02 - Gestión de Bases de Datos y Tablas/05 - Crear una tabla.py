# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Definir los parámetros
config = {
    "user": "root",
    "password": "root"
    }
conn = mysql.connect(**config)

# Definir cursor
cursor = conn.cursor()

# Crear una base de datos
db_nombre = "clientes"
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_nombre}")
# Verificar
dbs = pd.read_sql(sql="SHOW DATABASES", con=conn)

if any(dbs.isin([db_nombre])):
    print("Base de Datos Creada")
    
# Usar nuestra base de datos
cursor.execute(f"USE {db_nombre}")
# Definir la estructura de la tabla
tabla_nombre = "agenda_contactos"
query = f"""
    CREATE TABLE IF NOT EXISTS {tabla_nombre} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL COMMENT 'Nombre del contacto',
        apellido VARCHAR(50) NOT NULL COMMENT 'Apellido del contacto',
        telefono VARCHAR(25) NOT NULL UNIQUE COMMENT 'Número de teléfono',
        email VARCHAR(100) UNIQUE COMMENT 'Dirección de correo electrónico',
        direccion VARCHAR(255) COMMENT 'Dirección del contacto',
        ciudad VARCHAR(50) COMMENT 'Ciudad de residencia del contacto',
        estado VARCHAR(50) COMMENT 'Estado de residencia del contacto',
        codigo_postal VARCHAR(10) COMMENT 'Código postal',
        fecha_nacimiento DATE COMMENT 'Fecha de nacimiento del cliente',
        fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha de registro del contacto',
        notas TEXT COMMENT 'Notas adicionales',
        foto LONGBLOB COMMENT 'Fotografía del contacto'
        )
"""
cursor.execute(query)

# Verificar
tablas = pd.read_sql_query(sql=f"SHOW TABLES FROM {db_nombre}", con=conn)
if any(tablas.isin([tabla_nombre])):
    print("Tabla Creada dentro de la base de datos:", db_nombre)

# Ver la estructura de nuestra agenda
estructura = pd.read_sql_query(sql="DESCRIBE clientes.agenda_contactos", con=conn)

# Consultar datos existentes
df = pd.read_sql(sql=f"SELECT * FROM {tabla_nombre}", con=conn)
print(df)

# Recordatorio:
#   - Crear tablas en bases de datos es clave para organizar y almacenar información. Definir columnas con cuidado
#     y considerar datos adicionales mejora la gestión de datos. Es crucial para evitar columnas inncesarias y mantener 
#     la eficiencia en nuestras bases de datos.
