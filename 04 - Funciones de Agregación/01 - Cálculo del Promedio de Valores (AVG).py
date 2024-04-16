# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(
    user="root",
    password="root",
    database="world",
    host="localhost"
    )
print("Estatus de la conexión:", conn.is_connected())
cursor = conn.cursor()

# Obtener los datos
query = "SELECT * FROM city"
df = pd.read_sql(sql=query, con=conn)
print(df.info())

# Consulta 1: Obtener el promedio de la población de todas las ciudades
query = "SELECT AVG(Population) AS Promedio_Ciudades FROM city"
promedio = pd.read_sql(sql=query, con=conn)

# Consulta 2: Obtener el promedio de la población de las ciudades en un país específico (por ejemplo, Argentina)
query = "SELECT AVG(Population) AS Promedio_Argentina FROM city WHERE CountryCode = 'ARG'"
promedio_ARG = pd.read_sql(sql=query, con=conn)

# Consulta 3: Obtener el promedio de la población de las ciudades con una población superior a 1 millón
query = "SELECT AVG(Population) FROM city WHERE Population > 1000000"
promedio_ciudades_grandes = pd.read_sql(sql=query, con=conn)

# Recordatorio:
#   - La función de agregación promedio (AVG) nos permite calcular la media de un conjunto de datos, ya se con o sin filtros,
#     para obtener un valor único representativo.
