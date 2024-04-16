# Importamos librerías
import mysql.connector as mysql

# Definir parámetros de conexión
config = {
    "user": "root",
    "password": "root",
    "database": None
    }
conn = mysql.connect(**config)
print("Estatus:", conn.is_connected())

# Definir cursor
cursor = conn.cursor()

# Seleccionar una base
query = "SHOW DATABASES"
cursor.execute(query)
dbs = list(cursor)


# Método 1: Intentar cambiar el parámetro interno
conn.database = dbs[-1][0]
print("Base de datos actual:", conn.database)

# Método 2: Mediante consulta
query = f"USE {dbs[-2][0]}"
cursor.execute(query)
print("Base de datos actual:", conn.database)

# Método 3: Establecer una nueva conexión (Ineficiente)
config = {
    "user": "root",
    "password": "root",
    "database": dbs[-3][0]
    }
conn = mysql.connect(**config)
print("Base de datos actual:", conn.database)

# Cerrar nuestra conexión
conn.close()

# Recordatorio:
#   - El cambio entre base de datos es posible y nos permite trabajar con múltiples Bases de datos en nuestros proyectos.
