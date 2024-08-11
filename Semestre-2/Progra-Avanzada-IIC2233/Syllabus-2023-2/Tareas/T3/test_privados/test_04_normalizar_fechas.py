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
            Funciones(id=5220, numero_sala=5, id_pelicula=62764502, horario=4, fecha='03-11-22'),
            Funciones(id=4718, numero_sala=8, id_pelicula=32152163, horario=6, fecha='05-11-22'),
            Funciones(id=3670, numero_sala=7, id_pelicula=32568878, horario=1, fecha='05-11-22'),
            Funciones(id=8512, numero_sala=3, id_pelicula=81187977, horario=1, fecha='01-11-22'),
            Funciones(id=2660, numero_sala=5, id_pelicula=72588542, horario=6, fecha='04-11-22'),
            Funciones(id=4252, numero_sala=1, id_pelicula=35569845, horario=6, fecha='03-11-22'),
            Funciones(id=9721, numero_sala=5, id_pelicula=72588542, horario=3, fecha='05-11-22'),
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha='03-11-22'),
        ]
        expected_lista_funciones = [
            Funciones(id=5220, numero_sala=5, id_pelicula=62764502, horario=4, fecha='2022-11-03'),
            Funciones(id=4718, numero_sala=8, id_pelicula=32152163, horario=6, fecha='2022-11-05'),
            Funciones(id=3670, numero_sala=7, id_pelicula=32568878, horario=1, fecha='2022-11-05'),
            Funciones(id=8512, numero_sala=3, id_pelicula=81187977, horario=1, fecha='2022-11-01'),
            Funciones(id=2660, numero_sala=5, id_pelicula=72588542, horario=6, fecha='2022-11-04'),
            Funciones(id=4252, numero_sala=1, id_pelicula=35569845, horario=6, fecha='2022-11-03'),
            Funciones(id=9721, numero_sala=5, id_pelicula=72588542, horario=3, fecha='2022-11-05'),
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha='2022-11-03'),
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
            Funciones(id=9795, numero_sala=8, id_pelicula=32152163, horario=3, fecha='30-12-21'),
            Funciones(id=7735, numero_sala=3, id_pelicula=81187977, horario=4, fecha='04-05-18'),
            Funciones(id=4638, numero_sala=8, id_pelicula=90803337, horario=4, fecha='01-08-15'),
            Funciones(id=2826, numero_sala=1, id_pelicula=85032662, horario=2, fecha='07-08-17'),
            Funciones(id=4718, numero_sala=8, id_pelicula=32152163, horario=6, fecha='08-02-08'),
        ]
        expected_lista_funciones = [
            Funciones(id=9795, numero_sala=8, id_pelicula=32152163, horario=3, fecha='2021-12-30'),
            Funciones(id=7735, numero_sala=3, id_pelicula=81187977, horario=4, fecha='2018-05-04'),
            Funciones(id=4638, numero_sala=8, id_pelicula=90803337, horario=4, fecha='2015-08-01'),
            Funciones(id=2826, numero_sala=1, id_pelicula=85032662, horario=2, fecha='2017-08-07'),
            Funciones(id=4718, numero_sala=8, id_pelicula=32152163, horario=6, fecha='2008-02-08'),
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
            Funciones(id=4678, numero_sala=2, id_pelicula=34304754, horario=6, fecha='11-12-20'),
            Funciones(id=6382, numero_sala=3, id_pelicula=84580833, horario=2, fecha='03-10-11'),
            Funciones(id=9795, numero_sala=8, id_pelicula=32152163, horario=3, fecha='10-02-07'),
            Funciones(id=4661, numero_sala=4, id_pelicula=28527704, horario=5, fecha='04-07-98'),
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha='13-07-24'),
        ]
        expected_lista_funciones = [
            Funciones(id=4678, numero_sala=2, id_pelicula=34304754, horario=6, fecha='2020-12-11'),
            Funciones(id=6382, numero_sala=3, id_pelicula=84580833, horario=2, fecha='2011-10-03'),
            Funciones(id=9795, numero_sala=8, id_pelicula=32152163, horario=3, fecha='2007-02-10'),
            Funciones(id=4661, numero_sala=4, id_pelicula=28527704, horario=5, fecha='1998-07-04'),
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha='1924-07-13'),
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
            Funciones(id=9795, numero_sala=8, id_pelicula=32152163, horario=3, fecha='29-12-82'),
            Funciones(id=9400, numero_sala=7, id_pelicula=41115118, horario=2, fecha='15-05-95'),
            Funciones(id=2826, numero_sala=1, id_pelicula=85032662, horario=2, fecha='01-03-79'),
        ]
        expected_lista_funciones = [
            Funciones(id=9795, numero_sala=8, id_pelicula=32152163, horario=3, fecha='1982-12-29'),
            Funciones(id=9400, numero_sala=7, id_pelicula=41115118, horario=2, fecha='1995-05-15'),
            Funciones(id=2826, numero_sala=1, id_pelicula=85032662, horario=2, fecha='1979-03-01'),
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
            Funciones(id=5517, numero_sala=7, id_pelicula=84580833, horario=3, fecha='11-06-20'),
            Funciones(id=9588, numero_sala=7, id_pelicula=84580833, horario=3, fecha='12-06-20'),
            Funciones(id=4638, numero_sala=7, id_pelicula=84580833, horario=3, fecha='14-06-20'),
        ]
        expected_lista_funciones = [
            Funciones(id=5517, numero_sala=7, id_pelicula=84580833, horario=3, fecha='2020-06-11'),
            Funciones(id=9588, numero_sala=7, id_pelicula=84580833, horario=3, fecha='2020-06-12'),
            Funciones(id=4638, numero_sala=7, id_pelicula=84580833, horario=3, fecha='2020-06-14'),
        ]

        generador = (p for p in lista_funciones)
        resultado = normalizar_fechas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_funciones)


if __name__ == '__main__':
    unittest.main(verbosity=2)
