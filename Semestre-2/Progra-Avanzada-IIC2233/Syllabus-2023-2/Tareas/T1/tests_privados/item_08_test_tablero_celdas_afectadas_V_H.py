import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestCeldasAfectadas(unittest.TestCase):
    # Ejemplo básico
    def test_2x2_posicion_invalida_vacia(self):
        tablero_str = [
            ["--", "--"],
            ["H1", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(0, 1)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, -1)

    def test_2x2_posicion_invalida_peon(self):
        tablero_str = [
            ["PP", "--"],
            ["--", "H1"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(0, 0)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, -1)

    def test__2x2_alcance_1_sin_peon(self):
        tablero_str = [
            ["--", "--"],
            ["H1", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(1, 0)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 2)

    def test_2x2_alcance_2_sin_peon(self):
        tablero_str = [
            ["--", "--"],
            ["H3", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(1, 0)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 2)

    def test_2x2_alcance_1_con_peon(self):
        tablero_str = [
            ["--", "--"],
            ["H3", "PP"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(1, 0)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 1)

    def test_3x3_alcance_1_sin_peon(self):
        tablero_str = [
            ["--", "H3", "--"],
            ["--", "--", "--"],
            ["--", "--", "V2"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(0, 1)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 3)

    def test_3x3_alcance_2_sin_peon(self):
        tablero_str = [
            ["--", "H3", "--"],
            ["--", "--", "--"],
            ["--", "--", "V2"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(2, 2)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 3)

    def test_3x3_alcance_1_con_peon(self):
        tablero_str = [
            ["--", "H3", "--"],
            ["--", "--", "V2"],
            ["--", "--", "PP"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(1, 2)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 2)

    def test_5x5_alcance_5_sin_peon(self):
        tablero_str = [
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ["H5", "H5", "H5", "H5", "H5"],
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(2, 2)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 5)

    def test_5x5_alcance_3_con_peon(self):
        tablero_str = [
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ["PP", "H5", "H5", "H5", "PP"],
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.celdas_afectadas(2, 2)
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 3)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
