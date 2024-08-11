import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import funciones_fecha
from utilidades import Funciones
from typing import Generator


class TestFuncionesFecha(unittest.TestCase):

    def test_0(self):
        """
        Varias funciones son de la fecha a buscar
        """
        lista_funciones = [
            Funciones(id=2221, numero_sala=4, id_pelicula=75901837, horario=1, fecha='04-12-23'),
            Funciones(id=4293, numero_sala=7, id_pelicula=32568878, horario=4, fecha='05-12-23'),
            Funciones(id=7777, numero_sala=6, id_pelicula=11615401, horario=5, fecha='05-12-23'),
            Funciones(id=1331, numero_sala=5, id_pelicula=75759551, horario=5, fecha='04-12-23'),
            Funciones(id=2247, numero_sala=2, id_pelicula=47191880, horario=4, fecha='05-12-23'),
            Funciones(id=3592, numero_sala=6, id_pelicula=11615401, horario=2, fecha='02-12-23'),
            Funciones(id=4211, numero_sala=1, id_pelicula=35569845, horario=3, fecha='03-12-23'),
            Funciones(id=1131, numero_sala=4, id_pelicula=57395306, horario=6, fecha='04-12-23'),
            Funciones(id=4561, numero_sala=2, id_pelicula=73020923, horario=5, fecha='01-12-23'),
            Funciones(id=6049, numero_sala=5, id_pelicula=62764502, horario=1, fecha='05-12-23'),
            Funciones(id=2534, numero_sala=3, id_pelicula=45064961, horario=6, fecha='03-12-23'),
            Funciones(id=8008, numero_sala=6, id_pelicula=40873645, horario=6, fecha='01-12-23'),
            Funciones(id=7666, numero_sala=8, id_pelicula=90803337, horario=1, fecha='03-12-23'),
            Funciones(id=9524, numero_sala=5, id_pelicula=75759551, horario=2, fecha='01-12-23'),
        ]
        expected_lista_funciones = [
            Funciones(id=4293, numero_sala=7, id_pelicula=32568878, horario=4, fecha='05-12-23'),
            Funciones(id=7777, numero_sala=6, id_pelicula=11615401, horario=5, fecha='05-12-23'),
            Funciones(id=2247, numero_sala=2, id_pelicula=47191880, horario=4, fecha='05-12-23'),
            Funciones(id=6049, numero_sala=5, id_pelicula=62764502, horario=1, fecha='05-12-23'),
        ]
        fecha_a_buscar = "05-12-2023"

        generador = (p for p in lista_funciones)
        resultado = funciones_fecha(generador, fecha_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_funciones)

    def test_1(self):
        """
        No hay funciones de la fecha a buscar
        """
        lista_funciones = [
            Funciones(id=3592, numero_sala=6, id_pelicula=11615401, horario=2, fecha='02-12-23'),
            Funciones(id=8512, numero_sala=3, id_pelicula=81187977, horario=1, fecha='03-12-23'),
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha='04-12-23'),
            Funciones(id=2660, numero_sala=5, id_pelicula=72588542, horario=6, fecha='05-12-23'),
            Funciones(id=4823, numero_sala=2, id_pelicula=34304754, horario=3, fecha='04-12-23'),
        ]
        expected_lista_funciones = []
        fecha_a_buscar = "06-12-2023"

        generador = (p for p in lista_funciones)
        resultado = funciones_fecha(generador, fecha_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_funciones)

    def test_2(self):
        """
        Todas las funciones son de la fecha a buscar
        """
        lista_funciones = [
            Funciones(id=1741, numero_sala=4, id_pelicula=57395306, horario=3, fecha='02-12-23'),
            Funciones(id=7617, numero_sala=8, id_pelicula=19177277, horario=2, fecha='02-12-23'),
            Funciones(id=4661, numero_sala=4, id_pelicula=28527704, horario=5, fecha='02-12-23'),
            Funciones(id=3566, numero_sala=4, id_pelicula=75901837, horario=4, fecha='02-12-23'),
            Funciones(id=4718, numero_sala=8, id_pelicula=32152163, horario=6, fecha='02-12-23'),
        ]
        expected_lista_funciones = [
            Funciones(id=1741, numero_sala=4, id_pelicula=57395306, horario=3, fecha='02-12-23'),
            Funciones(id=7617, numero_sala=8, id_pelicula=19177277, horario=2, fecha='02-12-23'),
            Funciones(id=4661, numero_sala=4, id_pelicula=28527704, horario=5, fecha='02-12-23'),
            Funciones(id=3566, numero_sala=4, id_pelicula=75901837, horario=4, fecha='02-12-23'),
            Funciones(id=4718, numero_sala=8, id_pelicula=32152163, horario=6, fecha='02-12-23'),
        ]
        fecha_a_buscar = '02-12-2023'

        generador = (p for p in lista_funciones)
        resultado = funciones_fecha(generador, fecha_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_funciones)

    def test_3(self):
        """
        Funciones de distinto año
        """
        lista_funciones = [
            Funciones(id=4718, numero_sala=8, id_pelicula=32152163, horario=6, fecha='05-08-94'),
            Funciones(id=4678, numero_sala=2, id_pelicula=34304754, horario=6, fecha='05-08-96'),
            Funciones(id=8008, numero_sala=6, id_pelicula=40873645, horario=6, fecha='05-08-22'),
            Funciones(id=4293, numero_sala=7, id_pelicula=32568878, horario=4, fecha='05-08-04'),
            Funciones(id=4638, numero_sala=8, id_pelicula=90803337, horario=4, fecha='01-08-22'),
            Funciones(id=7666, numero_sala=8, id_pelicula=90803337, horario=1, fecha='03-08-22'),
            Funciones(id=6566, numero_sala=1, id_pelicula=61384134, horario=4, fecha='05-01-22'),
            Funciones(id=4823, numero_sala=2, id_pelicula=34304754, horario=3, fecha='05-05-22'),
            Funciones(id=3224, numero_sala=8, id_pelicula=19177277, horario=5, fecha='05-08-13'),
            Funciones(id=2660, numero_sala=5, id_pelicula=72588542, horario=6, fecha='05-08-22'),
            Funciones(id=9584, numero_sala=3, id_pelicula=45064961, horario=3, fecha='05-08-22'),
            Funciones(id=4561, numero_sala=2, id_pelicula=73020923, horario=5, fecha='05-08-19'),
        ]
        expected_lista_funciones = [
            Funciones(id=8008, numero_sala=6, id_pelicula=40873645, horario=6, fecha='05-08-22'),
            Funciones(id=2660, numero_sala=5, id_pelicula=72588542, horario=6, fecha='05-08-22'),
            Funciones(id=9584, numero_sala=3, id_pelicula=45064961, horario=3, fecha='05-08-22'),
        ]
        fecha_a_buscar = '05-08-2022'

        generador = (p for p in lista_funciones)
        resultado = funciones_fecha(generador, fecha_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_funciones)

    def test_4(self):
        """
        Funciones siglo 20
        """
        lista_funciones = [
            Funciones(id=4252, numero_sala=1, id_pelicula=35569845, horario=6, fecha='18-12-99'),
            Funciones(id=9584, numero_sala=3, id_pelicula=45064961, horario=3, fecha='08-11-85'),
            Funciones(id=5517, numero_sala=3, id_pelicula=84580833, horario=5, fecha='06-09-77'),
            Funciones(id=7617, numero_sala=8, id_pelicula=19177277, horario=2, fecha='26-09-94'),
            Funciones(id=2660, numero_sala=7, id_pelicula=32568878, horario=4, fecha='06-09-94'),
            Funciones(id=9729, numero_sala=2, id_pelicula=47191880, horario=1, fecha='06-01-94'),
            Funciones(id=3592, numero_sala=6, id_pelicula=11615401, horario=2, fecha='16-04-96'),
            Funciones(id=4823, numero_sala=2, id_pelicula=34304754, horario=3, fecha='03-07-94'),
        ]
        expected_lista_funciones = [
            Funciones(id=2660, numero_sala=7, id_pelicula=32568878, horario=4, fecha='06-09-94'),
        ]
        fecha_a_buscar = '06-09-1994'

        generador = (p for p in lista_funciones)
        resultado = funciones_fecha(generador, fecha_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_funciones)


if __name__ == '__main__':
    unittest.main(verbosity=2)
