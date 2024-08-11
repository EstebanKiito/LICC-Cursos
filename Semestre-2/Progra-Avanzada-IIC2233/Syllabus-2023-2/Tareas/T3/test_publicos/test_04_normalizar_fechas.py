import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import normalizar_fechas
from utilidades import Funciones
from typing import Generator


class TestNormalizarFechas(unittest.TestCase):

    def test_0(self):
        """
        Todas las funciones del mismo año
        """
        lista_funciones = [
            Funciones(id=5181, numero_sala=6, id_pelicula=40873645, horario=3, fecha='03-12-23'),
            Funciones(id=7777, numero_sala=6, id_pelicula=11615401, horario=5, fecha='05-12-23'),
            Funciones(id=2247, numero_sala=2, id_pelicula=47191880, horario=4, fecha='05-12-23'),
            Funciones(id=4252, numero_sala=1, id_pelicula=35569845, horario=6, fecha='01-12-23'),
            Funciones(id=6566, numero_sala=1, id_pelicula=61384134, horario=4, fecha='04-12-23'),
            Funciones(id=5408, numero_sala=2, id_pelicula=73020923, horario=2, fecha='03-12-23'),
            Funciones(id=6049, numero_sala=5, id_pelicula=62764502, horario=1, fecha='05-12-23'),
            Funciones(id=4661, numero_sala=4, id_pelicula=28527704, horario=5, fecha='03-12-23'),
        ]
        expected_lista_funciones = [
            Funciones(id=5181, numero_sala=6, id_pelicula=40873645, horario=3, fecha='2023-12-03'),
            Funciones(id=7777, numero_sala=6, id_pelicula=11615401, horario=5, fecha='2023-12-05'),
            Funciones(id=2247, numero_sala=2, id_pelicula=47191880, horario=4, fecha='2023-12-05'),
            Funciones(id=4252, numero_sala=1, id_pelicula=35569845, horario=6, fecha='2023-12-01'),
            Funciones(id=6566, numero_sala=1, id_pelicula=61384134, horario=4, fecha='2023-12-04'),
            Funciones(id=5408, numero_sala=2, id_pelicula=73020923, horario=2, fecha='2023-12-03'),
            Funciones(id=6049, numero_sala=5, id_pelicula=62764502, horario=1, fecha='2023-12-05'),
            Funciones(id=4661, numero_sala=4, id_pelicula=28527704, horario=5, fecha='2023-12-03'),
        ]

        generador = (p for p in lista_funciones)
        resultado = normalizar_fechas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_funciones)

    def test_1(self):
        """
        Funciones de distintos años
        """
        lista_funciones = [
            Funciones(id=1131, numero_sala=4, id_pelicula=57395306, horario=6, fecha='30-12-23'),
            Funciones(id=6382, numero_sala=3, id_pelicula=84580833, horario=2, fecha='04-05-19'),
            Funciones(id=6049, numero_sala=5, id_pelicula=62764502, horario=1, fecha='05-07-15'),
            Funciones(id=4293, numero_sala=7, id_pelicula=32568878, horario=4, fecha='07-08-17'),
            Funciones(id=9584, numero_sala=3, id_pelicula=45064961, horario=3, fecha='08-01-09'),
        ]
        expected_lista_funciones = [
            Funciones(id=1131, numero_sala=4, id_pelicula=57395306, horario=6, fecha='2023-12-30'),
            Funciones(id=6382, numero_sala=3, id_pelicula=84580833, horario=2, fecha='2019-05-04'),
            Funciones(id=6049, numero_sala=5, id_pelicula=62764502, horario=1, fecha='2015-07-05'),
            Funciones(id=4293, numero_sala=7, id_pelicula=32568878, horario=4, fecha='2017-08-07'),
            Funciones(id=9584, numero_sala=3, id_pelicula=45064961, horario=3, fecha='2009-01-08'),
        ]

        generador = (p for p in lista_funciones)
        resultado = normalizar_fechas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_funciones)

    def test_2(self):
        """
        Funciones del siglo 20 y 21
        """
        lista_funciones = [
            Funciones(id=7617, numero_sala=8, id_pelicula=19177277, horario=2, fecha='11-12-20'),
            Funciones(id=9400, numero_sala=7, id_pelicula=41115118, horario=2, fecha='03-10-11'),
            Funciones(id=3670, numero_sala=7, id_pelicula=32568878, horario=1, fecha='10-02-09'),
            Funciones(id=1131, numero_sala=4, id_pelicula=57395306, horario=6, fecha='04-07-97'),
            Funciones(id=5517, numero_sala=7, id_pelicula=84580833, horario=3, fecha='13-07-24'),
        ]
        expected_lista_funciones = [
            Funciones(id=7617, numero_sala=8, id_pelicula=19177277, horario=2, fecha='2020-12-11'),
            Funciones(id=9400, numero_sala=7, id_pelicula=41115118, horario=2, fecha='2011-10-03'),
            Funciones(id=3670, numero_sala=7, id_pelicula=32568878, horario=1, fecha='2009-02-10'),
            Funciones(id=1131, numero_sala=4, id_pelicula=57395306, horario=6, fecha='1997-07-04'),
            Funciones(id=5517, numero_sala=7, id_pelicula=84580833, horario=3, fecha='1924-07-13'),
        ]

        generador = (p for p in lista_funciones)
        resultado = normalizar_fechas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_funciones)

    def test_3(self):
        """
        Funciones del siglo 20
        """
        lista_funciones = [
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha='30-12-87'),
            Funciones(id=9524, numero_sala=5, id_pelicula=75759551, horario=2, fecha='15-05-96'),
            Funciones(id=5517, numero_sala=3, id_pelicula=84580833, horario=5, fecha='01-09-79'),
        ]
        expected_lista_funciones = [
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha='1987-12-30'),
            Funciones(id=9524, numero_sala=5, id_pelicula=75759551, horario=2, fecha='1996-05-15'),
            Funciones(id=5517, numero_sala=3, id_pelicula=84580833, horario=5, fecha='1979-09-01'),
        ]

        generador = (p for p in lista_funciones)
        resultado = normalizar_fechas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_funciones)

    def test_4(self):
        """
        Funciones de la misma pelicula en el mismo horario y en la misma sala
        """
        lista_funciones = [
            Funciones(id=2548, numero_sala=7, id_pelicula=84580833, horario=3, fecha='11-07-21'),
            Funciones(id=9524, numero_sala=7, id_pelicula=84580833, horario=3, fecha='12-07-21'),
            Funciones(id=5517, numero_sala=7, id_pelicula=84580833, horario=3, fecha='13-07-21'),
        ]
        expected_lista_funciones = [
            Funciones(id=2548, numero_sala=7, id_pelicula=84580833, horario=3, fecha='2021-07-11'),
            Funciones(id=9524, numero_sala=7, id_pelicula=84580833, horario=3, fecha='2021-07-12'),
            Funciones(id=5517, numero_sala=7, id_pelicula=84580833, horario=3, fecha='2021-07-13'),
        ]

        generador = (p for p in lista_funciones)
        resultado = normalizar_fechas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_funciones)

if __name__ == '__main__':
    unittest.main(verbosity=2)