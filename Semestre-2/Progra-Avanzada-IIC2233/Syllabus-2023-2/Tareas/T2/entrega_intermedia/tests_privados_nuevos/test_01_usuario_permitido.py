import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_servidor import usuario_permitido


class TestUsuarioPermitido(unittest.TestCase):

    def test_no_permitido_0(self):
        nombre = "jorgimunoz"
        lista = ["jorgimunoz"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_1(self):
        nombre = "nombregenerico20000"
        lista = ["nombregenerico20000", "jorgimunoz"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_2(self):
        nombre = "Gtrean"
        lista = ["Gtrean", "sheren_cattan"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_3(self):
        nombre = "#e"
        lista = ["#e", "evol_gato"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_4(self):
        nombre = "gate chico"
        lista = ["gate chico", "#e"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_permitido_0(self):
        nombre = "pacalain100"
        lista = ["@HernqV", "Lilq416"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_1(self):
        nombre = "@HernqV"
        lista = []
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_2(self):
        nombre = "Lily426"
        lista = ["Lily42623"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_3(self):
        nombre = "Gewwya1"
        lista = ["Gewwya10", "Lily41623"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_4(self):
        nombre = "Gatoyhico1"
        lista = ["Gewwww10", "Lily41623"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)


if __name__ == "__main__":
    unittest.main(verbosity=2)
