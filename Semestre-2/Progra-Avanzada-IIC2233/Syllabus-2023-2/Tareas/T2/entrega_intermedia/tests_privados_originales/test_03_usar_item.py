import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_cliente import usar_item


class TestUsarItem(unittest.TestCase):

    def test_0(self):
        respuesta = usar_item("congelador", ["manzana", "congelador", "manzana", "congelador", "manzana"])
        self.assertEqual(respuesta, (True, ["manzana", "manzana", "congelador", "manzana"]))

    def test_1(self):
        respuesta = usar_item("congelador", ["manzana", "manzana", "manzana", "manzana"])
        self.assertEqual(respuesta, (False, ["manzana", "manzana", "manzana", "manzana"]))

    def test_2(self):
        respuesta = usar_item("manzana", [])
        self.assertEqual(respuesta, (False, []))

    def test_4(self):
        respuesta = usar_item("manzana", ["manzana", "congelador", "manzana", "congelador", "manzana"])
        self.assertEqual(respuesta, (True, ["congelador", "manzana", "congelador", "manzana"]))

    def test_5(self):
        respuesta = usar_item("manzana", ["congelador"])
        self.assertEqual(respuesta, (False, ["congelador"]))

    def test_6(self):
        respuesta = usar_item("congelador", ["congelador"])
        self.assertEqual(respuesta, (True, []))


if __name__ == "__main__":
    unittest.main(verbosity=2)
