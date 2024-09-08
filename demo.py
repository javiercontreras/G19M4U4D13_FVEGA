from campana import Campana

c = Campana("La gran Camapana","05-08-2024","05-08-2025",
            [{"tipo":"video", "url_clic" : "url",
              "url_archivo0":"C://archivo",
              "sub)_tipo":"instream",
              "dutacion":30
              }])
try:
    nombre = input("Ingrese nuevo nombre de Campana\n")
    sub_tipo = input("Ingrese un nuevo sub tipo del anuncion\n")
    c.nombre = nombre
    c.anuncios[0].sub_tipo = sub_tipo
except Exception as e:
    with open("error.log","+a") as log:
        log.write(f"{e}\n")

