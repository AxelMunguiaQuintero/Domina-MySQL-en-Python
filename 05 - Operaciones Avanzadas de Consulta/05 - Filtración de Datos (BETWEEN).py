# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Establecer parámetros
config = {
    "user": "root",
    "password": "root",
    "database": "world",
    "host": "localhost",
    "port": 3306
    }
# Definir la conexión
conn = mysql.connect(**config)

# Consulta 1: Obtener los países cuy apoblación está entre 1_000_000 y 10_000_000
query = """
    SELECT name AS Pais, Population FROM country
    WHERE Population BETWEEN 1000000 AND 10000000
"""
df = pd.read_sql_query(sql=query, con=conn)

# Consulta 2: Obtener los datos cuyo ID esté entre 50 y 100, y 120 y 125.
query = """
    SELECT * FROM city
    WHERE (ID BETWEEN 50 AND 100) OR (ID BETWEEN 120 AND 125)
"""
df = pd.read_sql_query(sql=query, con=conn)

# Consulta 3: Obtener las ciudades cuya población esté entre 500_000 y 1_000_000, y están en un país cuyo nombre empiezan con "A"
query = """
    SELECT city.Name AS Ciudad, city.Population, country.Name AS Pais FROM city
    INNER JOIN country ON city.CountryCode = country.Code
    WHERE (city.Population BETWEEN 500000 AND 1000000)
    AND (country.Name >= 'A' AND country.Name < 'B')
    ORDER BY Pais
"""
df = pd.read_sql_query(sql=query, con=conn)

# Recordatorio:
#   - BETWEEN se utiliza para filtrar los resultados de una consulta según un rango de valores específicado.
