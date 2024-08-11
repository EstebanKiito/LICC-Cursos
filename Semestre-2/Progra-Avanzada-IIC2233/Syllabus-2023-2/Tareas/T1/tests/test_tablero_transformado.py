import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero
from pieza_explosiva import PiezaExplosiva


class TestTableroTransformado(unittest.TestCase):
    # Ejemplo básico
    def test_tablero_vacio(self):
        tablero_str = [["--", "--"], ["--", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.tablero_transformado
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, tablero_str)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)


    def test_tablero_vacio_y_peon(self):
        tablero_str = [["--", "PP"], ["--", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.tablero_transformado
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, tablero_str)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_una_pieza_explosiva(self):
        tablero_str = [["--", "PP"], ["--", "R8"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.tablero_transformado
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        # Testear posiciones
        self.assertEqual(respuesta[0][0], "--")
        self.assertEqual(respuesta[0][1], "PP")
        self.assertEqual(respuesta[1][0], "--")
        self.assertIsInstance(respuesta[1][1], PiezaExplosiva)
        respuesta_esperada = PiezaExplosiva(8, "R", [1, 1])
        self.assertEqual(respuesta[1][1].__dict__, respuesta_esperada.__dict__)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x3(self):
        tablero_str = [
            ["V3", "--","PP"],
            ["--", "PP","--"],
            ["H2", "--","R5"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.tablero_transformado
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        # Testear posición al azar
        self.assertEqual(respuesta[0][1], "--")
        self.assertEqual(respuesta[0][2], "PP")
        self.assertEqual(respuesta[2][1], "--")
        self.assertIsInstance(respuesta[0][0], PiezaExplosiva)
        self.assertEqual(respuesta[0][0].__dict__, PiezaExplosiva(3, "V", [0, 0]).__dict__)
        self.assertIsInstance(respuesta[2][0], PiezaExplosiva)
        self.assertEqual(respuesta[2][0].__dict__, PiezaExplosiva(2, "H", [2, 0]).__dict__)
        self.assertIsInstance(respuesta[2][2], PiezaExplosiva)
        self.assertEqual(respuesta[2][2].__dict__, PiezaExplosiva(5, "R", [2, 2]).__dict__)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x2(self):
        tablero_str = [
            ["H2", "--"],
            ["V2", "PP"],
            ["PP", "R1"],
            ["R5", "--"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.tablero_transformado
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        # Testear posición al azar
        self.assertEqual(respuesta[0][1], "--")
        self.assertEqual(respuesta[1][1], "PP")
        self.assertEqual(respuesta[2][0], "PP")
        self.assertIsInstance(respuesta[0][0], PiezaExplosiva)
        self.assertEqual(respuesta[0][0].__dict__, PiezaExplosiva(2, "H", [0, 0]).__dict__)
        self.assertIsInstance(respuesta[1][0], PiezaExplosiva)
        self.assertEqual(respuesta[1][0].__dict__, PiezaExplosiva(2, "V", [1, 0]).__dict__)
        self.assertIsInstance(respuesta[2][1], PiezaExplosiva)
        self.assertEqual(respuesta[2][1].__dict__, PiezaExplosiva(1, "R", [2, 1]).__dict__)
        self.assertIsInstance(respuesta[3][0], PiezaExplosiva)
        self.assertEqual(respuesta[3][0].__dict__, PiezaExplosiva(5, "R", [3, 0]).__dict__)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)


if __name__ == "__main__":
    unittest.main(verbosity=2)
