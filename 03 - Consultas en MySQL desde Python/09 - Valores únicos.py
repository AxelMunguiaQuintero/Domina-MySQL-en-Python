# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(
    user="root",
    password="root",
    database="empresa",
    host="localhost",
    port=3306
    )
cursor = conn.cursor()

# Consulta 1: Obtener los nombres únicos de los países en la tabla colaboradores
query = "SELECT DISTINCT pais FROM colaboradores"
df = pd.read_sql(sql=query, con=conn)
print(f"Hay {df.shape[0]} diferentes países")

# Consulta 2: Contar la cantidad de trabajos únicos en la tabla colaboradores
query = "SELECT COUNT(DISTINCT trabajo) as diferentes_trabajos FROM colaboradores"
df = pd.read_sql(sql=query, con=conn)
print("\nVariedad de trabajos:\n", df)

# Consulta 3: Obtener los nombres únicos de los trabajos y ordenarlos alfabéticamente
query = "SELECT DISTINCT trabajo FROM colaboradores ORDER BY trabajo ASC"
df = pd.read_sql(sql=query, con=conn)

# Consulta 4: Contar la cantidad de colaboradores únicos por país
query = "SELECT pais, COUNT(DISTINCT nombre) AS cantidad_colaboradores FROM colaboradores GROUP BY pais"
df = pd.read_sql(sql=query, con=conn)

# Cerrar conexión
conn.close()

# Recordatorio:
#   - DISTINCT nos permite seleccionar valores únicos de una columna o conjunto de columnas en una tabla, eliminando
#     las filas duplicadas de los resultados de la consulta.
    