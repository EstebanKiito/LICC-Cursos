from abc import ABC, abstractmethod
from os import path


def leer(nombre_archivo):
    with open(nombre_archivo) as archivo:
        # La primera línea son los nombres de los argumentos
        argumentos = archivo.readline().strip().split(";")
        n_argumentos = len(argumentos)
        # Ahora para cada línea queremos crear un diccionario donde la llave es el nombre del
        # argumento y el valor es que indica el archivo. Podemos retornar un generador (usando
        # yield para cada diccionario) o retornar una lista con todos los diccionarios.


class PrograAvanzada:

    def __init__(self, semestre):
        self.semestre = semestre
        self.ayudantes = []
        self.clases_ayudantes = {"electrica": AyudanteElectrica, "robotica": AyudanteRobotica,
                                 "ingemat": AyudanteIngemat, "dcc": AyudanteDcc}

    def añadir_ayudantes(self, nombre_archivo):
        # buscamos la clase según el nombre del archivo en clases_ayudantes
        clase = self.clases_ayudantes[path.split(nombre_archivo)[-1][:-4]]
        # luego usamos la función leer() para leer el archivo e instanciamos cada ayudante con
        # nuestra variable clase, recordando que el operador ** nos permite desempaquetar un
        # diccionario en argumentos por keyword.

    def saludo_ayudantes(self):
        for ayudante in self.ayudantes:
            ayudante.saludar()


class Ayudante(ABC):

    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = int(creditos)

    @abstractmethod
    def saludar(self):
        pass


class AyudanteElectrica(Ayudante):

    def __init__(self, ramos_electrica, profe_favorito, **kwargs):
        super().__init__(**kwargs)
        self.ramos_electrica = ramos_electrica.split("|")
        self.profe_favorito = profe_favorito

    def saludar(self):
        print(f"Hola soy {self.nombre}! Estudio Ingeniería Eléctrica y mi profe",
              f"favorito es {self.profe_favorito}")


class AyudanteRobotica(Ayudante):

    def __init__(self, ramos_robotica, nombre_robot, **kwargs):
        super().__init__(**kwargs)
        self.ramos_robotica = ramos_robotica.split("|")
        self.nombre_robot = nombre_robot

    def saludar(self):
        print(f"Hola soy {self.nombre}! Estudio Ingeniería Robótica y",
              f"mi nombre robot es {self.nombre_robot}")


class AyudanteIngemat(Ayudante):

    def __init__(self, ramos_ingemat, formula_favorita, **kwargs):
        super().__init__(**kwargs)
        self.ramos_ingemat = ramos_ingemat.split("|")
        self.formula_favorita = formula_favorita

    def saludar(self):
        print(f"Hola soy {self.nombre}! Estudio Ingeniería Matemática y",
              f"mi fórmula favorita es {self.formula_favorita}")


class AyudanteDcc(Ayudante):

    def __init__(self, ramos_dcc, lenguaje, os, **kwargs):
        super().__init__(**kwargs)
        self.ramos_dcc = ramos_dcc.split("|")
        self.lenguaje = lenguaje
        self.os = os

    def saludar(self):
        print(f"Hola soy {self.nombre}! Estudio Ingeniería en Computación y",
              f"uso el lenguaje {self.lenguaje} en {self.os}")


avanzada = PrograAvanzada("2023-1")
avanzada.añadir_ayudantes(path.join("ayudantes", "dcc.csv"))
avanzada.añadir_ayudantes(path.join("ayudantes", "electrica.csv"))
avanzada.añadir_ayudantes(path.join("ayudantes", "ingemat.csv"))
avanzada.añadir_ayudantes(path.join("ayudantes", "robotica.csv"))
avanzada.saludo_ayudantes()
