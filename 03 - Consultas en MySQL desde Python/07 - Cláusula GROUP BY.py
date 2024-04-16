# Importar librerías
import mysql.connector as mysql
import pandas as pd
from faker import Faker
from warnings import filterwarnings
filterwarnings("ignore")


# Instancia
fake = Faker()
# Crear datos
print("Nombre:", fake.name())
print("Trabajo:", fake.job())
print("Salario:", fake.random_number(digits=5))
print("País de Origen:", fake.country())

# Crear los registros de nuestra tabla
datos = [[fake.name(), fake.job(), fake.random_number(digits=5), fake.country()] for i in range(10_000)]

# Establecer la conexión
conn = mysql.connect(
    user="root",
    password="root",
    database="empresa"
    )
cursor = conn.cursor()

# Crear tabla
cursor.execute("""
               CREATE TABLE IF NOT EXISTS colaboradores (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   nombre VARCHAR(100),
                   trabajo VARCHAR(150),
                   salario DECIMAL(10, 2),
                   pais VARCHAR(100)
                   )
               """)
               
# Insertar los datos
query = "INSERT INTO colaboradores (nombre, trabajo, salario, pais) VALUES (%s, %s, %s, %s)" 
cursor.executemany(query, datos)
# Confirmar cambios
conn.commit()     
               
# Recuperar los datos
colaboradores = pd.read_sql("SELECT * FROM colaboradores", con=conn)
               
# Consulta No. 1: Contar la cantidad de colaboradores por país
query = """
SELECT pais, COUNT(*) AS cantidad_colaboradores FROM colaboradores GROUP BY pais
"""
colaboradores_pais = pd.read_sql_query(sql=query, con=conn)
print("País con mayor número de trabajadores es:", colaboradores_pais["cantidad_colaboradores"].max())               
               
# Consulta No. 2: Calcular el salario promedio por trabajo
query = """
SELECT trabajo, AVG(salario) AS salario_promedio FROM colaboradores GROUP BY trabajo
"""
trabajo_salario = pd.read_sql_query(sql=query, con=conn)

# Consulta No. 3: Obtener la suma total de salarios por país
query = """
SELECT pais, SUM(salario) AS suma_salarios FROM colaboradores GROUP BY pais
"""
salario_pais = pd.read_sql_query(sql=query, con=conn)
               
# Consulta No. 4: Obtener el salario máximo por país
query = """
SELECT pais, MAX(salario) AS salario_maximo FROM colaboradores GROUP BY pais
"""
salario_maximo_pais = pd.read_sql_query(sql=query, con=conn) 
               
# Consulta No. 5: Contar la cantidad de colaboradores por trabajo con un salario superior a $50,000.00
query = """
SELECT trabajo, COUNT(*) AS cantidad_colaboradores FROM colaboradores WHERE salario > 50000 GROUP BY trabajo
"""
trabajadores_ingreso_sup = pd.read_sql_query(sql=query, con=conn)
               
# Recordatorio:
#   - GROUP BY, nos permite organizazr nuestros datos de una manera significativa y útil para un análisis más profundo o una mejor
#     percepción de la distribución de los datos.
       