import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_servidor import usuario_permitido


class TestUsuarioPermitido(unittest.TestCase):

    def test_no_permitido_0(self):
        nombre = "Alice"
        lista = ["Bob", "Charlie", "David", "Alice"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_1(self):
        nombre = "Eva"
        lista = ["Bob", "Charlie", "David", "Eva"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_2(self):
        nombre = "John"
        lista = ["Bob", "Charlie", "David", "John"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_3(self):
        nombre = "Mike"
        lista = ["Bob", "Charlie", "David", "Mike"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_no_permitido_4(self):
        nombre = "Sarah"
        lista = ["Sarah"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_permitido_0(self):
        nombre = "Bob"
        lista = ["Charlie", "David"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_1(self):
        nombre = "David"
        lista = ["Bob", "Charlie"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_2(self):
        nombre = "Alice"
        lista = []
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_3(self):
        nombre = "Eve"
        lista = ["Bob", "Charlie", "David"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_permitido_4(self):
        nombre = "Charlie"
        lista = ["Bob", "David"]
        respuesta = usuario_permitido(nombre, lista)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)


if __name__ == "__main__":
    unittest.main(verbosity=2)
