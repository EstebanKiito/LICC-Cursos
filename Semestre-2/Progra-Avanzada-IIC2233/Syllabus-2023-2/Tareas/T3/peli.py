import api
import requests


class Peliculas:

    def __init__(self, host, port):
        self.base = f"http://{host}:{port}"

    def saludar(self) -> dict:
        # Completar
        return "Completar"

    def verificar_informacion(self, pelicula: str) -> bool:
        # Completar
        return "Completar"

    def dar_informacion(self, pelicula: str) -> dict:
        # Completar
        return "Completar"

    def dar_informacion_aleatoria(self) -> dict:
        # Completar
        return "Completar"

    def agregar_informacion(self, pelicula: str, sinopsis: str, access_token: str):
        # Completar
        return "Completar"

    def actualizar_informacion(self, pelicula: str, sinopsis: str, access_token: str):
        # Completar
        return "Completar"

    def eliminar_pelicula(self, pelicula: str, access_token: str):
        # Completar
        return "Completar"

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 4444
    DATABASE = {
        "Mamma Mia": "Mamma Mia es una Comedia musical con ABBA",
        "Monsters Inc": "Monsters Inc trata sobre monstruos que asustan, niños y risas",
        "Incredibles": "Incredibles trata de una familia de superhéroes que salva el mundo",
        "Avengers": "Avengers trata de superhéroes que luchan contra villanos poderosos",
        "Titanic": "Titanic es sobre amor trágico en el hundimiento del Titanic",
        "Akira": "Akira es una película de ciencia ficción japonesa con poderes psíquicos",
        "High School Musical": "High School Musical es un drama musical adolescente en East High",
        "The Princess Diaries": "The Princess Diaries es sobre Mia, una joven que descubre que es" 
        "princesa de Genovia",
        "Iron Man": "Iron Man trata sobre un hombre construye traje de alta tecnología "
        "para salvar al mundo",
        "Tarzan": "Tarzan es sobre un hombre criado por simios en la jungla",
        "The Pianist": "The Pianist es sobre un músico judío que sobrevive en Varsovia"
        " durante el Holocausto",
    }
    thread = api.Server(HOST, PORT, DATABASE)
    thread.start()

    Peliculas = Peliculas(HOST, PORT)
    print(Peliculas.saludar())
    print(Peliculas.dar_informacion_aleatoria())
    print(Peliculas.actualizar_informacion("Titanic", "Titanic es sobre amor trágico inspitado"
                                          " en el historico hundimiento del Titanic","tereiic2233"))
    print(Peliculas.verificar_informacion("Tarzan"))
    print(Peliculas.dar_informacion("The Princess Diaries"))
    print(Peliculas.dar_informacion("Monsters Inc"))
    print(Peliculas.agregar_informacion("Matilda", "Matilda es sobre una niña con poderes"
                                     "telequinéticos que enfrenta a su malvada directora", 
                                      "tereiic2233"))
    print(Peliculas.dar_informacion("Matilda"))