import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import personas_reservas
from utilidades import Reservas
from typing import Generator

class TestPersonasReservas(unittest.TestCase):

    def test_0(self):
        """
        Test básico de personas_reservas
        """
        lista_reservas = [
            Reservas(id_persona=245769, id_funcion=4718, numero_butaca="C10"),
            Reservas(id_persona=278561, id_funcion=4293, numero_butaca="A2"),
            Reservas(id_persona=138975, id_funcion=7617, numero_butaca="F1"),
            Reservas(id_persona=673894, id_funcion=9721, numero_butaca="E7"),
            Reservas(id_persona=621438, id_funcion=7617, numero_butaca="D3"),
            Reservas(id_persona=739182, id_funcion=4293, numero_butaca="E9"),
            Reservas(id_persona=463289, id_funcion=9391, numero_butaca="G7"),
            Reservas(id_persona=463289, id_funcion=4718, numero_butaca="C7"),
            Reservas(id_persona=364298, id_funcion=7617, numero_butaca="H6"),
            Reservas(id_persona=954362, id_funcion=4718, numero_butaca="C4"),
            Reservas(id_persona=984723, id_funcion=7617, numero_butaca="D5"),
            Reservas(id_persona=149872, id_funcion=9391, numero_butaca="B5"),
            Reservas(id_persona=735242, id_funcion=7617, numero_butaca="B10"),
            Reservas(id_persona=245769, id_funcion=7617, numero_butaca="F7"),
            Reservas(id_persona=376581, id_funcion=7617, numero_butaca="E5"),
            Reservas(id_persona=951827, id_funcion=9721, numero_butaca="H6"),
            Reservas(id_persona=946353, id_funcion=9391, numero_butaca="G2"),
            Reservas(id_persona=376581, id_funcion=9721, numero_butaca="C8"),
            Reservas(id_persona=419725, id_funcion=4718, numero_butaca="G1"),
            Reservas(id_persona=824156, id_funcion=4718, numero_butaca="C5"),
        ]

        expected_set_funciones = {245769, 278561, 138975, 673894, 621438, 739182, 463289, 364298,
            954362, 984723, 149872, 735242, 376581, 951827, 946353, 419725, 824156}

        resultado = personas_reservas(iter(lista_reservas))
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        for n in list(expected_set_funciones):
            self.assertIn(n, list(resultado))
        for n in list(resultado):
            self.assertIn(n, list(expected_set_funciones))

    def test_1(self):
        """
        Test sin repetidos
        """
        lista_reservas = [
            Reservas(id_persona=697413, id_funcion=9721, numero_butaca="D1"),
            Reservas(id_persona=781245, id_funcion=4718, numero_butaca="C9"),
            Reservas(id_persona=184926, id_funcion=4718, numero_butaca="C2"),
            Reservas(id_persona=278561, id_funcion=4293, numero_butaca="A2"),
            Reservas(id_persona=836197, id_funcion=4293, numero_butaca="D8"),
            Reservas(id_persona=954362, id_funcion=4293, numero_butaca="B3"),
            Reservas(id_persona=573912, id_funcion=6237, numero_butaca="F10"),
            Reservas(id_persona=186243, id_funcion=9721, numero_butaca="H10"),
            Reservas(id_persona=138975, id_funcion=7617, numero_butaca="F1"),
            Reservas(id_persona=721584, id_funcion=9391, numero_butaca="B3"),
            Reservas(id_persona=857474, id_funcion=9391, numero_butaca="F8"),
            Reservas(id_persona=956362, id_funcion=6237, numero_butaca="B9"),
            Reservas(id_persona=654365, id_funcion=7617, numero_butaca="B3"),
            Reservas(id_persona=463289, id_funcion=4293, numero_butaca="B6"),
            Reservas(id_persona=534127, id_funcion=7617, numero_butaca="A1"),
            Reservas(id_persona=596318, id_funcion=6237, numero_butaca="D10"),
            Reservas(id_persona=765476, id_funcion=6237, numero_butaca="H5"),
            Reservas(id_persona=317984, id_funcion=4293, numero_butaca="C1"),
            Reservas(id_persona=745219, id_funcion=4293, numero_butaca="D2"),
            Reservas(id_persona=598127, id_funcion=6237, numero_butaca="G6"),
        ]

        expected_set_funciones = {857474, 186243, 745219, 654365, 317984, 278561,
                                  765476, 721584, 463289, 781245, 697413, 956362,
                                  573912, 596318, 184926, 138975, 836197, 534127,
                                  598127, 954362}

        resultado = personas_reservas(iter(lista_reservas))
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        for n in list(expected_set_funciones):
            self.assertIn(n, list(resultado))
        for n in list(resultado):
            self.assertIn(n, list(expected_set_funciones))

    def test_2(self):
        """
        Test básico 2 de personas_reservas
        """
        lista_reservas = [
            Reservas(id_persona=654546, id_funcion=4293, numero_butaca="H4"),
            Reservas(id_persona=781245, id_funcion=4718, numero_butaca="C9"),
            Reservas(id_persona=745219, id_funcion=6237, numero_butaca="D9"),
            Reservas(id_persona=278561, id_funcion=4293, numero_butaca="A2"),
            Reservas(id_persona=765476, id_funcion=7617, numero_butaca="B4"),
            Reservas(id_persona=962734, id_funcion=4293, numero_butaca="C5"),
            Reservas(id_persona=745219, id_funcion=4293, numero_butaca="D2"),
            Reservas(id_persona=781245, id_funcion=6237, numero_butaca="C7"),
            Reservas(id_persona=895642, id_funcion=9721, numero_butaca="A3"),
            Reservas(id_persona=596318, id_funcion=4718, numero_butaca="D7"),
            Reservas(id_persona=745219, id_funcion=4718, numero_butaca="E4"),
            Reservas(id_persona=917346, id_funcion=4293, numero_butaca="F4"),
            Reservas(id_persona=367591, id_funcion=4718, numero_butaca="G8"),
            Reservas(id_persona=312497, id_funcion=7617, numero_butaca="D9"),
            Reservas(id_persona=138975, id_funcion=9391, numero_butaca="G8"),
            Reservas(id_persona=765653, id_funcion=9391, numero_butaca="F7"),
            Reservas(id_persona=691734, id_funcion=4718, numero_butaca="H4"),
            Reservas(id_persona=518367, id_funcion=4718, numero_butaca="E3"),
            Reservas(id_persona=917346, id_funcion=4718, numero_butaca="H6"),
            Reservas(id_persona=248765, id_funcion=6237, numero_butaca="F7"),
        ]

        expected_set_funciones = {654546, 781245, 745219, 278561, 765476, 962734, 745219, 781245,
            895642, 596318, 745219, 917346, 367591, 312497, 138975, 765653, 691734, 518367,
            917346, 248765}

        resultado = personas_reservas(iter(lista_reservas))
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        for n in list(expected_set_funciones):
            self.assertIn(n, list(resultado))
        for n in list(resultado):
            self.assertIn(n, list(expected_set_funciones))

    def test_3(self):
        """
        Solo 1 persona reserva
        """
        lista_reservas = [
            Reservas(id_persona=463289, id_funcion=9721, numero_butaca="H6"),
            Reservas(id_persona=463289, id_funcion=4718, numero_butaca="C7"),
            Reservas(id_persona=463289, id_funcion=9721, numero_butaca="A7"),
            Reservas(id_persona=463289, id_funcion=7617, numero_butaca="B1"),
            Reservas(id_persona=463289, id_funcion=9721, numero_butaca="E3"),
            Reservas(id_persona=463289, id_funcion=9391, numero_butaca="B3"),
            Reservas(id_persona=463289, id_funcion=9391, numero_butaca="G7"),
            Reservas(id_persona=463289, id_funcion=4293, numero_butaca="D3"),
            Reservas(id_persona=463289, id_funcion=9391, numero_butaca="D5"),
            Reservas(id_persona=463289, id_funcion=4718, numero_butaca="C5"),
            Reservas(id_persona=463289, id_funcion=9721, numero_butaca="F8"),
            Reservas(id_persona=463289, id_funcion=9721, numero_butaca="E4"),
            Reservas(id_persona=463289, id_funcion=7617, numero_butaca="F2"),
            Reservas(id_persona=463289, id_funcion=7617, numero_butaca="B10"),
            Reservas(id_persona=463289, id_funcion=9721, numero_butaca="D1"),
            Reservas(id_persona=463289, id_funcion=9721, numero_butaca="C9"),
            Reservas(id_persona=463289, id_funcion=4718, numero_butaca="B2"),
            Reservas(id_persona=463289, id_funcion=4293, numero_butaca="A4"),
            Reservas(id_persona=463289, id_funcion=7617, numero_butaca="A1"),
            Reservas(id_persona=463289, id_funcion=7617, numero_butaca="E9"),
        ]

        expected_set_funciones = {463289}

        resultado = personas_reservas(iter(lista_reservas))
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        for n in list(expected_set_funciones):
            self.assertIn(n, list(resultado))
        for n in list(resultado):
            self.assertIn(n, list(expected_set_funciones))

    def test_4(self):
        """
        Ninguna reserva
        """
        lista_reservas = [
        ]

        expected_set_funciones = []

        resultado = personas_reservas(iter(lista_reservas))
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        for n in list(expected_set_funciones):
            self.assertIn(n, list(resultado))
        for n in list(resultado):
            self.assertIn(n, list(expected_set_funciones))


if __name__ == '__main__':
    unittest.main(verbosity=2)