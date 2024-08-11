import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import fechas_funciones_pelicula
from utilidades import Peliculas, Funciones
from typing import Generator


class TestVacioFechasFuncionesPelicula(unittest.TestCase):

    def test_0(self):
        """
        Sin fechas
        """
        lista_peliculas = [
            Peliculas(id=35100234, titulo="Terminator 2: Judgment Day", genero="Animación", rating=8.5),
            Peliculas(id=78376301, titulo="Smart House", genero="Ciencia Ficción", rating=6.2),
            Peliculas(id=32608840, titulo="Johnny Tsunami", genero="Deportes", rating=6.3),
            Peliculas(id=85068287, titulo="Wendy Wu: Homecoming Warrior", genero="Acción", rating=6.2),
            Peliculas(id=40873645, titulo="The Terminator", genero="Ciencia Ficción", rating=8.5),
        ]
        lista_funciones = [
            Funciones(id=3123, numero_sala=7, id_pelicula=86774390, horario=2, fecha="05-06-23"),
            Funciones(id=2346, numero_sala=8, id_pelicula=88027031, horario=2, fecha="25-10-23"),
            Funciones(id=3235, numero_sala=5, id_pelicula=29083237, horario=1, fecha="26-06-23"),
            Funciones(id=9294, numero_sala=4, id_pelicula=61001468, horario=9, fecha="11-08-23"),
            Funciones(id=7479, numero_sala=1, id_pelicula=81701052, horario=7, fecha="06-01-23"),
            Funciones(id=3386, numero_sala=7, id_pelicula=63134024, horario=5, fecha="06-05-23"),
            Funciones(id=8479, numero_sala=2, id_pelicula=57491053, horario=4, fecha="20-08-23"),
            Funciones(id=7813, numero_sala=6, id_pelicula=62366916, horario=7, fecha="13-04-23"),
            Funciones(id=8429, numero_sala=9, id_pelicula=27498454, horario=6, fecha="06-06-23"),
            Funciones(id=8733, numero_sala=8, id_pelicula=59430757, horario=8, fecha="13-05-23"),
            Funciones(id=3086, numero_sala=4, id_pelicula=57981107, horario=6, fecha="06-03-23"),
            Funciones(id=4389, numero_sala=8, id_pelicula=67658942, horario=6, fecha="17-08-23"),
            Funciones(id=1231, numero_sala=2, id_pelicula=72264876, horario=9, fecha="23-11-23"),
            Funciones(id=2815, numero_sala=2, id_pelicula=65723576, horario=1, fecha="10-07-23"),
            Funciones(id=1598, numero_sala=4, id_pelicula=75833906, horario=1, fecha="13-03-23"),
            Funciones(id=7053, numero_sala=6, id_pelicula=46277397, horario=5, fecha="10-04-23"),
            Funciones(id=7658, numero_sala=8, id_pelicula=13798758, horario=2, fecha="09-04-23"),
            Funciones(id=8307, numero_sala=5, id_pelicula=30778620, horario=4, fecha="07-06-23"),
            Funciones(id=8015, numero_sala=4, id_pelicula=97655179, horario=4, fecha="07-11-23"),
            Funciones(id=9224, numero_sala=7, id_pelicula=99311227, horario=2, fecha="20-12-23"),
            Funciones(id=3051, numero_sala=2, id_pelicula=33650549, horario=4, fecha="12-10-23"),
            Funciones(id=4831, numero_sala=1, id_pelicula=16444895, horario=4, fecha="12-06-23"),
            Funciones(id=5157, numero_sala=2, id_pelicula=23958063, horario=6, fecha="20-10-23"),
            Funciones(id=1670, numero_sala=3, id_pelicula=53503185, horario=1, fecha="22-07-23"),
            Funciones(id=2852, numero_sala=7, id_pelicula=94189754, horario=8, fecha="12-03-23"),
            Funciones(id=2889, numero_sala=3, id_pelicula=64365740, horario=8, fecha="02-01-23"),
            Funciones(id=3784, numero_sala=2, id_pelicula=31674859, horario=1, fecha="16-07-23"),
            Funciones(id=4199, numero_sala=7, id_pelicula=93593850, horario=5, fecha="03-10-23"),
            Funciones(id=5595, numero_sala=8, id_pelicula=66552474, horario=4, fecha="05-12-23"),
            Funciones(id=2265, numero_sala=7, id_pelicula=92974203, horario=1, fecha="16-08-23"),
        ]

        lista_esperada = []

        resultado = fechas_funciones_pelicula(iter(lista_peliculas), iter(lista_funciones), "Smart House")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        self.assertEqual(len(lista_resultado), len(lista_esperada))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)

    def test_1(self):
        """
        Pelicula no existe
        """
        lista_peliculas = [
            Peliculas(id=63162203, titulo="The Departed", genero="Animación", rating=8.2),
            Peliculas(id=38937194, titulo="Tangled", genero="Animación", rating=8.0),
            Peliculas(id=33612645, titulo="Goodfellas", genero="Animación", rating=8.9),
            Peliculas(id=96374386, titulo="The Lord of the Rings: The Two Towers", genero="Animación", rating=8.7),
            Peliculas(id=76172796, titulo="Inception", genero="Ciencia Ficción", rating=8.8),
        ]
        lista_funciones = [
            Funciones(id=1631, numero_sala=2, id_pelicula=33612645, horario=1, fecha="11-08-23"),
            Funciones(id=7459, numero_sala=4, id_pelicula=89085283, horario=2, fecha="13-12-23"),
            Funciones(id=8644, numero_sala=5, id_pelicula=80427597, horario=9, fecha="26-05-23"),
            Funciones(id=8889, numero_sala=2, id_pelicula=33612645, horario=4, fecha="23-02-23"),
            Funciones(id=9393, numero_sala=5, id_pelicula=62184306, horario=5, fecha="22-12-23"),
            Funciones(id=2123, numero_sala=7, id_pelicula=33612645, horario=4, fecha="19-04-23"),
            Funciones(id=7410, numero_sala=9, id_pelicula=33612645, horario=5, fecha="01-05-23"),
            Funciones(id=3767, numero_sala=3, id_pelicula=33612645, horario=7, fecha="19-07-23"),
            Funciones(id=1090, numero_sala=2, id_pelicula=11475813, horario=9, fecha="21-08-23"),
            Funciones(id=6467, numero_sala=5, id_pelicula=70204243, horario=3, fecha="03-11-23"),
            Funciones(id=7771, numero_sala=8, id_pelicula=15636790, horario=7, fecha="04-07-23"),
            Funciones(id=2787, numero_sala=5, id_pelicula=70447498, horario=4, fecha="11-04-23"),
            Funciones(id=1291, numero_sala=8, id_pelicula=17813511, horario=8, fecha="14-11-23"),
            Funciones(id=3084, numero_sala=9, id_pelicula=19047123, horario=4, fecha="13-09-23"),
            Funciones(id=3211, numero_sala=5, id_pelicula=13238118, horario=1, fecha="24-02-23"),
            Funciones(id=2088, numero_sala=5, id_pelicula=96095321, horario=8, fecha="23-12-23"),
            Funciones(id=1273, numero_sala=8, id_pelicula=33612645, horario=1, fecha="11-06-23"),
            Funciones(id=2629, numero_sala=3, id_pelicula=44190826, horario=9, fecha="14-07-23"),
            Funciones(id=7723, numero_sala=3, id_pelicula=33612645, horario=4, fecha="17-04-23"),
            Funciones(id=9433, numero_sala=3, id_pelicula=14484341, horario=4, fecha="26-08-23"),
            Funciones(id=6060, numero_sala=7, id_pelicula=33612645, horario=8, fecha="27-02-23"),
            Funciones(id=2514, numero_sala=1, id_pelicula=63891330, horario=8, fecha="12-08-23"),
            Funciones(id=9395, numero_sala=5, id_pelicula=81100522, horario=2, fecha="10-01-23"),
            Funciones(id=3747, numero_sala=9, id_pelicula=80930857, horario=5, fecha="03-01-23"),
            Funciones(id=2404, numero_sala=1, id_pelicula=22955276, horario=4, fecha="26-08-23"),
            Funciones(id=2477, numero_sala=7, id_pelicula=72968975, horario=1, fecha="08-05-23"),
            Funciones(id=7519, numero_sala=1, id_pelicula=32724095, horario=1, fecha="22-12-23"),
            Funciones(id=8156, numero_sala=9, id_pelicula=98511213, horario=2, fecha="04-09-23"),
            Funciones(id=6473, numero_sala=6, id_pelicula=59968539, horario=5, fecha="27-12-23"),
            Funciones(id=4090, numero_sala=7, id_pelicula=32565409, horario=5, fecha="13-07-23"),
        ]

        lista_esperada = []

        resultado = fechas_funciones_pelicula(iter(lista_peliculas), iter(lista_funciones), "Tangled 2")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        self.assertEqual(len(lista_resultado), len(lista_esperada))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)


if __name__ == '__main__':
    unittest.main(verbosity=2)
