import sys
import unittest
import copy

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from tablero import Tablero


class TestSolucionar(unittest.TestCase):
    # Ejemplo básico
    def test_tablero_vacio(self):
        tablero_str = [["--"]]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [[["--"]], [["PP"]]]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_solucion_unica(self):
        tablero_str = [["--", "H1"], ["V1", "H2"]]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [["PP", "H1"], ["V1", "H2"]])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_sin_solucion(self):
        tablero_str = [["--", "--"], ["--", "V3"]]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x4(self):
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
            ["PP", "PP", "V4", "--"],
            ["V3", "--", "--", "--"],
            ["--", "--", "H3", "--"],
            ["R8", "--", "--", "PP"],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
                ['PP', 'PP', 'V4', '--'],
                ['V3', '--', '--', '--'],
                ['--', '--', 'H3', 'PP'],
                ['R8', '--', '--', 'PP']
            ]
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_4x4_solo_H_V(self):
        tablero_str = [
            ["V2", "--", "--", "H4"],
            ["--", "--", "PP", "--"],
            ["--", "PP", "--", "--"],
            ["--", "H4", "--", "--"],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
                ['V2', '--', '--', 'H4'],
                ['--', '--', 'PP', '--'],
                ['PP', 'PP', '--', '--'],
                ['--', 'H4', '--', '--']
            ],
            [
                ['V2', '--', '--', 'H4'],
                ['--', '--', 'PP', '--'],
                ['PP', 'PP', '--', 'PP'],
                ['--', 'H4', '--', '--']
            ], 
            [
                ['V2', '--', '--', 'H4'],
                ['--', '--', 'PP', 'PP'],
                ['PP', 'PP', '--', '--'],
                ['--', 'H4', '--', '--']
            ]
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x4(self):
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

    def test_tablero_3x3_sin_solucion(self):
        tablero_str = [
            ["--", "--", "--"],
            ["--", "R3", "--"],
            ["--", "--", "V2"],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_3x3(self):
        tablero_str = [
            ["PP", "--", "--"],
            ["--", "H3", "--"],
            ["--", "PP", "V2"],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
                ['PP', '--', 'PP'],
                ['--', 'H3', '--'],
                ['--', 'PP', 'V2']
            ],
            [
                ['PP', '--', 'PP'],
                ['--', 'H3', '--'],
                ['PP', 'PP', 'V2']
            ]
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_2x3(self):
        tablero_str = [
            ["--", "V2"],
            ["R3", "--"],
            ["--", "--"],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
                ['PP', 'V2'],
                ['R3', '--'],
                ['PP', 'PP']
            ]
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_2x3_sin_solucion(self):
        tablero_str = [
            ["--", "V2"],
            ["H1", "--"],
            ["--", "--"],
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertListEqual(respuesta, [])
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)

    def test_tablero_2x2(self):
        tablero_str = [
            ["R2", "--"],
            ["--", "--"]
        ]
        tablero = Tablero(copy.deepcopy(tablero_str))
        respuesta = tablero.solucionar()
        opciones_validas = [
            [
                ['R2', '--'],
                ['PP', 'PP']
            ],
            [
                ['R2', 'PP'],
                ['--', 'PP']
            ],
            [
                ['R2', 'PP'],
                ['PP', '--']
            ]
        ]
        # Verificar formato y respuesta
        self.assertIsInstance(respuesta, list)
        self.assertIn(respuesta, opciones_validas)
        # Verificar que no modificó el original
        self.assertListEqual(tablero.tablero, tablero_str)
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
