# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(user="root", password="root", database="empresa")

df = pd.read_sql(sql="SELECT * FROM colaboradores", con=conn, index_col="id")

# Operadores lógicos

# Ejemplo 1: Seleccionar colaboradores con salarios entre 40000 y 60000
rango_valores = df[(df["salario"] >= 40000) & (df["salario"] <= 60000)]

# Ejemplo 2: Seleccionar colaboradores que no sean de Austria o que tengan salarios superiores a 15000
doble_condicional = df[(df["pais"] != "Austria") | (df["salario"] > 15000)]

# ORDER BY

# Ejemplo 1: Agrupar colaboradores por país y calcular el salario promedio
pais_salario = df.groupby("pais")["salario"].mean()

# Ejemplo 2: Agrupar colaboradores por país y trabajo, y calcular el salario máximo en cada grupo
max_sal = df.groupby(["pais", "trabajo"])["salario"].max()

# HAVING

# Ejemplo 1: Agrupar colaboradores por país, calcular el salario promedio y filtrar aquellos que ganan más de 50000
pais_salario_superior = df.groupby("pais")["salario"].mean()
pais_salario_superior = pais_salario_superior[pais_salario_superior > 50000]

# Valores únicos

# Ejemplo 1: Obtener los países únicos en la tabla
resultado1 = df["pais"].unique()

# Ejemplo 2: Obtener los trabajos únicos en la tabla
resultado2 = df["trabajo"].unique()

# Recordatorio:
#   - Pandas ofrece una potente funcionalidad de filtrado de información que permite seleccionar y manipular datos de manera ágil y eficiente.
