# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(user="root", password="root", database="world")
cursor = conn.cursor()

# Recuperar los datos
query = "SELECT * FROM city"
df = pd.read_sql(sql=query, con=conn)

# Consulta 1: Encontrar la población mínima en general
query = "SELECT MIN(Population) AS MinPoblacion FROM city"
min_poblacion = pd.read_sql(sql=query, con=conn)
print(f"La ciudad con la menor población con un total de habitantes de {min_poblacion.iloc[0, 0]}")

# Consulta 2: Encontrar la población mínima de las ciudades de un país (España)
query = """
    SELECT name, Population as Poblacion FROM city
    WHERE Population = (
        SELECT MIN(Population) FROM city WHERE CountryCode = 'ESP'
        ) and CountryCode = 'ESP'
"""
min_Esp = pd.read_sql_query(sql=query, con=conn)
print(f"La ciudad de España con menor población es {min_Esp.iloc[0, 0]} con una población total de {min_Esp.iloc[0, 1]}")

# Caso Prueba
query = "SELECT name, MIN(Population) as Poblacion FROM city WHERE CountryCode = 'ESP'"
caso_prueba = pd.read_sql_query(sql=query, con=conn)
# Inspeccionar la población real del nombre que devuelve
query = "SELECT * FROM city WHERE CountryCode = 'ESP'"
validacion = pd.read_sql_query(sql=query, con=conn)

# Recordatorio:
#   - La función de agregación MIN nos permite identificar el valor mínimo en un conjunto de datos.
#   - Debemos ser explícitos al realizar consultas, ya que podemos obtener una salida de datos que no arroje errores, pero estará incorrecta.
