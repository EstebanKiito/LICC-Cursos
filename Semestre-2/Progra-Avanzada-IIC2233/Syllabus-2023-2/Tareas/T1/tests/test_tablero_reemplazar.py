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
        tablero_str = [["--", "--", "--"], ["--", "--", "--"], ["--", "--", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.reemplazar("test_1")
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)
        # Verificar formato y respuesta
        self.assertListEqual(tablero.dimensiones, [2, 2])
        self.assertListEqual(tablero.tablero, [["R2","--"],["PP","PP"]])
    
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

    def test_tablero_solo_peones(self):
        tablero_str = [["--", "PP"], ["PP", "--"], ["--", "PP"], ["PP", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.reemplazar("test_2")
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)
        # Verificar formato y respuesta
        self.assertListEqual(tablero.dimensiones, [2, 3])
        self.assertListEqual(tablero.tablero, [["--","--","PP"],["PP","--","--"]])

    def test_tablero_grande(self):
        tablero_str = [["--", "PP", "--", "H3", "--"], ["PP", "V5", "--", "PP", "--"]]
        tablero = Tablero(tablero_str)
        respuesta = tablero.reemplazar("test_3")
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)
        # Verificar formato y respuesta
        self.assertListEqual(tablero.dimensiones, [6, 4])
        self.assertListEqual(tablero.tablero, [
            ['--', 'R3', 'PP', '--'],
            ['H2', '--', 'PP', 'V5'],
            ['--', 'PP', '--', 'V2'],
            ['R7', '--', 'PP', '--'],
            ['PP', '--', '--', 'R3'],
            ['PP', 'PP', 'H4', '--']
        ])


if __name__ == "__main__":
    unittest.main(verbosity=2)
