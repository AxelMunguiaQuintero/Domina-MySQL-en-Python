# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(
    user="root",
    password="root",
    database="world"
    )

# Consulta 1: Obtener las primeras 10 ciudades con nombres que contiene "New" o "City", ordenados alfabéticamente
query = """
    SELECT Name AS Ciudad, Population FROM city
    WHERE Name LIKE '%NEW%' OR Name LIKE '%CITY%'
    ORDER BY Name ASC
    LIMIT 10
"""
df = pd.read_sql(sql=query, con=conn)

# Consulta 2: Obtener los primeros 12 países con población mayor a 50 millones, ordenados por población descendente
query = """
    SELECT Name AS Pais, Population FROM country
    WHERE Population > 50000000
    ORDER BY Population DESC
    LIMIT 12
"""
df = pd.read_sql(sql=query, con=conn)

# Consulta 3: Obtener los paises cuyos nombres estén en una lista específica
paises = ["Spain", "Canada", "Italy", "Germany"]
query = """
    SELECT Name AS Pais, Population FROM country
    WHERE Name IN ('{}', '{}', '{}', '{}')
""".format(*paises)
df = pd.read_sql(sql=query, con=conn)

# Consulta 4: Obtener los idiomas hablados en los países con nombre que empiezan con "A"
query = """
    SELECT cl.language, COUNT(*) AS Num_Paises FROM countrylanguage AS cl
    WHERE cl.CountryCode IN (
        SELECT c.Code FROM country AS c
        WHERE c.Name LIKE 'A%'
        )
    GROUP BY cl.language
    ORDER BY Num_Paises DESC
    LIMIT 10
"""
df = pd.read_sql(sql=query, con=conn)

# Recordatorio:
#   - IN se utiliza para especificar múltiples valores en una condición de búsqueda.
#   - LIMIT se utiliza para limitar el número de filas devueltas por una consulta.
