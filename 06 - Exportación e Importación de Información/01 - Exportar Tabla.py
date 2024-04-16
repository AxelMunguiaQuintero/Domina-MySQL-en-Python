# Importar librerías
import subprocess

# Definir credenciales
usuario = "root"
contra = "root"
host = "localhost"

# Definir función
def exportar_tabla(base_datos: str, tabla: str, archivo: str, esperar_exportacion: bool = True) -> None:
    
    """
    Exporta una tabla de MySQL en formato .sql
    
    Parámetros
    ----------
    base_datos : str
        Base de datos de donde se exportará la tabla
    tabla : str
        Tabla que se desea exportar.
    archivo : str
        Nombre del archivo donde se guardará la tabla (incluir extensión).
    esperar_exportacion : bool, opcional
        Indica si se debe de esperar a que la exportación termine.
        Si es True (por defecto), esperará a que se complete la exportación.
        Si es False, la exportación se ejecutará en la terminal sin esperar a que termine.
        
    Salida
    ----------
    return : NoneType : None.
    """
    
    # Exportar
    comando = "mysqldump --add-drop-table -h {host} -u {usuario} -p{contraseña} {bd} {tabla} > {nombre_archivo}"
    
    comando = comando.format(host=host, 
                             usuario=usuario,
                             contraseña=contra,
                             bd=base_datos,
                             tabla=tabla,
                             nombre_archivo=archivo)
    
    if esperar_exportacion:
        print(subprocess.call(comando, shell=True, stderr=subprocess.STDOUT))
    else:
        print(subprocess.Popen(comando, shell=True, stderr=subprocess.STDOUT))
        
# "Country" -> "world"
exportar_tabla(base_datos="world", tabla="country", archivo="tabla.sql")

# Recordatorio:
#   - Exportar una tabla puede ser útil para asegurarnos de que los datos estén a salvo y disponibles cuando se necesiten.
