import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestPiezasExplosivasInvalidas_V_H_R(unittest.TestCase):
    def test_tablero_vacio(self):
        tablero_str = [
            ["--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_tablero_solo_piezas_validas_1(self):
        tablero_str = [
            ['R8', 'V3', '--', 'PP'],
            ['--', 'H3', 'R5', '--'],
            ['H1', 'PP', 'R9', 'R1'],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_tablero_solo_piezas_validas_2(self):
        tablero_str = [
            ['R7', 'PP'],
            ['H2', '--'],
            ['--', 'R6'],
            ['R8', 'V3'],
            ['--', 'R7'],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_piezas_invalidas_1(self):
        tablero_str = [
            ["R9", "PP", "--"],
            ["--", "R9", "V5"],
            ["PP", "H2", "R5"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 2)

    def test_piezas_invalidas_2(self):
        tablero_str = [
            ["R8", "V4", "R9", "--", "PP"],
            ["--", "R6", "--", "H5", "R7"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 3)

    def test_piezas_invalidas_3(self):
        tablero_str = [
            ["V6", "R9"],
            ["--", "V7"],
            ["R8", "H3"],
            ["--", "--"],
            ["PP", "R7"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 4)

    def test_piezas_invalidas_4(self):
        tablero_str = [
            ["--", "R6"],
            ["R6", "PP"],
            ["--", "V3"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 1)

    def test_piezas_invalidas_5(self):
        tablero_str = [
            ["R9", "--", "R3"],
            ["H3", "--", "PP"],
            ["--", "R9", "--"],
            ["PP", "V1", "R1"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 1)

    def test_piezas_invalidas_6(self):
        tablero_str = [
            ["R8", "V3", "--", "R4", "PP"],
            ["--", "PP", "H7", "R1", "V6"],
            ["--", "R1", "--", "--", "--"],
            ["--", "H2", "--", "R5", "H4"],
            ["--", "R7", "PP", "V5", "PP"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 2)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
