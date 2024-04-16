# Importar librerí­as
import requests
import newspaper # pip3 install newspaper3k
import json


# Definir clase
class Extraccion:
    
    """
    Esta clase se encarga de extraer los artí­culos de una url proporcionada
    """
    
    def __init__(self, api_key: str) -> None:
        
        """
        Constructor
        """
        
        # Atributos
        self.api_key = api_key
        self.url_articulos_populares = "https://api.nytimes.com/svc/mostpopular/v2/"
        self.endpoint_populares = "viewed/1.json"
        self.url_articulos_palabra = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
        self.articulos = []
        
    def obtener_articulos_populares(self) -> list:
        
        """
        Esta función obtiene los artí­culos más populares del dí­a
        """
        
        # Realizar requests
        url = self.url_articulos_populares + self.endpoint_populares + "?api-key=" + self.api_key
        r = requests.get(url)
        # Revisar estado interno
        if r.status_code == 200:
            datos = r.json()
            for articulo in datos["results"]:
                self.articulos.append(articulo["url"])
        else:
            print("Error al obtener los datos:", r.status_code)
            print("Contenido:", r.content)
            
        return self.articulos
    
    def obtener_articulos_busqueda(self, palabra: str) -> list:
        
        """
        Esta función obtiene artí­culos que tengan alguna palabra clave
        """
        
        # Realizar request
        params = {
            "q": palabra,
            "api-key": self.api_key
            }
        r = requests.get(self.url_articulos_palabra, params=params)
        if r.status_code == 200:
            datos = r.json()
            for articulo in datos["response"]["docs"]:
                self.articulos.append(articulo["web_url"])
        else:
            print("Error al obtener los datos:", r.status_code)
            print("Contenido:", r.content)
            
            
        return self.articulos
    
    def extraer_articulo(self, url: str) -> dict:
        
        """
        Esta función extraer todo el contenido del artí­culo que se encuentra en la url que pasamos
        """
        
        # Extraer
        articulo = newspaper.Article(url=url, language="en")
        articulo.download()
        articulo.parse()
        
        articulo_info = {
            "titulo": str(articulo.title),
            "texto": str(articulo.text),
            "autores": str(articulo.authors),
            "dia_publicacion": str(articulo.publish_date),
            "url_imagen": str(articulo.top_image),
            "videos": articulo.movies,
            "palabras_clave": articulo.keywords,
            "resumen": str(articulo.summary),
            "url": url
            
            }
        
        return articulo_info
    

if __name__ == "__main__":
    # Instanciar clase
    api_key = "3uszsAvho6xajqj9ewRn15jogeFDisLG"
    ext = Extraccion(api_key)
    # Extraer urls iniciales
    ext.obtener_articulos_populares()
    # Definir lista
    palabras = ["democracy", "economy", "technology", "crisis"]
    [ext.obtener_articulos_busqueda(i) for i in palabras]
    print(json.dumps(ext.extraer_articulo(url=ext.articulos[0]), indent=4))
