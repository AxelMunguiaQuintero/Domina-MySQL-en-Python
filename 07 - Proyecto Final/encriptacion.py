# Importar librerías
from cryptography.fernet import Fernet
import json
import os

# Definir clase
class Encriptacion:
    
    """
    Clase que desencripta y encripta credenciales necesarias para la base de datos y para la API de New York Times
    """
    
    def __init__(self, clave_secreta: str) -> None:
        
        """
        Constructor
        """
        
        # Atributos
        self.clave_secreta = clave_secreta
        # Crear un objeto Fernet con la clave secreta
        self.fernet = Fernet(key=self.clave_secreta)
        
    def encriptar(self, credenciales_ruta: str, encriptacion_ruta: str) -> None:
        
        """
        Encripta un documento que contenga las credenciales
        """
        
        # Leer datos
        credenciales = open(credenciales_ruta, "r").read()
        # Convertir bytes
        json_bytes = credenciales.encode()
        # Encriptar los datos usando la clave secreta y el objeto Fernet
        datos_encriptados = self.fernet.encrypt(json_bytes)
        # Guardar datos
        with open(encriptacion_ruta, "wb") as credenciales_encriptadas:
            credenciales_encriptadas.write(datos_encriptados)
            credenciales_encriptadas.close()
        
    def desencriptar(self, encriptacion_ruta) -> dict:
        
        """
        Desencripta las credenciales que están encriptadas
        """
        
        # Desencriptar los datos
        datos_encriptados = open(encriptacion_ruta, "rb").read()
        datos_desencriptados = self.fernet.decrypt(datos_encriptados)
        # Convertir los datos desencriptados de bytes a un diccionario
        credenciales = json.loads(datos_desencriptados.decode())
        
        return credenciales

if __name__ == "__main__":
    # Definir la palabra clave
    palabra_clave = Fernet.generate_key() # Crear una clave única para cifrar y descifrar los datos
    # Instanciar clase
    enc = Encriptacion(palabra_clave)
    # Crear un archivo json
    credenciales_ejemplo = {"usuario": "usuario", "contraseña": "contraseña"}
    credenciales_ejemplo = json.dumps(credenciales_ejemplo)
    with open("credenciales_ejemplo.json", "w") as credenciales:
        credenciales.write(credenciales_ejemplo)
    # Encriptar
    enc.encriptar(credenciales_ruta="credenciales_ejemplo.json", encriptacion_ruta="clave_secreta.key")
    # Mostar credenciales encriptadas
    print(open("clave_secreta.key", "rb").read())
    # Desencriptar
    credenciales = enc.desencriptar("clave_secreta.key")
    print(credenciales)
    # Eliminar documentos para no confundirnos
    os.remove("clave_secreta.key")
    os.remove("credenciales_ejemplo.json")
    
    # Recordatorio:
    #   - Fernet es un tipo de encriptación que se asegura de que los mensajes o datos que envías y recibes por internet
    #     sean privados y seguros. Funciona conviertiendo la información en un código que solo puede ser descifrado con una
    #     clave específica.
    