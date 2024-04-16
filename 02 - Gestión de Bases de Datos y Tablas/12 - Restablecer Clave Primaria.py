# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")


# Conexión
conn = mysql.connect(user="root", password="root", database="clientes")
# Cursor
cursor = conn.cursor()

# Obtener las columnas de nuestra tabla
query = "SHOW COLUMNS FROM agenda_contactos"
estructura = pd.read_sql(sql=query, con=conn)

# Nueva estructura de clave primaria
query = "ALTER TABLE agenda_contactos ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY"
# Eliminar clave primaria existente
query_eliminar = "ALTER TABLE agenda_contactos DROP COLUMN id"
cursor.execute(query_eliminar)
# Establecer una nueva Clave Primaria
cursor.execute(query)

# Validar
contactos = pd.read_sql(sql="SHOW COLUMNS FROM agenda_contactos", con=conn)

# Clave primaria original
query = "ALTER TABLE agenda_contactos RENAME COLUMN identificador TO id"
cursor.execute(query)
# Verificar
query = "SHOW COLUMNS FROM agenda_contactos"
estructura_original = pd.read_sql_query(sql=query, con=conn)
if all(estructura_original.sort_values(by="Field")["Field"].values == estructura.sort_values(by="Field")["Field"].values):
    print("¡Clave Primaria se encuentra en su estado inicial!")
    
# Recordatorio:
#   - La Clave Primaria garantiza la unicidad de cada fila en una base de datos, facilitando la gestión y la integridad de los datos.
#   - Debemos de tener especial cuidado en el proceso de cambiar la Clave Primaria porque podríamos experimentar pérdida de información.
