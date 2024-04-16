# Importar librerías
import mysql.connector as mysql
import time


# Definir nuestra conexión
config = {
    "user": "root",
    "password": "root",
    "host": "localhost",
    "port": 3306,
    "database": None
    }
conn = mysql.connect(**config)
print("Estado de la conexión:", conn.is_connected())

# Definir cursor
cursor = conn.cursor()

# Crear una base de datos
db_nombre = "base_datos_prueba"
query = f"CREATE DATABASE IF NOT EXISTS {db_nombre}"
cursor.execute(query)
# Verificar
cursor.execute("SHOW DATABASES")
print("Bases de Datos:", list(cursor))

# Eliminar la base de datos
print("¡Cuidado! Estas por eliminar una base de datos. Tienes 5 segundos para detener el código")
time.sleep(5)
query = f"DROP DATABASE {db_nombre}"
cursor.execute(query)
print("Base de datos ha sido eliminada")
# Verificar que ya no existe
cursor.execute("SHOW DATABASES")
print("Bases de Datos:", list(cursor))


# Eliminar por segunda ocasión nuestra base de datos
try: 
    query = f"DROP DATABASE {db_nombre}"
    cursor.execute(query)
except Exception as error:
    print("Error:", error)
    
query = f"DROP DATABASE IF EXISTS {db_nombre}"
cursor.execute(query)

# Recordatorio:
#   - Eliminar una base de datos es una acción irreversible y puede resultar en la pérdida total de los datos almacenados en ella.
#   - Por lo general, no tendremos privilegios de administrador, pero debemos tener cuidado porque dañaríamos la totalidad de los datos.
