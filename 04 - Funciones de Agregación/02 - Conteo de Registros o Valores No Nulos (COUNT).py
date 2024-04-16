# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(user="root", password="root", database="world")
cursor = conn.cursor()

# Recuperar los datos
query = "SELECT * FROM country"
df = pd.read_sql(sql=query, con=conn)
print(df.info())

# Consulta 1: Contar el número total de países
query = "SELECT COUNT(*) FROM country"
paises = pd.read_sql(sql=query, con=conn)
# Validar que el número de países sea igual a la extensión de nuestro df
if len(df) == paises.iloc[0, 0]:
    print(f"Hay {len(df)} países únicos")
    
# Consulta 2: Contar el núero de países en Europa
query = "SELECT COUNT(*) FROM country WHERE Continent = 'EUROPE'"
paises_Europa = pd.read_sql(sql=query, con=conn)
print(f"Hay un registro de {paises_Europa} países de Europa")

# Consulta 3: Contar el número de países con una población superior a 100 millones
query = "SELECT COUNT(*) FROM country WHERE Population > 1000000"
poblaciones_grandes =  pd.read_sql(sql=query, con=conn)
print(f"Hay {poblaciones_grandes.iloc[0, 0]} países con más de 1'000,000 de habitantes")

# Recordatorio:
#   - COUNT cuenta el número de filas que cumplen ciertos criterios en una tabla. Es útil para obtener recuentos de datos en consultas
