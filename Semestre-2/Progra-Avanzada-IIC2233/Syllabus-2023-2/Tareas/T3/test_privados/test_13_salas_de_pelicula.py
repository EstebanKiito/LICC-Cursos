import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import salas_de_pelicula
from utilidades import Peliculas, Funciones
from typing import Generator


class TestSalasDePelicula(unittest.TestCase):

    def test_0(self):
        """
        Test basico
        """
        lista_peliculas = [
            Peliculas(id=73079370, titulo="Thor: The Dark World", genero="Ciencia Ficción", rating=8.1),
            Peliculas(id=98811629, titulo="Braveheart", genero="Animación", rating=8.5),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
            Peliculas(id=84580833, titulo="Wreck-It Ralph", genero="Animación", rating=7.5),
            Peliculas(id=73020923, titulo="Blade Runne", genero="Animación", rating=7.2),
        ]
        lista_funciones = [
            Funciones(id=5408, numero_sala=2, id_pelicula=73020923, horario=2, fecha="03-12-23"),
            Funciones(id=4678, numero_sala=8, id_pelicula=73079370, horario=8, fecha="02-12-23"),
            Funciones(id=9795, numero_sala=8, id_pelicula=32152163, horario=3, fecha="05-12-23"),
            Funciones(id=2534, numero_sala=3, id_pelicula=45064961, horario=6, fecha="03-12-23"),
            Funciones(id=4582, numero_sala=6, id_pelicula=33896817, horario=4, fecha="04-12-23"),
            Funciones(id=3670, numero_sala=9, id_pelicula=73079370, horario=9, fecha="02-12-23"),
            Funciones(id=2247, numero_sala=2, id_pelicula=47191880, horario=4, fecha="05-12-23"),
            Funciones(id=8008, numero_sala=6, id_pelicula=40873645, horario=6, fecha="01-12-23"),
            Funciones(id=7666, numero_sala=8, id_pelicula=90803337, horario=1, fecha="03-12-23"),
            Funciones(id=4718, numero_sala=8, id_pelicula=32152163, horario=6, fecha="03-12-23"),
            Funciones(id=9721, numero_sala=5, id_pelicula=72588542, horario=3, fecha="02-12-23"),
            Funciones(id=7777, numero_sala=5, id_pelicula=73079370, horario=5, fecha="05-12-23"),
            Funciones(id=2660, numero_sala=5, id_pelicula=72588542, horario=6, fecha="05-12-23"),
            Funciones(id=1131, numero_sala=4, id_pelicula=57395306, horario=6, fecha="04-12-23"),
            Funciones(id=1741, numero_sala=4, id_pelicula=98811629, horario=3, fecha="01-12-23"),
            Funciones(id=5220, numero_sala=5, id_pelicula=98811629, horario=4, fecha="03-12-23"),
            Funciones(id=9524, numero_sala=5, id_pelicula=75759551, horario=2, fecha="01-12-23"),
            Funciones(id=5181, numero_sala=6, id_pelicula=40873645, horario=3, fecha="03-12-23"),
            Funciones(id=4736, numero_sala=4, id_pelicula=98811629, horario=2, fecha="05-12-23"),
            Funciones(id=6382, numero_sala=3, id_pelicula=84580833, horario=2, fecha="04-12-23"),
            Funciones(id=3592, numero_sala=6, id_pelicula=11615401, horario=2, fecha="02-12-23"),
            Funciones(id=4823, numero_sala=2, id_pelicula=34304754, horario=3, fecha="04-12-23"),
            Funciones(id=1331, numero_sala=5, id_pelicula=75759551, horario=5, fecha="04-12-23"),
            Funciones(id=4661, numero_sala=4, id_pelicula=73079370, horario=4, fecha="03-12-23"),
            Funciones(id=9584, numero_sala=3, id_pelicula=98811629, horario=3, fecha="05-12-23"),
        ]

        nombre_pelicula = "Thor: The Dark World"
        lista_esperada = [8, 9, 5, 4]

        resultado = salas_de_pelicula(lista_peliculas, lista_funciones, nombre_pelicula)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), lista_esperada)

    def test_1(self):
        """
        Nombre en 2 peliculas
        """
        lista_peliculas = [
            Peliculas(id=38463448, titulo="Spider-Man: Homecoming", genero="Superhéroes", rating=7.5),
            Peliculas(id=19745618, titulo="Cow Belles", genero="Acción", rating=9.0),
            Peliculas(id=95417284, titulo="Camp Rock", genero="Musical", rating=5.1),
            Peliculas(id=19745654, titulo="The Dark Knight: re", genero="Comedia", rating=6.1),
            Peliculas(id=19745617, titulo="The Dark Knight", genero="Comedia", rating=6.1),
            Peliculas(id=48119451, titulo="The Thirteenth Year", genero="Fantasía", rating=6.6),
        ]
        lista_funciones = [
            Funciones(id=3592, numero_sala=6, id_pelicula=11615401, horario=2, fecha="02-12-23"),
            Funciones(id=7666, numero_sala=8, id_pelicula=90803337, horario=1, fecha="03-12-23"),
            Funciones(id=9584, numero_sala=3, id_pelicula=45064961, horario=3, fecha="05-12-23"),
            Funciones(id=2826, numero_sala=1, id_pelicula=85032662, horario=2, fecha="02-12-23"),
            Funciones(id=1741, numero_sala=4, id_pelicula=57395306, horario=3, fecha="01-12-23"),
            Funciones(id=6382, numero_sala=3, id_pelicula=84580833, horario=2, fecha="04-12-23"),
            Funciones(id=5181, numero_sala=6, id_pelicula=19745617, horario=3, fecha="03-12-23"),
            Funciones(id=5220, numero_sala=5, id_pelicula=62764502, horario=4, fecha="03-12-23"),
            Funciones(id=7617, numero_sala=8, id_pelicula=19177277, horario=2, fecha="04-12-23"),
            Funciones(id=9729, numero_sala=2, id_pelicula=47191880, horario=1, fecha="02-12-23"),
            Funciones(id=4582, numero_sala=1, id_pelicula=19745617, horario=4, fecha="04-12-23"),
            Funciones(id=7777, numero_sala=6, id_pelicula=11615401, horario=5, fecha="05-12-23"),
            Funciones(id=8008, numero_sala=6, id_pelicula=40873645, horario=6, fecha="01-12-23"),
            Funciones(id=8512, numero_sala=3, id_pelicula=81187977, horario=1, fecha="03-12-23"),
            Funciones(id=6237, numero_sala=1, id_pelicula=61384134, horario=1, fecha="01-12-23"),
            Funciones(id=9400, numero_sala=7, id_pelicula=81744489, horario=2, fecha="03-12-23"),
            Funciones(id=2247, numero_sala=2, id_pelicula=19745617, horario=4, fecha="05-12-23"),
            Funciones(id=3224, numero_sala=8, id_pelicula=19177277, horario=5, fecha="02-12-23"),
            Funciones(id=2534, numero_sala=3, id_pelicula=45064961, horario=6, fecha="03-12-23"),
            Funciones(id=3566, numero_sala=4, id_pelicula=75901837, horario=4, fecha="02-12-23"),
            Funciones(id=1131, numero_sala=4, id_pelicula=19745617, horario=6, fecha="04-12-23"),
            Funciones(id=4678, numero_sala=2, id_pelicula=34304754, horario=6, fecha="02-12-23"),
            Funciones(id=7735, numero_sala=3, id_pelicula=19745617, horario=4, fecha="01-12-23"),
            Funciones(id=4638, numero_sala=8, id_pelicula=81744489, horario=4, fecha="01-12-23"),
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha="04-12-23"),
        ]

        nombre_pelicula = "The Dark Knight"
        lista_esperada = [6, 1, 2, 4, 3]

        resultado = salas_de_pelicula(lista_peliculas, lista_funciones, nombre_pelicula)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), lista_esperada)


if __name__ == '__main__':
    unittest.main(verbosity=2)
