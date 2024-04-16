# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión 
conn = mysql.connect(user="root", password="root", database="world")

# Recuperar los datos
datos = pd.read_sql(sql="SELECT * FROM city", con=conn)

# Cerrar la conexión
conn.close()

# Calcular la media (AVG) de la población de las ciudades
media_poblacion = datos["Population"].mean()
print("La media de la población de las ciudades es:", int(media_poblacion))

# Contar el número total de ciudades
total_ciudades = datos.shape[0]
total_ciudades_unicas = datos["Name"].nunique() 

# Encontrar la ciudad con la población mínima
indice = datos["Population"].idxmin()
ciudad_min_poblacion = datos.loc[indice]
print("La ciudad con la población mínima:", ciudad_min_poblacion)

# Encontrar la ciudad con la población máxima
indice = datos["Population"].idxmax()
ciudad_max_poblacion = datos.loc[indice]
print("La ciudad con la población máximo:", ciudad_max_poblacion)

# Calcular la suma total de la población de todas las ciudades
suma_poblacion_total = datos["Population"].sum()
print("La suma total de la población es:", suma_poblacion_total)

# Calcular la suma de la población por país y ordenarlos de mayor a menor
media_poblacion_pais = datos.groupby(["CountryCode"])[["Population"]].sum().sort_values(by="Population", ascending=False)

# Contar el número de ciudades por país y odenarlos de menor a mayor
numero_ciudades_pais = datos.groupby(["CountryCode"])[["Population"]].count().sort_values(by="Population", ascending=True)

# Recordatorio:
#   - Pandas ofrece una forma poderosa y flexible de realizar operaciones de agregación y tratamiento de datos similares a los
#     que se pueden realizar con consultas SQL en una base de datos.
