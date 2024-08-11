import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_cliente import validacion_formato


class TestValidacionFormato(unittest.TestCase):

    def test_0(self):
        nombre = "a"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_1(self):
        nombre = "Juanito"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_2(self):
        nombre = "Juanito 123"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_3(self):
        nombre = "1234567890l"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_4(self):
        nombre = "Abcdefghijklmnopqrstuvwxyz"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_5(self):
        nombre = "name12345"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_6(self):
        nombre = "@JohnDoe@123"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_7(self):
        nombre = "John123Doe"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_8(self):
        nombre = "A1B2C3"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_9(self):
        nombre = "ValidName123"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)


if __name__ == "__main__":
    unittest.main(verbosity=2)
