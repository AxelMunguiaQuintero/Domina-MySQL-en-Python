# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Parámetros
config = {
    
    "user": "root",
    "password": "root",
    "database": "world"
    }
# Conexión
conn = mysql.connect(**config)

# Consulta 1: Obtener las ciudades cuyo nombre comienza con "s"
query = """
    SELECT Name AS ciudad, Population FROM city
    WHERE Name LIKE 'S%' ORDER BY Ciudad
"""
ciudades_s = pd.read_sql(sql=query, con=conn)

# Consulta 2: Obtener todos los países cuyp nombre contiene 'land'
query = """
    SELECT Name AS Pais, Population FROM country
    WHERE Name LIKE '%land%' ORDER BY Pais
"""
paises_land = pd.read_sql(sql=query, con=conn)

# Consulta 3: Obtener todas las ciudades cuyo nombre termine 'burg'
query = """
    SELECT Name AS Ciudad, Population FROM city
    WHERE Name LIKE '%burg' ORDER BY Ciudad
"""
ciudades_burg = pd.read_sql(sql=query, con=conn)

# Recordatorio:
#   - LIKE se utiliza para realizar búsquedas de patrones en "columnas de texto".
#   - LIKE nos permite buscar valores que coincidan con un cierto patrón específicado.
