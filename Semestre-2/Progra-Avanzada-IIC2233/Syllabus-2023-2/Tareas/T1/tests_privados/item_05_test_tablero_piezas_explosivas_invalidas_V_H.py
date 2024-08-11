import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestPiezasExplosivasInvalidas_V_H(unittest.TestCase):
    def test_tablero_vacio(self):
        tablero_str = [
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_tablero_solo_piezas_validas_1(self):
        tablero_str = [
            ['PP', '--', '--', '--', 'PP'],
            ['--', 'V1', '--', 'PP', 'PP'],
            ['PP', '--', '--', 'PP', 'H5'],
            ['V4', 'PP', 'PP', 'H4', '--'],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_tablero_solo_piezas_validas_2(self):
        tablero_str = [
                ['V2', 'V5', 'H2', 'PP'],
                ['--', '--', 'H4', 'PP'],
                ['--', 'PP', 'V3', 'PP'],
                ['V3', 'H1', '--', 'V5'],
                ['--', 'H4', 'PP', 'H1'],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_piezas_invalidas_1(self):
        tablero_str = [
            ['H5', 'PP', 'PP', 'PP'],
            ['V1', 'V4', 'H1', 'V7'],
            ['--', 'H4', 'V3', 'PP'],
            ['PP', 'PP', 'PP', 'H3'],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 2)

    def test_piezas_invalidas_2(self):
        tablero_str = [
            ['H8', 'V6', '--', 'PP', 'H1'],
            ['--', 'PP', 'H3', '--', 'PP'],
            ['PP', '--', 'PP', 'V7', 'PP'],
            ['V1', 'PP', '--', 'H2', 'H5'],
            ['--', 'H9', 'V5', '--', '--'],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 4)

    def test_piezas_invalidas_3(self):
        tablero_str = [
            ['H7', '--', 'H3'],
            ['PP', 'PP', 'V8'],
            ['H2', 'H4', 'PP'],
            ['PP', 'PP', '--'],
            ['--', 'V5', 'V4'],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 3)

    def test_piezas_invalidas_4(self):
        tablero_str = [
            ['H9', 'H7', 'V1', 'V3', '--', 'PP'],
            ['V2', 'PP', 'H2', 'H7', 'V5', 'H6'],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 5)

    def test_piezas_invalidas_5(self):
        tablero_str = [
            ['--', 'H7', 'V4', 'V5', 'V2'],
            ['PP', 'H9', 'V5', '--', 'PP'],
            ['V4', '--', 'PP', 'PP', '--'],
            ['--', 'V4', 'H7', '--', 'H6'],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 6)

    def test_piezas_invalidas_6(self):
        tablero_str = [
                ['V6', 'H5'],
                ['H1', '--'],
                ['--', 'V1'],
                ['PP', '--'],
                ['H2', 'PP'],
                ['V6', '--'],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 1)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
