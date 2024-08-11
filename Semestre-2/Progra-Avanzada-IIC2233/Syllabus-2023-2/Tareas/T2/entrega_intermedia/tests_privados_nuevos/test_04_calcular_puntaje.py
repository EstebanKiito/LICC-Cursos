import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_cliente import calcular_puntaje


class TestCalcularPuntaje(unittest.TestCase):

    def test_0(self):
        tiempo = 17
        vidas = 0
        cantidad_lobos = 1
        PUNTAJE_LOBO = 3
        puntaje = calcular_puntaje(tiempo, vidas, cantidad_lobos, PUNTAJE_LOBO)
        self.assertIsInstance(puntaje, float)
        self.assertEqual(puntaje, 0)

    def test_1(self):
        tiempo = 34
        vidas = 3
        cantidad_lobos = 8
        PUNTAJE_LOBO = 3
        puntaje = calcular_puntaje(tiempo, vidas, cantidad_lobos, PUNTAJE_LOBO)
        self.assertIsInstance(puntaje, float)
        self.assertEqual(puntaje, 4.25)

    def test_2(self):
        tiempo = 14
        vidas = 6
        cantidad_lobos = 10
        PUNTAJE_LOBO = 3
        puntaje = calcular_puntaje(tiempo, vidas, cantidad_lobos, PUNTAJE_LOBO)
        self.assertIsInstance(puntaje, float)
        self.assertEqual(puntaje, 2.80)

    def test_3(self):
        tiempo = 11
        vidas = 3
        cantidad_lobos = 11
        PUNTAJE_LOBO = 3
        puntaje = calcular_puntaje(tiempo, vidas, cantidad_lobos, PUNTAJE_LOBO)
        self.assertIsInstance(puntaje, float)
        self.assertEqual(puntaje, 1.00)

    def test_4(self):
        tiempo = 11
        vidas = 5
        cantidad_lobos = 0
        PUNTAJE_LOBO = 3
        puntaje = calcular_puntaje(tiempo, vidas, cantidad_lobos, PUNTAJE_LOBO)
        self.assertIsInstance(puntaje, float)
        self.assertEqual(puntaje, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)