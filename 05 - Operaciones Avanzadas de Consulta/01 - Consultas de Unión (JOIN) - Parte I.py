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

# Tipos de JOINS:
# INNER JOIN: Devuelve los registros que tienen coincidencias en ambas tablas.
# LEFT JOIN: Devuelve todos los registros de la tabla izqueirda y los registros coincidentes de la tabla derecha.
# RIGHT JOIN: Devuelve todos los registros de la tabla derecha y los registros coincidentes de la tabla izquierda.

# Consulta No. 1: Unir las tablas de country y city para obtener el nombre de la ciudad y el nombre del país con INNER JOIN.
query = """
    SELECT country.Name AS Nombre_Pais, city.Name AS Nombre_Ciudad FROM city
    INNER JOIN country ON city.CountryCode = country.Code ORDER BY country.Name
"""
inner_join = pd.read_sql(sql=query, con=conn)

# Consulta No. 2: Obtener el nombre del país con el número total de las ciudades con LEFT JOIN
query = """
    SELECT country.Name AS Nombre_Pais, COUNT(city.Name) AS Total_Ciudades FROM country
    LEFT JOIN city ON country.Code = city.CountryCode
    GROUP BY country.Name ORDER BY Total_Ciudades DESC
"""
left_join = pd.read_sql(sql=query, con=conn)

# Consulta No. 3: Obtener el nombre del país, el número total de ciudades y la población total por país con RIGHT JOIN
query = """
    SELECT country.Name AS Nombre_Pais, COUNT(DISTINCT city.Name) AS Total_Ciudades, SUM(city.Population) AS Poblacion_Total FROM city
    RIGHT JOIN country ON city.CountryCode = country.Code GROUP BY country.Name ORDER BY Total_Ciudades DESC
"""
right_join = pd.read_sql(sql=query, con=conn)

# Recordatorio:
#   - Los JOINs son herramientas que nos permiten combinar datos de diferentes tablas en una sola consulta:
#       * INNER JOIN: Datos que coinciden en ambas tablas.
#       * LEFT JOIN: Nos da todas las filas de la tabla izquierda y las coincidentes de la derecha.
#       * RIGHT JOIN: Nos da todas las filas de la tabla derecha y las coincidentes de la izquierda.
