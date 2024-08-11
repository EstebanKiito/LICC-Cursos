import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_servidor import separar_mensaje


class TestSepararMensaje(unittest.TestCase):

    def test_0(self):
        mensaje = bytearray(b"Hola Mendo")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [bytearray(b'HMe'), bytearray(b'o n'), bytearray(b'lado')])

    def test_1(self):
        mensaje = bytearray(b"\xc2\xb4+{}[]\xc2\xa8*!#$%A/()")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(
            respuesta, [bytearray(b'\xc2[]#$)'), bytearray(b'\xb4}\xc2!%('), bytearray(b'+{\xa8*A/')])

    def test_2(self):
        mensaje = bytearray(b"A\xc3\xb1o nuevo, vada nueva")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(
            respuesta, [bytearray(b'Anu vnu'), bytearray(b'\xc3 e,a e'), bytearray(b'\xb1ovodava')])

    def test_3(self):
        mensaje = bytearray(b"\xc3\xb1e\xc3\xb1e\xc3\xb1i\xc3\xb1d\xc3\xb1r\xc3"
                            b"\xb1t\xc3\xb1ch\xc3\xb1h\xc3\xb1l\xc3\xb1\xc3\xb1"
                            b"\xc2\xb4\xc2\xb4\xc3\xb1\xc3\xb1\xc2\xb4\xc2\xb4\xc3\xb1")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\xc3e\xc3d\xc3t\xc3\xb1h\xb1\xc3\xb4\xc3\xb4\xc2'),
            bytearray(b'\xb1\xb1\xb1\xb1\xb1\xb1\xb1\xc3\xc3\xc3\xb1\xc2\xb1\xc2\xb4'),
            bytearray(b'e\xc3i\xc3r\xc3ch\xb1l\xc2\xb4\xc3\xb1\xc3\xb1')
        ])

    def test_4(self):
        mensaje = bytearray(
            b"{]\xc2\xb4+[]\xc2\xa8*^`\xc2\xa8~\'\xc2\xbf?\xc2\xa1\\\xc2\xb8\xc2"
            b"\xa8*^`\xc2\xa8~\'\xc2\xbf?\xc2\xa1\\\xc2\xb8|\xc2\xb0\xc2"
            b"\xac!#$%&/()=|@\xc2\xb7~\xc2\xbd\xc2\xac{[]}")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta,  [
            bytearray(b'{[]`\xc2\xbf?\xb8\xc2\xc2\xa8?\xc2|\xc2#$)=~\xc2[]'),
            bytearray(b']+\xc2^\xa8\xc2\xc2\xc2\xa8`~\xbf\xa1\xb8\xb0!%(|\xb7\xbd{}'),
            bytearray(b"\xc2\xb4\xa8*~\'\xa1\\*^\'\xc2\\\xc2\xc2\xac&/@\xc2\xc2\xac")
        ])

    def test_5(self):
        mensaje = bytearray(
            b"\xe2\x11\xa1\xe2\x80\xa0\xc6\x92\xe2\x82\xac\xe2\x80\xb0\xc5\xa0\xc5\x92\xc5\xbd")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\xe2\xa0\xc6\xe2\x80\x92\xc5'),
            bytearray(b'\x11\x80\x92\xac\xb0\xc5\xbd'),
            bytearray(b'\xa1\xe2\xe2\x82\xc5\xa0')
        ])

    def test_6(self):
        mensaje = bytearray(b"\n\t\r\x0b\x0c")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\n'),
            bytearray(b'\t\x0c'),
            bytearray(b'\r\x0b')
        ])

    def test_7(self):
        mensaje = bytearray(b"hola Mundo\nHola Mundo\nHola Mundo\n")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'hMuHounolnd'),
            bytearray(b'o n\nlMdHauo'),
            bytearray(b'ladoa o\n M\n')
        ])

    def test_8(self):
        mensaje = bytearray(b"a               c                g")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'a          '),
            bytearray(b'     c     '),
            bytearray(b'           g')
        ])

    def test_9(self):
        mensaje = bytearray(b"21 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 11")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'21 1 1 1 1 1 1 '),
            bytearray(b'1 1 1 1 1 1 1 11'),
            bytearray(b' 1 1 1 1 1 1 1 1')])


if __name__ == "__main__":
    unittest.main(verbosity=2)
