import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_servidor import separar_mensaje


class TestSepararMensaje(unittest.TestCase):

    def test_0(self):
        mensaje = bytearray(b"La vida es lo que pasa mientras haces otros planes.")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'Ldalo pmiasesosne'),
            bytearray(b'ai   ea er c r as'),
            bytearray(b' vesqusanthaotpl.')
        ])

    def test_1(self):
        mensaje = bytearray(b"El conocimiento es el poder.\n")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(
            respuesta, [
                bytearray(b'Enoens od'),
                bytearray(b'lociteepe\n'),
                bytearray(b' cimo l r.')
            ])

    def test_2(self):
        mensaje = bytearray(b"Nunca es tarde para ser lo que podr\xc3\xadas haber\nsido.")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(
            respuesta, [
                bytearray(b'N erdra le \xc3\xadabid'),
                bytearray(b'uasaea roupraheso'),
                bytearray(b'nc t pse qods r\n.')
            ])

    def test_3(self):
        mensaje = bytearray(b"        ")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [bytearray(b'   '), bytearray(b'   '), bytearray(b'  ')])

    def test_4(self):
        mensaje = bytearray(
            b"La \xc3\xbaltima reuni\xc3\xb3n ser\xc3\xa1 en el rinc\xc3\xb3n "
            b"m\xc3\xa1s \xc3\xadntimo del jard\xc3\xadn.")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'Lltre\xb3n\xc3\xa1elc\xc3\xc3\xa1ntderd'),
            bytearray(b'a\xbai u\xc3 r   n\xb3ms\xadi la\xc3.'),
            bytearray(b' \xc3maniseenrin  \xc3mo j\xadn')
        ])

    def test_5(self):
        mensaje = bytearray(
            b"\xd8\xa7\xd9\x84\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85 \xd8"
            b"\xb9\xd9\x84\xd9\x8a\xd9\x83\xd9\x85")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\xd8\xb3\xd9\x85 \xd9\x8a'),
            bytearray(b'\xa7\xd8\x84\xd9\xd8\x84\xd9\x85'),
            bytearray(b'\xd9\x84\xd8\xa7\xb9\xd9\x83\xd9')
        ])

    def test_6(self):
        mensaje = bytearray(
            b"\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xb1\xcf\x82! \xce\x9a\xce"
            b"\xb1\xce\xbb\xce\xb7\xce\xbc\xce\xad\xcf\x81\xce\xb1 \xce\xb1\xcf\x80"
            b"\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xcf\x8c\xce\xbc\xce\xbf\xcf\x81\xcf"
            b"\x86\xce\xb7 \xce\x91\xce\xb8\xce\xae\xce\xbd\xce\xb1.")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\xce\xb9\xce\xce\xb1\xce\x9a\xce\xb7\xcf\x81\xb1\xcf\xcf\x84 \xcf\xbf'
            b'\xcf\xb7 \xce\xae.'),
            bytearray(b'\x93\xce\xac\x83\xcf \xce\xbb\xce\xad\xce\xce\x80 \xce\xbd\x8c\xce\x81'
            b'\xce\xce\xb8\xce\xb1'),
            bytearray(b'\xce\xb5 \xcf\x82!\xb1\xce\xbc\xce\xb1 \xcf\x8c\xb7\xce\xce\xbc\xcf\x86'
            b'\x91\xce\xbd\xce')
        ])

    def test_7(self):
        mensaje = bytearray(
            b"\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xe3"
            b"\x80\x81\xe6\x9d\xb1\xe4\xba\xac\xe3\x81\x8b\xe3\x82\x89\xe3\x81"
            b"\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xef\xbc\x81")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\xe3\x93\xe3\xa1\xe3\x81\xe6\xac\xe3\x89\xe3\x93\xe3\xa1\xe3\x81'),
            bytearray(b'\x81\x82\x81\x81\x81\x80\x9d\xba\x81\x82\x81\x82\x81\x81\x81\xbc'),
            bytearray(b'\x93\xe3\xab\xe3\xaf\xe3\xb1\xe4\x8b\xe3\x93\xe3\xab\xe3\xaf\xef')
        ])

    def test_8(self):
        mensaje = bytearray(b"\xc3\x9cber den Wolken schweben die V\xc3\xb6gel.")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\xc3 dolscen Vl.'),
            bytearray(b'\x9creWk hb e\xc3e'),
            bytearray(b'ben enwedi\xb6g')
        ])

    def test_9(self):
        mensaje = bytearray(
            b"\xd0\x97\xd0\xb4\xd1\x80\xd0\xb0\xd0\xb2\xd1\x81\xd1\x82\xd0"
            b"\xb2\xd1\x83\xd0\xb9\xd1\x82\xd0\xb5, \xd0\xba\xd0\xb0\xd0\xba \xd0\xb2"
            b"\xd1\x8b \xd1\x81\xd0\xb5\xd0\xb3\xd0\xbe\xd0\xb4\xd0\xbd\xd1\x8f?")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            bytearray(b'\xd0\x80\xd0\x81\xd1\x83\xd0\xb5,\xb0\xd0\xd1\x8b\xb5\xd0\xb4\xd0'),
            bytearray(b'\x97\xd1\xb0\xd1\x82\xd1\xb9\xd0 \xd0\xba\xb2 \xd0\xb3\xd0\xbd?'),
            bytearray(b'\xd0\xb4\xd0\xb2\xd0\xb2\xd1\x82\xd0\xba \xd0\xd1\x81\xd0\xbe\xd1\x8f')
        ])


if __name__ == "__main__":
    unittest.main(verbosity=2)
