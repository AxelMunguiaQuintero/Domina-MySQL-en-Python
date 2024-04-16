# Importar librerías
import mysql.connector as mysql


# Establecer la conexión
conn = mysql.connect(user="root", password="root", host="localhost")
print("Estatus:", conn.is_connected())

# Definir cursor
cursor = conn.cursor()

# Declarar el nombre de la base de datos
nombre = "base_datos_prueba"
query = f"CREATE DATABASE {nombre}"
cursor.execute(query)

# Consultar su existencia
cursor.execute("SHOW DATABASES")
dbs = cursor.fetchall()
print(dbs)

try: 
    cursor.execute(query)
except Exception as error:
    print("No se pudo crear la base de datos con error:", error)
    
query = f"CREATE DATABASE IF NOT EXISTS {nombre}"
cursor.execute(query)

# Recordatorio:
#   - Se pueden crear las bases de datos desde Python, pero debemos tener cuidado al momento de intentar crear bases
#     existentes, pues si no se utiliza una correcta sintaxis podríamos detener la ejecución de nuestra aplicación por 
#     los errores o afectar todo el proceso.
