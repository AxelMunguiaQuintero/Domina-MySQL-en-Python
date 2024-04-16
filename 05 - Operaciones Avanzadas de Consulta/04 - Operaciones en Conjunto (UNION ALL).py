# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión a la base de datos
conn = mysql.connect(user="root", password="root", database="world")

# Cláusulas
clausulas = ["UNION", "UNION ALL"]
query = """
    SELECT Code FROM country
    {}
    SELECT CountryCode FROM city
"""

# Realizar las consultas
for i in clausulas:
    df = pd.read_sql(sql=query.format(i), con=conn)
    print(f"Con la cláusula: {i} tenemos {df.shape[0]}")
    
# Recordatorio:
#   - UNION ALL también combina el resultado de dos o más consutlas, pero a diferencia de UNION, no elimina las filas duplicadas.
