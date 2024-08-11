import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import butacas_por_funcion
from utilidades import Reservas, Funciones

class TestButacasPorFuncion(unittest.TestCase):

    def test_0(self):
        """
        Una función
        """
        reservas = [
            Reservas(id_persona=437219, id_funcion=3566, numero_butaca='A3'),
            Reservas(id_persona=367591, id_funcion=3566, numero_butaca='B1'),
            Reservas(id_persona=278561, id_funcion=3566, numero_butaca='H1'),
            Reservas(id_persona=312497, id_funcion=3566, numero_butaca='H10'),
            Reservas(id_persona=825469, id_funcion=3566, numero_butaca='E9'),
            Reservas(id_persona=895642, id_funcion=3566, numero_butaca='F6'),
            Reservas(id_persona=248765, id_funcion=3566, numero_butaca='A6'),
            Reservas(id_persona=954362, id_funcion=3566, numero_butaca='H5'),
            Reservas(id_persona=138975, id_funcion=3566, numero_butaca='D4'),
            Reservas(id_persona=463518, id_funcion=3566, numero_butaca='B6'),
            Reservas(id_persona=463289, id_funcion=3566, numero_butaca='F2'),
        ]
        funciones = [
            Funciones(id=3566, numero_sala=4, id_pelicula=75901837, horario=4, fecha='02-12-23'),
        ]
        id_funcion = 3566

        expected_result = 11

        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = butacas_por_funcion(gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, int)
        self.assertEqual(result, expected_result)

    def test_1(self):
        """
        Varias funciones
        """
        reservas = [
            Reservas(id_persona=138975, id_funcion=4252, numero_butaca='D6'),
            Reservas(id_persona=954362, id_funcion=4252, numero_butaca='E8'),
            Reservas(id_persona=852647, id_funcion=4252, numero_butaca='A9'),
            Reservas(id_persona=645321, id_funcion=4252, numero_butaca='D10'),
            Reservas(id_persona=654546, id_funcion=4252, numero_butaca='E6'),
            Reservas(id_persona=149872, id_funcion=7777, numero_butaca='A7'),
            Reservas(id_persona=824156, id_funcion=4252, numero_butaca='B10'),
            Reservas(id_persona=534254, id_funcion=7777, numero_butaca='C3'),
            Reservas(id_persona=518367, id_funcion=7777, numero_butaca='C10'),
            Reservas(id_persona=917346, id_funcion=4252, numero_butaca='F3'),
            Reservas(id_persona=857474, id_funcion=4252, numero_butaca='A5'),
            Reservas(id_persona=376581, id_funcion=7777, numero_butaca='H3'),
            Reservas(id_persona=573912, id_funcion=7777, numero_butaca='H8'),
            Reservas(id_persona=745219, id_funcion=7777, numero_butaca='A1'),
            Reservas(id_persona=184926, id_funcion=7777, numero_butaca='B1'),
            Reservas(id_persona=984723, id_funcion=4252, numero_butaca='H4'),
            Reservas(id_persona=654365, id_funcion=4252, numero_butaca='G5'),
        ]
        funciones = [
            Funciones(id=7777, numero_sala=6, id_pelicula=11615401, horario=5, fecha='05-12-23'),
            Funciones(id=4252, numero_sala=1, id_pelicula=35569845, horario=6, fecha='01-12-23'),
        ]
        id_funcion = 7777

        expected_result = 7

        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = butacas_por_funcion(gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, int)
        self.assertEqual(result, expected_result)

    def test_2(self):
        """
        Ninguna de las reservas corresponde a la función
        """
        reservas = [
            Reservas(id_persona=983156, id_funcion=4293, numero_butaca='E4'),
            Reservas(id_persona=518367, id_funcion=4293, numero_butaca='E6'),
            Reservas(id_persona=312497, id_funcion=4293, numero_butaca='G10'),
            Reservas(id_persona=317984, id_funcion=4293, numero_butaca='B5'),
            Reservas(id_persona=529874, id_funcion=4293, numero_butaca='G7'),
            Reservas(id_persona=824156, id_funcion=4293, numero_butaca='F2'),
            Reservas(id_persona=954362, id_funcion=4293, numero_butaca='E10'),
        ]
        funciones = [
            Funciones(id=4293, numero_sala=7, id_pelicula=32568878, horario=4, fecha='05-12-23'),
            Funciones(id=4252, numero_sala=1, id_pelicula=35569845, horario=6, fecha='01-12-23'),
        ]
        id_funcion = 4252

        expected_result = 0

        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = butacas_por_funcion(gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, int)
        self.assertEqual(result, expected_result)

    def test_3(self):
        """
        Varias funciones de la misma película en la misma fecha
        """
        reservas = [
            Reservas(id_persona=946353, id_funcion=3592, numero_butaca='A4'),
            Reservas(id_persona=735242, id_funcion=3592, numero_butaca='E7'),
            Reservas(id_persona=317984, id_funcion=9795, numero_butaca='F3'),
            Reservas(id_persona=852647, id_funcion=7666, numero_butaca='H9'),
            Reservas(id_persona=721584, id_funcion=3592, numero_butaca='C1'),
            Reservas(id_persona=596318, id_funcion=9795, numero_butaca='H5'),
            Reservas(id_persona=763215, id_funcion=9795, numero_butaca='B6'),
            Reservas(id_persona=312497, id_funcion=3592, numero_butaca='B7'),
            Reservas(id_persona=926342, id_funcion=3592, numero_butaca='D7'),
            Reservas(id_persona=367591, id_funcion=9795, numero_butaca='A9'),
            Reservas(id_persona=463289, id_funcion=9795, numero_butaca='D8'),
            Reservas(id_persona=654546, id_funcion=9795, numero_butaca='D4'),
            Reservas(id_persona=352429, id_funcion=3592, numero_butaca='G5'),
            Reservas(id_persona=126734, id_funcion=3592, numero_butaca='A2'),
            Reservas(id_persona=419725, id_funcion=3592, numero_butaca='B8'),
            Reservas(id_persona=691734, id_funcion=3592, numero_butaca='C3'),
            Reservas(id_persona=534254, id_funcion=7666, numero_butaca='F5'),
            Reservas(id_persona=917346, id_funcion=9795, numero_butaca='C9'),
            Reservas(id_persona=245769, id_funcion=7666, numero_butaca='E9'),
            Reservas(id_persona=543254, id_funcion=9795, numero_butaca='H8'),
            Reservas(id_persona=542978, id_funcion=9795, numero_butaca='D10'),
            Reservas(id_persona=697413, id_funcion=9795, numero_butaca='F7'),
        ]
        funciones = [
            Funciones(id=3592, numero_sala=6, id_pelicula=90803337, horario=3, fecha='02-12-23'),
            Funciones(id=9795, numero_sala=8, id_pelicula=90803337, horario=3, fecha='02-12-23'),
            Funciones(id=7666, numero_sala=8, id_pelicula=90803337, horario=1, fecha='02-12-23'),
        ]
        id_funcion = 9795

        expected_result = 10

        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = butacas_por_funcion(gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, int)
        self.assertEqual(result, expected_result)

    def test_4(self):
        """
        Muchas funciones
        """
        reservas = [
            Reservas(id_persona=857474, id_funcion=8386, numero_butaca='H8'),
            Reservas(id_persona=962734, id_funcion=4582, numero_butaca='H7'),
            Reservas(id_persona=428362, id_funcion=6566, numero_butaca='C4'),
            Reservas(id_persona=598127, id_funcion=8386, numero_butaca='E2'),
            Reservas(id_persona=312497, id_funcion=6566, numero_butaca='D2'),
            Reservas(id_persona=184926, id_funcion=4252, numero_butaca='B6'),
            Reservas(id_persona=463518, id_funcion=5220, numero_butaca='C8'),
            Reservas(id_persona=673894, id_funcion=4252, numero_butaca='B2'),
            Reservas(id_persona=352429, id_funcion=8386, numero_butaca='D9'),
            Reservas(id_persona=149872, id_funcion=8386, numero_butaca='A8'),
            Reservas(id_persona=926242, id_funcion=8386, numero_butaca='A3'),
            Reservas(id_persona=763215, id_funcion=4252, numero_butaca='G8'),
            Reservas(id_persona=376581, id_funcion=5220, numero_butaca='A7'),
            Reservas(id_persona=419725, id_funcion=4252, numero_butaca='D8'),
            Reservas(id_persona=765476, id_funcion=4582, numero_butaca='H10'),
            Reservas(id_persona=529874, id_funcion=1910, numero_butaca='D6'),
        ]
        funciones = [
            Funciones(id=4582, numero_sala=6, id_pelicula=33896817, horario=4, fecha='04-12-23'),
            Funciones(id=5220, numero_sala=5, id_pelicula=62764502, horario=4, fecha='03-12-23'),
            Funciones(id=1910, numero_sala=6, id_pelicula=33896817, horario=1, fecha='01-12-23'),
            Funciones(id=6566, numero_sala=1, id_pelicula=61384134, horario=4, fecha='04-12-23'),
            Funciones(id=7617, numero_sala=8, id_pelicula=19177277, horario=2, fecha='04-12-23'),
            Funciones(id=8386, numero_sala=7, id_pelicula=41115118, horario=5, fecha='01-12-23'),
            Funciones(id=4252, numero_sala=1, id_pelicula=35569845, horario=6, fecha='01-12-23'),
        ]
        id_funcion = 6566

        expected_result = 2

        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = butacas_por_funcion(gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, int)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main(verbosity=2)