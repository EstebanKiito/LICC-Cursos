import sys
import unittest
import copy

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestSolucionar_sin_solucion(unittest.TestCase):

    def test_tablero_2x2_sin_solucion(self):
        tablero_str = [
            ["--", "--"],
            ["--", "V3"]
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x3_sin_solucion(self):
        tablero_str = [
            ['--', 'R6', '--'],
            ['--', '--', '--'],
            ['R2', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x4_sin_solucion(self):
        tablero_str = [
            ['--', '--', '--', 'R7'],
            ['--', '--', 'R1', '--'],
            ['--', 'V1', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x4_sin_solucion(self):
        tablero_str = [
            ['--', 'R4', '--', 'V3'],
            ['--', 'R6', '--', 'V9'],
            ['V4', 'R4', '--', 'V4'],
            ['H3', '--', '--', 'H2'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_5x4_sin_solucion(self):
        tablero_str = [
            ['R9', '--', '--', '--', 'V2'],
            ['--', 'V9', '--', '--', 'R8'],
            ['--', 'R2', '--', 'R9', '--'],
            ['--', 'H5', '--', 'R7', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_5x5_sin_solucion(self):
        tablero_str = [
            ['--', 'R5', '--', 'R9', '--'],
            ['H5', '--', '--', '--', '--'],
            ['--', 'V3', '--', '--', 'R4'],
            ['--', '--', 'V2', '--', 'H3'],
            ['V1', 'V4', '--', 'R1', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)



if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
