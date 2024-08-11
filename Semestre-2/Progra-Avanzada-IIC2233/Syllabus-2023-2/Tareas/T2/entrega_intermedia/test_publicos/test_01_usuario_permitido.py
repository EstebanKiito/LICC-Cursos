import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_servidor import usuario_permitido


class TestUsuarioPermitido(unittest.TestCase):

    def test_no_permitido_0(self):
        nombre = "jorgemunoz"
        lista = ["jorgemunoz"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_1(self):
        nombre = "nombregenerico10000"
        lista = ["nombregenerico10000", "jorgemunoz"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_2(self):
        nombre = "Gtruan"
        lista = ["Gtruan", "sherin_cattan"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_3(self):
        nombre = "#a"
        lista = ["#a", "evil_gato"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_4(self):
        nombre = "gato chico"
        lista = ["gato chico", "#a"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_permitido_0(self):
        nombre = "pacalein100"
        lista = ["@HernyV", "Lily416"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_1(self):
        nombre = "@HernyV"
        lista = []
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_2(self):
        nombre = "Lily416"
        lista = ["Lily41623"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_3(self):
        nombre = "Gewwyw1"
        lista = ["Gewwyw10", "Lily41623"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_4(self):
        nombre = "Gatochico1"
        lista = ["Gewwyw10", "Lily41623"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)


if __name__ == "__main__":
    unittest.main(verbosity=2)
