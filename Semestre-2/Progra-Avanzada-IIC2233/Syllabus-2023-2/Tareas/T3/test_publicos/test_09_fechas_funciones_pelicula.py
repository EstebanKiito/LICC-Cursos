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
            Funciones(id=1043, numero_sala=1, id_pelicula=98064084, horario=4, fecha="20-01-23"),
            Funciones(id=1572, numero_sala=8, id_pelicula=28683172, horario=1, fecha="02-09-23"),
            Funciones(id=2010, numero_sala=2, id_pelicula=59873209, horario=2, fecha="24-07-23"),
            Funciones(id=3570, numero_sala=5, id_pelicula=69065378, horario=2, fecha="25-04-23"),
            Funciones(id=5063, numero_sala=3, id_pelicula=62342163, horario=2, fecha="04-03-23"),
            Funciones(id=2426, numero_sala=2, id_pelicula=56634603, horario=4, fecha="16-11-23"),
            Funciones(id=5610, numero_sala=5, id_pelicula=69065378, horario=1, fecha="01-02-23"),
            Funciones(id=3972, numero_sala=1, id_pelicula=39930643, horario=6, fecha="06-09-23"),
            Funciones(id=1553, numero_sala=2, id_pelicula=57302539, horario=1, fecha="17-06-23"),
            Funciones(id=6099, numero_sala=4, id_pelicula=69065378, horario=7, fecha="21-11-23"),
            Funciones(id=7012, numero_sala=6, id_pelicula=95168166, horario=2, fecha="11-05-23"),
            Funciones(id=7185, numero_sala=9, id_pelicula=31171792, horario=7, fecha="26-12-23"),
            Funciones(id=8296, numero_sala=3, id_pelicula=13383219, horario=9, fecha="13-09-23"),
            Funciones(id=4655, numero_sala=9, id_pelicula=17165770, horario=1, fecha="22-12-23"),
            Funciones(id=5367, numero_sala=3, id_pelicula=52069998, horario=8, fecha="06-09-23"),
            Funciones(id=3610, numero_sala=1, id_pelicula=69065378, horario=9, fecha="27-06-23"),
            Funciones(id=1554, numero_sala=3, id_pelicula=48466025, horario=8, fecha="28-11-23"),
            Funciones(id=9349, numero_sala=8, id_pelicula=61309831, horario=3, fecha="19-06-23"),
            Funciones(id=6899, numero_sala=5, id_pelicula=96590129, horario=6, fecha="17-10-23"),
            Funciones(id=1407, numero_sala=8, id_pelicula=30026979, horario=3, fecha="13-11-23"),
            Funciones(id=5241, numero_sala=6, id_pelicula=80427907, horario=1, fecha="02-10-23"),
            Funciones(id=8563, numero_sala=6, id_pelicula=69065378, horario=1, fecha="28-11-23"),
            Funciones(id=4999, numero_sala=5, id_pelicula=69065378, horario=2, fecha="26-05-23"),
            Funciones(id=9627, numero_sala=4, id_pelicula=12632673, horario=5, fecha="02-10-23"),
            Funciones(id=2172, numero_sala=7, id_pelicula=58528689, horario=7, fecha="13-11-23"),
            Funciones(id=3111, numero_sala=3, id_pelicula=94948733, horario=1, fecha="18-05-23"),
            Funciones(id=4581, numero_sala=1, id_pelicula=69065378, horario=4, fecha="20-01-23"),
            Funciones(id=3632, numero_sala=8, id_pelicula=69065378, horario=8, fecha="24-06-23"),
        ]

        lista_esperada = ['25-04-23', '01-02-23', '21-11-23', '27-06-23', '28-11-23', '26-05-23', '20-01-23', '24-06-23']

        resultado = fechas_funciones_pelicula(iter(lista_peliculas), iter(lista_funciones), "Black Panther")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        self.assertEqual(len(lista_resultado), len(lista_esperada))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)


    def test_1(self):
        """
        Fechas repetidas
        """
        lista_peliculas = [
            Peliculas(id=64787434, titulo="Casino", genero="Western", rating=8.5),
            Peliculas(id=63162203, titulo="The Departed", genero="Animación", rating=8.2),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
            Peliculas(id=85068287, titulo="Wendy Wu: Homecoming Warrior", genero="Acción", rating=6.2),
            Peliculas(id=23678361, titulo="Scarface", genero="Crimen", rating=8.8),
        ]
        lista_funciones = [
            Funciones(id=2103, numero_sala=9, id_pelicula=19776889, horario=3, fecha="12-01-23"),
            Funciones(id=9520, numero_sala=1, id_pelicula=23336383, horario=8, fecha="20-06-23"),
            Funciones(id=9043, numero_sala=5, id_pelicula=74227690, horario=1, fecha="15-02-23"),
            Funciones(id=4802, numero_sala=2, id_pelicula=34305543, horario=6, fecha="10-01-23"),
            Funciones(id=2631, numero_sala=8, id_pelicula=81292116, horario=6, fecha="03-10-23"),
            Funciones(id=3609, numero_sala=9, id_pelicula=30362798, horario=4, fecha="07-03-23"),
            Funciones(id=2853, numero_sala=2, id_pelicula=85068287, horario=8, fecha="21-02-23"),
            Funciones(id=9025, numero_sala=6, id_pelicula=47639875, horario=1, fecha="06-09-23"),
            Funciones(id=2619, numero_sala=2, id_pelicula=88846705, horario=1, fecha="02-02-23"),
            Funciones(id=5322, numero_sala=2, id_pelicula=85068287, horario=3, fecha="21-02-23"),
            Funciones(id=2130, numero_sala=9, id_pelicula=60661930, horario=5, fecha="08-04-23"),
            Funciones(id=4624, numero_sala=9, id_pelicula=50249494, horario=6, fecha="24-12-23"),
            Funciones(id=4095, numero_sala=8, id_pelicula=85068287, horario=7, fecha="21-02-23"),
            Funciones(id=5159, numero_sala=5, id_pelicula=30636399, horario=3, fecha="01-08-23"),
            Funciones(id=1316, numero_sala=5, id_pelicula=85068287, horario=5, fecha="21-02-23"),
            Funciones(id=8939, numero_sala=6, id_pelicula=88308012, horario=1, fecha="09-06-23"),
            Funciones(id=8135, numero_sala=3, id_pelicula=54996221, horario=8, fecha="09-02-23"),
            Funciones(id=9722, numero_sala=1, id_pelicula=27466919, horario=5, fecha="18-12-23"),
            Funciones(id=2996, numero_sala=5, id_pelicula=85068287, horario=5, fecha="17-02-23"),
            Funciones(id=9059, numero_sala=2, id_pelicula=74680442, horario=3, fecha="17-01-23"),
            Funciones(id=7956, numero_sala=9, id_pelicula=85068287, horario=7, fecha="13-07-23"),
            Funciones(id=2538, numero_sala=4, id_pelicula=71010104, horario=2, fecha="08-08-23"),
            Funciones(id=9538, numero_sala=4, id_pelicula=90032087, horario=9, fecha="27-01-23"),
            Funciones(id=9202, numero_sala=3, id_pelicula=48553580, horario=7, fecha="08-07-23"),
            Funciones(id=9068, numero_sala=4, id_pelicula=50431973, horario=5, fecha="19-10-23"),
            Funciones(id=9581, numero_sala=2, id_pelicula=23602311, horario=9, fecha="01-05-23"),
            Funciones(id=5855, numero_sala=2, id_pelicula=80301822, horario=8, fecha="09-01-23"),
            Funciones(id=6204, numero_sala=4, id_pelicula=88209468, horario=9, fecha="26-04-23"),
            Funciones(id=9659, numero_sala=8, id_pelicula=71708905, horario=5, fecha="02-07-23"),
            Funciones(id=7395, numero_sala=5, id_pelicula=34851230, horario=9, fecha="13-12-23"),
        ]

        lista_esperada = ['21-02-23', '21-02-23', '21-02-23', '21-02-23', '17-02-23', '13-07-23']

        resultado = fechas_funciones_pelicula(iter(lista_peliculas), iter(lista_funciones), "Wendy Wu: Homecoming Warrior")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        self.assertEqual(len(lista_resultado), len(lista_esperada))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)


    def test_2(self):
        """
        Sin fechas
        """
        lista_peliculas = [
            Peliculas(id=35100234, titulo="Terminator 2: Judgment Day", genero="Animación", rating=8.5),
            Peliculas(id=32608840, titulo="Johnny Tsunami", genero="Deportes", rating=6.3),
            Peliculas(id=85068287, titulo="Wendy Wu: Homecoming Warrior", genero="Acción", rating=6.2),
            Peliculas(id=40873645, titulo="The Terminator", genero="Ciencia Ficción", rating=8.5),
            Peliculas(id=78376301, titulo="Smart House", genero="Ciencia Ficción", rating=6.2),
        ]
        lista_funciones = [
            Funciones(id=2346, numero_sala=8, id_pelicula=88027031, horario=2, fecha="25-10-23"),
            Funciones(id=3123, numero_sala=7, id_pelicula=86774390, horario=2, fecha="05-06-23"),
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

        resultado = fechas_funciones_pelicula(iter(lista_peliculas), iter(lista_funciones), "Terminator 2: Judgment Day")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        self.assertEqual(len(lista_resultado), len(lista_esperada))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)


    def test_3(self):
        """
        Peli no existe
        """
        lista_peliculas = [
            Peliculas(id=38937194, titulo="Tangled", genero="Animación", rating=8.0),
            Peliculas(id=76172796, titulo="Inception", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=63162203, titulo="The Departed", genero="Animación", rating=8.2),
            Peliculas(id=96374386, titulo="The Lord of the Rings: The Two Towers", genero="Animación", rating=8.7),
            Peliculas(id=33612645, titulo="Goodfellas", genero="Animación", rating=8.9),
        ]
        lista_funciones = [
            Funciones(id=9393, numero_sala=5, id_pelicula=62184306, horario=5, fecha="22-12-23"),
            Funciones(id=1090, numero_sala=2, id_pelicula=11475813, horario=9, fecha="21-08-23"),
            Funciones(id=6467, numero_sala=5, id_pelicula=70204243, horario=3, fecha="03-11-23"),
            Funciones(id=4090, numero_sala=7, id_pelicula=32565409, horario=5, fecha="13-07-23"),
            Funciones(id=3084, numero_sala=9, id_pelicula=19047123, horario=4, fecha="13-09-23"),
            Funciones(id=3211, numero_sala=5, id_pelicula=13238118, horario=1, fecha="24-02-23"),
            Funciones(id=2088, numero_sala=5, id_pelicula=96095321, horario=8, fecha="23-12-23"),
            Funciones(id=1273, numero_sala=8, id_pelicula=33612645, horario=1, fecha="11-06-23"),
            Funciones(id=2629, numero_sala=3, id_pelicula=44190826, horario=9, fecha="14-07-23"),
            Funciones(id=9433, numero_sala=3, id_pelicula=14484341, horario=4, fecha="26-08-23"),
            Funciones(id=6060, numero_sala=7, id_pelicula=33612645, horario=8, fecha="27-02-23"),
            Funciones(id=2514, numero_sala=1, id_pelicula=63891330, horario=8, fecha="12-08-23"),
            Funciones(id=9395, numero_sala=5, id_pelicula=81100522, horario=2, fecha="10-01-23"),
            Funciones(id=3747, numero_sala=9, id_pelicula=80930857, horario=5, fecha="03-01-23"),
            Funciones(id=1631, numero_sala=2, id_pelicula=33612645, horario=1, fecha="11-08-23"),
            Funciones(id=7459, numero_sala=4, id_pelicula=89085283, horario=2, fecha="13-12-23"),
            Funciones(id=8644, numero_sala=5, id_pelicula=80427597, horario=9, fecha="26-05-23"),
            Funciones(id=8889, numero_sala=2, id_pelicula=33612645, horario=4, fecha="23-02-23"),
            Funciones(id=2404, numero_sala=1, id_pelicula=22955276, horario=4, fecha="26-08-23"),
            Funciones(id=2477, numero_sala=7, id_pelicula=72968975, horario=1, fecha="08-05-23"),
            Funciones(id=7519, numero_sala=1, id_pelicula=32724095, horario=1, fecha="22-12-23"),
            Funciones(id=8156, numero_sala=9, id_pelicula=98511213, horario=2, fecha="04-09-23"),
            Funciones(id=6473, numero_sala=6, id_pelicula=59968539, horario=5, fecha="27-12-23"),
            Funciones(id=7771, numero_sala=8, id_pelicula=15636790, horario=7, fecha="04-07-23"),
            Funciones(id=2787, numero_sala=5, id_pelicula=70447498, horario=4, fecha="11-04-23"),
            Funciones(id=1291, numero_sala=8, id_pelicula=17813511, horario=8, fecha="14-11-23"),
            Funciones(id=7723, numero_sala=3, id_pelicula=33612645, horario=4, fecha="17-04-23"),
            Funciones(id=2123, numero_sala=7, id_pelicula=33612645, horario=4, fecha="19-04-23"),
            Funciones(id=7410, numero_sala=9, id_pelicula=33612645, horario=5, fecha="01-05-23"),
            Funciones(id=3767, numero_sala=3, id_pelicula=33612645, horario=7, fecha="19-07-23"),
        ]

        lista_esperada = []

        resultado = fechas_funciones_pelicula(iter(lista_peliculas), iter(lista_funciones), "Goodfellas 2")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        self.assertEqual(len(lista_resultado), len(lista_esperada))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)


    def test_4(self):
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
            Funciones(id=4262, numero_sala=5, id_pelicula=34321575, horario=7, fecha="20-01-23"),
            Funciones(id=5528, numero_sala=6, id_pelicula=34321575, horario=6, fecha="20-01-23"),
            Funciones(id=8226, numero_sala=6, id_pelicula=34321575, horario=6, fecha="20-01-23"),
            Funciones(id=4738, numero_sala=2, id_pelicula=34321575, horario=8, fecha="20-01-23"),
            Funciones(id=5871, numero_sala=5, id_pelicula=34321575, horario=1, fecha="20-01-23"),
            Funciones(id=2443, numero_sala=9, id_pelicula=34321575, horario=2, fecha="20-01-23"),
            Funciones(id=1946, numero_sala=9, id_pelicula=34321575, horario=6, fecha="20-01-23"),
            Funciones(id=2117, numero_sala=9, id_pelicula=34321575, horario=5, fecha="20-01-23"),
            Funciones(id=9823, numero_sala=3, id_pelicula=49466538, horario=4, fecha="24-02-23"),
            Funciones(id=3704, numero_sala=5, id_pelicula=72119926, horario=4, fecha="16-01-23"),
            Funciones(id=8746, numero_sala=3, id_pelicula=71886005, horario=9, fecha="15-02-23"),
            Funciones(id=2559, numero_sala=8, id_pelicula=66482652, horario=5, fecha="26-04-23"),
            Funciones(id=3021, numero_sala=7, id_pelicula=73353128, horario=5, fecha="23-06-23"),
            Funciones(id=9374, numero_sala=9, id_pelicula=23857790, horario=5, fecha="22-12-23"),
            Funciones(id=4523, numero_sala=2, id_pelicula=19920072, horario=3, fecha="06-12-23"),
            Funciones(id=8838, numero_sala=2, id_pelicula=68277932, horario=5, fecha="27-03-23"),
            Funciones(id=8960, numero_sala=2, id_pelicula=56268681, horario=9, fecha="27-08-23"),
            Funciones(id=6310, numero_sala=1, id_pelicula=29536346, horario=1, fecha="18-09-23"),
            Funciones(id=7527, numero_sala=9, id_pelicula=28423220, horario=5, fecha="07-10-23"),
            Funciones(id=8792, numero_sala=4, id_pelicula=77299807, horario=9, fecha="07-03-23"),
            Funciones(id=5472, numero_sala=2, id_pelicula=39172110, horario=2, fecha="07-11-23"),
            Funciones(id=2050, numero_sala=9, id_pelicula=13314362, horario=8, fecha="05-05-23"),
            Funciones(id=9613, numero_sala=7, id_pelicula=84693516, horario=9, fecha="25-09-23"),
            Funciones(id=5424, numero_sala=2, id_pelicula=62786539, horario=7, fecha="08-01-23"),
            Funciones(id=7258, numero_sala=1, id_pelicula=69182988, horario=2, fecha="08-12-23"),
            Funciones(id=2411, numero_sala=8, id_pelicula=82666468, horario=4, fecha="20-04-23"),
            Funciones(id=4692, numero_sala=9, id_pelicula=36796729, horario=4, fecha="09-02-23"),
            Funciones(id=2106, numero_sala=2, id_pelicula=27748061, horario=6, fecha="24-12-23"),
            Funciones(id=3099, numero_sala=1, id_pelicula=99558152, horario=6, fecha="24-01-23"),
        ]

        lista_esperada = ['20-01-23', '20-01-23', '20-01-23', '20-01-23', '20-01-23', '20-01-23', '20-01-23', '20-01-23']

        resultado = fechas_funciones_pelicula(iter(lista_peliculas), iter(lista_funciones), "Ant-Man and The Wasp")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        lista_resultado = list(resultado)
        self.assertEqual(len(lista_resultado), len(lista_esperada))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)

if __name__ == '__main__':
    unittest.main(verbosity=2)