# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(
    user = "root",
    password = "root"
    )
cursor = conn.cursor()


# Base de Datos que usaremos
cursor.execute("USE clientes")

# Obtener la estructura de la tabla
tabla_nombre = "agenda_contactos"
estructura = pd.read_sql(sql=f"DESCRIBE {tabla_nombre}", con=conn)
print(f"Número de columnas = {estructura.shape[0]}")

# Agregar columna
query = f"ALTER TABLE clientes.{tabla_nombre} ADD COLUMN licenciatura VARCHAR(50) NOT NULL COMMENT 'Licenciatura Estudiada'"
cursor.execute(query)

# Verificar si la nueva estructura es diferente
nueva_estructura = pd.read_sql(sql=f"DESCRIBE {tabla_nombre}", con=conn)
print(f"Número de columnas = {nueva_estructura.shape[0]}")

# Recordatorio:
#   - Agregar una nueva columna a una tabla existente a veces surge debido a la necesidad de incluir información adicional que no se
#     había considerado originalmente o de la cual no se tenía previo aviso.
