# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")


# Establecer conexión
conn = mysql.connect(user="root", password="root", host="localhost", port=3306)
print("Estatus de la conexión:", conn.is_connected())
print("Base de datos:", conn.database)
# Cursor
cursor = conn.cursor()

# Definir la consulta
db = "clientes"
tabla = "agenda_contactos"
columna = "licenciatura"
query = f"ALTER TABLE {db}.{tabla} DROP COLUMN {columna}"

# Verificar estructura
estructura = pd.read_sql(sql=f"DESCRIBE {db}.{tabla}", con=conn)
print("Número de columnas de nuestra tabla es:", estructura.shape[0])

# Ejecutar la consulta
cursor.execute(query)

# Verificar estructura
estructura = pd.read_sql(sql=f"DESCRIBE {db}.{tabla}", con=conn)
print("Número de columnas de nuestra tabla es:", estructura.shape[0])

# Eliminar nuevamente
try: 
    cursor.execute(query)
except Exception as error:
    print(error)
    
    
# Validar existencia
query = f"SHOW COLUMNS FROM {db}.{tabla}"
columnas = pd.read_sql(sql=query, con=conn)
print(columnas)
if columna in columnas["Field"]:
    query = f"ALTER TABLA {db}.{tabla} DROP COLUMN {columna}"
    cursor.execute(query)
else:
    print("¡La columna ya ha sido eliminada!")
    
# Recordatorio:
#   - Ciertamente, cualquier tipo de eliminación de datos (columnas, tablas o bases de datos) conlleva riesgos y debe manejarse
#     con precaución, ya que puede conllevar a una pérdida irreversible de información.
