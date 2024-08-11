import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestLimpiar(unittest.TestCase):
    # Ejemplo básico
    def test_con_un_peon(self):
        tablero_str = [["--", "--"], ["--", "PP"]]
        tablero = Tablero(tablero_str)
        tablero.limpiar()
        # Verificar formato y respuesta
        self.assertIsInstance(tablero.tablero, list)
        self.assertListEqual(tablero.tablero, [["--", "--"], ["--", "--"]])

    def test_4x4_1(self):
        tablero_str = [
            ["PP", "V1", "PP", "H1"],
            ["V1", "PP", "H1", "PP"],
            ["PP", "V1", "PP", "H1"],
            ["V1", "PP", "H1", "PP"],
        ]
        tablero = Tablero(tablero_str)
        tablero.limpiar()
        # Verificar formato y respuesta
        self.assertIsInstance(tablero.tablero, list)
        self.assertListEqual(tablero.tablero, [
            ["--", "V1", "--", "H1"],
            ["V1", "--", "H1", "--"],
            ["--", "V1", "--", "H1"],
            ["V1", "--", "H1", "--"],
            ])

    def test_4x4_2(self):
        tablero_str = [
            ["PP", "--", "--", "PP"],
            ["--", "H2", "PP", "R2"],
            ["V2", "PP", "H1", "--"],
            ["--", "--", "V3", "--"],
        ]
        tablero = Tablero(tablero_str)
        tablero.limpiar()
        # Verificar formato y respuesta
        self.assertIsInstance(tablero.tablero, list)
        self.assertListEqual(tablero.tablero, [
            ["--", "--", "--", "--"],
            ["--", "H2", "--", "R2"],
            ["V2", "--", "H1", "--"],
            ["--", "--", "V3", "--"],
            ])

    def test_5x5_lleno(self):
        tablero_str = [
            ["PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP"],
        ]
        tablero = Tablero(tablero_str)
        tablero.limpiar()
        # Verificar formato y respuesta
        self.assertIsInstance(tablero.tablero, list)
        self.assertListEqual(tablero.tablero, [
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ])

    def test_10x10_lleno_peones(self):
        tablero_str = [
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
        ]
        tablero = Tablero(tablero_str)
        tablero.limpiar()
        # Verificar formato y respuesta
        self.assertIsInstance(tablero.tablero, list)
        self.assertListEqual(tablero.tablero, [
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ])

    def test_10x10_lleno(self):
        tablero_str = [
            ["PP", "V4", "PP", "PP", "PP", "H2", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "V4", "PP", "PP", "PP", "R5", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "V4", "PP", "V4", "PP", "PP"],
            ["PP", "H2", "R5", "PP", "PP", "PP", "H2", "PP", "PP", "R5"],
            ["PP", "PP", "PP", "PP", "V4", "PP", "PP", "PP", "PP", "PP"],
            ["V4", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP", "PP"],
            ["PP", "PP", "PP", "H2", "PP", "PP", "R5", "PP", "V4", "PP"],
            ["PP", "H2", "PP", "PP", "R5", "PP", "PP", "PP", "H2", "PP"],
            ["PP", "PP", "PP", "PP", "PP", "PP", "PP", "R5", "PP", "PP"],
            ["R5", "PP", "V4", "PP", "PP", "V4", "H2", "PP", "PP", "PP"],
        ]
        tablero = Tablero(tablero_str)
        tablero.limpiar()
        # Verificar formato y respuesta
        self.assertIsInstance(tablero.tablero, list)
        self.assertListEqual(tablero.tablero, [
            ["--", "V4", "--", "--", "--", "H2", "--", "--", "--", "--"],
            ["--", "--", "V4", "--", "--", "--", "R5", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "V4", "--", "V4", "--", "--"],
            ["--", "H2", "R5", "--", "--", "--", "H2", "--", "--", "R5"],
            ["--", "--", "--", "--", "V4", "--", "--", "--", "--", "--"],
            ["V4", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "H2", "--", "--", "R5", "--", "V4", "--"],
            ["--", "H2", "--", "--", "R5", "--", "--", "--", "H2", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "R5", "--", "--"],
            ["R5", "--", "V4", "--", "--", "V4", "H2", "--", "--", "--"],
            ])


if __name__ == "__main__":
    unittest.main(verbosity=2)
