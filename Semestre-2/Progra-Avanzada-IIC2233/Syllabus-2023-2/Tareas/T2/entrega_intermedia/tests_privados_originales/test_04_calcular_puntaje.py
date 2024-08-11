import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_cliente import calcular_puntaje


class TestCalcularPuntaje(unittest.TestCase):

    def test_0(self):
        tiempo = 10
        vidas = 4
        cantidad_lobos = 2
        PUNTAJE_LOBO = 3
        puntaje = calcular_puntaje(tiempo, vidas, cantidad_lobos, PUNTAJE_LOBO)
        self.assertIsInstance(puntaje, float)
        self.assertEqual(puntaje, 6.67)

    def test_1(self):
        tiempo = 27
        vidas = 2
        cantidad_lobos = 4
        PUNTAJE_LOBO = 3
        puntaje = calcular_puntaje(tiempo, vidas, cantidad_lobos, PUNTAJE_LOBO)
        self.assertIsInstance(puntaje, float)
        self.assertEqual(puntaje, 4.50)

    def test_2(self):
        tiempo = 34
        vidas = 1
        cantidad_lobos = 6
        PUNTAJE_LOBO = 3
        puntaje = calcular_puntaje(tiempo, vidas, cantidad_lobos, PUNTAJE_LOBO)
        self.assertIsInstance(puntaje, float)
        self.assertEqual(puntaje, 1.89)

    def test_3(self):
        tiempo = 41
        vidas = 5
        cantidad_lobos = 7
        PUNTAJE_LOBO = 3
        puntaje = calcular_puntaje(tiempo, vidas, cantidad_lobos, PUNTAJE_LOBO)
        self.assertIsInstance(puntaje, float)
        self.assertEqual(puntaje, 9.76)

    def test_4(self):
        tiempo = 44
        vidas = 3
        cantidad_lobos = 0
        PUNTAJE_LOBO = 3
        puntaje = calcular_puntaje(tiempo, vidas, cantidad_lobos, PUNTAJE_LOBO)
        self.assertIsInstance(puntaje, float)
        self.assertEqual(puntaje, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)