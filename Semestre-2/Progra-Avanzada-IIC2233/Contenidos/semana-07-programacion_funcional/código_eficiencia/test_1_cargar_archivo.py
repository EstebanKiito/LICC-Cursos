from functools import reduce
import unittest
from typing import Generator

from utils import timeout, timer_decorator, memory_decorator, ruta_archivo, N


# --- Consultas a testear ---

def cargar_archivo_generador() -> Generator:
    with open(ruta_archivo, encoding='utf-8') as file:
        for line in file:
            yield line.strip().split(',')

def cargar_archivo_memoria() -> Generator:
    with open(ruta_archivo, encoding='utf-8') as file:
        for line in file.readlines():
            yield line.strip().split(',')


# --- Función general para obtener datos desde las funciones a testear ---

def procesar_resultados(generador: Generator) -> list:
    return reduce(lambda x, _: x + 1, generador, 0)


# --- Clase encargada de probar el código y hacer que tenga un tiempo máximo de ejecución ---

class TestCargarArchivo(unittest.TestCase):

    @timeout(60)
    @memory_decorator
    @timer_decorator
    def test_cargar_archivo_generador(self) -> None:
        len_data = procesar_resultados(cargar_archivo_generador())
        self.assertEqual(len_data, N)

    @timeout(60)
    @memory_decorator
    @timer_decorator
    def test_cargar_archivo_memoria(self) -> None:
        len_data = procesar_resultados(cargar_archivo_memoria())
        self.assertEqual(len_data, N)
