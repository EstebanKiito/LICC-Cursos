import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from pieza_explosiva import PiezaExplosiva


class TestVerificarAlcance(unittest.TestCase):
    # Pieza Horizontal
    def test_pieza_H_celda_propia(self):
        pieza = PiezaExplosiva(4, "H", [1, 3])
        respuesta = pieza.verificar_alcance(1, 3)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_H_celda_derecha(self):
        pieza = PiezaExplosiva(4, "H", [1, 3])
        respuesta = pieza.verificar_alcance(1, 9)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_H_celda_izquierda(self):
        pieza = PiezaExplosiva(4, "H", [1, 3])
        respuesta = pieza.verificar_alcance(1, 1)
        self.assertTrue(respuesta)

    def test_pieza_H_celda_arriba(self):
        pieza = PiezaExplosiva(4, "H", [1, 3])
        respuesta = pieza.verificar_alcance(0, 3)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_pieza_H_celda_abajo(self):
        pieza = PiezaExplosiva(4, "H", [1, 3])
        respuesta = pieza.verificar_alcance(4, 3)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_pieza_H_celda_diagonal(self):
        pieza = PiezaExplosiva(4, "H", [1, 3])
        respuesta = pieza.verificar_alcance(0, 2)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_pieza_H_celda_fuera_del_rango(self):
        pieza = PiezaExplosiva(4, "H", [1, 3])
        respuesta = pieza.verificar_alcance(0, 0)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    # Pieza Vertical
    def test_pieza_V_celda_propia(self):
        pieza = PiezaExplosiva(4, "V", [1, 3])
        respuesta = pieza.verificar_alcance(1, 3)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_V_celda_derecha(self):
        pieza = PiezaExplosiva(4, "V", [1, 3])
        respuesta = pieza.verificar_alcance(1, 9)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_pieza_V_celda_izquierda(self):
        pieza = PiezaExplosiva(4, "V", [1, 3])
        respuesta = pieza.verificar_alcance(1, 1)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_pieza_V_celda_arriba(self):
        pieza = PiezaExplosiva(4, "V", [1, 3])
        respuesta = pieza.verificar_alcance(0, 3)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_V_celda_abajo(self):
        pieza = PiezaExplosiva(4, "V", [1, 3])
        respuesta = pieza.verificar_alcance(4, 3)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_V_celda_diagonal(self):
        pieza = PiezaExplosiva(4, "V", [1, 3])
        respuesta = pieza.verificar_alcance(0, 2)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_pieza_V_celda_fuera_del_rango(self):
        pieza = PiezaExplosiva(4, "V", [1, 3])
        respuesta = pieza.verificar_alcance(0, 0)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_pieza_R_celda_propia(self):
        pieza = PiezaExplosiva(4, "R", [1, 3])
        respuesta = pieza.verificar_alcance(1, 3)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_R_celda_derecha(self):
        pieza = PiezaExplosiva(4, "R", [1, 3])
        respuesta = pieza.verificar_alcance(1, 9)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_R_celda_izquierda(self):
        pieza = PiezaExplosiva(4, "R", [1, 3])
        respuesta = pieza.verificar_alcance(1, 0)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_R_celda_arriba(self):
        pieza = PiezaExplosiva(4, "R", [1, 3])
        respuesta = pieza.verificar_alcance(0, 3)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_R_celda_abajo(self):
        pieza = PiezaExplosiva(4, "R", [1, 3])
        respuesta = pieza.verificar_alcance(4, 3)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_R_celda_diagonal_arriba_izquierda(self):
        pieza = PiezaExplosiva(4, "R", [1, 3])
        respuesta = pieza.verificar_alcance(0, 2)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_R_celda_diagonal_arriba_derecha(self):
        pieza = PiezaExplosiva(4, "R", [1, 3])
        respuesta = pieza.verificar_alcance(0, 4)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_R_celda_diagonal_abajo_izquierda(self):
        pieza = PiezaExplosiva(4, "R", [1, 3])
        respuesta = pieza.verificar_alcance(2, 2)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_R_celda_diagonal_abajo_derecha(self):
        pieza = PiezaExplosiva(4, "R", [1, 3])
        respuesta = pieza.verificar_alcance(2, 4)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_pieza_R_celda_fuera_del_rango(self):
        pieza = PiezaExplosiva(4, "R", [1, 3])
        respuesta = pieza.verificar_alcance(0, 0)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)




if __name__ == "__main__":
    unittest.main(verbosity=2)
