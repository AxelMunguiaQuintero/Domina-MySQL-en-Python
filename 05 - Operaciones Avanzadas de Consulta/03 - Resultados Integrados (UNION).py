# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión y Cursor
conn = mysql.connect(
    user="root",
    password="root",
    database="world"
    )
cursor = conn.cursor()

# Consulta 1: Unir nombre de ciudades y países (valores únicos)
query = "SELECT Name FROM country UNION SELECT Name FROM city"
cp_union = pd.read_sql_query(sql=query, con=conn)

# Validar
df1 = pd.read_sql(sql="SELECT Name FROM country", con=conn)
df2 = pd.read_sql(sql="SELECT Name FROM city", con=conn)
df_combinado = pd.concat([df1, df2], axis=0).drop_duplicates()
if df_combinado.shape == cp_union.shape:
    print("¡Ambos objetos tienen la misma estructura!")
    
# Consulta 2: Obtener nombres de ciudades y países con poblaciones mayores a 5 millones
query = """
    SELECT Name FROM city WHERE Population > 5000000
    UNION
    SELECT Name FROM country WHERE Population > 5000000
"""
poblaciones_grandes = pd.read_sql(sql=query, con=conn)

# Consulta 3: Obtener nombre y población de ciudades y países
query = """
    SELECT Name, Population FROM city
    UNION
    SELECT Name, Population FROM country
"""
nombre_poblacion = pd.read_sql(sql=query, con=conn)

# Recordatorio:
#   - UNION se utiliza para combinar los resultados de dos o más consultas SELECT, en un solo conjunto de resultados.
#   - Ambas consultas deben devolver el mismo número de columnas y los mismos tipos de datos en cada columna.
