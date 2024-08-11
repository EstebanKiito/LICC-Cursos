import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestDesglose(unittest.TestCase):
    # Ejemplo básico
    def test_tablero_vacio(self):
        tablero_str = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 0)
        self.assertEqual(c_peones, 0)
        self.assertEqual(c_vacias, 64)

    def test_tablero_solo_peones(self):
        tablero_str = [
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 0)
        self.assertEqual(c_peones, 64)
        self.assertEqual(c_vacias, 0)

    def test_tablero_solo_explosivas(self):
        tablero_str = [
            ["R1", "R1", "R1", "R1", "R1", "R1", "R1", "R1"],
            ["R1", "R1", "R1", "R1", "R1", "R1", "R1", "R1"],
            ["R1", "R1", "R1", "R1", "R1", "R1", "R1", "R1"],
            ["R1", "R1", "R1", "R1", "R1", "R1", "R1", "R1"],
            ["R1", "R1", "R1", "R1", "R1", "R1", "R1", "R1"],
            ["R1", "R1", "R1", "R1", "R1", "R1", "R1", "R1"],
            ["R1", "R1", "R1", "R1", "R1", "R1", "R1", "R1"],
            ["R1", "R1", "R1", "R1", "R1", "R1", "R1", "R1"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 64)
        self.assertEqual(c_peones, 0)
        self.assertEqual(c_vacias, 0)

    def test_tablero_peones_y_bombas(self):
        tablero_str = [
            ["PP", "H9", "PP", "H9", "PP", "H9", "PP", "H9"],
            ["H9", "PP", "H9", "PP", "H9", "PP", "H9", "PP"],
            ["PP", "H9", "PP", "H9", "PP", "H9", "PP", "H9"],
            ["H9", "PP", "H9", "PP", "H9", "PP", "H9", "PP"],
            ["PP", "H9", "PP", "H9", "PP", "H9", "PP", "H9"],
            ["H9", "PP", "H9", "PP", "H9", "PP", "H9", "PP"],
            ["PP", "H9", "PP", "H9", "PP", "H9", "PP", "H9"],
            ["H9", "PP", "H9", "PP", "H9", "PP", "H9", "PP"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 32)
        self.assertEqual(c_peones, 32)
        self.assertEqual(c_vacias, 0)

    def test_tablero_equitativo(self):
        tablero_str = [
            ["R1", "PP", "--", "V8", "PP", "--", "H8", "PP", "--"],
            ["PP", "--", "V8", "PP", "--", "H8", "PP", "--", "R1"],
            ["--", "V8", "PP", "--", "H8", "PP", "--", "R1", "PP"],
            ["R1", "PP", "--", "V8", "PP", "--", "H8", "PP", "--"],
            ["PP", "--", "V8", "PP", "--", "H8", "PP", "--", "R1"],
            ["--", "V8", "PP", "--", "H8", "PP", "--", "R1", "PP"],
            ["R1", "PP", "--", "V8", "PP", "--", "H8", "PP", "--"],
            ["PP", "--", "V8", "PP", "--", "H8", "PP", "--", "R1"],
            ["--", "V8", "PP", "--", "H8", "PP", "--", "R1", "PP"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 27)
        self.assertEqual(c_peones, 27)
        self.assertEqual(c_vacias, 27)

    def test_tablero_30x30(self):
        tablero_str = [
            ['V8', 'PP', '--', 'PP', '--', 'PP', '--', 'PP', 'PP', '--', 'PP', 'R8', '--', '--', 'PP', 'PP', '--', 'H8', 'V8', 'PP', '--', 'PP', 'PP', '--', 'PP', 'V8', 'H8', 'PP', '--', 'V8'],
            ['PP', '--', '--', '--', 'PP', '--', '--', 'R8', 'R8', 'V8', 'PP', '--', 'V8', 'PP', '--', '--', 'R8', 'PP', 'V8', '--', 'PP', '--', '--', '--', '--', 'H8', 'V8', 'PP', '--', '--'],
            ['PP', 'PP', '--', 'PP', 'PP', 'PP', '--', 'H8', '--', '--', 'PP', '--', 'PP', 'H8', 'PP', 'PP', '--', 'PP', '--', 'PP', '--', '--', '--', 'PP', 'PP', '--', 'PP', 'R8', '--', 'PP'],
            ['PP', '--', 'PP', '--', '--', '--', '--', 'R8', '--', 'V8', 'V8', 'R8', '--', '--', 'R8', 'PP', 'PP', '--', '--', 'PP', 'H8', 'V8', 'PP', 'V8', 'R8', '--', 'R8', 'PP', '--', 'H8'],
            ['--', '--', 'H8', 'R8', 'H6', 'PP', 'PP', 'R8', 'V8', 'PP', 'PP', 'PP', 'V8', 'PP', '--', '--', 'PP', '--', 'H8', 'R8', 'PP', 'H5', 'PP', 'PP', 'PP', 'R8', '--', 'V8', '--', '--'],
            ['PP', 'R8', 'V8', '--', 'V8', 'PP', 'PP', '--', 'PP', '--', 'V8', '--', '--', 'PP', 'PP', 'R8', 'PP', '--', 'V8', 'R3', '--', 'H8', 'PP', 'PP', 'H8', 'PP', 'H8', '--', 'R8', 'PP'],
            ['PP', 'PP', 'R8', '--', 'H5', 'PP', 'V8', 'PP', '--', 'V8', '--', '--', 'PP', '--', 'H8', 'PP', 'PP', 'H8', 'V8', 'V8', 'V8', 'PP', 'H8', '--', 'PP', '--', 'R8', 'R8', '--', '--'],
            ['PP', 'R8', 'PP', 'PP', '--', 'V8', '--', 'H8', '--', 'R8', '--', 'H8', 'PP', 'H8', 'H8', 'H8', 'PP', 'H8', 'PP', '--', 'H8', 'H8', '--', 'PP', '--', '--', 'V8', '--', 'PP', '--'],
            ['V8', 'PP', 'PP', 'H8', 'R8', 'PP', '--', 'R8', 'H8', 'PP', '--', 'PP', '--', '--', 'V8', 'PP', 'PP', 'PP', 'PP', 'R8', '--', 'H8', '--', 'PP', 'PP', '--', 'R8', '--', 'R8', 'PP'],
            ['PP', 'PP', '--', '--', '--', 'V8', '--', '--', 'R8', 'PP', 'PP', 'R8', 'V1', 'PP', '--', 'H8', 'R8', 'R8', 'V8', 'PP', 'PP', '--', '--', '--', '--', 'PP', '--', 'PP', 'R9', 'V8'],
            ['V8', 'V8', '--', 'PP', 'V8', 'PP', '--', 'H8', '--', 'PP', 'PP', '--', '--', 'H8', 'H8', 'H8', 'H8', '--', 'R8', 'R8', '--', 'V8', '--', '--', 'R8', '--', 'PP', 'PP', 'PP', 'H8'],
            ['PP', 'R8', 'PP', 'V8', '--', 'PP', 'H8', 'R8', 'PP', '--', 'H8', 'R3', 'PP', 'R8', '--', 'PP', 'R8', 'V8', 'R8', '--', 'V8', 'PP', 'H8', '--', '--', 'H8', '--', '--', '--', '--'],
            ['--', 'PP', 'H8', 'PP', '--', 'PP', '--', '--', '--', '--', 'R8', '--', 'R8', 'PP', 'H8', 'PP', '--', '--', '--', '--', 'H8', '--', 'PP', '--', 'R8', '--', 'PP', 'H8', '--', '--'],
            ['H8', 'PP', 'V8', 'PP', 'R8', 'R3', '--', '--', '--', '--', '--', '--', '--', '--', 'PP', '--', 'R8', 'R8', '--', 'PP', '--', 'R8', 'PP', 'PP', 'PP', 'V8', 'H8', '--', 'PP', 'V8'],
            ['PP', '--', 'V8', 'H8', 'R8', 'R8', 'PP', 'PP', 'PP', 'PP', 'H8', '--', 'PP', '--', '--', 'PP', 'PP', '--', '--', 'PP', 'PP', '--', 'PP', 'V8', 'PP', 'PP', 'H8', '--', '--', '--'],
            ['PP', '--', 'PP', 'H8', 'R3', 'H8', 'V8', 'R7', 'PP', '--', 'PP', 'PP', '--', 'R8', 'R9', 'PP', 'PP', 'PP', '--', 'PP', 'R8', '--', 'H3', '--', '--', 'V8', 'PP', '--', '--', 'PP'],
            ['PP', 'PP', 'R8', 'PP', 'PP', 'V8', 'V8', '--', 'PP', 'R8', '--', '--', 'H8', 'H8', '--', '--', 'H8', 'R8', '--', 'PP', 'R8', 'PP', 'PP', 'R8', 'R8', 'PP', 'H8', '--', 'PP', 'PP'],
            ['PP', 'H8', 'PP', 'PP', 'PP', '--', 'R8', 'R8', 'H9', 'V8', 'H8', 'PP', 'PP', 'PP', '--', '--', 'PP', '--', '--', '--', 'PP', 'PP', 'PP', 'PP', 'H8', 'PP', '--', 'PP', '--', 'V8'],
            ['R4', 'H8', 'H8', '--', '--', 'V8', 'V8', 'R4', 'PP', 'V8', 'R8', '--', '--', 'PP', 'PP', '--', 'V8', 'R8', '--', 'PP', 'H8', '--', '--', '--', 'PP', 'R8', 'PP', '--', 'V8', 'V8'],
            ['--', 'PP', '--', '--', 'PP', 'V8', 'H8', '--', '--', 'V8', '--', 'PP', '--', 'H8', 'PP', 'R8', 'H8', '--', '--', 'PP', 'PP', '--', '--', 'PP', '--', '--', '--', 'V8', '--', 'PP'],
            ['PP', 'PP', 'PP', 'H8', 'H8', 'PP', '--', '--', '--', 'R1', '--', 'R8', 'PP', '--', 'V8', 'R8', '--', '--', 'H8', 'PP', 'R8', 'H8', '--', '--', 'V8', 'PP', 'PP', '--', 'PP', 'PP'],
            ['PP', 'H7', '--', '--', 'PP', 'V8', 'H8', '--', '--', 'PP', '--', 'PP', 'R8', '--', 'PP', 'V8', 'R8', '--', 'PP', 'R8', 'V8', 'V8', '--', 'PP', '--', 'H8', '--', 'H8', '--', 'H8'],
            ['PP', 'PP', 'H8', 'PP', 'V8', 'PP', 'V8', 'R8', '--', '--', 'R8', '--', 'PP', '--', '--', 'PP', '--', 'V8', '--', '--', 'R8', '--', 'PP', 'R8', 'H8', 'R8', '--', 'V8', 'PP', 'R8'],
            ['--', '--', 'PP', '--', '--', 'PP', '--', 'R8', 'H8', 'PP', 'PP', '--', 'PP', 'PP', '--', '--', '--', 'PP', 'V8', 'PP', 'PP', 'H4', 'R8', 'R8', '--', '--', 'PP', '--', '--', 'PP'],
            ['PP', '--', 'H8', 'PP', 'PP', 'V8', 'PP', 'PP', 'V8', '--', '--', 'H8', 'PP', '--', 'H8', 'V8', 'V8', '--', '--', 'V8', 'PP', '--', 'PP', 'PP', '--', 'V8', 'PP', 'PP', 'V8', '--'],
            ['R8', '--', 'V8', 'PP', 'H6', 'PP', '--', 'R8', 'R5', '--', 'PP', 'R8', 'V8', 'V8', '--', 'R8', 'R8', 'PP', 'H8', '--', 'R8', '--', '--', 'H8', '--', 'V8', 'H8', 'V8', 'PP', 'PP'],
            ['V6', 'V8', '--', 'PP', 'V4', 'R8', '--', '--', 'PP', '--', 'V8', 'H8', 'V8', 'PP', 'R8', 'H8', 'PP', '--', 'H8', 'PP', 'V8', '--', '--', 'PP', 'H8', 'PP', 'PP', 'V8', 'R8', '--'],
            ['PP', 'PP', 'PP', 'R8', '--', 'H8', 'PP', 'H1', 'V8', 'PP', 'PP', 'PP', '--', '--', '--', 'V7', '--', 'PP', '--', 'R8', '--', 'PP', '--', 'PP', '--', 'PP', 'R8', 'PP', 'R8', 'PP'],
            ['R8', 'PP', 'H8', '--', 'PP', 'PP', 'PP', 'H8', '--', 'H8', 'R8', 'PP', 'PP', 'PP', 'V8', 'PP', 'H8', 'V8', 'PP', 'V8', '--', '--', '--', 'PP', 'R8', '--', 'R8', 'R8', 'PP', '--'],
            ['PP', '--', 'PP', '--', 'R8', 'PP', 'H8', 'H8', 'PP', 'V8', 'R8', 'PP', 'PP', '--', 'V8', '--', 'PP', 'R9', '--', 'PP', 'H8', '--', 'PP', 'V8', '--', '--', 'H8', 'PP', 'R8', 'H8'],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 308)
        self.assertEqual(c_peones, 289)
        self.assertEqual(c_vacias, 303)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
