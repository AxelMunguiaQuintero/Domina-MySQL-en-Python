# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Establecer los parámetros
config = {
    
    "user": "root",
    "password": "root",
    "host": "localhost",
    "database": "world",
    "port": 3306
    
    }

# Conexión
conn = mysql.connect(**config)
print("Estatus conexión:", conn.is_connected())
# Definir cursor
cursor = conn.cursor()

# Mostremos las tablas

# Extracción 1: Iterar sobre los resultados
cursor.execute("SHOW TABLES")
for i in cursor:
    print(f"Tabla: {i[0]}")
    
# Extracción 2: Extraer la consulta en una lista
cursor.execute("SHOW TABLES")
tablas = list(cursor)
print(tablas)

# Extracción 3: Método fetchall del cursor
cursor.execute("SHOW TABLES")
tablas_fetchall = cursor.fetchall()
print(tablas_fetchall)

# Extracción 4: Usando pandas
tablas_pd = pd.read_sql_query(sql="SHOW TABLES", con=conn)
print(tablas_pd)

# Recordatorio:
#   - El tratamiento que se le da a los datos que recibimos de nuestras consultas depende de la necesidad de nuestra aplicación.
