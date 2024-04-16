# Importar librerías
import mysql.connector as mysql 


# Establecer los parámetros de conexión
config = {
    
    "user": "root", # Nombre de usuario de MySQL
    "password": "root", # Contraseña de MySQL
    "host": "localhost", # Dirección del host de MySQL (Podría ser una Dirección IP o un nombre de Host)
    "database": None, # Nombre de la Base a la que te quieres conectar
    "raise_on_warnings": True # Esta configuración hará que se lancen excepciones en caso de advertencias
    
    }

# Establecer Conexión
conn = mysql.connect(**config)
print("¡Conexión ha sido exitosa!")

# Imprimir información de conexión
print("--------- Información de Conexión ---------")
print("Versión de MySQL:", conn.get_server_info())
print("Id de la conexión:", conn.connection_id)
print("Servidor Host:", conn.server_host)
print("Puerto del servidor:", conn.server_port)
print("Base de datos:", conn.database)
print("Usuario:", conn.user)
print("Contraseña:", conn._password)
print("Conexión Activa:", conn.is_connected())
print("Conexión Cerrado:", conn.is_closed())
print("-" * 20)


# Definir el cursor
cursor = conn.cursor()
# Identificar las Bases de Datos Actuales
cursor.execute("SHOW DATABASES")
# Extraer los resultados
for i in cursor:
    print(i)
    
# Cerrrar conexión
conn.close()
# Corroborar que la conexión no sigue activa
print("Conexión Activa:", conn.is_connected())

# Recordatorio:
#   - Se puede establecer la conexión a MySQL desde Python. Debemos tener cuidado en todo momento con la posible filtración
#     de nuestras credenciales.
