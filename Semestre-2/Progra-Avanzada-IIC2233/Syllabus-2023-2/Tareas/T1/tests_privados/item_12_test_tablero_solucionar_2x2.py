import sys
import unittest
import copy

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestSolucionar_2x2(unittest.TestCase):

    def test_tablero_solucion_unica_1(self):
        tablero_str = [
            ["V1", "H2"],
            ["--", "H1"]
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [
            ["V1", "H2"],
            ["PP", "H1"]
        ])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_solucion_unica_2(self):
        tablero_str = [
            ['--', 'V2'],
            ['--', 'R2'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [
            ['PP', 'V2'],
            ['PP', 'R2'],
        ])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_multiples_soluciones_1(self):
        tablero_str = [
            ['--', 'PP'],
            ['--', 'V1'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, [
        [
            ['--', 'PP'],
            ['--', 'V1'],
        ],
        [
            ['--', 'PP'],
            ['PP', 'V1'],
        ],
        [
            ['PP', 'PP'],
            ['--', 'V1'],
        ],
        ])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_multiples_soluciones_2(self):
        tablero_str = [
            ['--', '--'],
            ['--', 'R2']
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, [
        [
            ['--', 'PP'],
            ['PP', 'R2']
        ],
        [
            ['PP', '--'],
            ['PP', 'R2']
        ],
        [
            ['PP', 'PP'],
            ['--', 'R2']
        ],
        ])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
