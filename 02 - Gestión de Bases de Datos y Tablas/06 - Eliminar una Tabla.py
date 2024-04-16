# Importar librerías
import mysql.connector as mysql


# Definir conexión
conn = mysql.connect(
    user="root",
    password="root",
    host="localhost"
    )
cursor = conn.cursor()

# Establecer la base de datos
cursor.execute("USE clientes")
# Crear una Tabla
cursor.execute("""
               CREATE TABLE IF NOT EXISTS tabla_eliminacion
               (
                   identificador INT AUTO_INCREMENT PRIMARY KEY,
                   nombre VARCHAR(100) NOT NULL
                   )
               """)
# Verificar la existencia
cursor.execute("SHOW TABLES")
print(list(cursor))

# Eliminar la tabla
query = "DROP TABLE IF EXISTS tabla_eliminacion"
cursor.execute(query)

# Validar que se ha eliminado
cursor.execute("SHOW TABLES")
tablas_existencia = [i[0] for i in cursor]
if "tabla_eliminacion" not in tablas_existencia:
    print("¡La tabla se ha eliminado exitosamente!")
else:
    raise ValueError("La tabla no se ha eliminado")
    
# Recordatorio:
#   - La eliminación de tablas es una operación irreversible que debe de realizarse con precaución. Antes de eliminar una tabla,
#     asegúrate de haber respaldado adecuadamente todos los datos y de comprender las implicaciones de esta acción. Una vez eliminada,
#     todos los datos y la estructura asociada a la tabla desaparecerán permanentemente.
