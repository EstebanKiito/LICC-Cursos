from abc import ABC
import unittest
from unittest.mock import patch
import types

from clases import Vehiculo, AutoBencina, AutoElectrico, FaitHibrido, Camioneta, Telsa


class VerificarClaseVehiculo(unittest.TestCase):

    def test_no_puede_instanciarse(self):
        self.assertRaises(TypeError, Vehiculo, 15)

    def test_metodo_abstracto_definido(self):
        self.assertIn('recorrer', Vehiculo.__abstractmethods__)

    def test_herencia_abc(self):
        self.assertIn(ABC, Vehiculo.__mro__)

    def test_property_energia_definida(self):
        self.assertIsInstance(Vehiculo.energia, property)

    def test_property_autonomia_definida(self):
        self.assertIsInstance(Vehiculo.autonomia, property)


class VerificarClaseAutoBencina(unittest.TestCase):

    def test_llama_init_vehiculo(self):
        with patch('clases.Vehiculo.__init__') as mock:
            mock.return_value = None
            AutoBencina(bencina_favorita=93, rendimiento=10, marca='chev', energia=100)
            mock.assert_called_once()

    def test_herencia_vehiculo(self):
        self.assertIn(Vehiculo, AutoBencina.__mro__)

    def test_init_correcto(self):
        id_inicial = Vehiculo.identificador
        auto = AutoBencina(bencina_favorita=93, rendimiento=10, marca='chev', energia=100)
        self.assertEqual(auto.bencina_favorita, 93)
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.marca, 'chev')
        self.assertEqual(auto.energia, 100)
        self.assertEqual(auto.identificador, id_inicial)

        auto2 = AutoBencina(bencina_favorita=95, rendimiento=11, marca='chev2', energia=101)
        self.assertEqual(auto2.bencina_favorita, 95)
        self.assertEqual(auto2.rendimiento, 11)
        self.assertEqual(auto2.marca, 'chev2')
        self.assertEqual(auto2.energia, 101)
        self.assertEqual(auto2.identificador, id_inicial + 1)

    def test_valor_energia_por_defecto_correcto_auto_bencina(self):
        auto = AutoBencina(bencina_favorita=93, rendimiento=10, marca='chev')
        self.assertEqual(auto.energia, 120)

    def test_metodo_recorrer_definido(self):
        self.assertIsInstance(AutoBencina.recorrer, types.FunctionType)

    def test_recorrer_sobre_autonomia(self):
        auto = AutoBencina(bencina_favorita=93, rendimiento=10, marca='chev', energia=100)
        resultado = auto.recorrer(100000)
        self.assertEqual(auto.energia, 0)
        self.assertEqual(resultado, 'Anduve por 1000Km y gasté 100L de bencina')

    def test_recorrer_bajo_autonomia(self):
        auto = AutoBencina(bencina_favorita=93, rendimiento=11, marca='chev', energia=100)
        resultado = auto.recorrer(99)
        self.assertEqual(auto.energia, 91)
        self.assertEqual(resultado, 'Anduve por 99Km y gasté 9L de bencina')

    def test_autonomia(self):
        auto = AutoBencina(bencina_favorita=93, rendimiento=3, marca='chev', energia=2)
        self.assertEqual(auto.autonomia, 6)
        auto2 = AutoBencina(bencina_favorita=93, rendimiento=7, marca='chev', energia=3)
        self.assertEqual(auto2.autonomia, 21)


