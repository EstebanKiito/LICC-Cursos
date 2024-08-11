import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestDesglose(unittest.TestCase):
    # Ejemplo básico
    def test_tablero_vacio(self):
        tablero_str = [["--", "--"], ["--", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 0)
        self.assertEqual(c_peones, 0)
        self.assertEqual(c_vacias, 4)

    def test_tablero_solo_peones(self):
        tablero_str = [["PP", "PP"], ["PP", "PP"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 0)
        self.assertEqual(c_peones, 4)
        self.assertEqual(c_vacias, 0)

    def test_tablero_solo_piezas_explosivas(self):
        tablero_str = [["H2", "V1"], ["R3", "V1"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 4)
        self.assertEqual(c_peones, 0)
        self.assertEqual(c_vacias, 0)

    def test_tablero_ejemplo_enunciado(self):
        tablero_str = [["V2", "PP", "--"], ["H1", "--", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 2)
        self.assertEqual(c_peones, 1)
        self.assertEqual(c_vacias, 3)

    def test_tablero_5x5(self):
        tablero_str = [
            ["--", "--", "--", "--", "R4"],
            ["PP", "H4", "PP", "H4", "--"],
            ["--", "PP", "--", "--", "PP"],
            ["--", "PP", "V1", "PP", "R4"],
            ["PP", "--", "--", "R3", "--"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 6)
        self.assertEqual(c_peones, 7)
        self.assertEqual(c_vacias, 12)

    def test_tablero_6x6(self):
        tablero_str = [
            ["--", "--", "--", "--", "R4", "--"],
            ["--", "PP", "V1", "PP", "--", "--"],
            ["--", "--", "--", "--", "PP", "--"],
            ["PP", "--", "PP", "H4", "--", "PP"],
            ["PP", "V4", "--", "--", "--", "V7"],
            ["--", "--", "R5", "--", "--", "PP"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 6)
        self.assertEqual(c_peones, 8)
        self.assertEqual(c_vacias, 22)

    def test_tablero_10x10(self):
        tablero_str = [
            ["--", "--", "--", "PP", "--", "--", "--", "PP", "--", "R5"],
            ["--", "V4", "PP", "--", "--", "PP", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "R8", "PP", "PP"],
            ["H6", "PP", "--", "V5", "--", "--", "V5", "--", "--", "--"],
            ["--", "--", "--", "--", "PP", "--", "--", "--", "--", "--"],
            ["--", "--", "PP", "--", "--", "--", "--", "PP", "H1", "--"],
            ["--", "PP", "--", "--", "--", "PP", "--", "--", "--", "--"],
            ["PP", "--", "R1", "--", "--", "--", "H2", "PP", "--", "PP"],
            ["--", "PP", "PP", "--", "H2", "--", "--", "--", "--", "V4"],
            ["H3", "--", "--", "--", "PP", "--", "--", "PP", "--", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.desglose
        # Verificar formato respuesta
        self.assertIsInstance(respuesta, list)
        self.assertEqual(len(respuesta), 3)

        # Verificar respuesta
        c_piezas_exp, c_peones, c_vacias = respuesta
        self.assertEqual(c_piezas_exp, 12)
        self.assertEqual(c_peones, 19)
        self.assertEqual(c_vacias, 69)


if __name__ == "__main__":
    unittest.main(verbosity=2)
