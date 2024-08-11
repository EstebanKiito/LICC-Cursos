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
            Reservas(id_persona=263081, id_funcion=9428, numero_butaca='A3'),
            Reservas(id_persona=193453, id_funcion=9428, numero_butaca='B1'),
            Reservas(id_persona=104423, id_funcion=9428, numero_butaca='H1'),
            Reservas(id_persona=138359, id_funcion=9428, numero_butaca='H10'),
            Reservas(id_persona=651331, id_funcion=9428, numero_butaca='E9'),
            Reservas(id_persona=721504, id_funcion=9428, numero_butaca='F6'),
            Reservas(id_persona=974627, id_funcion=9428, numero_butaca='A6'),
            Reservas(id_persona=780224, id_funcion=9428, numero_butaca='H5'),
            Reservas(id_persona=864837, id_funcion=9428, numero_butaca='D4'),
            Reservas(id_persona=289380, id_funcion=9428, numero_butaca='B6'),
            Reservas(id_persona=289151, id_funcion=9428, numero_butaca='F2'),
        ]
        funciones = [
            Funciones(id=9428, numero_sala=7, id_pelicula=83827699, horario=7, fecha='02-12-23'),
        ]
        id_funcion = 9428

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
            Reservas(id_persona=864837, id_funcion=1114, numero_butaca='D6'),
            Reservas(id_persona=780224, id_funcion=1114, numero_butaca='E8'),
            Reservas(id_persona=678509, id_funcion=1114, numero_butaca='A9'),
            Reservas(id_persona=471183, id_funcion=1114, numero_butaca='D10'),
            Reservas(id_persona=480408, id_funcion=1114, numero_butaca='E6'),
            Reservas(id_persona=875734, id_funcion=4639, numero_butaca='A7'),
            Reservas(id_persona=650018, id_funcion=1114, numero_butaca='B10'),
            Reservas(id_persona=360116, id_funcion=4639, numero_butaca='C3'),
            Reservas(id_persona=344229, id_funcion=4639, numero_butaca='C10'),
            Reservas(id_persona=743208, id_funcion=1114, numero_butaca='F3'),
            Reservas(id_persona=683336, id_funcion=1114, numero_butaca='A5'),
            Reservas(id_persona=202443, id_funcion=4639, numero_butaca='H3'),
            Reservas(id_persona=399774, id_funcion=4639, numero_butaca='H8'),
            Reservas(id_persona=571081, id_funcion=4639, numero_butaca='A1'),
            Reservas(id_persona=910788, id_funcion=4639, numero_butaca='B1'),
            Reservas(id_persona=810585, id_funcion=1114, numero_butaca='H4'),
            Reservas(id_persona=480227, id_funcion=1114, numero_butaca='G5'),
        ]
        funciones = [
            Funciones(id=4639, numero_sala=9, id_pelicula=19541263, horario=8, fecha='05-12-23'),
            Funciones(id=1114, numero_sala=4, id_pelicula=43495707, horario=9, fecha='01-12-23'),
        ]
        id_funcion = 4639

        expected_result = 7

        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = butacas_por_funcion(gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, int)
        self.assertEqual(result, expected_result)

    def test_2(self):
        """
        Varias funciones de la misma película en la misma fecha
        """
        reservas = [
            Reservas(id_persona=772215, id_funcion=9454, numero_butaca='A4'),
            Reservas(id_persona=561104, id_funcion=9454, numero_butaca='E7'),
            Reservas(id_persona=143846, id_funcion=6657, numero_butaca='F3'),
            Reservas(id_persona=678509, id_funcion=4528, numero_butaca='H9'),
            Reservas(id_persona=547446, id_funcion=9454, numero_butaca='C1'),
            Reservas(id_persona=422180, id_funcion=6657, numero_butaca='H5'),
            Reservas(id_persona=589077, id_funcion=6657, numero_butaca='B6'),
            Reservas(id_persona=138359, id_funcion=9454, numero_butaca='B7'),
            Reservas(id_persona=752204, id_funcion=9454, numero_butaca='D7'),
            Reservas(id_persona=193453, id_funcion=6657, numero_butaca='A9'),
            Reservas(id_persona=289151, id_funcion=6657, numero_butaca='D8'),
            Reservas(id_persona=480408, id_funcion=6657, numero_butaca='D4'),
            Reservas(id_persona=178291, id_funcion=9454, numero_butaca='G5'),
            Reservas(id_persona=852596, id_funcion=9454, numero_butaca='A2'),
            Reservas(id_persona=245587, id_funcion=9454, numero_butaca='B8'),
            Reservas(id_persona=517596, id_funcion=9454, numero_butaca='C3'),
            Reservas(id_persona=360116, id_funcion=4528, numero_butaca='F5'),
            Reservas(id_persona=743208, id_funcion=6657, numero_butaca='C9'),
            Reservas(id_persona=971631, id_funcion=4528, numero_butaca='E9'),
            Reservas(id_persona=369116, id_funcion=6657, numero_butaca='H8'),
            Reservas(id_persona=368840, id_funcion=6657, numero_butaca='D10'),
            Reservas(id_persona=523275, id_funcion=6657, numero_butaca='F7'),
        ]
        funciones = [
            Funciones(id=9454, numero_sala=9, id_pelicula=98729199, horario=6, fecha='02-12-23'),
            Funciones(id=6657, numero_sala=2, id_pelicula=98729199, horario=6, fecha='02-12-23'),
            Funciones(id=4528, numero_sala=2, id_pelicula=98729199, horario=4, fecha='02-12-23'),
        ]
        id_funcion = 6657

        expected_result = 10

        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = butacas_por_funcion(gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, int)
        self.assertEqual(result, expected_result)

    def test_3(self):
        """
        Muchas funciones
        """
        reservas = [
            Reservas(id_persona=683336, id_funcion=5248, numero_butaca='H8'),
            Reservas(id_persona=788596, id_funcion=1444, numero_butaca='H7'),
            Reservas(id_persona=254224, id_funcion=3428, numero_butaca='C4'),
            Reservas(id_persona=423989, id_funcion=5248, numero_butaca='E2'),
            Reservas(id_persona=138359, id_funcion=3428, numero_butaca='D2'),
            Reservas(id_persona=910788, id_funcion=1114, numero_butaca='B6'),
            Reservas(id_persona=289380, id_funcion=2082, numero_butaca='C8'),
            Reservas(id_persona=499756, id_funcion=1114, numero_butaca='B2'),
            Reservas(id_persona=178291, id_funcion=5248, numero_butaca='D9'),
            Reservas(id_persona=875734, id_funcion=5248, numero_butaca='A8'),
            Reservas(id_persona=752104, id_funcion=5248, numero_butaca='A3'),
            Reservas(id_persona=589077, id_funcion=1114, numero_butaca='G8'),
            Reservas(id_persona=202443, id_funcion=2082, numero_butaca='A7'),
            Reservas(id_persona=245587, id_funcion=1114, numero_butaca='D8'),
            Reservas(id_persona=591338, id_funcion=1444, numero_butaca='H10'),
            Reservas(id_persona=355736, id_funcion=7772, numero_butaca='D6'),
        ]
        funciones = [
            Funciones(id=1444, numero_sala=9, id_pelicula=41822679, horario=7, fecha='04-12-23'),
            Funciones(id=2082, numero_sala=8, id_pelicula=70690364, horario=7, fecha='03-12-23'),
            Funciones(id=7772, numero_sala=9, id_pelicula=41822679, horario=4, fecha='01-12-23'),
            Funciones(id=3428, numero_sala=4, id_pelicula=69309996, horario=7, fecha='04-12-23'),
            Funciones(id=4479, numero_sala=2, id_pelicula=27103139, horario=5, fecha='04-12-23'),
            Funciones(id=5248, numero_sala=1, id_pelicula=49040980, horario=8, fecha='01-12-23'),
            Funciones(id=1114, numero_sala=4, id_pelicula=43495707, horario=9, fecha='01-12-23'),
        ]
        id_funcion = 3428

        expected_result = 2

        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = butacas_por_funcion(gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, int)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
