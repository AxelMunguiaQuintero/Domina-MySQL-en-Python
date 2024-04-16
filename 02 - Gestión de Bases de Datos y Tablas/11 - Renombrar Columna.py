# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(
    user="root",
    password="root",
    database="clientes"
    )
cursor = conn.cursor()

# Columnas actuales
tabla = "agenda_contactos"
columnas = pd.read_sql_query(sql=f"SHOW COLUMNS FROM {tabla}", con=conn)
columnas = columnas["Field"]


# Modificar nombre columna
nombre_viejo = "email"
nombre_nuevo = "correo_electronico"
query = f"ALTER TABLE {tabla} RENAME COLUMN {nombre_viejo} TO {nombre_nuevo}"
cursor.execute(query)

# Validar
tabla = "agenda_contactos"
nuevas_columnas = pd.read_sql_query(sql=f"SHOW COLUMNS FROM {tabla}", con=conn)
nuevas_columnas = nuevas_columnas["Field"]

# Cambiiar a su estado original
query = f"ALTER TABLE {tabla} RENAME COLUMN {nombre_nuevo} TO {nombre_viejo}"
cursor.execute(query)

# Validar
columnas_iniciales = pd.read_sql_query(sql=f"SHOW COLUMNS FROM {tabla}", con=conn)["Field"]
if all(columnas_iniciales == columnas):
    print("¡Columnas originales!")
    
# Recordatorio:
#   - El renombrar una columna nos ayuda a mantener la legibilidad y comprensión de nuestros datos tanto para usuarios como para desarrolladores.
