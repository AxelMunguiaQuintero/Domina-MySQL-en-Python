# Importar librerías
import mysql.connector as mysql
import subprocess
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Definir credenciales
credenciales = {
    
    "user": "root",
    "password": "root",
    "database": None
    
    }

# Conexión
conn = mysql.connect(**credenciales)
cursor = conn.cursor()

# Eliminar la base de datos "world"
bd = "world"
cursor.execute("DROP DATABASE IF EXISTS " + bd)

# Verificar
bds = pd.read_sql(sql="SHOW DATABASES", con=conn)
if bds.isin([bd]).sum().iloc[0] == 0:
    print("¡La base de datos se ha eliminado de manera exitosa!")
    
# Importar Base de Datos
comando = "mysql -u {usuario} -p{contraseña} --comments < {archivo}"
comando = comando.format(usuario=credenciales["user"],
                         contraseña=credenciales["password"],
                         archivo="base_datos.sql")
print(subprocess.call(comando, shell=True, stderr=subprocess.STDOUT))

# Establecer conexión
conn = mysql.connect(**credenciales)
cursor = conn.cursor()

# Validar
bds = pd.read_sql(sql="SHOW DATABASES", con=conn)
if bds.isin([bd]).sum().iloc[0] == 1:
    print("¡La base de datos se ha importado de manera exitosa!")
tablas = pd.read_sql(sql="SHOW TABLES FROM world", con=conn)
print(tablas)

# Recuperar los datos
cursor.execute("USE world")
city = pd.read_sql(sql="SELECT * FROM city", con=conn)
country = pd.read_sql(sql="SELECT * FROM country", con=conn)
countrylanguage = pd.read_sql(sql="SELECT * FROM countrylanguage", con=conn)

# Recordatorio:
#   - La importación de una base de datos incluye todas sus tablas y sus respectivas estructuras.
#   - Considerar al importar, que cualquier base de datos existente con el mismo nombre será eliminada.
