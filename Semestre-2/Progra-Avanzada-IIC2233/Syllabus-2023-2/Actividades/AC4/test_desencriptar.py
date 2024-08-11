import unittest
from main import deserializar_tortuga, decodificar_largo, \
    separar_msg_encriptado, decodificar_rango, desencriptar
from clases import Tortuga
from unittest.mock import patch


class TestDesencriptar(unittest.TestCase):
    def test_deserializar_tortuga(self):
        """
        Verificar resultado correcto de esta función.
        """
        t1 = bytearray(b'\x80\x04\x957\x00\x00\x00\x00\x00\x00\x00\x8c\x06clases\x94\x8c\x07Tortuga\x94\x93\x94)\x81\x94}\x94(\x8c\x06nombre\x94\x8c\x04Tama\x94\x8c\x04edad\x94K\x00ub.')
        test = deserializar_tortuga(t1)
        res = Tortuga("Tama")

        # Verificar tipo de dato pedido
        self.assertIsInstance(test, Tortuga)
        # Verificar resultados
        self.assertDictEqual(test.__dict__, res.__dict__)

    def test_deserializar_tortuga_excepcion(self):
        """
        Verificar el correcto levantamiento de excepciones
        """
        # Verificar que lavanta excepcion
        no_deserializable = b'\x80\x14K\x91.'
        self.assertRaises(
            AttributeError, deserializar_tortuga, no_deserializable)

        # Verificar que no levanta excepcion
        desserializable = bytearray(
            b'\x80\x04\x957\x00\x00\x00\x00\x00\x00\x00\x8c\x06clases\x94\x8c\x07Tortuga\x94\x93\x94)\x81\x94}\x94(\x8c\x06nombre\x94\x8c\x04Tama\x94\x8c\x04edad\x94K\x00ub.')
        try:
            deserializar_tortuga(desserializable)
        except:
            self.fail(
                "Se levantó una excepción con un input que si se puede deserializar")

    def test_decodificar_largo_pequeño(self):
        """
        Verificar decodificación con número pequeño
        """
        test = decodificar_largo(bytearray(b'\x00\x00\x02'))
        res = 2
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, int)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_decodificar_largo_grande(self):
        """
        Verificar decodificación con número grande
        """
        test = decodificar_largo(bytearray(b'\xA1\x11\xA0'))
        res = 10555808
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, int)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_separar_msg_encriptado_par(self):
        """
        Verificar que separa el mensaje correctamente
        """
        def new_decodificar_largo(*args, **kwargs):
            return 2

        with patch('main.decodificar_largo', side_effect=new_decodificar_largo):
            test = separar_msg_encriptado(
                bytearray(b'\x00\x00\x02\x02\x01\x03\x00\x01\x00\x00\x00\x01\x00\x00\x04'))
            res = [
                bytearray(b'\x02\x01'),
                bytearray(b'\x03\x00\x01\x00'),
                bytearray(b'\x00\x00\x01\x00\x00\x04')
            ]
            # Verificar tipo de dato pedido
            self.assertIsInstance(res, list)
            # Verificar resultados
            self.assertListEqual(test, res)

    def test_separar_msg_encriptado_impar(self):
        """
        Verificar que separa el mensaje correctamente y lo invierto cuando el largo era impar
        """
        def decodificar_largo(*args, **kwargs):
            return 3

        with patch('main.decodificar_largo', side_effect=decodificar_largo):
            test = separar_msg_encriptado(
                bytearray(b'\x00\x00\x03\x44\x02\x01\x03\x00\x01\x02\x00\x00\x00\x01\x00\x00\x05'))
            res = [
                bytearray(b'\x01\x02\x44'),
                bytearray(b'\x03\x00\x01\x02\x00'),
                bytearray(b'\x00\x00\x01\x00\x00\x05')
            ]
            # Verificar tipo de dato pedido
            self.assertIsInstance(res, list)
            # Verificar resultados
            self.assertListEqual(test, res)

    def test_decodificar_rango_pequeño(self):
        """
        Verificar decodificación de rango con números pequeños
        """
        test = decodificar_rango(bytearray(b'\x00\x00\x01\x00\x00\x03'))
        res = [1, 3]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res, list)
        # Verificar resultados
        self.assertListEqual(test, res)

    def test_decodificar_rango_grande(self):
        """
        Verificar decodificación de rango con números grandes
        """
        test = decodificar_rango(bytearray(b'\x00\x00\x0B\x00\x11\x5C'))
        res = [11, 4444]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res, list)
        # Verificar resultados
        self.assertListEqual(test, res)

    def test_desencriptar(self):
        """
        Verificar correcto armado del mensaje encriptado asumuiendo que "decodificar_largo", "separar" y "decodificar" están buenos
        """
        def separar_msg_encriptado(*args, **kwargs):
            return [bytearray(b'\x80\x02\x04'), 
                    bytearray(b'\x09\x00\x01\x02\x08'), 
                    bytearray(b'\x00\x00\x01\x00\x00\x03')]

        def decodificar_rango(*args, **kwargs):
            return [1, 3]
        
        def decodificar_largo(*args, **kwargs):
            return 3

        with patch('main.decodificar_largo', side_effect=decodificar_largo):
            with patch('main.separar_msg_encriptado', side_effect=separar_msg_encriptado):
                with patch('main.decodificar_rango', side_effect=decodificar_rango):
                    test = desencriptar(
                        bytearray(b'\x00\x00\x03\x04\x02\x80\x09\x00\x01\x02\x08\x00\x00\x01\x00\x00\x03'))
                    res = bytearray(b'\x09\x80\x02\x04\x08')
                    # Verificar tipo de dato pedido
                    self.assertIsInstance(res, bytearray)
                    # Verificar resultados
                    self.assertEqual(test, res)


if __name__ == '__main__':
    unittest.main(verbosity=2)
