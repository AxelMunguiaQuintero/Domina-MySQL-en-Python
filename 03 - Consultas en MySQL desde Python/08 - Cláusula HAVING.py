# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(
    user="root",
    password="root",
    database="empresa"
    )
cursor = conn.cursor()

# Consulta No. 1: Salario promedio por país para países con más de 35 empleados
query = """
SELECT pais, AVG(salario) AS salario_promedio FROM colaboradores
GROUP BY pais HAVING COUNT(*) > 35
"""
mas_35 = pd.read_sql(sql=query, con=conn)

# Consulta No. 2: Número de empleados por trabajo para trabajos con un salario promedio superior a $50,000
query = """
SELECT trabajo, COUNT(*) AS cantidad_empleados FROM colaboradores GROUP BY trabajo
HAVING AVG(salario) > 50000
"""
salario_mas50 = pd.read_sql_query(sql=query, con=conn)

# Consulta No. 3: Países con al menos 3 empleados y un salario mínimo que debe de ser superior a 5000, ordenados por salario
#                 de forma ascendente
query = """
SELECT pais, MIN(salario) AS salario_minimo FROM colaboradores
GROUP BY pais HAVING COUNT(*) >=3 AND MIN(salario) > 5000 ORDER BY salario_minimo ASC
"""
emp3_sal5 = pd.read_sql_query(sql=query, con=conn)

# Consulta No. 4: Trabajos con más de 20000 en salario promedio y al menos 20 empleados, ordenados por cantidad de empleados de forma
#                 ascendente
query = """
SELECT trabajo, COUNT(*) AS cantidad_empleados FROM colaboradores GROUP BY trabajo
HAVING AVG(salario) > 20000 AND COUNT(*) >= 20 ORDER BY cantidad_empleados DESC
"""
salario20_emp20 = pd.read_sql_query(sql=query, con=conn)
 
# Recordatorio:
#   - La cláusula HAVING en SQL se utiliza junto con GROUP BY para filtrar los resultados agregados basados en condiciones específicas.
#     También, permite aplicar restricciones a los grupos de datos resultantes, lo que es útil para realizar análisis detallados y obtener
#     información relevante de conjuntos de datos agrupados.
