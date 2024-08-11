import api
import requests


class Yolanda:

    def __init__(self, host, port):
        self.base = f"http://{host}:{port}"
        self.regex_validador_fechas = ''  # TODO: Completar
        self.regex_extractor_signo = ''  # TODO: Completar

    def saludar(self) -> dict:
        # TODO: Completar
        return "Completar"

    def verificar_horoscopo(self, signo: str) -> bool:
        # TODO: Completar
        return "Completar"

    def dar_horoscopo(self, signo: str) -> dict:
        # TODO: Completar
        return "Completar"

    def dar_horoscopo_aleatorio(self) -> dict:
        # TODO: Completar
        return "Completar"

    def agregar_horoscopo(self, signo: str, mensaje: str, access_token: str) -> str:
        # TODO: Completar
        return "Completar"

    def actualizar_horoscopo(self, signo: str, mensaje: str, access_token: str) -> str:
        # TODO: Completar
        return "Completar"

    def eliminar_signo(self, signo: str, access_token: str) -> str:
        # TODO: Completar
        return "Completar"


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 4444
    DATABASE = {
        "acuario": "Hoy será un hermoso día",
        "leo": "No salgas de casa.... te lo recomiendo",
    }
    thread = api.Server(HOST, PORT, DATABASE)
    thread.start()

    yolanda = Yolanda(HOST, PORT)
    print(yolanda.saludar())
    print(yolanda.dar_horoscopo_aleatorio())
    print(yolanda.verificar_horoscopo("acuario"))
    print(yolanda.verificar_horoscopo("pokemon"))
    print(yolanda.dar_horoscopo("acuario"))
    print(yolanda.dar_horoscopo("pokemon"))
    print(yolanda.agregar_horoscopo("a", "aaaaa", "pepaiic2233"))
    print(yolanda.dar_horoscopo("a"))
