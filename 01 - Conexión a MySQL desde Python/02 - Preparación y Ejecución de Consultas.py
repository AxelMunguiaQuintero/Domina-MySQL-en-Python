# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")


# Definir funciones
def establecer_conexion(usuario: str, contraseña: str, host: str, base_datos: str, puerto: int=3306):
    
    """
    Establece una conexión a MySQL.
    
    Parámetros
    ----------
    usuario (str):
        Nombre de usuario de MySQL.
    contraseña (str):
        Contraseña de MySQL.
    host (str):
        Dirección del Host.
    base_datos (str):
        Base de datos a la que nos queremos conectar.
    puerto (int):
        Número del puerto. Por defecto es 3306.
        
    Salida
    ----------
    return : Objeto de la conexión.
    """
    
    # Establecer los parámetros
    config = {
        
        "user": usuario,
        "password": contraseña,
        "host": host,
        "database": base_datos,
        "port": puerto
        
        }
    
    # Establecer conexión
    conn = mysql.connect(**config)
    
    return conn


# Conexión
conn = establecer_conexion(usuario="root", contraseña="root", host="localhost", base_datos=None)
print("Estatus de la conexión:", conn.is_connected())
# Cursor
cursor = conn.cursor()
    
    
def ejecutar_consulta(consulta: str):
    
    """
    Ejecutar una consulta en la base de datos
    
    Args:
        consulta (str): Consulta SQL a ejecutar
        
    Salida:
        Cursor que contiene los resultados de la consulta
    """
    
    # Ejecutar
    cursor.execute(consulta)
    
    return cursor


# Distintas consultas
query = "SHOW DATABASES"
db_existentes = ejecutar_consulta(query)
for n, i in enumerate(db_existentes):
    print(f"Base de Datos No. {n}: {i[0]}")

# Realizar con pandas
db_existentes_pd = pd.read_sql(sql=query, con=conn)
print(db_existentes_pd)    
    
# Usar una base de datos
db_usar = db_existentes_pd.iloc[-1, 0]
ejecutar_consulta(f"USE {db_usar}")
print("Trabajando con la Base de Datos:", conn.database)
    
# Realizar con pandas
try: 
    pd.read_sql_query(sql=f"USE {db_usar}", con=conn)
except Exception as error:
    print("No se pudo ejecutar con error: ", error)
    
# Recordatorio:
#   - El resultado de nuestra consulta está almacenado dentro del mismo cursor. Debemos extraer dicho contenido
#     para poder trabajar con la información.
    