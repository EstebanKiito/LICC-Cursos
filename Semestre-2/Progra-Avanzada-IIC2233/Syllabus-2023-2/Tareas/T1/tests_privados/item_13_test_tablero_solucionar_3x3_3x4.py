import sys
import unittest
import copy

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestSolucionar_3x3_3x4(unittest.TestCase):

    def test_tablero_3x3_1(self):
        tablero_str = [
            ['R3', '--', '--'],
            ['--', '--', 'V1'],
            ['--', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['R3', '--', 'PP'],
            ['--', 'PP', 'V1'],
            ['PP', '--', 'PP'],
            ],
            [
            ['R3', '--', 'PP'],
            ['PP', '--', 'V1'],
            ['--', '--', 'PP'],
            ],
            [
            ['R3', '--', 'PP'],
            ['PP', '--', 'V1'],
            ['--', 'PP', 'PP'],
            ],
            [
            ['R3', '--', 'PP'],
            ['PP', '--', 'V1'],
            ['PP', '--', 'PP'],
            ],
            [
            ['R3', 'PP', 'PP'],
            ['--', '--', 'V1'],
            ['PP', '--', 'PP'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x3_2(self):
        tablero_str = [
            ['--', '--', 'V1'],
            ['R4', 'R5', '--'],
            ['--', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['--', 'PP', 'V1'],
            ['R4', 'R5', 'PP'],
            ['PP', '--', 'PP'],
            ],
            [
            ['PP', '--', 'V1'],
            ['R4', 'R5', 'PP'],
            ['PP', '--', 'PP'],
            ],
            [
            ['PP', 'PP', 'V1'],
            ['R4', 'R5', 'PP'],
            ['--', '--', 'PP'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x3_3(self):
        tablero_str = [
            ['H2', '--', '--'],
            ['--', '--', '--'],
            ['--', 'R4', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['H2', '--', 'PP'],
            ['--', 'PP', '--'],
            ['--', 'R4', 'PP'],
            ],
            [
            ['H2', '--', 'PP'],
            ['--', 'PP', '--'],
            ['PP', 'R4', '--'],
            ],
            [
            ['H2', '--', 'PP'],
            ['PP', '--', '--'],
            ['PP', 'R4', 'PP'],
            ],
            [
            ['H2', '--', 'PP'],
            ['PP', '--', 'PP'],
            ['PP', 'R4', '--'],
            ],
            [
            ['H2', '--', 'PP'],
            ['PP', 'PP', '--'],
            ['--', 'R4', '--'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x3_4(self):
        tablero_str = [
            ['R5', '--', '--'],
            ['--', 'R8', '--'],
            ['R7', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['R5', 'PP', '--'],
            ['--', 'R8', '--'],
            ['R7', '--', '--'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x3_5(self):
        tablero_str = [
            ['--', 'H3', 'R6'],
            ['--', '--', '--'],
            ['R6', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['--', 'H3', 'R6'],
            ['--', '--', '--'],
            ['R6', '--', 'PP'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x3_6(self):
        tablero_str = [
            ['--', '--', 'R7'],
            ['--', 'H2', '--'],
            ['--', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['--', '--', 'R7'],
            ['PP', 'H2', '--'],
            ['--', '--', '--'],
            ],
            [
            ['--', '--', 'R7'],
            ['PP', 'H2', '--'],
            ['--', 'PP', '--'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x4_1(self):
        tablero_str = [
            ["V2", "--", "--", "PP"],
            ["R3", "--", "--", "--"],
            ["--", "--", "H3", "--"],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
                ['V2', 'PP', '--', 'PP'],
                ['R3', 'PP', '--', '--'],
                ['PP', '--', 'H3', '--']
            ],
            [
                ['V2', 'PP', '--', 'PP'],
                ['R3', 'PP', '--', 'PP'],
                ['PP', '--', 'H3', '--']
            ]
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x4_2(self):
        tablero_str = [
            ['--', 'R4', '--', 'R2'],
            ['--', '--', '--', '--'],
            ['R4', '--', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['--', 'R4', 'PP', 'R2'],
            ['--', '--', 'PP', '--'],
            ['R4', 'PP', '--', 'PP'],
            ],
            [
            ['--', 'R4', 'PP', 'R2'],
            ['PP', '--', 'PP', '--'],
            ['R4', '--', '--', 'PP'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x4_3(self):
        tablero_str = [
            ['--', 'V2', '--', '--'],
            ['--', '--', 'R6', '--'],
            ['--', '--', 'R6', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['--', 'V2', '--', 'PP'],
            ['PP', '--', 'R6', '--'],
            ['--', 'PP', 'R6', 'PP'],
            ],
            [
            ['--', 'V2', '--', 'PP'],
            ['PP', '--', 'R6', 'PP'],
            ['--', 'PP', 'R6', '--'],
            ],
            [
            ['--', 'V2', 'PP', 'PP'],
            ['PP', '--', 'R6', '--'],
            ['--', 'PP', 'R6', '--'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x4_4(self):
        tablero_str = [
            ['--', '--', '--', '--'],
            ['--', '--', 'R8', '--'],
            ['--', 'V1', '--', 'R7'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['--', '--', '--', '--'],
            ['--', 'PP', 'R8', '--'],
            ['PP', 'V1', '--', 'R7'],
            ],
            [
            ['PP', '--', '--', '--'],
            ['--', 'PP', 'R8', '--'],
            ['PP', 'V1', '--', 'R7'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x4_5(self):
        tablero_str = [
            ['--', '--', 'R3', '--'],
            ['V3', '--', '--', '--'],
            ['--', '--', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['--', 'PP', 'R3', '--'],
            ['V3', 'PP', '--', 'PP'],
            ['--', '--', 'PP', '--'],
            ],
            [
            ['--', 'PP', 'R3', 'PP'],
            ['V3', 'PP', '--', '--'],
            ['--', '--', 'PP', '--'],
            ],
            [
            ['--', 'PP', 'R3', 'PP'],
            ['V3', 'PP', '--', '--'],
            ['--', '--', 'PP', 'PP'],
            ],
            [
            ['--', 'PP', 'R3', 'PP'],
            ['V3', 'PP', '--', 'PP'],
            ['--', '--', '--', '--'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x4_6(self):
        tablero_str = [
            ['V2', '--', 'PP', '--'],
            ['--', '--', '--', '--'],
            ['--', 'V1', 'PP', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['V2', '--', 'PP', '--'],
            ['--', 'PP', '--', '--'],
            ['PP', 'V1', 'PP', '--'],
            ],
            [
            ['V2', '--', 'PP', '--'],
            ['--', 'PP', '--', '--'],
            ['PP', 'V1', 'PP', 'PP'],
            ],
            [
            ['V2', '--', 'PP', '--'],
            ['--', 'PP', '--', 'PP'],
            ['PP', 'V1', 'PP', '--'],
            ],
            [
            ['V2', '--', 'PP', 'PP'],
            ['--', 'PP', '--', '--'],
            ['PP', 'V1', 'PP', '--'],
            ],
            [
            ['V2', '--', 'PP', 'PP'],
            ['--', 'PP', '--', '--'],
            ['PP', 'V1', 'PP', 'PP'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)


if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