class VerificarClaseAutoElectrico(unittest.TestCase):

    def test_herencia_vehiculo(self):
        self.assertIn(Vehiculo, AutoElectrico.__mro__)

    def test_llama_init_vehiculo(self):
        with patch('clases.Vehiculo.__init__') as mock:
            mock.return_value = None
            AutoElectrico(vida_util_bateria=2, rendimiento=10, marca='c', energia=100)
            mock.assert_called_once()

    def test_init_correcto(self):
        auto = AutoElectrico(vida_util_bateria=2, rendimiento=10, marca='c', energia=100)
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.vida_util_bateria, 2)
        self.assertEqual(auto.marca, 'c')
        self.assertEqual(auto.energia, 100)

        auto2 = AutoElectrico(vida_util_bateria=1, rendimiento=11, marca='c2', energia=101)
        self.assertEqual(auto2.rendimiento, 11)
        self.assertEqual(auto2.vida_util_bateria, 1)
        self.assertEqual(auto2.marca, 'c2')
        self.assertEqual(auto2.energia, 101)

    def test_valor_energia_por_defecto_correcto_auto_electrico(self):
        auto = AutoElectrico(vida_util_bateria=93, rendimiento=10, marca='chev')
        self.assertEqual(auto.energia, 120)

    def test_recorrer_sobre_autonomia(self):
        auto = AutoElectrico(vida_util_bateria=93, rendimiento=10, marca='chev', energia=100)
        resultado = auto.recorrer(100000)
        self.assertEqual(auto.energia, 0)
        self.assertEqual(resultado, 'Anduve por 1000Km y gasté 100W de energía eléctrica')

    def test_recorrer_bajo_autonomia(self):
        auto = AutoElectrico(vida_util_bateria=93, rendimiento=11, marca='chev', energia=100)
        resultado = auto.recorrer(99)
        self.assertEqual(auto.energia, 91)
        self.assertEqual(resultado, 'Anduve por 99Km y gasté 9W de energía eléctrica')


class VerificarClaseCamioneta(unittest.TestCase):

    def test_herencia_vehiculo_bencina(self):
        self.assertIn(AutoBencina, Camioneta.__mro__)

    def test_init_correcto(self):
        auto = Camioneta(capacidad_maleta=10, rendimiento=10, marca='c',
                         energia=100, bencina_favorita=93)
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.marca, 'c')
        self.assertEqual(auto.bencina_favorita, 93)
        self.assertEqual(auto.energia, 100)

        auto2 = Camioneta(capacidad_maleta=1, rendimiento=1, marca='c2',
                          energia=101, bencina_favorita=95)
        self.assertEqual(auto2.rendimiento, 1)
        self.assertEqual(auto2.bencina_favorita, 95)
        self.assertEqual(auto2.marca, 'c2')
        self.assertEqual(auto2.energia, 101)

    def test_llama_init_vehiculo(self):
        with patch('clases.Vehiculo.__init__') as mock:
            mock.return_value = None
            Camioneta(capacidad_maleta=10, rendimiento=10, marca='c',
                      energia=100, bencina_favorita=92)
            mock.assert_called_once()

    def test_llama_init_auto_bencina(self):
        with patch('clases.AutoBencina.__init__') as mock:
            mock.return_value = None
            Camioneta(capacidad_maleta=10, rendimiento=10, marca='c',
                      energia=100, bencina_favorita=92)
            mock.assert_called_once()

    def test_no_llama_init_auto_electrico(self):
        with patch('clases.AutoElectrico.__init__') as mock:
            mock.return_value = None
            Camioneta(capacidad_maleta=10, rendimiento=10, marca='c',
                      energia=100, bencina_favorita=92)
            mock.assert_not_called()


