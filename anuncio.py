from abc import ABC, abstractmethod
from error import SubTipoInvalidoError
class Anuncio(ABC):
    FORMATO = ""
    SUB_TIPOS = ()
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_click:str, sub_tipo):
        self.__ancho = self.validar_dimension(ancho)
        self.__alto = self.validar_dimension(alto)
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo

    
    @property
    def ancho(self):
        return self.__ancho   
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = self.validar_ancho(ancho) 
         
    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self, alto):
        self.__ancho = self.validar_dimension(alto)  


    @property
    def url_archivo(self):
        return self.__url_archivo
    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_click(self):
        return self.__url_click
    @url_click.setter
    def url_click(self, url_click):
        self.__url_click = url_click
    
    @property
    def sub_tipo(self):
        return self.__sub_tipo  
    @sub_tipo .setter
    def sub_tipo(self, sub_tipo ):
        if( isinstance(self,Video) and sub_tipo not in Video.SUB_TIPOS or isinstance(self,Display) and sub_tipo not in Display.SUB_TIPOS or isinstance(self,Social) and sub_tipo not in Social.SUB_TIPOS ):
            raise SubTipoInvalidoError("El sub tipo no esta dentro de los permitidos")
        else:
            self.__sub_tipo = sub_tipo

    #Funciones
    def validar_dimension(self, dimension):
        return dimension if dimension > 0 else 1

    @staticmethod
    def mostrar_formatos():
        for f in Video.SUB_TIPOS:
            print(f"Formato video : {f}")
        for f in Display.SUB_TIPOS:
            print(f"Formato Displauy : {f}")
        for f in Social.SUB_TIPOS:
            print(f"Formato Social : {f}")
        
        
    @abstractmethod
    def comprimir_anuncio():
        pass
    @abstractmethod
    def redimensionar_anuncio():
        pass



class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream","outstream")
    def __init__( self,url_archivo: str, url_click: str, sub_tipo, duracion:int):
        super().__init__(1, 1, url_archivo, url_click, sub_tipo)
        self.__duracion = duracion if duracion >0 else 5

    @property
    def duracion(self):
        return self.__duracion
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion if duracion > 0 else 5

    def comprimir_anuncio():
        print("Comprension de video aun no implementada")
    
    def redimensionar_anuncio():
        print("Redimnesionamiento aun no implementado")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional","native")
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_click: str, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)
    
    def comprimir_anuncio():
        print("Comprension de display aun no implementada")

    def redimensionar_anuncio():
        print("Redimnesionamiento de display aun no implementado")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook","linkedin")
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_click: str, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio():
        print("Comprension de Social aun no implementada")

    def redimensionar_anuncio():
        print("Redimnesionamiento de Social aun no implementado")
if __name__ == '__main__':

    a = Anuncio(ancho= -45, alto= 1, url_archivo="https://archivo", url_click="click", sub_tipo="tipo")
    a.FORMATO = "mp4"
    a.mostrar_formatos()
 