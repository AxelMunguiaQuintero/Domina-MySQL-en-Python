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
cursor = conn.cursor()

# Consulta 1: Obtener el nombre de la ciudad, el país y el idioma oficional con INNER JOIN
query = """
    SELECT country.Name AS Nombre_Pais, city.Name AS Nombre_Ciudad, countrylanguage.Language AS Idioma FROM city
    INNER JOIN country ON city.CountryCode = country.Code
    INNER JOIN countrylanguage ON country.Code = countrylanguage.CountryCode
    ORDER BY Nombre_Pais ASC, Nombre_Ciudad ASC
"""
inner_join = pd.read_sql_query(sql=query, con=conn)

# Consulta 2: Obtener el nombre de la ciudad, el país y los idiomas oficiales con LEFT JOIN
query = """
    SELECT country.Name AS Nombre_Pais, city.Name AS Nombre_Ciudad, countrylanguage.Language AS Idioma FROM city
    LEFT JOIN country ON city.CountryCode = country.Code
    LEFT JOIN countrylanguage ON country.Code = countrylanguage.CountryCode AND countrylanguage.IsOfficial = 'T'
    ORDER BY Nombre_Pais ASC
"""
left_join = pd.read_sql_query(sql=query, con=conn)

# Consulta 3: Obtener el nombre del país y el total de idiomas distintos hablados en las ciudades
query = """
    SELECT country.Name AS Nombre_Pais, COUNT(DISTINCT countrylanguage.Language) AS Total_Idiomas FROM countrylanguage
    RIGHT JOIN country ON countrylanguage.CountryCode = country.Code
    RIGHT JOIN city ON country.Code = city.CountryCode
    GROUP BY country.Name
    ORDER BY Total_Idiomas DESC
"""
right_join = pd.read_sql_query(sql=query, con=conn)

# Recordatorio:
#   - El uso de JOINs nos permite combinar información de múltiples tablas en una sola consulta. Esto nos ayuda a realizar un análisis
#     más profundo y obtener información más completa.
