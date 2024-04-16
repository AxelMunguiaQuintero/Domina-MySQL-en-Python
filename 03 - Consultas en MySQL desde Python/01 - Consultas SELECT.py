# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="world",
    port=3306
    )
print("Estatus de la conexión:", conn.is_connected())
print("Base de datos:", conn.database)

# Definir cursor
cursor = conn.cursor()

# Seleccionar una tabla
cursor.execute("SHOW TABLES")
tablas = cursor.fetchall()
print(tablas)

# Traer datos y almacenarlos
datos = {}
for i in tablas:
    # Pandas para dar formato
    df = pd.read_sql(sql=f"SELECT * FROM {i[0]}", con=conn)
    # Almacenar
    datos[i[0]] = df
print(datos)

# Extraer subconjuntos de nuestras bases de datos
sub_conjuntos = {}
for i in tablas:
    # Usaremos las primeras 2 columnas
    cursor.execute(f"DESCRIBE {i[0]}")
    columnas_info = cursor.fetchall()
    cols = [columnas_info[0][0], columnas_info[1][0]]    
    cols_formateo = ", ".join(cols)
    # Realizar consulta
    df = pd.read_sql(sql=f"SELECT {cols_formateo} FROM {i[0]}", con=conn)
    sub_conjuntos[i[0]] = df
print(sub_conjuntos)
    
# Imprimir las dimensiones de los conjuntos de datos
for i in tablas:
    print("Tabla:", i[0], "- Dimensión:", datos[i[0]].shape)
    print("Subconjuntos:", i[0], "- Dimensión:", sub_conjuntos[i[0]].shape)
    
# Recordatorio:
#   - Las consultas SELECT nos permiten recuperar datos específicos de una base de datos. Estos pueden ser la totalidad de los
#     datos o un subconjunto de los mismos.
