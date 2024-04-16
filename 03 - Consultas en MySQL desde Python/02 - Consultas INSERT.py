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

# Eliminar base de datos
cursor.execute("DROP DATABASE catalogo_productos")

# Verificar su inexistencia
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

# Recordatorio:
#   - INSERT nos permite agregar datos a una tabla existente en una base de datos. Se utiliza para insertar uno o varios registros
#     en una tabla, especificando los valores para cada columna en la fila que se va a insertar.
