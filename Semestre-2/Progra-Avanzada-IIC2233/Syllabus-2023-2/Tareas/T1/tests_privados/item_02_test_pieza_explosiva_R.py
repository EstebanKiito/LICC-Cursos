import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from pieza_explosiva import PiezaExplosiva


class TestVerificarAlcance_R(unittest.TestCase):
    # Pieza Reina

    N = 3
    coord = [7, 7]

    def test_pieza_R_celda_propia(self):
        pieza = PiezaExplosiva(self.N, "R", self.coord)
        respuesta = pieza.verificar_alcance(self.coord[0], self.coord[1])
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_R_celda_fuera_del_rango(self):
        pieza = PiezaExplosiva(4, "R", [1, 3])
        respuesta = pieza.verificar_alcance(0, 0)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_pieza_R_celdas_horizontales(self):
        pieza = PiezaExplosiva(self.N, "R", self.coord)

        # Verificar muchas posiciones validas
        for n in range(1, self.N * 2):
            respuesta_derecha = pieza.verificar_alcance(self.coord[0], self.coord[1] + n)
            self.assertIsInstance(respuesta_derecha, bool)
            self.assertTrue(respuesta_derecha)

            respuesta_izquierda = pieza.verificar_alcance(self.coord[0], self.coord[1] - n)
            self.assertIsInstance(respuesta_izquierda, bool)
            self.assertTrue(respuesta_izquierda)

    def test_pieza_R_celdas_verticales(self):
        pieza = PiezaExplosiva(self.N, "R", self.coord)

        # Verificar muchas posiciones validas
        for n in range(1, self.N * 2):
            respuesta_arriba = pieza.verificar_alcance(self.coord[0] - n, self.coord[1])
            self.assertIsInstance(respuesta_arriba, bool)
            self.assertTrue(respuesta_arriba)

            respuesta_abajo = pieza.verificar_alcance(self.coord[0] + n, self.coord[1])
            self.assertIsInstance(respuesta_abajo, bool)
            self.assertTrue(respuesta_abajo)

    def test_pieza_R_celdas_diagonales(self):
        pieza = PiezaExplosiva(self.N, "R", self.coord)

        # Verificar muchas posiciones invalidas
        for n in range(1, self.N * 2):
            respuesta_arriba_izq = pieza.verificar_alcance(self.coord[0] - n, self.coord[1] - n)
            self.assertIsInstance(respuesta_arriba_izq, bool)
            self.assertTrue(respuesta_arriba_izq)

            respuesta_arriba_der = pieza.verificar_alcance(self.coord[0] - n, self.coord[1] + n)
            self.assertIsInstance(respuesta_arriba_der, bool)
            self.assertTrue(respuesta_arriba_der)

            respuesta_abajo_der = pieza.verificar_alcance(self.coord[0] + n, self.coord[1] + n)
            self.assertIsInstance(respuesta_abajo_der, bool)
            self.assertTrue(respuesta_abajo_der)

            respuesta_abajo_izq = pieza.verificar_alcance(self.coord[0] + n, self.coord[1] - n)
            self.assertIsInstance(respuesta_abajo_izq, bool)
            self.assertTrue(respuesta_abajo_izq)

if __name__ == "__main__":
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stdout', new=StringIO()):
        unittest.main(verbosity=1)
