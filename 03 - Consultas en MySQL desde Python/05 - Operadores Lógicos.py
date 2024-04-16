# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Establecer la conexión
conn = mysql.connect(user="root", password="root")
cursor = conn.cursor()

# Crear una base de datos
query = "CREATE DATABASE IF NOT EXISTS empresa"
cursor.execute(query)

# Crear una tabla
cursor.execute("USE empresa")
cursor.execute("""
               CREATE TABLE IF NOT EXISTS empleados (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   nombre VARCHAR(50),
                   edad INT,
                   salario DECIMAL(10, 2)                   
                   )
               """)
               
# Definir nuestros datos de ejemplo
empleados = [
    ("Juan", 30, 2500.00),
    ("María", 25, 3000.00),
    ("Pedro", 40, 2000.00),
    ("Ana", 35, 3500.00),
    ("Luis", 28, None),
    ("José", None, 500.00),
    ("Francisco", 38, 3200.00),
    ("Victoria", 27, 1200.00)
    ]

# Insertar datos
query = "INSERT INTO empleados (nombre, edad, salario) VALUES (%s, %s, %s)"
cursor.executemany(query, empleados)
# Confirmar cambios
conn.commit()

# Mostrar todos los empleados
empleados = pd.read_sql_query(sql="SELECT * FROM empleados", con=conn)

# Operadores de comparación: WHERE -> Filtra los resultados de una consulta según una condición específica. 
# Mostrar empleados mayores a 30 años
query = "SELECT * FROM empleados WHERE edad > 30"
mas_30 = pd.read_sql_query(sql=query, con=conn)

# Operador lógico: AND -> Combina múltiples condiciones en una consulta, devolviendo registros donde todas las condiciones son verdaderas.
# Mostrar empleados mayores de 30 años y con salario inferior a 2500
query = "SELECT * FROM empleados WHERE edad > 30 AND salario < 2500"
operador_and = pd.read_sql_query(sql=query, con=conn)

# Operador lógico: OR -> Combina múltiples condiciones en una consulta, devolviendo registros donde se cumplen cualquier de las condiciones
# Mostrar empleados menores de 25 años o con salario superior a 2000
query = "SELECT * FROM empleados WHERE edad < 25 OR salario > 2000"
operador_or = pd.read_sql_query(sql=query, con=conn)

# Operador lógico: NOT -> Niega una condición en una consulta, devolviendo registros que no cumplen con la condición especificada.
# Mostrar empleados que no se llamen "Juan" o "Francisco"
query = "SELECT * FROM empleados WHERE NOT (nombre = 'Juan' OR nombre = 'Francisco')"
operador_not = pd.read_sql_query(sql=query, con=conn)

# Recordatorio:
#   - Los operadores lógicos son fundamentales en consultas para combinar y filtrar datos de manera práctica, permitiendo obtener resultados
#     más relevantes de la base de datos.
