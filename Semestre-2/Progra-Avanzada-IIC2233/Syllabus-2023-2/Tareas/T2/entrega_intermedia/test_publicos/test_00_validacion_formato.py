import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_cliente import validacion_formato


class TestValidacionFormato(unittest.TestCase):

    def test_0(self):
        nombre = "jorgemunoz"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_1(self):
        nombre = "nombregenerico10000"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_2(self):
        nombre = "Gtruan"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_3(self):
        nombre = "#a"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_4(self):
        nombre = "gato chico"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_5(self):
        nombre = "pacalein100"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_6(self):
        nombre = "@HernyV"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertFalse(respuesta)

    def test_7(self):
        nombre = "Lily416"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_8(self):
        nombre = "Gewwyw1"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)

    def test_9(self):
        nombre = "Gatochico1"
        respuesta = validacion_formato(nombre)
        self.assertIsInstance(respuesta, bool)
        self.assertTrue(respuesta)


if __name__ == "__main__":
    unittest.main(verbosity=2)
