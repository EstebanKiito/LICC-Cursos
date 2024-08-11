import sys
import unittest
import copy

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestSolucionar_4x4_4x5(unittest.TestCase):

    def test_tablero_4x4_1(self):
        tablero_str = [
            ["V2", "--", "--", "H4"],
            ["--", "--", "--", "--"],
            ["--", "--", "R4", "--"],
            ["--", "--", "--", "--"],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
                ['V2', '--', '--', 'H4'],
                ['--', 'PP', 'PP', '--'],
                ['PP', '--', 'R4', 'PP'],
                ['--', 'PP', '--', 'PP']
            ],
            [
                ['V2', '--', '--', 'H4'],
                ['--', 'PP', 'PP', '--'],
                ['PP', '--', 'R4', 'PP'],
                ['--', 'PP', 'PP', '--']
            ]
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x4_2(self):
        tablero_str = [
            ['--', '--', '--', '--'],
            ['--', '--', '--', '--'],
            ['--', 'V3', 'R7', '--'],
            ['--', 'H4', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
                ['PP', 'PP', '--', '--'],
                ['--', '--', 'PP', '--'],
                ['PP', 'V3', 'R7', 'PP'],
                ['--', 'H4', '--', '--'],
            ],
            [
                ['PP', 'PP', '--', '--'],
                ['--', '--', 'PP', 'PP'],
                ['PP', 'V3', 'R7', '--'],
                ['--', 'H4', '--', '--'],
            ],
            [
                ['PP', 'PP', '--', 'PP'],
                ['--', '--', 'PP', '--'],
                ['PP', 'V3', 'R7', 'PP'],
                ['--', 'H4', '--', '--'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x4_3(self):
        tablero_str = [
            ['--', '--', '--', '--'],
            ['--', '--', '--', 'R3'],
            ['--', '--', '--', '--'],
            ['R8', '--', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['--', '--', 'PP', '--'],
            ['PP', 'PP', '--', 'R3'],
            ['--', '--', 'PP', 'PP'],
            ['R8', '--', '--', '--'],
            ],
            [
            ['--', '--', 'PP', 'PP'],
            ['--', 'PP', '--', 'R3'],
            ['--', '--', 'PP', '--'],
            ['R8', '--', '--', 'PP'],
            ],
            [
            ['PP', '--', '--', 'PP'],
            ['--', 'PP', '--', 'R3'],
            ['--', '--', 'PP', 'PP'],
            ['R8', '--', '--', '--'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x4_4(self):
        tablero_str = [
            ['--', 'R2', '--', '--'],
            ['--', 'R4', '--', '--'],
            ['--', '--', '--', '--'],
            ['--', '--', 'R4', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['PP', 'R2', 'PP', '--'],
            ['PP', 'R4', 'PP', '--'],
            ['--', 'PP', '--', '--'],
            ['PP', '--', 'R4', 'PP'],
            ],
            [
            ['PP', 'R2', 'PP', '--'],
            ['PP', 'R4', 'PP', '--'],
            ['--', 'PP', '--', 'PP'],
            ['--', '--', 'R4', 'PP'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x4_5(self):
        tablero_str = [
            ['--', '--', '--', '--'],
            ['--', '--', 'V3', '--'],
            ['H3', '--', 'R7', '--'],
            ['--', '--', '--', 'H3'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['--', '--', 'PP', '--'],
            ['--', 'PP', 'V3', 'PP'],
            ['H3', '--', 'R7', 'PP'],
            ['PP', '--', '--', 'H3'],
            ],
            [
            ['--', '--', 'PP', '--'],
            ['PP', 'PP', 'V3', 'PP'],
            ['H3', '--', 'R7', 'PP'],
            ['PP', '--', '--', 'H3'],
            ],
            [
            ['PP', '--', 'PP', '--'],
            ['--', 'PP', 'V3', 'PP'],
            ['H3', '--', 'R7', 'PP'],
            ['PP', '--', '--', 'H3'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x4_6(self):
        tablero_str = [
            ['--', 'R9', '--', '--'],
            ['V1', '--', '--', '--'],
            ['--', '--', '--', '--'],
            ['--', 'R9', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['PP', 'R9', '--', '--'],
            ['V1', '--', '--', '--'],
            ['PP', '--', '--', '--'],
            ['--', 'R9', '--', '--'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x5_1(self):
        tablero_str = [
            ['R8', '--', '--', '--', '--'],
            ['--', 'PP', 'V3', 'R9', 'PP'],
            ['--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', 'PP'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['R8', '--', '--', '--', '--'],
            ['--', 'PP', 'V3', 'R9', 'PP'],
            ['--', '--', '--', '--', '--'],
            ['--', 'PP', 'PP', '--', 'PP'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x5_2(self):
        tablero_str = [
            ['--', 'PP', '--', '--', '--'],
            ['--', '--', '--', '--', '--'],
            ['PP', '--', 'PP', 'R5', '--'],
            ['--', 'H5', '--', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['--', 'PP', '--', 'PP', '--'],
            ['--', '--', 'PP', '--', 'PP'],
            ['PP', '--', 'PP', 'R5', 'PP'],
            ['--', 'H5', '--', '--', '--'],
            ],
            [
            ['--', 'PP', '--', 'PP', '--'],
            ['PP', '--', 'PP', '--', 'PP'],
            ['PP', '--', 'PP', 'R5', 'PP'],
            ['--', 'H5', '--', '--', '--'],
            ],
            [
            ['PP', 'PP', '--', 'PP', '--'],
            ['--', '--', 'PP', '--', 'PP'],
            ['PP', '--', 'PP', 'R5', 'PP'],
            ['--', 'H5', '--', '--', '--'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x5_3(self):
        tablero_str = [
            ['--', '--', '--', '--', 'H4'],
            ['R4', 'PP', '--', '--', '--'],
            ['--', '--', '--', '--', '--'],
            ['--', '--', '--', 'H2', 'R2'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['PP', '--', '--', '--', 'H4'],
            ['R4', 'PP', '--', '--', '--'],
            ['--', '--', '--', 'PP', 'PP'],
            ['PP', '--', 'PP', 'H2', 'R2'],
            ],
            [
            ['PP', '--', '--', '--', 'H4'],
            ['R4', 'PP', '--', '--', '--'],
            ['--', 'PP', '--', 'PP', 'PP'],
            ['--', '--', 'PP', 'H2', 'R2'],
            ],
            [
            ['PP', '--', '--', '--', 'H4'],
            ['R4', 'PP', 'PP', '--', '--'],
            ['--', '--', '--', 'PP', 'PP'],
            ['PP', '--', 'PP', 'H2', 'R2'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x5_4(self):
        tablero_str = [
            ['PP', '--', '--', 'R6', 'R7'],
            ['--', 'V4', 'V3', '--', 'H4'],
            ['--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['PP', '--', 'PP', 'R6', 'R7'],
            ['PP', 'V4', 'V3', '--', 'H4'],
            ['--', '--', '--', 'PP', '--'],
            ['PP', '--', '--', '--', 'PP'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x5_5(self):
        tablero_str = [
            ['PP', '--', '--', '--', 'R8'],
            ['--', 'V4', 'V3', 'V4', '--'],
            ['--', '--', '--', '--', 'H5'],
            ['--', '--', 'V3', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['PP', '--', 'PP', '--', 'R8'],
            ['--', 'V4', 'V3', 'V4', '--'],
            ['--', '--', '--', '--', 'H5'],
            ['--', '--', 'V3', '--', '--'],
            ],
            [
            ['PP', '--', 'PP', '--', 'R8'],
            ['--', 'V4', 'V3', 'V4', '--'],
            ['--', '--', '--', '--', 'H5'],
            ['PP', '--', 'V3', '--', '--'],
            ],
            [
            ['PP', '--', 'PP', '--', 'R8'],
            ['PP', 'V4', 'V3', 'V4', '--'],
            ['--', '--', '--', '--', 'H5'],
            ['--', '--', 'V3', '--', '--'],
            ],
            [
            ['PP', '--', 'PP', '--', 'R8'],
            ['PP', 'V4', 'V3', 'V4', '--'],
            ['--', '--', '--', '--', 'H5'],
            ['PP', '--', 'V3', '--', '--'],
            ],
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x5_6(self):
        tablero_str = [
            ['H5', '--', '--', 'R9', '--'],
            ['--', '--', '--', '--', '--'],
            ['--', '--', 'R9', 'V4', 'R8'],
            ['V2', '--', '--', '--', '--'],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
            ['H5', '--', '--', 'R9', '--'],
            ['PP', '--', 'PP', '--', '--'],
            ['--', 'PP', 'R9', 'V4', 'R8'],
            ['V2', '--', 'PP', '--', 'PP'],
            ],
            [
            ['H5', '--', '--', 'R9', '--'],
            ['PP', '--', 'PP', '--', '--'],
            ['--', 'PP', 'R9', 'V4', 'R8'],
            ['V2', 'PP', '--', '--', 'PP'],
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
