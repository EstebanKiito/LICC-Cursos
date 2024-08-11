import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from pieza_explosiva import PiezaExplosiva


class TestVerificarAlcance_V_H(unittest.TestCase):
    # Pieza Horizontal
    def test_pieza_H_celda_propia(self):
        pieza = PiezaExplosiva(3, "H", [5, 5])
        respuesta = pieza.verificar_alcance(5, 5)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_H_celdas_horizontales(self):
        N = 3
        coord = [7, 7]
        pieza = PiezaExplosiva(N, "H", coord)

        # Verificar muchas posiciones válidas
        for n in range(1, N + 3):
            respuesta_derecha = pieza.verificar_alcance(coord[0], coord[1] + n)
            self.assertIsInstance(respuesta_derecha, bool)
            self.assertTrue(respuesta_derecha)

            respuesta_izquierda = pieza.verificar_alcance(coord[0], coord[1] - n)
            self.assertIsInstance(respuesta_izquierda, bool)
            self.assertTrue(respuesta_izquierda)

    def test_pieza_H_celdas_verticales(self):
        N = 3
        coord = [7, 7]
        pieza = PiezaExplosiva(N, "H", coord)

        # Verificar muchas posiciones invalidas
        for n in range(1, N + 3):
            respuesta_arriba = pieza.verificar_alcance(coord[0] - n, coord[1])
            self.assertIsInstance(respuesta_arriba, bool)
            self.assertFalse(respuesta_arriba)

            respuesta_abajo = pieza.verificar_alcance(coord[0] + n, coord[1])
            self.assertIsInstance(respuesta_abajo, bool)
            self.assertFalse(respuesta_abajo)

    def test_pieza_H_celdas_diagonales(self):
        N = 3
        pieza = PiezaExplosiva(N, "H", [5, 5])

        # Verificar muchas posiciones invalidas
        for n in range(1, N + 1):
            respuesta_arriba_izq = pieza.verificar_alcance(5 - n, 5 - n)
            self.assertIsInstance(respuesta_arriba_izq, bool)
            self.assertFalse(respuesta_arriba_izq)

            respuesta_arriba_der = pieza.verificar_alcance(5 - n, 5 + n)
            self.assertIsInstance(respuesta_arriba_der, bool)
            self.assertFalse(respuesta_arriba_der)

            respuesta_abajo_der = pieza.verificar_alcance(5 + n, 5 + n)
            self.assertIsInstance(respuesta_abajo_der, bool)
            self.assertFalse(respuesta_abajo_der)

            respuesta_abajo_izq = pieza.verificar_alcance(5 + n, 5 - n)
            self.assertIsInstance(respuesta_abajo_izq, bool)
            self.assertFalse(respuesta_abajo_izq)



    # Pieza Vertical
    def test_pieza_V_celda_propia(self):
        pieza = PiezaExplosiva(3, "V", [5, 5])
        respuesta = pieza.verificar_alcance(5, 5)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_V_celdas_verticales(self):
        N = 3
        coord = [7, 7]
        pieza = PiezaExplosiva(N, "V", coord)

        # Verificar muchas posiciones validas
        for n in range(1, N + 3):
            respuesta_arriba = pieza.verificar_alcance(coord[0] - n, coord[1])
            self.assertIsInstance(respuesta_arriba, bool)
            self.assertTrue(respuesta_arriba)

            respuesta_abajo = pieza.verificar_alcance(coord[0] + n, coord[1])
            self.assertIsInstance(respuesta_abajo, bool)
            self.assertTrue(respuesta_abajo)

    def test_pieza_V_celdas_horizontales(self):
        N = 3
        coord = [7, 7]
        pieza = PiezaExplosiva(N, "V", coord)

        # Verificar muchas posiciones invalidas
        for n in range(1, N + 1):
            respuesta_derecha = pieza.verificar_alcance(coord[0], coord[1] + n)
            self.assertIsInstance(respuesta_derecha, bool)
            self.assertFalse(respuesta_derecha)

            respuesta_izquierda = pieza.verificar_alcance(coord[0], coord[1] + n)
            self.assertIsInstance(respuesta_izquierda, bool)
            self.assertFalse(respuesta_izquierda)

    def test_pieza_V_celdas_diagonales(self):
        N = 3
        coord = [7, 7]
        pieza = PiezaExplosiva(N, "V", coord)

        # Verificar muchas posiciones invalidas
        for n in range(1, N + 1):
            respuesta_arriba_izq = pieza.verificar_alcance(coord[0] - n, coord[1] - n)
            self.assertIsInstance(respuesta_arriba_izq, bool)
            self.assertFalse(respuesta_arriba_izq)

            respuesta_arriba_der = pieza.verificar_alcance(coord[0] - n, coord[1] + n)
            self.assertIsInstance(respuesta_arriba_der, bool)
            self.assertFalse(respuesta_arriba_der)

            respuesta_abajo_der = pieza.verificar_alcance(coord[0] + n, coord[1] + n)
            self.assertIsInstance(respuesta_abajo_der, bool)
            self.assertFalse(respuesta_abajo_der)

            respuesta_abajo_izq = pieza.verificar_alcance(coord[0] + n, coord[1] - n)
            self.assertIsInstance(respuesta_abajo_izq, bool)
            self.assertFalse(respuesta_abajo_izq)




if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
