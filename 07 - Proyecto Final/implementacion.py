# Importar librerías
import mysql.connector as mysql
import threading
import pandas as pd
from cryptography.fernet import Fernet
import json
import os
import encriptacion
import extraccion_articulos
from warnings import filterwarnings
filterwarnings("ignore")

# Encriptar credenciales
credenciales = {"usuario": "root", "contraseña": "root", "api_key": "3uszsAvho6xajqj9ewRn15jogeFDisLG"}
with open("credenciales.json", "w") as archivo:
    archivo.write(json.dumps(credenciales))
    archivo.close()
# Generar clave
clave = Fernet.generate_key()
encr = encriptacion.Encriptacion(clave)
encr.encriptar(credenciales_ruta="credenciales.json", encriptacion_ruta="clave_privada.key")

# Obtener las credenciales
credenciales = encr.desencriptar("clave_privada.key")

# Extraer artículos
ext = extraccion_articulos.Extraccion(credenciales["api_key"])
# Variables necesarias
diccionario_articulos = {}
mutex = threading.Lock()

# Función que se ejecutará en paralelo
def extraer_paralelo(url: str) -> None:
    
    """
    Función que servirá para extraer de manera paralelizada los artículos
    """
    
    articulo = ext.extraer_articulo(url=url)
    # Adquirir el sincronizador
    mutex.acquire()
    diccionario_articulos[articulo["titulo"]] = articulo
    mutex.release()
    
    
# Inicializar estructuras de código paralelo
ext.obtener_articulos_populares()
palabras = ["democracy", "economy", "technology", "crisis"]
[ext.obtener_articulos_busqueda(i) for i in palabras]
print("Total de urls:", len(set(ext.articulos)))
    
hilos = []
for url in ext.articulos:
    t = threading.Thread(target=extraer_paralelo, args=[url])
    hilos.append(t)
    t.start()
    
# Esperar a que cesen su ejecución
for t in hilos:
    t.join()
    
# Definir conexión
conn = mysql.connect(
    user=credenciales["usuario"],
    password=credenciales["contraseña"],
    host="localhost"
    )
print("Estatus de la conexión:", conn.is_connected())

# Definir cursor
cursor = conn.cursor()

# Definir el nombre de la bd
db_nombre = "Noticias_NYT"
query = "CREATE DATABASE IF NOT EXISTS " + db_nombre
cursor.execute(query)

# Consultar la existencia
cursor.execute("SHOW DATABASES")
dbs = cursor.fetchall()
print(dbs)
    
# Usar la bd creada
cursor.execute("USE " + db_nombre)
# Crear tabla
tabla_nombre = "articulos"
query = f"""
    CREATE TABLE IF NOT EXISTS {tabla_nombre} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(350) NOT NULL COMMENT 'Titulo del articulo',
        texto TEXT NOT NULL COMMENT 'Contenido del articulo',
        autores VARCHAR(350) NULL COMMENT 'Autores del articulo',
        dia_publicacion DATE NULL COMMENT 'Fecha que se ha publicado',
        url_imagen VARCHAR(350) NULL COMMENT 'Url de la imagen que aparece en el articulo',
        url VARCHAR(350) NULL COMMENT 'Url del articulo'
        )
"""
cursor.execute(query)
# Verificar
tablas = pd.read_sql(sql="SHOW TABLES FROM " + db_nombre, con=conn)
print(tablas)
    
# Convertir los artículos a DataFrame
articulos = pd.DataFrame(diccionario_articulos).T.reset_index(drop=True)
columnas = ["titulo", "texto", "autores", "dia_publicacion", "url_imagen", "url"]
articulos = articulos[columnas]
articulos["autores"] = articulos["autores"].apply(lambda x: " | ".join(eval(x)))
    
# Insertar todos los datos en la tabla
columnas = ", ".join(articulos.columns.tolist())
query = f"INSERT INTO {tabla_nombre} ({columnas}) VALUES (%s, %s, %s, %s, %s, %s)"
values = [tuple(row) for row in articulos.values]
for i in range(len(values)):
    try:
        cursor.execute(query, values[i])
    except Exception as error:
        print("Índice:", i, "Tiene un error ->", error)
        
query = "SELECT * FROM articulos"
articulos = pd.read_sql(sql=query, con=conn)
    
# Eliminar credenciales
os.remove("credenciales.json")
os.remove("clave_privada.key")
    
# Recordatorio:
#   - La encriptación de datos mejora el nivel de seguridad que tenemos con nuestra información.
#   - El cómputo paralelo nos ayuda a hacer más eficiente nuestro código al acelerar la ejecución de nuestro 
#     programa. Solo debemos de tomar las medidas necesarias para no corromper nuestros datos.
#   - El mundo del Big Data produce cantidades enormes de información que podemos recoletar para procesarla
#     y trabajar con ella.
