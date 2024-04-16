# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(database="world", user="root", password="root")
cursor = conn.cursor()

# Recuperar los datos
query = "SELECT * FROM countrylanguage"
df = pd.read_sql(sql=query, con=conn)
print(df.info())

# Consulta 1: Encontrar el porcentaje máximo de hablantes de un idioma
query = "SELECT MAX(Percentage) FROM countrylanguage"
hablantes_maximo = pd.read_sql_query(sql=query, con=conn)
print("Porcentaje máximo de hablantes de un idioma es:", hablantes_maximo.iloc[0, 0])

# Consulta 2: Encontrar el país con el porcentaje máximo de hablantes de un idioma
query = """
    SELECT CountryCode
    FROM countrylanguage
    WHERE Percentage = (
        SELECT MAX(Percentage) FROM countrylanguage
        )
"""
paises_1idioma = pd.read_sql_query(sql=query, con=conn)
print(f"Hay {paises_1idioma.shape[0]} países que solo hablan un solo idioma")

# Consulta 3: Encontrar el idioma más hablado en términos de porcentaje en cada país
query = """
    SELECT CountryCode, language, Percentage FROM countrylanguage as cl1 
    WHERE Percentage = (
        SELECT MAX(Percentage) FROM countrylanguage as cl2 
        WHERE cl1.CountryCode = cl2.CountryCode
        )
"""
max_idioma_pais = pd.read_sql_query(sql=query, con=conn)

# Recordatorio:
#   - La función de agregación MAX nos permite identificar el valor máximo en un conjunto de datos. Utilizándola, podemos encontrar
#     el valor más alto en una columna específica de una tabla o un subconjunto de datos.
