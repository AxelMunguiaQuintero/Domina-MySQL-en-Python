# Importar librerías
import mysql.connector as mysql
import subprocess
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Credenciales
credenciales = {
    
    "user": "root",
    "password": "root",
    "database": None
    
    }
# Conexión
conn = mysql.connect(**credenciales)
cursor = conn.cursor()

# Crear una base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS world_copia")

# Usar nueva bd
cursor.execute("USE world_copia")

# Importar la tabla a la base de datos
comando = "mysql -u {usuario} -p{contraseña} {bd} < {archivo}".format(usuario=credenciales["user"], contraseña=credenciales["password"],
                                                                      bd="world_copia", archivo="tabla.sql")
# Ejecutar el comando
importacion = subprocess.call(comando, shell=True, stderr=subprocess.STDOUT)
print(importacion)

# Recuperar los datos
country_df = pd.read_sql(sql="SELECT * FROM country", con=conn)

# Veremos las tablas existentes
tablas = pd.read_sql(sql="SHOW TABLES", con=conn)
print(tablas)

# Recordatorio:
#   - La importación de tablas puede ser a bases con nombres diferentes.
#   - Si existe una tabla con el mismo nombre en la base de datos a la que la vamos a importar, esta será eliminada.
