import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestCeldasAfectadas_V_H_R(unittest.TestCase):

    def test_3x3_alcance_R_sin_peon(self):
        tablero_str = [
            ["--", "--", "--"],
            ["--", "R3", "--"],
            ["--", "--", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(1, 1)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 9)

    def test_3x3_alcance_R_con_peon(self):
        tablero_str = [
            ["--", "--", "--"],
            ["--", "R3", "--"],
            ["--", "PP", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(1, 1)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 8)

    def test_3x3_posicion_invalida_peon(self):
        tablero_str = [
            ["--", "--", "--"],
            ["--", "R3", "--"],
            ["--", "PP", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(2, 1)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, -1)

    def test_3x3_posicion_invalida_vacia(self):
        tablero_str = [
            ["--", "--", "--"],
            ["--", "PP", "--"],
            ["R3", "PP", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(0, 2)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, -1)

    def test_3x4_alcance_1_sin_peon(self):
        tablero_str = [
            ["R3", "--", "--", "--"],
            ["--", "--", "--", "--"],
            ["--", "--", "--", "V4"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(0, 0)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 8)

    def test_3x4_alcance_2_sin_peon(self):
        tablero_str = [
            ["R3", "--", "--", "--"],
            ["--", "--", "--", "--"],
            ["--", "--", "--", "V4"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(2, 3)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 3)

    def test_3x4_alcance_1_con_peon(self):
        tablero_str = [
            ["R3", "--", "--", "PP"],
            ["--", "--", "--", "--"],
            ["PP", "--", "PP", "V4"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(0, 0)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 5)

    def test_3x4_alcance_2_con_peon(self):
        tablero_str = [
            ["R3", "--", "--", "PP"],
            ["--", "--", "--", "--"],
            ["--", "--", "--", "V4"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(2, 3)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 2)

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
