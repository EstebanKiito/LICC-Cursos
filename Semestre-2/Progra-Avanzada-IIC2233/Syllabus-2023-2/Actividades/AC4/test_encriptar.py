import unittest
from main import serializar_tortuga, verificar_rango, \
    codificar_rango, codificar_largo, separar_msg, encriptar
from clases import Tortuga
from unittest.mock import patch


class TestEncriptar(unittest.TestCase):

    def test_serializar_tortuga(self):
        """
        Verificar resultado correcto de esta función.
        """
        tama = Tortuga("Tama")
        test = serializar_tortuga(tama)
        res = bytearray(
            b'\x80\x04\x957\x00\x00\x00\x00\x00\x00\x00\x8c\x06clases\x94\x8c\x07Tortuga\x94\x93\x94)\x81\x94}\x94(\x8c\x06nombre\x94\x8c\x04Tama\x94\x8c\x04edad\x94K\x00ub.')

        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_serializar_tortuga_excepcion(self):
        """
        Verificar el correcto levantamiento de excepciones
        """
        # Verificar que lavanta excepcion
        def no_serializable(x):
            return x+1

        self.assertRaises(ValueError, serializar_tortuga, no_serializable)

        # Verificar que no levanta excepcion
        serializable = Tortuga("Tama")
        try:
            serializar_tortuga(serializable)
        except:
            self.fail(
                "Se levantó una excepción con un input que si se puede serializar")

    def test_verificar_rango_None(self):
        """
        Verificar que retorne None
        """
        mensaje = bytearray(b'\x00\x01\x02\x03')
        self.assertIsNone(verificar_rango(mensaje, 1, 2))

    def test_verificar_rango_minimo(self):
        """
        Verificar excepción cuando inicio es menor a 0
        """
        mensaje = bytearray(b'\x00\x01\x02\x03')
        self.assertRaises(AttributeError, verificar_rango, mensaje, -5, 2)

    def test_verificar_rango_maximo(self):
        """
        Verificar excepción cuando fin es mayor al largo
        """
        mensaje = bytearray(b'\x00\x01\x02\x03')
        self.assertRaises(AttributeError, verificar_rango, mensaje, 0, 4444)

    def test_verificar_rango_creciente(self):
        """
        Verificar excepción cuando fin es menor a inicio
        """
        mensaje = bytearray(b'\x00\x01\x02\x03')
        self.assertRaises(AttributeError, verificar_rango, mensaje, 3, 0)

    def test_codificar_secuencia_pequeño(self):
        """
        Verificar correcta codificación con números pequeños
        """
        test = codificar_rango(1, 3)
        res = bytearray(b'\x00\x00\x01\x00\x00\x03')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_codificar_secuencia_grande(self):
        """
        Verificar correcta codificación con números grandes
        """
        test = codificar_rango(1, 4444)
        res = bytearray(b'\x00\x00\x01\x00\x11\\')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_codificar_largo_pequeño(self):
        """
        Verificar correcta codificación con número pequeño
        """
        test = codificar_largo(4)
        res = bytearray(b'\x00\x00\x04')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_codificar_largo_grande(self):
        """
        Verificar correcta codificación con número grande
        """
        test = codificar_largo(4242)
        res = bytearray(b'\x00\x10\x92')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_separar_msg(self):
        """
        Verificar correcta separación de mensaje donde largo es impar
        """
        test = separar_msg(bytearray(b'\x00\x01\x02\x03'), 1, 3)
        res = [bytearray(b'\x03\x02\x01'), bytearray(b'\x00\x00\x01\x02')]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res, list)
        # Verificar resultados
        self.assertListEqual(test, res)

    def test_separar_msg_2(self):
        """
        Verificar correcta separación de mensaje donde largo es par
        """
        test = separar_msg(bytearray(b'\x00\x01\x02\x03'), 1, 2)
        res = [bytearray(b'\x01\x02'), bytearray(b'\x00\x00\x01\x03')]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res, list)
        # Verificar resultados
        self.assertListEqual(test, res)

    def test_separar_msg_3(self):
        """
        Verificar correcta separación de mensaje donde largo es impar y partiendo de 0
        """
        test = separar_msg(bytearray(b'\x08\x09\x0A\x0B'), 0, 2)
        res = [bytearray(b'\x0A\x09\x08'), bytearray(b'\x00\x01\x02\x0B')]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res, list)
        # Verificar resultados
        self.assertListEqual(test, res)


if __name__ == '__main__':
    unittest.main(verbosity=2)
