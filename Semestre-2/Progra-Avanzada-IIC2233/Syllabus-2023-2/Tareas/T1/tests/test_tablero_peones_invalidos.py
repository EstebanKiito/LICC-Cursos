import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestPeonesInvalidos(unittest.TestCase):
    # Ejemplo básico
    def test_tablero_vacio(self):
        tablero_str = [["--", "--"], ["--", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.peones_invalidos
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_solo_peones_validos(self):
        tablero_str = [["PP", "--"], ["--", "PP"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.peones_invalidos
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)

    def test_ejemplo_enunciado(self):
        tablero_str = [["PP", "PP", "PP"], ["PP", "--", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.peones_invalidos
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 2)

    def test_solo_peones_invalidos(self):
        tablero_str = [["PP", "PP"], ["PP", "PP"], ["--", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.peones_invalidos
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 4)

    def test_con_piezas_explosivas(self):
        tablero_str = [
            ["PP", "--", "R4"],
            ["--", "H2", "PP"],
            ["V2", "PP", "PP"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.peones_invalidos
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 1)

    def test_esquinas(self):
        tablero_str = [
            ["PP", "--", "--", "--", "PP", "PP"],
            ["--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--"],
            ["PP", "--", "--", "--", "--", "PP"],
            ["PP", "PP", "--", "--", "--", "PP"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.peones_invalidos
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 1)

    def test_bordes(self):
        tablero_str = [
            ["--", "PP", "PP", "--"],
            ["--", "--", "--", "PP"],
            ["PP", "--", "--", "PP"],
            ["--", "--", "--", "PP"],
            ["--", "--", "PP", "--"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.peones_invalidos
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 1)
        
    def test_5x4(self):
        tablero_str = [
            ["PP", "PP", "--", "PP"],
            ["--", "R3", "PP", "--"],
            ["PP", "PP", "PP", "PP"],
            ["PP", "V2", "PP", "--"],
            ["--", "H3", "--", "PP"]
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.peones_invalidos
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 3)

    def test_2x4(self):
        tablero_str = [
            ["PP", "--", "PP", "--"],
            ["PP", "V2", "--", "PP"],
        ]
        tablero = Tablero(tablero_str)
        respuesta = tablero.peones_invalidos
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, int)
        self.assertEqual(respuesta, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
