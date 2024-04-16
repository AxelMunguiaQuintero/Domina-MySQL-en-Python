# Importar librerías
import mysql.connector as mysql
import json

# Realizar nuestra conexión
conn = mysql.connect(
    user="root",
    password="root",
    host="localhost"
    )
print("Estatus de conexión:", conn.is_connected())
# Definir cursor 
cursor = conn.cursor()

# Información de MySQL
print("Usuario:", conn.user)
print("Versión:", conn.get_server_info())
print("Host:", conn.server_host)
print("Puerto:", conn.server_port)

# Consultar las Bases de Datos
query = "SHOW DATABASES"
cursor.execute(query)
dbs = cursor.fetchall()
print("Bases de datos:", dbs)

# Consultar tablas en cada base
db_muestra = "world"
query=f"SHOW TABLES FROM {db_muestra}"
cursor.execute(query)
tablas_world = cursor.fetchall()
print(tablas_world)

# Describir cada tabla
query = "DESCRIBE {base_datos}.{tabla}".format(base_datos=db_muestra, tabla=tablas_world[0][0])
cursor.execute(query)
contenido_tabla = cursor.fetchall()
print(contenido_tabla)

def obtener_MySQL_info():
    
    """
    Obtiene la información existente dentro de MySQL.
    
    Salida
    ------
        Diccionario con información de nuestras bases de datos dentro de MySQL.
    """
    
    # Almacenar 
    db_info = {
        "MySQL": {
            "Server": conn.get_server_info(),
            "Host": conn.server_host,
            "Port": conn.server_port,
            "DBs": {}
            }
        }
    # Obtener BDs
    cursor.execute("SHOW DATABASES")
    for i in cursor:
        db_info["MySQL"]["DBs"][i[0]] = {}
    # Consultar las tablas dentro de cada base 
    for i in db_info["MySQL"]["DBs"]:
        query = f"SHOW TABLES FROM {i}"
        cursor.execute(query)
        tablas = cursor.fetchall()
        # Obtener la estructura de cada tabla
        for t in tablas:
            cursor.execute(f"DESCRIBE {i}.{t[0]}")
            estructura_tabla = cursor.fetchall()
            db_info["MySQL"]["DBs"][i][t[0]] = estructura_tabla
            
    return db_info

# Recuperar información
mysql_info = obtener_MySQL_info()
print("Información General de MySQL:\n", json.dumps(mysql_info, indent=4))

# Recordatorio:
#   - Podemos consultar toda la información existente en MySQL desde Python.
