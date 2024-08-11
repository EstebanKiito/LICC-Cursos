import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_servidor import codificar_mensaje


class TestCodificarMensaje(unittest.TestCase):

    def test_0(self):
        mensaje = bytearray(b"La vida es lo que pasa mientras haces otros planes.")
        respuesta = codificar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for i in respuesta:
            self.assertIsInstance(i, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\x00\x00\x003'),
            bytearray(b'\x00\x00\x00\x01'),
            bytearray(b'La vida es lo que pasa mientras hace'),
            bytearray(b'\x00\x00\x00\x02'),
            bytearray(b's otros planes.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                      b'\x00\x00\x00\x00\x00\x00\x00\x00')])

    def test_1(self):
        mensaje = bytearray(b"El conocimiento es el poder.\n")
        respuesta = codificar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for i in respuesta:
            self.assertIsInstance(i, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\x00\x00\x00\x1d'),
            bytearray(b'\x00\x00\x00\x01'),
            bytearray(b'El conocimiento es el poder.\n\x00\x00\x00\x00\x00\x00\x00')])

    def test_2(self):
        mensaje = bytearray(b"Nunca es tarde para ser lo que podr\xc3\xadas haber\nsido.")
        respuesta = codificar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for i in respuesta:
            self.assertIsInstance(i, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\x00\x00\x003'),
            bytearray(b'\x00\x00\x00\x01'),
            bytearray(b'Nunca es tarde para ser lo que podr\xc3'),
            bytearray(b'\x00\x00\x00\x02'),
            bytearray(b'\xadas haber\nsido.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                      b'\x00\x00\x00\x00\x00\x00\x00\x00')])

    def test_3(self):
        mensaje = bytearray(b"        ")
        respuesta = codificar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for i in respuesta:
            self.assertIsInstance(i, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\x00\x00\x00\x08'),
            bytearray(b'\x00\x00\x00\x01'),
            bytearray(b'        \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                      b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')])

    def test_4(self):
        mensaje = bytearray(
            b"La \xc3\xbaltima reuni\xc3\xb3n ser\xc3\xa1 en el rinc\xc3\xb3n "
            b"m\xc3\xa1s \xc3\xadntimo del jard\xc3\xadn.")
        respuesta = codificar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for i in respuesta:
            self.assertIsInstance(i, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\x00\x00\x00A'),
            bytearray(b'\x00\x00\x00\x01'),
            bytearray(b'La \xc3\xbaltima reuni\xc3\xb3n ser\xc3\xa1 en el rinc'),
            bytearray(b'\x00\x00\x00\x02'),
            bytearray(b'\xc3\xb3n m\xc3\xa1s \xc3\xadntimo del jard\xc3\xadn.'
                      b'\x00\x00\x00\x00\x00\x00\x00')])

    def test_5(self):
        mensaje = bytearray(
            b"\xd8\xa7\xd9\x84\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85 \xd8"
            b"\xb9\xd9\x84\xd9\x8a\xd9\x83\xd9\x85")
        respuesta = codificar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for i in respuesta:
            self.assertIsInstance(i, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\x00\x00\x00\x17'),
            bytearray(b'\x00\x00\x00\x01'),
            bytearray(b'\xd8\xa7\xd9\x84\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85 \xd8\xb9'
                      b'\xd9\x84\xd9\x8a\xd9\x83\xd9\x85\x00\x00\x00\x00\x00\x00'
                      b'\x00\x00\x00\x00\x00\x00\x00')])

    def test_6(self):
        mensaje = bytearray(
            b"\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xb1\xcf\x82! \xce\x9a\xce"
            b"\xb1\xce\xbb\xce\xb7\xce\xbc\xce\xad\xcf\x81\xce\xb1 \xce\xb1\xcf\x80"
            b"\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xcf\x8c\xce\xbc\xce\xbf\xcf\x81\xcf"
            b"\x86\xce\xb7 \xce\x91\xce\xb8\xce\xae\xce\xbd\xce\xb1.")
        respuesta = codificar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for i in respuesta:
            self.assertIsInstance(i, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\x00\x00\x00H'),
            bytearray(b'\x00\x00\x00\x01'),
            bytearray(b'\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xb1\xcf\x82! \xce\x9a\xce'
                      b'\xb1\xce\xbb\xce\xb7\xce\xbc\xce\xad\xcf\x81\xce\xb1 \xce\xb1'),
            bytearray(b'\x00\x00\x00\x02'),
            bytearray(b'\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xcf\x8c\xce\xbc\xce\xbf\xcf'
                      b'\x81\xcf\x86\xce\xb7 \xce\x91\xce\xb8\xce\xae\xce\xbd\xce\xb1.')])

    def test_7(self):
        mensaje = bytearray(
            b"\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xe3"
            b"\x80\x81\xe6\x9d\xb1\xe4\xba\xac\xe3\x81\x8b\xe3\x82\x89\xe3\x81"
            b"\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xef\xbc\x81")
        respuesta = codificar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for i in respuesta:
            self.assertIsInstance(i, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\x00\x00\x000'),
            bytearray(b'\x00\x00\x00\x01'),
            bytearray(b'\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xe3\x80\x81'
                      b'\xe6\x9d\xb1\xe4\xba\xac\xe3\x81\x8b\xe3\x82\x89\xe3\x81\x93\xe3\x82\x93'),
            bytearray(b'\x00\x00\x00\x02'),
            bytearray(b'\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xef\xbc\x81\x00\x00\x00\x00\x00\x00'
                      b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')])

    def test_8(self):
        mensaje = bytearray(b"\xc3\x9cber den Wolken schweben die V\xc3\xb6gel.")
        respuesta = codificar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for i in respuesta:
            self.assertIsInstance(i, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\x00\x00\x00%'),
            bytearray(b'\x00\x00\x00\x01'),
            bytearray(b'\xc3\x9cber den Wolken schweben die V\xc3\xb6gel'),
            bytearray(b'\x00\x00\x00\x02'),
            bytearray(b'.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                      b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')])

    def test_9(self):
        mensaje = bytearray(
            b"\xd0\x97\xd0\xb4\xd1\x80\xd0\xb0\xd0\xb2\xd1\x81\xd1\x82\xd0"
            b"\xb2\xd1\x83\xd0\xb9\xd1\x82\xd0\xb5, \xd0\xba\xd0\xb0\xd0\xba \xd0\xb2"
            b"\xd1\x8b \xd1\x81\xd0\xb5\xd0\xb3\xd0\xbe\xd0\xb4\xd0\xbd\xd1\x8f?")
        respuesta = codificar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for i in respuesta:
            self.assertIsInstance(i, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\x00\x00\x005'),
            bytearray(b'\x00\x00\x00\x01'),
            bytearray(b'\xd0\x97\xd0\xb4\xd1\x80\xd0\xb0\xd0\xb2\xd1\x81\xd1\x82\xd0\xb2\xd1\x83'
                      b'\xd0\xb9\xd1\x82\xd0\xb5, \xd0\xba\xd0\xb0\xd0\xba \xd0\xb2\xd1'),
            bytearray(b'\x00\x00\x00\x02'),
            bytearray(b'\x8b \xd1\x81\xd0\xb5\xd0\xb3\xd0\xbe\xd0\xb4\xd0\xbd\xd1\x8f?\x00\x00'
                      b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')])


if __name__ == "__main__":
    unittest.main(verbosity=2)
