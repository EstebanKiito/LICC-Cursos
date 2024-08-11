import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import butacas_por_funcion
from utilidades import Reservas, Funciones


class TestVacioButacasPorFuncion(unittest.TestCase):

    def test_0(self):
        """
        Ninguna de las reservas corresponde a la función
        """
        reservas = [
            Reservas(id_persona=809018, id_funcion=1155, numero_butaca='E4'),
            Reservas(id_persona=344229, id_funcion=1155, numero_butaca='E6'),
            Reservas(id_persona=138359, id_funcion=1155, numero_butaca='G10'),
            Reservas(id_persona=143846, id_funcion=1155, numero_butaca='B5'),
            Reservas(id_persona=355736, id_funcion=1155, numero_butaca='G7'),
            Reservas(id_persona=650018, id_funcion=1155, numero_butaca='F2'),
            Reservas(id_persona=780224, id_funcion=1155, numero_butaca='E10'),
        ]
        funciones = [
            Funciones(id=1155, numero_sala=1, id_pelicula=40494740, horario=7, fecha='05-12-23'),
            Funciones(id=1114, numero_sala=4, id_pelicula=43495707, horario=9, fecha='01-12-23'),
        ]
        id_funcion = 1114

        expected_result = 0

        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = butacas_por_funcion(gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, int)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
