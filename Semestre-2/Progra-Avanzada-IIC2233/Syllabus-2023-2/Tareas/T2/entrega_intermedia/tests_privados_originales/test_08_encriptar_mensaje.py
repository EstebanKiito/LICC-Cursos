import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_servidor import encriptar_mensaje


class TestEncriptarMensaje(unittest.TestCase):

    def test_0(self):
        mensaje = bytearray(b"La vida es lo que pasa mientras haces otros planes.")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        opciones_validas = [
            bytearray(b'\x00ai   ea er c r asLdalo pmiasesosne vesqusanthaotpl.'),
            bytearray(b'0ai   ea er c r asLdalo pmiasesosne vesqusanthaotpl.'),
        ]
        self.assertIn(respuesta, opciones_validas)

    def test_1(self):
        mensaje = bytearray(b"El conocimiento es el poder.\n")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        opciones_validas = [
            bytearray(b'\x00lociteepe\nEnoens od cimo l r.'),
            bytearray(b'0lociteepe\nEnoens od cimo l r.'),
        ]
        self.assertIn(respuesta, opciones_validas)

    def test_2(self):
        mensaje = bytearray(b"Nunca es tarde para ser lo que podr\xc3\xadas haber\nsido.")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        opciones_validas = [
            bytearray(b'\x00uasaea rouprahesoN erdra le \xc3\xadabidnc t pse qods r\n.'),
            bytearray(b'0uasaea rouprahesoN erdra le \xc3\xadabidnc t pse qods r\n.'),
        ]
        self.assertIn(respuesta, opciones_validas)

    def test_3(self):
        mensaje = bytearray(b"        ")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        opciones_validas = [
            bytearray(b'\x01        '),
            bytearray(b'1        '),
        ]
        self.assertIn(respuesta, opciones_validas)

    def test_4(self):
        mensaje = bytearray(
            b"La \xc3\xbaltima reuni\xc3\xb3n ser\xc3\xa1 en el rinc\xc3\xb3n "
            b"m\xc3\xa1s \xc3\xadntimo del jard\xc3\xadn.")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        opciones_validas = [
            bytearray(b'\x01Lltre\xb3n\xc3\xa1elc\xc3\xc3\xa1ntderd \xc3maniseenrin  '
                      b'\xc3mo j\xadna\xbai u\xc3 r   n\xb3ms\xadi la\xc3.'),
            bytearray(b'1Lltre\xb3n\xc3\xa1elc\xc3\xc3\xa1ntderd \xc3maniseenrin  '
                      b'\xc3mo j\xadna\xbai u\xc3 r   n\xb3ms\xadi la\xc3.'),
        ]
        self.assertIn(respuesta, opciones_validas)

    def test_5(self):
        mensaje = bytearray(
            b"\xd8\xa7\xd9\x84\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85 \xd8"
            b"\xb9\xd9\x84\xd9\x8a\xd9\x83\xd9\x85")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        opciones_validas = [
            bytearray(b'\x01\xd8\xb3\xd9\x85 \xd9\x8a\xd9\x84\xd8\xa7\xb9\xd9\x83\xd9\xa7'
            b'\xd8\x84\xd9\xd8\x84\xd9\x85'),
            bytearray(b'1\xd8\xb3\xd9\x85 \xd9\x8a\xd9\x84\xd8\xa7\xb9\xd9\x83\xd9\xa7\xd8'
            b'\x84\xd9\xd8\x84\xd9\x85'),
        ]
        self.assertIn(respuesta, opciones_validas)

    def test_6(self):
        mensaje = bytearray(
            b"\xce\x93\xce\xb5\xce\xb9\xce\xac \xcf\x83\xce\xb1\xcf\x82! \xce\x9a\xce"
            b"\xb1\xce\xbb\xce\xb7\xce\xbc\xce\xad\xcf\x81\xce\xb1 \xce\xb1\xcf\x80"
            b"\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xcf\x8c\xce\xbc\xce\xbf\xcf\x81\xcf"
            b"\x86\xce\xb7 \xce\x91\xce\xb8\xce\xae\xce\xbd\xce\xb1.")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        opciones_validas = [
            bytearray(b'\x00\x93\xce\xac\x83\xcf \xce\xbb\xce\xad\xce\xce\x80 \xce\xbd\x8c\xce'
                      b'\x81\xce\xce\xb8\xce\xb1\xce\xb9\xce\xce\xb1\xce\x9a\xce\xb7\xcf\x81\xb1'
                      b'\xcf\xcf\x84 \xcf\xbf\xcf\xb7 \xce\xae.\xce\xb5 \xcf\x82!\xb1\xce\xbc\xce'
                      b'\xb1 \xcf\x8c\xb7\xce\xce\xbc\xcf\x86\x91\xce\xbd\xce'),
            bytearray(b'0\x93\xce\xac\x83\xcf \xce\xbb\xce\xad\xce\xce\x80 \xce\xbd\x8c\xce'
                      b'\x81\xce\xce\xb8\xce\xb1\xce\xb9\xce\xce\xb1\xce\x9a\xce\xb7\xcf\x81\xb1'
                      b'\xcf\xcf\x84 \xcf\xbf\xcf\xb7 \xce\xae.\xce\xb5 \xcf\x82!\xb1\xce\xbc\xce'
                      b'\xb1 \xcf\x8c\xb7\xce\xce\xbc\xcf\x86\x91\xce\xbd\xce'),
        ]
        self.assertIn(respuesta, opciones_validas)

    def test_7(self):
        mensaje = bytearray(
            b"\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xe3"
            b"\x80\x81\xe6\x9d\xb1\xe4\xba\xac\xe3\x81\x8b\xe3\x82\x89\xe3\x81"
            b"\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xef\xbc\x81")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        opciones_validas = [
            bytearray(b'\x01\xe3\x93\xe3\xa1\xe3\x81\xe6\xac\xe3\x89\xe3\x93\xe3\xa1\xe3\x81\x93'
                      b'\xe3\xab\xe3\xaf\xe3\xb1\xe4\x8b\xe3\x93\xe3\xab\xe3\xaf\xef\x81\x82\x81'
                      b'\x81\x81\x80\x9d\xba\x81\x82\x81\x82\x81\x81\x81\xbc'),
            bytearray(b'1\xe3\x93\xe3\xa1\xe3\x81\xe6\xac\xe3\x89\xe3\x93\xe3\xa1\xe3\x81\x93'
                      b'\xe3\xab\xe3\xaf\xe3\xb1\xe4\x8b\xe3\x93\xe3\xab\xe3\xaf\xef\x81\x82\x81'
                      b'\x81\x81\x80\x9d\xba\x81\x82\x81\x82\x81\x81\x81\xbc'),
        ]
        self.assertIn(respuesta, opciones_validas)

    def test_8(self):
        mensaje = bytearray(b"\xc3\x9cber den Wolken schweben die V\xc3\xb6gel.")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        opciones_validas = [
            bytearray(b'\x01\xc3 dolscen Vl.ben enwedi\xb6g\x9creWk hb e\xc3e'),
            bytearray(b'1\xc3 dolscen Vl.ben enwedi\xb6g\x9creWk hb e\xc3e'),
        ]
        self.assertIn(respuesta, opciones_validas)

    def test_9(self):
        mensaje = bytearray(
            b"\xd0\x97\xd0\xb4\xd1\x80\xd0\xb0\xd0\xb2\xd1\x81\xd1\x82\xd0"
            b"\xb2\xd1\x83\xd0\xb9\xd1\x82\xd0\xb5, \xd0\xba\xd0\xb0\xd0\xba \xd0\xb2"
            b"\xd1\x8b \xd1\x81\xd0\xb5\xd0\xb3\xd0\xbe\xd0\xb4\xd0\xbd\xd1\x8f?")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        opciones_validas = [
            bytearray(b'\x00\x97\xd1\xb0\xd1\x82\xd1\xb9\xd0 \xd0\xba\xb2 \xd0\xb3\xd0\xbd?\xd0'
                      b'\x80\xd0\x81\xd1\x83\xd0\xb5,\xb0\xd0\xd1\x8b\xb5\xd0\xb4\xd0\xd0\xb4\xd0'
                      b'\xb2\xd0\xb2\xd1\x82\xd0\xba \xd0\xd1\x81\xd0\xbe\xd1\x8f'),
            bytearray(b'0\x97\xd1\xb0\xd1\x82\xd1\xb9\xd0 \xd0\xba\xb2 \xd0\xb3\xd0\xbd?\xd0'
                      b'\x80\xd0\x81\xd1\x83\xd0\xb5,\xb0\xd0\xd1\x8b\xb5\xd0\xb4\xd0\xd0\xb4\xd0'
                      b'\xb2\xd0\xb2\xd1\x82\xd0\xba \xd0\xd1\x81\xd0\xbe\xd1\x8f'),
        ]
        self.assertIn(respuesta, opciones_validas)


if __name__ == "__main__":
    unittest.main(verbosity=2)
