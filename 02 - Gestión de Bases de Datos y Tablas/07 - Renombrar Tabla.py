# Importar librerías
import mysql.connector as mysql

# Definir la conexión
conn = mysql.connect(
    user="root",
    password="root",
    host="localhost"
    )

print("Estatus:", conn.is_connected())

# Definir cursor
cursor = conn.cursor()

# Definir la base de datos a usar
bd = "clientes"
cursor.execute(f"USE {bd}")
# Modificar nombre de la tabla
nombre_viejo = "agenda_contactos"
nombre_nuevo = "contactos"
query = f"ALTER TABLE {nombre_viejo} RENAME TO {nombre_nuevo}"
cursor.execute(query)

# Verificar el nombre de tabla
cursor.execute("SHOW TABLES")
print(list(cursor))

# Cambiar nombre al original
query = f"ALTER TABLE {nombre_nuevo} RENAME TO {nombre_viejo}"
cursor.execute(query)

# Verificar el nombre de la tabla
cursor.execute("SHOW TABLES")
print(list(cursor))

# Recordatorio:
#   - Renombrar una tabla puede formar parte de un proceso de mantenimiento destinado a la consistencia o para dar mayor claridad
#     a la información que contiene la tabla.
