class Error(Exception):
    pass

class LargoExcedidoError(Error):
    def __init__(self, mensaje:str) -> None:
        self.__mensaje = mensaje
    pass

class SubTipoInvalidoError(Error):
    pass

