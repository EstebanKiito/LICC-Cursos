import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_cliente import usar_item


class TestUsarItem(unittest.TestCase):

    def test_0(self):
        respuesta = usar_item("manzana", ["congelador", "manzana", "congelador", "manzana"])
        self.assertEqual(respuesta, (True, ["congelador", "congelador", "manzana"]))

    def test_1(self):
        respuesta = usar_item("manzana", ["congelador", "congelador"])
        self.assertEqual(respuesta, (False, ["congelador", "congelador"]))

    def test_2(self):
        respuesta = usar_item("congelador", [])
        self.assertEqual(respuesta, (False, []))

    def test_4(self):
        respuesta = usar_item("congelador", ["manzana", "congelador", "manzana", "congelador", "manzana"])
        self.assertEqual(respuesta, (True, ["manzana", "manzana", "congelador", "manzana"]))

    def test_5(self):
        respuesta = usar_item("congelador", ["manzana"])
        self.assertEqual(respuesta, (False, ["manzana"]))

    def test_6(self):
        respuesta = usar_item("manzana", ["manzana"])
        self.assertEqual(respuesta, (True, []))


if __name__ == "__main__":
    unittest.main(verbosity=2)
