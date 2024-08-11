import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero
from pieza_explosiva import PiezaExplosiva


class TestReemplazar(unittest.TestCase):
    # Ejemplo básico
    def test_tablero_reina_y_peon(self):
        tablero_str = [
            ["--", "--", "--"],
            ["--", "--", "PP"],
            ["--", "--", "--"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.reemplazar("test_1")
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)
        # Verificar formato y respuesta
        self.assertListEqual(tablero.dimensiones, [2, 2])
        self.assertListEqual(tablero.tablero, [
            ["R5", "--"],
            ["PP", "PP"]
            ])

    def test_tablero_no_existe(self):
        tablero_str = [["--", "--", "--"], ["--", "--", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.reemplazar("test_no_existe")
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.dimensiones, [2, 3])
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_1(self):
        tablero_str = [
            ["PP", "--", "--"],
            ["--", "--", "PP"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.reemplazar("name_1")
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)
        # Verificar formato y respuesta
        self.assertListEqual(tablero.dimensiones, [3, 3])
        self.assertListEqual(tablero.tablero, [
                ['V1', 'PP', '--'],
                ['--', 'PP', '--'],
                ['--', '--', 'PP'],
            ])

    def test_2(self):
        tablero_str = [
            ["PP", "--", "--"],
            ["--", "--", "PP"],
            ["--", "--", "--"],
            ["PP", "--", "--"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.reemplazar("name_2")
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)
        # Verificar formato y respuesta
        self.assertListEqual(tablero.dimensiones, [5, 5])
        self.assertListEqual(tablero.tablero, [
                ['R7', '--', 'PP', '--', '--'],
                ['--', 'V1', 'V4', 'R5', 'PP'],
                ['--', '--', 'PP', 'H5', '--'],
                ['H5', 'H5', '--', 'R3', 'PP'],
                ['--', 'R7', 'PP', 'V1', '--'],
            ])

    def test_3(self):
        tablero_str = [
            ["--", "PP", "PP", "--"],
            ["--", "--", "--", "--"],
            ["--", "PP", "--", "PP"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.reemplazar("name_3")
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)
        # Verificar formato y respuesta
        self.assertListEqual(tablero.dimensiones, [4, 5])
        self.assertListEqual(tablero.tablero, [
                ['R3', 'H5', '--', 'H7', 'PP'],
                ['--', 'PP', '--', 'R2', 'PP'],
                ['--', 'PP', '--', '--', '--'],
                ['PP', 'V9', 'PP', 'R3', 'PP'],
            ])

    def test_4(self):
        tablero_str = [
            ["PP", "--"],
            ["--", "PP"],
            ["PP", "--"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.reemplazar("name_4")
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)
        # Verificar formato y respuesta
        self.assertListEqual(tablero.dimensiones, [5, 4])
        self.assertListEqual(tablero.tablero, [
                ['R5', 'H7', '--', 'PP'],
                ['R4', 'PP', 'R3', 'PP'],
                ['R4', 'H5', 'V7', 'H3'],
                ['V4', 'V1', '--', 'R2'],
                ['--', 'PP', 'PP', 'PP'],
            ])

    def test_5(self):
        tablero_str = [
            ["--", "--", "--", "PP", "--"],
            ["PP", "--", "PP", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ["--", "PP", "--", "--", "--"],
            ["--", "--", "--", "PP", "--"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.reemplazar("name_5")
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)
        # Verificar formato y respuesta
        self.assertListEqual(tablero.dimensiones, [2, 5])
        self.assertListEqual(tablero.tablero, [
                ['--', 'PP', 'R6', 'PP', 'PP'],
                ['R7', '--', 'V3', 'PP', 'H2'],
            ])



if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
