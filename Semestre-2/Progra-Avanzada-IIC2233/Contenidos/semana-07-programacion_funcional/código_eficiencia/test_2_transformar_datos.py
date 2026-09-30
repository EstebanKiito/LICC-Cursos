import unittest
from collections import namedtuple
from typing import Generator

from utils import timeout, timer_decorator, memory_decorator, ruta_archivo, N


# --- Elementos a testear ---

NamedTupleLengua = namedtuple('Lengua', 'id,speakers')


class ClaseLengua:
    def __init__(self, _id, speakers):
        self._id = _id
        self.speakers = speakers


def cargar_namedtuples() -> Generator:
    with open(ruta_archivo, encoding='utf-8') as file:
        file.readline()
        for line in file:
            info = (int(x) for x in line.strip().split(',')[::5])
            yield NamedTupleLengua(*info)

def cargar_clases() -> Generator:
    with open(ruta_archivo, encoding='utf-8') as file:
        file.readline()
        for line in file:
            info = (int(x) for x in line.strip().split(',')[::5])
            yield ClaseLengua(*info)


# --- Función general para obtener datos desde los elementos a testear ---

def obtener_resultados(generador) -> list:
    return [next(generador) for _ in range(N - 1)]


# --- Clase encargada de probar el código y hacer que tenga un tiempo máximo de ejecución ---

class TestNamedtuplesClases(unittest.TestCase):

    @timeout(60)
    @memory_decorator
    @timer_decorator
    def test_cargar_namedtuples(self) -> None:
        data = obtener_resultados(cargar_namedtuples())
        self.assertEqual(len(data), N - 1)

    @timeout(60)
    @memory_decorator
    @timer_decorator
    def test_cargar_clases(self) -> None:
        data = obtener_resultados(cargar_clases())
        self.assertEqual(len(data), N - 1)
