# Importar librerías
import mysql.connector as mysql
import time

# Conexión
conn = mysql.connect(
    user="root",
    password="root",
    database="world"
    )
# Definir cursor
cursor = conn.cursor()

# Consulta Ineficiente
query = "SELECT * FROM city WHERE CountryCode = 'USA' OR CountryCode = 'BRA' OR CountryCode = 'CHIL' OR  CountryCode = 'MXN'"
inicio_ineficiente = time.time()
for i in range(15_000):
    cursor.execute(query)
    resultados_ineficientes = cursor.fetchall()
tiempo_ineficiente = time.time() - inicio_ineficiente

# Consulta eficiente
query = "SELECT * FROM city WHERE CountryCode IN ('USA', 'BRA', 'CHIL', 'MXN')"
inicio_eficiente = time.time()
for i in range(15_000):
    cursor.execute(query)
    resultados_eficientes = cursor.fetchall()
tiempo_eficiente = time.time() - inicio_eficiente

# Imprimir el tiempo de ejecución de cada consulta
print("Tiempo de ejecución de la consulta ineficiente =", tiempo_ineficiente)
print("Tiempo de ejecución de la consulta eficiente =", tiempo_eficiente)

# Recordatorio:
#   - Las consultas eficientes pueden minimizar el tiempo de procesamiento y maximizar la velocidad de respuesta.
#   - También nos pueden ayudar a reducir el consumo de recursos y costos.
