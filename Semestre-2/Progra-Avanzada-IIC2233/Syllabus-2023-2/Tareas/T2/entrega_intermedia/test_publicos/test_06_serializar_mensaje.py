import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_servidor import serializar_mensaje


class TestSerializarMensaje(unittest.TestCase):

    def test_0(self):
        mensaje = "Hola Mundo"
        respuesta = serializar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, b"Hola Mundo")

    def test_1(self):
        mensaje = "Hola Mundo\n"
        respuesta = serializar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, b"Hola Mundo\n")

    def test_2(self):
        mensaje = "Hola Mundo\nHola Mundo\nHola Mundo\n"
        respuesta = serializar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, b"Hola Mundo\nHola Mundo\nHola Mundo\n")

    def test_3(self):
        mensaje = ""
        respuesta = serializar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, b"")

    def test_4(self):
        mensaje = "Año nuevo, vida nueva"
        respuesta = serializar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, b"A\xc3\xb1o nuevo, vida nueva")

    def test_5(self):
        mensaje = "´+{}[]¨*!#$%&/()"
        respuesta = serializar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, b"\xc2\xb4+{}[]\xc2\xa8*!#$%&/()")

    def test_6(self):
        mensaje = "ñañeñiñdñrñtñchñhñlññ´´ññ´´ñ"
        respuesta = serializar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta,
                         b"\xc3\xb1a\xc3\xb1e\xc3\xb1i\xc3\xb1d\xc3\xb1r\xc3\xb1t\xc3"
                         b"\xb1ch\xc3\xb1h\xc3\xb1l\xc3\xb1\xc3\xb1\xc2\xb4\xc2\xb4\xc3"
                         b"\xb1\xc3\xb1\xc2\xb4\xc2\xb4\xc3\xb1")

    def test_7(self):
        mensaje = "{}´+[]¨*^`¨~'¿?¡\¸¨*^`¨~'¿?¡\¸|°¬!#$%&/()=|@·~½¬{[]}"
        respuesta = serializar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, b"{}\xc2\xb4+[]\xc2\xa8*^`\xc2\xa8~\'\xc2\xbf?"
                         b"\xc2\xa1\\\xc2\xb8\xc2\xa8*^`\xc2\xa8~\'\xc2\xbf?\xc2\xa1"
                         b"\\\xc2\xb8|\xc2\xb0\xc2\xac!#$%&/()=|@\xc2\xb7~\xc2\xbd\xc2\xac{[]}")

    def test_8(self):
        mensaje = "‡†ƒ€‰ŠŒŽ"
        respuesta = serializar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, b"\xe2\x80\xa1\xe2\x80\xa0\xc6\x92\xe2\x82\xac"
                         b"\xe2\x80\xb0\xc5\xa0\xc5\x92\xc5\xbd")

    def test_9(self):
        mensaje = "\t\n\r\v\f"
        respuesta = serializar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, b"\t\n\r\x0b\x0c")


if __name__ == "__main__":
    unittest.main(verbosity=2)