class VerificarClaseTelsa(unittest.TestCase):

    def test_herencia_vehiculo_Electrico(self):
        self.assertIn(AutoElectrico, Telsa.__mro__)

    def test_init_correcto(self):
        auto = Telsa(rendimiento=10, marca='c', energia=100, vida_util_bateria=3)
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.marca, 'c')
        self.assertEqual(auto.energia, 100)
        self.assertEqual(auto.vida_util_bateria, 3)

        auto2 = Telsa(vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
        self.assertEqual(auto2.rendimiento, 1)
        self.assertEqual(auto2.marca, 'c2')
        self.assertEqual(auto2.energia, 101)
        self.assertEqual(auto2.vida_util_bateria, 1)

    def test_llama_init_vehiculo(self):
        with patch('clases.Vehiculo.__init__') as mock:
            mock.return_value = None
            Telsa(capacidad_maleta=1, vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
            mock.assert_called_once()

    def test_no_llama_init_auto_bencina(self):
        with patch('clases.AutoBencina.__init__') as mock:
            mock.return_value = None
            Telsa(vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
            mock.assert_not_called()

    def test_llama_init_auto_electrico(self):
        with patch('clases.AutoElectrico.__init__') as mock:
            mock.return_value = None
            Telsa(vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
            mock.assert_called_once()

    def test_llama_recorrer_clase_padres(self):
        with patch('clases.AutoElectrico.recorrer') as mock:
            mock.return_value = 'test'
            auto = Telsa(vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
            res = auto.recorrer(12)
            mock.assert_called_once_with(12)
            self.assertEqual(res, 'testde forma inteligente')


class VerificarClaseFaitHibrido(unittest.TestCase):

    def test_herencia_vehiculo_Electrico(self):
        self.assertIn(AutoElectrico, FaitHibrido.__mro__)

    def test_herencia_vehiculo_Bencina(self):
        self.assertIn(AutoBencina, FaitHibrido.__mro__)

    def test_init_correcto(self):
        auto = FaitHibrido(rendimiento=7, marca='c', energia=101, bencina_favorita=95)
        self.assertEqual(auto.rendimiento, 7)
        self.assertEqual(auto.marca, 'c')
        self.assertEqual(auto.energia, 101)
        self.assertEqual(auto.vida_util_bateria, 5)

        auto2 = FaitHibrido(rendimiento=2, marca='c2', energia=131, bencina_favorita=95)
        self.assertEqual(auto2.rendimiento, 2)
        self.assertEqual(auto2.marca, 'c2')
        self.assertEqual(auto2.energia, 131)
        self.assertEqual(auto2.vida_util_bateria, 5)

    def test_llama_init_vehiculo_solo_una_vez(self):
        with patch('clases.Vehiculo.__init__') as mock:
            mock.return_value = None
            FaitHibrido(rendimiento=1, marca='c2', energia=101, bencina_favorita=95)
            mock.assert_called_once()

    def test_llama_recorrer_clases_padres(self):
        with patch('clases.AutoBencina.recorrer') as mock:
            mock.return_value = 'a'
            with patch('clases.AutoElectrico.recorrer') as mock2:
                mock2.return_value = 'b'
                auto = FaitHibrido(rendimiento=1, marca='c2', energia=101, bencina_favorita=95)
                res = auto.recorrer(12)
                mock.assert_called_once_with(auto, 6.0)
                mock2.assert_called_once_with(auto, 6.0)
                self.assertIn(res, ['ab', 'ba'])

    def test_llama_recorrer_clases_padres2(self):
        with patch('clases.AutoBencina.recorrer') as mock:
            mock.return_value = 'd'
            with patch('clases.AutoElectrico.recorrer') as mock2:
                mock2.return_value = 'c'
                auto2 = FaitHibrido(rendimiento=1, marca='c2', energia=101, bencina_favorita=95)
                res = auto2.recorrer(10)
                mock.assert_called_once_with(auto2, 5.0)
                mock2.assert_called_once_with(auto2, 5.0)
                self.assertIn(res, ['cd', 'dc'])

    def test_no_llama_init_auto_bencina(self):
        with patch('clases.AutoBencina.__init__') as mock:
            mock.return_value = None
            FaitHibrido(rendimiento=1, marca='c2', energia=101, bencina_favorita=95)
            mock.assert_called_once()

    def test_llama_init_auto_electrico(self):
        with patch('clases.AutoElectrico.__init__') as mock:
            mock.return_value = None
            FaitHibrido(rendimiento=1, marca='c2', energia=101, bencina_favorita=95)
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main(verbosity=2)
