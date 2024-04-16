# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(user="root", password="root", database="empresa")

df = pd.read_sql(sql="SELECT * FROM colaboradores", con=conn, index_col="id")

# Insertar Datos

# Ejemplo 1: Insertar múltiples colaboradores (concatenar)
nuevos_colaboradores = pd.DataFrame({
    "nombre": ["Bob", "Carol"],
    "trabajo": ["Gerente", "Ingeniero"],
    "salario": [50000, 60000],
    "pais": ["Reino Unido", "Canadá"]
    }, index = [df.index[-1] + 1, df.index[-1] + 2])
df = pd.concat([df, nuevos_colaboradores])
print("DataFrame con {} columnas y {} filas".format(*df.shape))

# Ejemplo 2: Insertar un nuevo colaborador (desde el índice)
ultimo_indice = df.index[-1] + 1
df.loc[ultimo_indice] = ["Gerardo", "Técnico", 45000, "España"]

# Update Datos

# Ejemplo 1: Aumentar el salario de todos los colaboradores por un 10%
df["salario"] = df["salario"] * 1.10 

# Ejemplo 2: Cambiar los salarios de un país específico 
df.loc[df["pais"] == "Mexico", "salario"] = 55000

# Ejemplo 3: Cambiar un valor en específicio 
df.loc[10003, "trabajo"] = "Periodista"

# Delete Datos

# Ejemplo 1: Eliminar colaboradores con salarios superiores a 400000
df = df[df["salario"] < 40000]

# Ejemplo 2: Eliminar colaboradores de un país específico 
df = df[df["pais"] != "Canada"]

# Recordatorio:
#   - El uso de Panddas para la gestión de datos ofrece una interfaz sencilla y eficiente, facilitando tareas de 
#     manipulación y análisis de datos de manera rápida y eficiente.
