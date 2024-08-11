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
            Peliculas(id=91153956, titulo="Blade Runner", genero="Ciencia Ficción", rating=8.1),
            Peliculas(id=98811629, titulo="Braveheart", genero="Animación", rating=8.5),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
            Peliculas(id=84580833, titulo="Wreck-It Ralph", genero="Animación", rating=7.5),
            Peliculas(id=73079370, titulo="Thor: The Dark World", genero="Animación", rating=7.2),
        ]
        lista_funciones = [
            Funciones(id=5408, numero_sala=2, id_pelicula=73020923, horario=2, fecha="03-12-23"),
            Funciones(id=4678, numero_sala=2, id_pelicula=91153956, horario=6, fecha="02-12-23"),
            Funciones(id=9795, numero_sala=8, id_pelicula=32152163, horario=3, fecha="05-12-23"),
            Funciones(id=2534, numero_sala=3, id_pelicula=45064961, horario=6, fecha="03-12-23"),
            Funciones(id=4582, numero_sala=6, id_pelicula=33896817, horario=4, fecha="04-12-23"),
            Funciones(id=3670, numero_sala=7, id_pelicula=91153956, horario=1, fecha="02-12-23"),
            Funciones(id=2247, numero_sala=2, id_pelicula=47191880, horario=4, fecha="05-12-23"),
            Funciones(id=8008, numero_sala=6, id_pelicula=40873645, horario=6, fecha="01-12-23"),
            Funciones(id=7666, numero_sala=8, id_pelicula=90803337, horario=1, fecha="03-12-23"),
            Funciones(id=4718, numero_sala=8, id_pelicula=32152163, horario=6, fecha="03-12-23"),
            Funciones(id=9721, numero_sala=5, id_pelicula=72588542, horario=3, fecha="02-12-23"),
            Funciones(id=7777, numero_sala=6, id_pelicula=91153956, horario=5, fecha="05-12-23"),
            Funciones(id=2660, numero_sala=5, id_pelicula=72588542, horario=6, fecha="05-12-23"),
            Funciones(id=1131, numero_sala=4, id_pelicula=57395306, horario=6, fecha="04-12-23"),
            Funciones(id=1741, numero_sala=4, id_pelicula=57395306, horario=3, fecha="01-12-23"),
            Funciones(id=5220, numero_sala=5, id_pelicula=62764502, horario=4, fecha="03-12-23"),
            Funciones(id=9524, numero_sala=5, id_pelicula=75759551, horario=2, fecha="01-12-23"),
            Funciones(id=5181, numero_sala=6, id_pelicula=40873645, horario=3, fecha="03-12-23"),
            Funciones(id=4736, numero_sala=4, id_pelicula=28527704, horario=2, fecha="05-12-23"),
            Funciones(id=6382, numero_sala=3, id_pelicula=84580833, horario=2, fecha="04-12-23"),
            Funciones(id=3592, numero_sala=6, id_pelicula=11615401, horario=2, fecha="02-12-23"),
            Funciones(id=4823, numero_sala=2, id_pelicula=34304754, horario=3, fecha="04-12-23"),
            Funciones(id=1331, numero_sala=5, id_pelicula=75759551, horario=5, fecha="04-12-23"),
            Funciones(id=4661, numero_sala=4, id_pelicula=91153956, horario=4, fecha="03-12-23"),
            Funciones(id=9584, numero_sala=3, id_pelicula=45064961, horario=3, fecha="05-12-23"),
        ]

        nombre_pelicula = "Blade Runner"
        lista_esperada = [2, 7, 6, 4]

        resultado = salas_de_pelicula(lista_peliculas, lista_funciones, nombre_pelicula)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)

    def test_1(self):
        """
        Pelicula sin funciones
        """
        lista_peliculas = [
            Peliculas(id=76916171, titulo="Captain America: The Winter Soldier", genero="Animación", rating=7.8),
            Peliculas(id=16359236, titulo="Mulan", genero="Deportes", rating=7.8),
            Peliculas(id=92004621, titulo="Truan y Cattan", genero="Romance", rating=7.7),
            Peliculas(id=42038936, titulo="The Matrix Revolutions", genero="Fantasía", rating=7.3),
            Peliculas(id=25227924, titulo="Kill Bill: Vol. 2", genero="Western", rating=8.7),
        ]
        lista_funciones = [
            Funciones(id=6237, numero_sala=1, id_pelicula=61384134, horario=1, fecha="01-12-23"),
            Funciones(id=7735, numero_sala=3, id_pelicula=81187977, horario=4, fecha="01-12-23"),
            Funciones(id=5220, numero_sala=5, id_pelicula=62764502, horario=4, fecha="03-12-23"),
            Funciones(id=4718, numero_sala=8, id_pelicula=32152163, horario=6, fecha="03-12-23"),
            Funciones(id=3566, numero_sala=4, id_pelicula=75901837, horario=4, fecha="02-12-23"),
            Funciones(id=8008, numero_sala=6, id_pelicula=40873645, horario=6, fecha="01-12-23"),
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha="04-12-23"),
            Funciones(id=5517, numero_sala=3, id_pelicula=84580833, horario=5, fecha="02-12-23"),
            Funciones(id=2660, numero_sala=5, id_pelicula=72588542, horario=6, fecha="05-12-23"),
            Funciones(id=2534, numero_sala=3, id_pelicula=45064961, horario=6, fecha="03-12-23"),
            Funciones(id=6382, numero_sala=3, id_pelicula=84580833, horario=2, fecha="04-12-23"),
            Funciones(id=8512, numero_sala=3, id_pelicula=81187977, horario=1, fecha="03-12-23"),
            Funciones(id=7777, numero_sala=6, id_pelicula=11615401, horario=5, fecha="05-12-23"),
            Funciones(id=4661, numero_sala=4, id_pelicula=28527704, horario=5, fecha="03-12-23"),
            Funciones(id=9391, numero_sala=1, id_pelicula=85032662, horario=5, fecha="05-12-23"),
            Funciones(id=9584, numero_sala=3, id_pelicula=45064961, horario=3, fecha="05-12-23"),
            Funciones(id=5408, numero_sala=2, id_pelicula=73020923, horario=2, fecha="03-12-23"),
            Funciones(id=4736, numero_sala=4, id_pelicula=28527704, horario=2, fecha="05-12-23"),
            Funciones(id=4561, numero_sala=2, id_pelicula=73020923, horario=5, fecha="01-12-23"),
            Funciones(id=2221, numero_sala=4, id_pelicula=75901837, horario=1, fecha="04-12-23"),
            Funciones(id=9524, numero_sala=5, id_pelicula=75759551, horario=2, fecha="01-12-23"),
            Funciones(id=1910, numero_sala=6, id_pelicula=33896817, horario=1, fecha="01-12-23"),
            Funciones(id=4582, numero_sala=6, id_pelicula=33896817, horario=4, fecha="04-12-23"),
            Funciones(id=3592, numero_sala=6, id_pelicula=11615401, horario=2, fecha="02-12-23"),
            Funciones(id=2247, numero_sala=2, id_pelicula=47191880, horario=4, fecha="05-12-23"),
        ]

        nombre_pelicula = "Truan y Cattan"
        lista_esperada = []

        resultado = salas_de_pelicula(lista_peliculas, lista_funciones, nombre_pelicula)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        self.assertEqual(lista_resultado, lista_esperada)

    def test_2(self):
        """
        Pelicula con salas repetidos
        """
        lista_peliculas = [
            Peliculas(id=96374386, titulo="The Lord of the Rings: The Two Towers", genero="Animación", rating=8.7),
            Peliculas(id=61384134, titulo="Truan y Cattan: Segunda parte", genero="Tragedia", rating=10.0),
            Peliculas(id=79145064, titulo="Forrest Gump", genero="Ciencia", rating=8.8),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=73020923, titulo="Captain America: The First Avenger", genero="Animación", rating=7.0),
        ]
        lista_funciones = [
            Funciones(id=2221, numero_sala=4, id_pelicula=75901837, horario=1, fecha="04-12-23"),
            Funciones(id=4718, numero_sala=8, id_pelicula=61384134, horario=6, fecha="03-12-23"),
            Funciones(id=4638, numero_sala=8, id_pelicula=90803337, horario=4, fecha="01-12-23"),
            Funciones(id=9729, numero_sala=2, id_pelicula=47191880, horario=1, fecha="02-12-23"),
            Funciones(id=9400, numero_sala=7, id_pelicula=41115118, horario=2, fecha="03-12-23"),
            Funciones(id=3592, numero_sala=6, id_pelicula=61384134, horario=2, fecha="02-12-23"),
            Funciones(id=8386, numero_sala=7, id_pelicula=41115118, horario=5, fecha="01-12-23"),
            Funciones(id=3224, numero_sala=8, id_pelicula=19177277, horario=5, fecha="02-12-23"),
            Funciones(id=8512, numero_sala=3, id_pelicula=61384134, horario=1, fecha="03-12-23"),
            Funciones(id=4561, numero_sala=2, id_pelicula=73020923, horario=5, fecha="01-12-23"),
            Funciones(id=2826, numero_sala=1, id_pelicula=61384134, horario=2, fecha="02-12-23"),
            Funciones(id=9795, numero_sala=8, id_pelicula=32152163, horario=3, fecha="05-12-23"),
            Funciones(id=1741, numero_sala=4, id_pelicula=57395306, horario=3, fecha="01-12-23"),
            Funciones(id=6049, numero_sala=5, id_pelicula=62764502, horario=1, fecha="05-12-23"),
            Funciones(id=5181, numero_sala=6, id_pelicula=40873645, horario=3, fecha="03-12-23"),
            Funciones(id=9391, numero_sala=1, id_pelicula=85032662, horario=5, fecha="05-12-23"),
            Funciones(id=5220, numero_sala=5, id_pelicula=62764502, horario=4, fecha="03-12-23"),
            Funciones(id=6382, numero_sala=3, id_pelicula=61384134, horario=2, fecha="04-12-23"),
            Funciones(id=2247, numero_sala=2, id_pelicula=61384134, horario=4, fecha="05-12-23"),
            Funciones(id=4736, numero_sala=4, id_pelicula=61384134, horario=2, fecha="05-12-23"),
            Funciones(id=7777, numero_sala=6, id_pelicula=11615401, horario=5, fecha="05-12-23"),
            Funciones(id=7666, numero_sala=8, id_pelicula=90803337, horario=1, fecha="03-12-23"),
            Funciones(id=7015, numero_sala=7, id_pelicula=70752273, horario=6, fecha="02-12-23"),
            Funciones(id=1331, numero_sala=5, id_pelicula=75759551, horario=5, fecha="04-12-23"),
            Funciones(id=4293, numero_sala=7, id_pelicula=61384134, horario=4, fecha="05-12-23"),
        ]

        nombre_pelicula = "Truan y Cattan: Segunda parte"
        lista_esperada = [8, 6, 3, 1, 3, 2, 4, 7]

        resultado = salas_de_pelicula(lista_peliculas, lista_funciones, nombre_pelicula)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)

    def test_3(self):
        """
        Nombre en 2 peliculas
        """
        lista_peliculas = [
            Peliculas(id=38463448, titulo="Spider-Man: Homecoming", genero="Superhéroes", rating=7.5),
            Peliculas(id=19745617, titulo="The Dark Knight", genero="Acción", rating=9.0),
            Peliculas(id=95417284, titulo="Camp Rock", genero="Musical", rating=5.1),
            Peliculas(id=81744482, titulo="Cow Belles: re", genero="Comedia", rating=6.1),
            Peliculas(id=81744489, titulo="Cow Belles", genero="Comedia", rating=6.1),
            Peliculas(id=48119451, titulo="The Thirteenth Year", genero="Fantasía", rating=6.6),
        ]
        lista_funciones = [
            Funciones(id=3592, numero_sala=6, id_pelicula=11615401, horario=2, fecha="02-12-23"),
            Funciones(id=7666, numero_sala=8, id_pelicula=90803337, horario=1, fecha="03-12-23"),
            Funciones(id=9584, numero_sala=3, id_pelicula=45064961, horario=3, fecha="05-12-23"),
            Funciones(id=2826, numero_sala=1, id_pelicula=85032662, horario=2, fecha="02-12-23"),
            Funciones(id=1741, numero_sala=4, id_pelicula=57395306, horario=3, fecha="01-12-23"),
            Funciones(id=6382, numero_sala=3, id_pelicula=84580833, horario=2, fecha="04-12-23"),
            Funciones(id=5181, numero_sala=6, id_pelicula=81744489, horario=3, fecha="03-12-23"),
            Funciones(id=5220, numero_sala=5, id_pelicula=62764502, horario=4, fecha="03-12-23"),
            Funciones(id=7617, numero_sala=8, id_pelicula=19177277, horario=2, fecha="04-12-23"),
            Funciones(id=9729, numero_sala=2, id_pelicula=47191880, horario=1, fecha="02-12-23"),
            Funciones(id=4582, numero_sala=6, id_pelicula=33896817, horario=4, fecha="04-12-23"),
            Funciones(id=7777, numero_sala=6, id_pelicula=11615401, horario=5, fecha="05-12-23"),
            Funciones(id=8008, numero_sala=6, id_pelicula=40873645, horario=6, fecha="01-12-23"),
            Funciones(id=8512, numero_sala=3, id_pelicula=81187977, horario=1, fecha="03-12-23"),
            Funciones(id=6237, numero_sala=1, id_pelicula=61384134, horario=1, fecha="01-12-23"),
            Funciones(id=9400, numero_sala=7, id_pelicula=81744489, horario=2, fecha="03-12-23"),
            Funciones(id=2247, numero_sala=2, id_pelicula=47191880, horario=4, fecha="05-12-23"),
            Funciones(id=3224, numero_sala=8, id_pelicula=19177277, horario=5, fecha="02-12-23"),
            Funciones(id=2534, numero_sala=3, id_pelicula=45064961, horario=6, fecha="03-12-23"),
            Funciones(id=3566, numero_sala=4, id_pelicula=75901837, horario=4, fecha="02-12-23"),
            Funciones(id=1131, numero_sala=4, id_pelicula=57395306, horario=6, fecha="04-12-23"),
            Funciones(id=4678, numero_sala=2, id_pelicula=34304754, horario=6, fecha="02-12-23"),
            Funciones(id=7735, numero_sala=3, id_pelicula=81187977, horario=4, fecha="01-12-23"),
            Funciones(id=4638, numero_sala=8, id_pelicula=81744489, horario=4, fecha="01-12-23"),
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha="04-12-23"),
        ]

        nombre_pelicula = "Cow Belles"
        lista_esperada = [6, 7, 8]

        resultado = salas_de_pelicula(lista_peliculas, lista_funciones, nombre_pelicula)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)

    def test_4(self):
        """
        Pelicula no existe
        """
        lista_peliculas = [
            Peliculas(id=75660450, titulo="The Incredible Hulk", genero="Animación", rating=6.7),
            Peliculas(id=41115118, titulo="Avatar", genero="Crimen", rating=7.8),
            Peliculas(id=76004798, titulo="Incredibles", genero="Animación", rating=8.0),
            Peliculas(id=20610700, titulo="The Princess and the Frog", genero="Animación", rating=7.1),
            Peliculas(id=59848286, titulo="The Silence of the Lambs", genero="Suspense", rating=8.6),
        ]
        lista_funciones = [
            Funciones(id=4293, numero_sala=7, id_pelicula=41115118, horario=4, fecha="05-12-23"),
            Funciones(id=3670, numero_sala=7, id_pelicula=41115118, horario=1, fecha="02-12-23"),
            Funciones(id=4823, numero_sala=2, id_pelicula=41115118, horario=3, fecha="04-12-23"),
            Funciones(id=3592, numero_sala=6, id_pelicula=41115118, horario=2, fecha="02-12-23"),
            Funciones(id=3224, numero_sala=8, id_pelicula=41115118, horario=5, fecha="02-12-23"),
            Funciones(id=1741, numero_sala=4, id_pelicula=41115118, horario=3, fecha="01-12-23"),
            Funciones(id=1910, numero_sala=6, id_pelicula=41115118, horario=1, fecha="01-12-23"),
            Funciones(id=5408, numero_sala=2, id_pelicula=41115118, horario=2, fecha="03-12-23"),
            Funciones(id=3566, numero_sala=4, id_pelicula=41115118, horario=4, fecha="02-12-23"),
            Funciones(id=9729, numero_sala=2, id_pelicula=41115118, horario=1, fecha="02-12-23"),
            Funciones(id=6237, numero_sala=1, id_pelicula=41115118, horario=1, fecha="01-12-23"),
            Funciones(id=1331, numero_sala=5, id_pelicula=41115118, horario=5, fecha="04-12-23"),
            Funciones(id=2660, numero_sala=5, id_pelicula=41115118, horario=6, fecha="05-12-23"),
            Funciones(id=4736, numero_sala=4, id_pelicula=28527704, horario=2, fecha="05-12-23"),
            Funciones(id=4252, numero_sala=1, id_pelicula=35569845, horario=6, fecha="01-12-23"),
            Funciones(id=7015, numero_sala=7, id_pelicula=70752273, horario=6, fecha="02-12-23"),
            Funciones(id=5181, numero_sala=6, id_pelicula=40873645, horario=3, fecha="03-12-23"),
            Funciones(id=9721, numero_sala=5, id_pelicula=72588542, horario=3, fecha="02-12-23"),
            Funciones(id=4561, numero_sala=2, id_pelicula=73020923, horario=5, fecha="01-12-23"),
            Funciones(id=9584, numero_sala=3, id_pelicula=45064961, horario=3, fecha="05-12-23"),
            Funciones(id=7735, numero_sala=3, id_pelicula=81187977, horario=4, fecha="01-12-23"),
            Funciones(id=8512, numero_sala=3, id_pelicula=81187977, horario=1, fecha="03-12-23"),
            Funciones(id=6382, numero_sala=3, id_pelicula=84580833, horario=2, fecha="04-12-23"),
            Funciones(id=5517, numero_sala=3, id_pelicula=84580833, horario=5, fecha="02-12-23"),
            Funciones(id=2221, numero_sala=4, id_pelicula=75901837, horario=1, fecha="04-12-23"),
        ]

        nombre_pelicula = "Avatar 3"
        lista_esperada = []

        resultado = salas_de_pelicula(lista_peliculas, lista_funciones, nombre_pelicula)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)

    def test_5(self):
        """
        Pelicula sin funciones 2
        """
        lista_peliculas = [
            Peliculas(id=51151305, titulo="Pocahontas", genero="Fantasía", rating=7.8),
            Peliculas(id=73465943, titulo="The Luck of the Irish", genero="Comedia", rating=6.4),
            Peliculas(id=52568632, titulo="Shutter Island", genero="Superhéroes", rating=8.5),
            Peliculas(id=41115118, titulo="Truan y Cattan: Tercer intento", genero="Crimen/Fanstasía", rating=7.8),
            Peliculas(id=62863901, titulo="The Prestige", genero="Superhéroes", rating=8.6),
        ]
        lista_funciones = [
            Funciones(id=8386, numero_sala=7, id_pelicula=41116118, horario=5, fecha="01-12-23"),
            Funciones(id=4661, numero_sala=4, id_pelicula=28527704, horario=5, fecha="03-12-23"),
            Funciones(id=4293, numero_sala=7, id_pelicula=32568878, horario=4, fecha="05-12-23"),
            Funciones(id=9795, numero_sala=8, id_pelicula=32152163, horario=3, fecha="05-12-23"),
            Funciones(id=8512, numero_sala=3, id_pelicula=81187977, horario=1, fecha="03-12-23"),
            Funciones(id=3670, numero_sala=7, id_pelicula=32568878, horario=1, fecha="02-12-23"),
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha="04-12-23"),
            Funciones(id=9721, numero_sala=5, id_pelicula=72588542, horario=3, fecha="02-12-23"),
            Funciones(id=3566, numero_sala=4, id_pelicula=75901837, horario=4, fecha="02-12-23"),
            Funciones(id=1741, numero_sala=4, id_pelicula=57395306, horario=3, fecha="01-12-23"),
            Funciones(id=3224, numero_sala=8, id_pelicula=19177277, horario=5, fecha="02-12-23"),
            Funciones(id=6237, numero_sala=1, id_pelicula=61384134, horario=1, fecha="01-12-23"),
            Funciones(id=5517, numero_sala=3, id_pelicula=84580833, horario=5, fecha="02-12-23"),
            Funciones(id=4561, numero_sala=2, id_pelicula=73020923, horario=5, fecha="01-12-23"),
            Funciones(id=9391, numero_sala=1, id_pelicula=85032662, horario=5, fecha="05-12-23"),
            Funciones(id=4736, numero_sala=4, id_pelicula=28527704, horario=2, fecha="05-12-23"),
            Funciones(id=2534, numero_sala=3, id_pelicula=45064961, horario=6, fecha="03-12-23"),
            Funciones(id=2826, numero_sala=1, id_pelicula=85032662, horario=2, fecha="02-12-23"),
            Funciones(id=8008, numero_sala=6, id_pelicula=40873645, horario=6, fecha="01-12-23"),
            Funciones(id=7666, numero_sala=8, id_pelicula=90803337, horario=1, fecha="03-12-23"),
            Funciones(id=3592, numero_sala=6, id_pelicula=11615401, horario=2, fecha="02-12-23"),
            Funciones(id=7777, numero_sala=6, id_pelicula=11615401, horario=5, fecha="05-12-23"),
            Funciones(id=7617, numero_sala=8, id_pelicula=19177277, horario=2, fecha="04-12-23"),
            Funciones(id=6382, numero_sala=3, id_pelicula=84580833, horario=2, fecha="04-12-23"),
            Funciones(id=4718, numero_sala=8, id_pelicula=32152163, horario=6, fecha="03-12-23"),
        ]

        nombre_pelicula = "Truan y Cattan: Tercer intento"
        lista_esperada = []

        resultado = salas_de_pelicula(lista_peliculas, lista_funciones, nombre_pelicula)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        self.assertEqual(lista_resultado, lista_esperada)

if __name__ == '__main__':
    unittest.main(verbosity=2)