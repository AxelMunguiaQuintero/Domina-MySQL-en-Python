# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión 
conn = mysql.connect(user="root", password="root", database="world")

# Consulta 1: Obtener la suma de la población de todas las ciudades
query = "SELECT SUM(Population) FROM city"
poblacion_total = pd.read_sql_query(sql=query, con=conn)
print("La población total en nuestros registros es de:", poblacion_total.iloc[0, 0])

# Consulta 2: Obtener la suma total de la población de todas las ciudades en un país
query = """
    SELECT SUM(Population) FROM city
    WHERE CountryCode = 'USA'
"""
usa_poblacion = pd.read_sql(sql=query, con=conn)
print("La población de las ciudades de USA en los registros es por un total de:", usa_poblacion.iloc[0, 0])

# Consulta 3: Obtener la suma total de la población de todas las ciudades en un país específico y con una población mayor a un valor dado
query = """
    SELECT SUM(Population) FROM city WHERE CountryCode = 'IND' AND Population > 150000
"""
poblacion_Ind = pd.read_sql(sql=query, con=conn)
print("La suma de las ciudades de Indica con una población mínima de 150,000 es:", poblacion_Ind.iloc[0, 0])

# Recordatorio:
#   - La función de agregación SUM se utiliza para calcular la suma total de los valores de una columna "numérica".
