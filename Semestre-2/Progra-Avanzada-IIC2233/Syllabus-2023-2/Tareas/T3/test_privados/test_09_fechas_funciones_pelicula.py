import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import fechas_funciones_pelicula
from utilidades import Peliculas, Funciones
from typing import Generator


class TestFechasFuncionesPelicula(unittest.TestCase):

    def test_0(self):
        """
        Test basico
        """
        lista_peliculas = [
            Peliculas(id=30060914, titulo="Get a Clue", genero="Comedia", rating=6.2),
            Peliculas(id=69065378, titulo="Black Panther", genero="Superhéroes", rating=8.0),
            Peliculas(id=47191880, titulo="Thor", genero="Animación", rating=7.2),
            Peliculas(id=73465943, titulo="The Luck of the Irish", genero="Comedia", rating=6.4),
            Peliculas(id=58643843, titulo="Iron Man 2", genero="Animación", rating=7.0),
        ]
        lista_funciones = [
            Funciones(id=8663, numero_sala=2, id_pelicula=94923443, horario=3, fecha="16-03-23"),
            Funciones(id=6562, numero_sala=2, id_pelicula=76508890, horario=9, fecha="22-02-23"),
            Funciones(id=1043, numero_sala=1, id_pelicula=58643843, horario=4, fecha="20-01-23"),
            Funciones(id=1572, numero_sala=8, id_pelicula=28683172, horario=1, fecha="02-09-23"),
            Funciones(id=2010, numero_sala=2, id_pelicula=59873209, horario=2, fecha="24-07-23"),
            Funciones(id=3570, numero_sala=5, id_pelicula=58643843, horario=2, fecha="25-04-23"),
            Funciones(id=5063, numero_sala=3, id_pelicula=62342163, horario=2, fecha="04-03-23"),
            Funciones(id=2426, numero_sala=2, id_pelicula=58643843, horario=4, fecha="16-11-23"),
            Funciones(id=5610, numero_sala=5, id_pelicula=69065378, horario=1, fecha="01-02-23"),
            Funciones(id=3972, numero_sala=1, id_pelicula=39930643, horario=6, fecha="06-09-23"),
            Funciones(id=1553, numero_sala=2, id_pelicula=57302539, horario=1, fecha="17-06-23"),
            Funciones(id=6099, numero_sala=4, id_pelicula=58643843, horario=7, fecha="21-11-23"),
            Funciones(id=7012, numero_sala=6, id_pelicula=95168166, horario=2, fecha="11-05-23"),
            Funciones(id=7185, numero_sala=9, id_pelicula=31171792, horario=7, fecha="26-12-23"),
            Funciones(id=8296, numero_sala=3, id_pelicula=13383219, horario=9, fecha="13-09-23"),
            Funciones(id=4655, numero_sala=9, id_pelicula=17165770, horario=1, fecha="22-12-23"),
            Funciones(id=5367, numero_sala=3, id_pelicula=52069998, horario=8, fecha="06-09-23"),
            Funciones(id=3610, numero_sala=1, id_pelicula=58643843, horario=9, fecha="27-06-23"),
            Funciones(id=1554, numero_sala=3, id_pelicula=48466025, horario=8, fecha="28-11-23"),
            Funciones(id=9349, numero_sala=8, id_pelicula=61309831, horario=3, fecha="19-06-23"),
            Funciones(id=6899, numero_sala=5, id_pelicula=96590129, horario=6, fecha="17-10-23"),
            Funciones(id=1407, numero_sala=8, id_pelicula=30026979, horario=3, fecha="13-11-23"),
            Funciones(id=5241, numero_sala=6, id_pelicula=58643843, horario=1, fecha="02-10-23"),
            Funciones(id=8563, numero_sala=6, id_pelicula=69065378, horario=1, fecha="28-11-23"),
            Funciones(id=4999, numero_sala=5, id_pelicula=69065378, horario=2, fecha="26-05-23"),
            Funciones(id=9627, numero_sala=4, id_pelicula=12632673, horario=5, fecha="02-10-23"),
            Funciones(id=2172, numero_sala=7, id_pelicula=58643843, horario=7, fecha="13-11-23"),
            Funciones(id=3111, numero_sala=3, id_pelicula=58643843, horario=1, fecha="18-05-23"),
            Funciones(id=4581, numero_sala=1, id_pelicula=69065378, horario=4, fecha="20-01-23"),
            Funciones(id=3632, numero_sala=8, id_pelicula=69065378, horario=8, fecha="24-06-23"),
        ]

        lista_esperada = ['20-01-23', '25-04-23', '16-11-23', '21-11-23', '27-06-23', '02-10-23',
                          '13-11-23', '18-05-23']

        resultado = fechas_funciones_pelicula(iter(lista_peliculas), iter(lista_funciones), "Iron Man 2")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), lista_esperada)

    def test_1(self):
        """
        Fechas repetidas
        """
        lista_peliculas = [
            Peliculas(id=64787434, titulo="Casino", genero="Western", rating=8.5),
            Peliculas(id=23678361, titulo="Scarface", genero="Crimen", rating=8.8),
            Peliculas(id=63162203, titulo="The Departed", genero="Animación", rating=8.2),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
            Peliculas(id=85068287, titulo="Wendy Wu: Homecoming Warrior", genero="Acción", rating=6.2),
        ]
        lista_funciones = [
            Funciones(id=2103, numero_sala=9, id_pelicula=19776889, horario=3, fecha="12-01-23"),
            Funciones(id=9520, numero_sala=1, id_pelicula=23336383, horario=8, fecha="20-06-23"),
            Funciones(id=9043, numero_sala=5, id_pelicula=23678361, horario=1, fecha="15-02-23"),
            Funciones(id=4802, numero_sala=2, id_pelicula=23678361, horario=6, fecha="10-01-23"),
            Funciones(id=2631, numero_sala=8, id_pelicula=81292116, horario=6, fecha="10-01-23"),
            Funciones(id=3609, numero_sala=9, id_pelicula=23678361, horario=4, fecha="07-03-23"),
            Funciones(id=2853, numero_sala=2, id_pelicula=85068287, horario=8, fecha="21-02-23"),
            Funciones(id=9025, numero_sala=6, id_pelicula=47639875, horario=1, fecha="06-09-23"),
            Funciones(id=2619, numero_sala=2, id_pelicula=88846705, horario=1, fecha="02-02-23"),
            Funciones(id=5322, numero_sala=2, id_pelicula=23678361, horario=3, fecha="21-02-23"),
            Funciones(id=2130, numero_sala=9, id_pelicula=60661930, horario=5, fecha="08-04-23"),
            Funciones(id=4624, numero_sala=9, id_pelicula=50249494, horario=6, fecha="24-12-23"),
            Funciones(id=4095, numero_sala=8, id_pelicula=85068287, horario=7, fecha="21-02-23"),
            Funciones(id=5159, numero_sala=5, id_pelicula=23678361, horario=3, fecha="01-08-23"),
            Funciones(id=1316, numero_sala=5, id_pelicula=85068287, horario=5, fecha="21-02-23"),
            Funciones(id=8939, numero_sala=6, id_pelicula=88308012, horario=1, fecha="09-06-23"),
            Funciones(id=8135, numero_sala=3, id_pelicula=54996221, horario=8, fecha="09-02-23"),
            Funciones(id=9722, numero_sala=1, id_pelicula=27466919, horario=5, fecha="18-12-23"),
            Funciones(id=2996, numero_sala=5, id_pelicula=85068287, horario=5, fecha="17-02-23"),
            Funciones(id=9059, numero_sala=2, id_pelicula=23678361, horario=3, fecha="17-01-23"),
            Funciones(id=7956, numero_sala=9, id_pelicula=85068287, horario=7, fecha="13-07-23"),
            Funciones(id=2538, numero_sala=4, id_pelicula=71010104, horario=2, fecha="08-08-23"),
            Funciones(id=9538, numero_sala=4, id_pelicula=90032087, horario=9, fecha="27-01-23"),
            Funciones(id=9202, numero_sala=3, id_pelicula=48553580, horario=7, fecha="08-07-23"),
            Funciones(id=9068, numero_sala=4, id_pelicula=23678361, horario=5, fecha="19-10-23"),
            Funciones(id=9581, numero_sala=2, id_pelicula=23602311, horario=9, fecha="01-05-23"),
            Funciones(id=5855, numero_sala=2, id_pelicula=80301822, horario=8, fecha="09-01-23"),
            Funciones(id=6204, numero_sala=4, id_pelicula=23678361, horario=9, fecha="26-07-23"),
            Funciones(id=9659, numero_sala=8, id_pelicula=23678361, horario=5, fecha="26-07-23"),
            Funciones(id=7395, numero_sala=5, id_pelicula=34851230, horario=9, fecha="13-12-23"),
        ]

        lista_esperada = ['15-02-23', '10-01-23', '07-03-23', '21-02-23', '01-08-23', '17-01-23',
                          '19-10-23', '26-07-23', '26-07-23']

        resultado = fechas_funciones_pelicula(iter(lista_peliculas), iter(lista_funciones), "Scarface")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), lista_esperada)

    def test_2(self):
        """
        Solo una fecha con muchas funciones
        """
        lista_peliculas = [
            Peliculas(id=19745617, titulo="The Dark Knight", genero="Acción", rating=9.0),
            Peliculas(id=61384134, titulo="Mamma Mia", genero="Musical", rating=10.0),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=62863901, titulo="The Prestige", genero="Superhéroes", rating=8.6),
            Peliculas(id=34321575, titulo="Ant-Man and The Wasp", genero="Superhéroes", rating=7.1),
        ]
        lista_funciones = [
            Funciones(id=3755, numero_sala=3, id_pelicula=77368352, horario=8, fecha="01-03-23"),
            Funciones(id=4262, numero_sala=5, id_pelicula=34321575, horario=7, fecha="20-04-23"),
            Funciones(id=5528, numero_sala=6, id_pelicula=34321575, horario=6, fecha="20-01-23"),
            Funciones(id=8226, numero_sala=6, id_pelicula=34321575, horario=6, fecha="20-04-23"),
            Funciones(id=4738, numero_sala=2, id_pelicula=34321575, horario=8, fecha="20-01-23"),
            Funciones(id=5871, numero_sala=5, id_pelicula=34321575, horario=1, fecha="20-04-23"),
            Funciones(id=2443, numero_sala=9, id_pelicula=34321575, horario=2, fecha="20-01-23"),
            Funciones(id=1946, numero_sala=9, id_pelicula=34321575, horario=6, fecha="20-01-23"),
            Funciones(id=2117, numero_sala=9, id_pelicula=34321575, horario=5, fecha="20-01-23"),
            Funciones(id=9823, numero_sala=3, id_pelicula=49466538, horario=4, fecha="20-04-23"),
            Funciones(id=3704, numero_sala=5, id_pelicula=72119926, horario=4, fecha="20-04-23"),
            Funciones(id=8746, numero_sala=3, id_pelicula=71886005, horario=9, fecha="15-02-23"),
            Funciones(id=2559, numero_sala=8, id_pelicula=66482652, horario=5, fecha="26-04-23"),
            Funciones(id=3021, numero_sala=7, id_pelicula=73353128, horario=5, fecha="23-06-23"),
            Funciones(id=9374, numero_sala=9, id_pelicula=23857790, horario=5, fecha="20-04-23"),
            Funciones(id=4523, numero_sala=2, id_pelicula=19920072, horario=3, fecha="06-12-23"),
            Funciones(id=8838, numero_sala=2, id_pelicula=68277932, horario=5, fecha="20-04-23"),
            Funciones(id=8960, numero_sala=2, id_pelicula=56268681, horario=9, fecha="20-04-23"),
            Funciones(id=6310, numero_sala=1, id_pelicula=29536346, horario=1, fecha="18-09-23"),
            Funciones(id=7527, numero_sala=9, id_pelicula=28423220, horario=5, fecha="07-10-23"),
            Funciones(id=8792, numero_sala=4, id_pelicula=77299807, horario=9, fecha="07-03-23"),
            Funciones(id=5472, numero_sala=2, id_pelicula=39172110, horario=2, fecha="20-04-23"),
            Funciones(id=2050, numero_sala=9, id_pelicula=13314362, horario=8, fecha="05-05-23"),
            Funciones(id=9613, numero_sala=7, id_pelicula=84693516, horario=9, fecha="25-09-23"),
            Funciones(id=5424, numero_sala=2, id_pelicula=62786539, horario=7, fecha="20-04-23"),
            Funciones(id=7258, numero_sala=1, id_pelicula=69182988, horario=2, fecha="08-12-23"),
            Funciones(id=2411, numero_sala=8, id_pelicula=82666468, horario=4, fecha="20-04-23"),
            Funciones(id=4692, numero_sala=9, id_pelicula=36796729, horario=4, fecha="09-02-23"),
            Funciones(id=2106, numero_sala=2, id_pelicula=27748061, horario=6, fecha="20-04-23"),
            Funciones(id=3099, numero_sala=1, id_pelicula=99558152, horario=6, fecha="24-01-23"),
        ]

        lista_esperada = ['20-04-23', '20-01-23', '20-04-23', '20-01-23', '20-04-23', '20-01-23',
                          '20-01-23', '20-01-23']

        resultado = fechas_funciones_pelicula(iter(lista_peliculas), iter(lista_funciones), "Ant-Man and The Wasp")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), lista_esperada)


if __name__ == '__main__':
    unittest.main(verbosity=2)
