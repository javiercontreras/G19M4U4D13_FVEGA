from anuncio import Video,Display,Social
from error import LargoExcedidoError

class Campana():
    def __init__(self, nombre:str,fecha_inicio, fecha_termino, anuncios:list):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.__obtener_instacia_anuncio(a) for a in anuncios]

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        if len(nombre) <= 250:
            self.__nombre = nombre
        else:
            raise LargoExcedidoError("El nombre no puede tener mas de 250 caracteres")
    
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio
    
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self,fecha_inicio):
        self.__fecha_termino = fecha_inicio
    
    @property
    def anuncios(self):
        return self.__anuncios
    
    def __str__(self):
        cant_video = len(list(filter(lambda i: isinstance(i,Video), self.anuncios)))
        cant_display = len(list(filter(lambda i: isinstance(i,Display), self.anuncios)))
        cant_social = len(list(filter(lambda i: isinstance(i,Social), self.anuncios)))

        return f"Nombre de la Campana: {self.__nombre} \nAnuncios :\n - {cant_video} Video\n- {cant_display} Display\n- {cant_social} Social\n"    
    
    def __obtener_instacia_anuncio(self, anuncio:dict):
        tipo_anuncio = anuncio.get("tipo","").lower()
        ancho = anuncio.get("ancho",0)
        alto = anuncio.get("alto",0)
        url_archivo = anuncio.get("url_archivo","")
        url_clic = anuncio.get("url_clic","")
        sub_tipo = anuncio.get("sub_tipo","")
        duracion = anuncio.get("duracion", 0)

        if tipo_anuncio == "video":
            return Video(url_archivo=url_archivo, url_click=url_clic,sub_tipo=sub_tipo,duracion=duracion)
        elif tipo_anuncio == "social":
            return Social(ancho=ancho,alto=alto,url_click=url_clic,url_archivo=url_archivo,sub_tipo=sub_tipo)
        else:
            return Display(ancho,alto,url_click=url_clic,url_archivo=url_archivo,sub_tipo=sub_tipo)
            