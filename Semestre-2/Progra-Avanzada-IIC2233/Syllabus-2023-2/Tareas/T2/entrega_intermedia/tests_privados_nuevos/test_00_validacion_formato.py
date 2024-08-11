import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_cliente import validacion_formato


class TestValidacionFormato(unittest.TestCase):

    def test_0(self):
        nombre = "jergemunoz"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_1(self):
        nombre = "nombregenerico20000"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_2(self):
        nombre = "Gtruen"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_3(self):
        nombre = "#e"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_4(self):
        nombre = "gato chice"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_5(self):
        nombre = "pacalain100"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_6(self):
        nombre = "@HerneV"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_7(self):
        nombre = "Lily426"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_8(self):
        nombre = "Gewgyw1"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_9(self):
        nombre = "Gatohhico1"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)


if __name__ == "__main__":
    unittest.main(verbosity=2)
