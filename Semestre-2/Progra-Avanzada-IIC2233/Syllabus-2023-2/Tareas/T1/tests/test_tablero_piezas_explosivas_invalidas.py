import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestPiezasExplosivasInvalidas(unittest.TestCase):
    # Ejemplo básico
    def test_tablero_vacio(self):
        tablero_str = [["--", "--"], ["--", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_tablero_solo_piezas_validas(self):
        tablero_str = [["H1", "--"], ["--", "V1"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_tablero_un_pieza_invalida(self):
        tablero_str = [["H9", "--"], ["--", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 1)

    def test_ejemplo_enunciado(self):
        tablero_str = [["H3", "V3", "PP"], ["R6", "PP", "R5"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 2)

    def test_9x9_1_pieza_invalida(self):
        tablero_str = [
            ["--", "--", "--", "--", "--", "--", "--", "--", "PP"],
            ["--", "PP", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "H1", "--", "PP", "--", "--", "PP", "--"],
            ["--", "--", "--", "--", "--", "--", "V3", "--", "--"],
            ["--", "PP", "--", "--", "R25", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "H3", "--"],
            ["--", "H2", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["PP", "--", "--", "V5", "--", "PP", "--", "--", "V10"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 1)

    def test_9x9_2_piezas_invalida(self):
        tablero_str = [
            ["PP", "--", "--", "--", "--", "PP", "--", "--", "--"],
            ["--", "--", "--", "--", "H3", "--", "--", "H3", "--"],
            ["--", "V3", "--", "PP", "--", "--", "PP", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "PP", "--", "R60", "--", "--", "--", "--"],
            ["--", "PP", "--", "--", "--", "PP", "--", "--", "--"],
            ["--", "--", "H3", "--", "--", "--", "--", "--", "PP"],
            ["--", "--", "--", "--", "--", "--", "H14", "PP", "--"],
            ["V4", "PP", "--", "PP", "--", "--", "--", "V3", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 2)

    def test_9x9_5_piezas_invalidas(self):
        tablero_str = [
            ["--", "PP", "PP", "PP", "PP", "PP", "--", "--", "V9"],
            ["--", "--", "PP", "--", "PP", "--", "--", "--", "--"],
            ["H14", "--", "--", "--", "--", "--", "--", "V11", "--"],
            ["--", "--", "R3", "--", "--", "--", "--", "--", "--"],
            ["--", "PP", "--", "--", "R25", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "H13", "PP", "--", "--", "--", "--", "V15", "--"],
            ["--", "--", "--", "--", "PP", "PP", "V7", "--", "--"],
            ["H9", "PP", "--", "R60", "--", "--", "PP", "PP", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 5)

    def test_9x9_10_piezas_invalidas(self):
        tablero_str = [
            ["--", "--", "--", "V10", "--", "--", "--", "--", "V11"],
            ["--", "R4", "--", "--", "--", "V7", "PP", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "R60", "--"],
            ["H14", "--", "R10", "--", "PP", "--", "--", "--", "--"],
            ["--", "--", "--", "PP", "R60", "V10", "PP", "--", "--"],
            ["--", "R60", "--", "--", "--", "--", "--", "--", "H4"],
            ["--", "--", "--", "--", "PP", "--", "--", "R20", "--"],
            ["--", "PP", "H2", "--", "--", "PP", "V14", "--", "--"],
            ["H12", "--", "--", "H13", "--", "--", "--", "PP", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 10)

    def test_2x15_0_piezas(self):
        tablero_str = [
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_2x15_2_piezas_invalidas(self):
        tablero_str = [
            ["--", "PP", "--", "--", "--", "--", "H3", "--", "PP", "--", "PP", "--", "H20", "--", "--"],
            ["V4", "--", "--", "PP", "PP", "--", "V2", "--", "PP", "PP", "PP", "PP", "--", "PP", "R15"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 2)

    def test_2x15_4_piezas_invalidas(self):
        tablero_str = [
            ["--", "V3", "--", "--", "--", "--", "V3", "--", "--", "--", "V3", "--", "H15", "--", "PP"],
            ["H4", "PP", "--", "--", "--", "PP", "H11", "PP", "--", "--", "--", "--", "--", "PP", "R20"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 4)

    def test_10x3_0_piezas_invalidas(self):
        tablero_str = [
            ["--", "V1", "--"],
            ["--", "--", "PP"],
            ["PP", "H1", "V1"],
            ["H1", "--", "--"],
            ["--", "R1", "PP"],
            ["--", "--", "H1"],
            ["V1", "--", "V1"],
            ["--", "H1", "--"],
            ["PP", "--", "--"],
            ["V1", "V1", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_10x3_31_piezas_invalidas(self):
        tablero_str = [
            ["H3", "H4", "H3"],
            ["H3", "H4", "H3"],
            ["H3", "H4", "H3"],
            ["H3", "H4", "H3"],
            ["H3", "H4", "H3"],
            ["H3", "H4", "H3"],
            ["H3", "H4", "H3"],
            ["H3", "H4", "H3"],
            ["H3", "H4", "H3"],
            ["H3", "H4", "H3"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 10)

    def test_10x3_30_piezas_invalidas(self):
        tablero_str = [
            ["H4", "H4", "H4"],
            ["H4", "H4", "H4"],
            ["H4", "H4", "H4"],
            ["H4", "H4", "H4"],
            ["H4", "H4", "H4"],
            ["H4", "H4", "H4"],
            ["H4", "H4", "H4"],
            ["H4", "H4", "H4"],
            ["H4", "H4", "H4"],
            ["H4", "H4", "H4"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 30)

    def test_15x1_1_piezas_invalidas(self):
        tablero_str = [
            ["PP"],
            ["PP"],
            ["PP"],
            ["PP"],
            ["PP"],
            ["PP"],
            ["PP"],
            ["R16"],
            ["PP"],
            ["PP"],
            ["PP"],
            ["PP"],
            ["PP"],
            ["PP"],
            ["PP"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.piezas_explosivas_invalidas
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
