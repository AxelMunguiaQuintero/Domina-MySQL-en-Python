# Importar librerías
import subprocess

# Definir parámetros
params = {
    
    "usuario": "root",
    "contraseña": "root",
    "host": "localhost",
    "bd": "world",
    "nombre_archivo": "base_datos.sql",
    "esperar_exportacion": True
    
    }

# Definir comando el exportación
comando = "mysqldump --databases --add-drop-database --add-drop-table -h {host} -u {usuario} -p{contra} {bd} > {archivo}"
comando = comando.format(host=params["host"],
                         usuario=params["usuario"],
                         contra=params["contraseña"],
                         bd=params["bd"],
                         archivo=params["nombre_archivo"])

# Exportar
if params["esperar_exportacion"]:
    print(subprocess.call(comando, shell=True, stderr=subprocess.STDOUT))
else:
    print(subprocess.Popen(comando, shell=True, stderr=subprocess.STDOUT))
    
# Recordatorio:
#   - Exportar una base de datos es fundamental para realizar copias de seguridad, transferir datos entre sistemas y cumplir con regulaciones
#     de privacidad y protección de datos.
