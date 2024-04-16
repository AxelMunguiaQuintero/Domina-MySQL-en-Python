# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")


# Conexión
conn = mysql.connect(user="root", password="root", host="localhost")
print("Estatus de la conexión:", conn.is_connected())
cursor = conn.cursor()

# Crear una base de datos para el catálogo de nuestros productos
query = "CREATE DATABASE IF NOT EXISTS catalogo_productos"
cursor.execute(query)

# Verificar existencia
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

# Crear nuestra tabla
query = """
    CREATE TABLE IF NOT EXISTS productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        precio DECIMAL,
        categoria VARCHAR(255),
        descripcion TEXT
        )
"""
cursor.execute("USE catalogo_productos")
cursor.execute(query)

# Verificar 
cursor.execute("SHOW TABLES")
print(cursor.fetchall())

# Definir los datos a insertar
productos_data = {
    "nombre": ["Laptop", "Teléfono", "Libro"] * 1000,
    "precio": [1200, 600, 20] * 1000,
    "categoria": ["Tecnología", "Tecnología", "Educación"] * 1000,
    "descripción": ["Potente laptop con pantalla de alta resolución",
                    "Teléfono inteligente con cámata de alta calidad",
                    "Libro de ficción clásico para lectores de todas las edades"] * 1000
    }
df_productos = pd.DataFrame(productos_data)

# Insertar los datos del DataFrame en la tabla "productos"
for indice, producto in df_productos.iterrows(): # Extraer el índice y los datos
    query = """
        INSERT INTO productos (nombre, precio, categoria, descripcion)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (producto["nombre"], producto["precio"], producto["categoria"], producto["descripción"]))

# Confirmar la ejecución de la consulta
conn.commit()

# Recuperación de datos
productos = pd.read_sql(sql="SELECT * FROM productos", con=conn)
print(productos)

# Actualizar los registros
query = """
    UPDATE {}
    SET precio = {}
    WHERE nombre = '{}'
"""

# Definir los datos que se van a actualizar
nombres = ["Laptop", "Teléfono", "Libro"]
incremento = 1.10
precios = [1200 * incremento, 600 * incremento, 20 * incremento]

for nomb, prec in zip(nombres, precios):
    cursor.execute(query.format("productos", prec, nomb))
    
# Confirmar la ejecución de la consulta
conn.commit()

# Verificar que los cambios han sido aplicados
productos_actualizados = pd.read_sql_query(sql="SELECT * FROM productos", con=conn)
if all(producto["precio"] != productos_actualizados["precio"]):
    print("Los precios han sido actualizados")

# Eliminar la bd
cursor.execute("DROP DATABASE catologo_productos")

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

# Recordatorio:
#   La consulta UPDATE es importante para modificar los datos existentes en una tabla, lo que permite actualizar registros
#   específicos con nuevos valores. Esto es fundamental para mantener la integridad y la precisión de la información almacenada,
#   así como para aplicar cambios o correcciones en los datos cuando sea necesario.
