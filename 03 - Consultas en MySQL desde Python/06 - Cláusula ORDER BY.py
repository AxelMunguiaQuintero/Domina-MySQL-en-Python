# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(user="root", password="root", database="empresa")
cursor = conn.cursor()

# Ordenar por nombre DESC
query = "SELECT * FROM empleados ORDER BY nombre DESC"
empleados_desc = pd.read_sql(sql=query, con=conn)

# Ordenar por nombre ASC
query = "SELECT * FROM empleados ORDER BY nombre ASC"
empleados_asc = pd.read_sql(sql=query, con=conn)

# Insertar valores con mismo nombre y diferentes valores
empleados = [
    ("Juan", 25, 1800.00),
    ("María", 29, 2000.00),
    ("Pedro", 33, 2800.00),
    ("Ana", 21, 550.00)
    ]

# Insertar los datos
query = "INSERT INTO empleados (nombre, edad, salario) VALUES (%s, %s, %s)"
cursor.executemany(query, empleados)
# Confirmar los cambios
conn.commit()

# Ordenar en base a 2 columnas
query = "SELECT * FROM empleados ORDER BY nombre, salario ASC"
empleados_2condicionales = pd.read_sql(sql=query, con=conn)

# Ordenar en base a 2 columnas
query = "SELECT * FROM empleados ORDER BY nombre ASC, salario DESC"
empleados_2condicionales = pd.read_sql(sql=query, con=conn)

# Recordatorio:
#   - La cláusula ORDER BY organiza los resultados según los valores de una o más columnas, facilitando la visualización y el análisis de datos.
