from datetime import date
import sys
from time import sleep
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from peli import Peliculas
from api import Server


class TestSaludar(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        HOST = "localhost"
        PORT = 4444
        DATABASE = {
            "Mamma Mia": "Comedia musical con ABBA",
            "Monsters Inc": "Monstruos asustan, niños y risas",
            "Incredibles": "Familia de superhéroes salva el mundo",
            "Avengers": "Superhéroes luchan contra villanos poderosos",
            "Titanic": "Amor trágico en el hundimiento del Titanic",
            "Akira": "Ciencia ficción japonesa con poderes psíquicos",
            "High School Musical": "Drama musical adolescente en la escuela East High",
            "The Princess Diaries": "Joven descubre que es princesa de Genovia",
            "Iron Man": "Hombre construye traje de alta tecnología para salvar al mundo",
            "Tarzan": "Hombre criado por simios en la jungla",
            "The Pianist": "Músico judío sobrevive en Varsovia durante el Holocausto",
        }
        self.peli = Peliculas(HOST, PORT)
        self.servidor = Server(HOST, PORT, DATABASE)
        self.servidor.start()
        self.servidor.server_started.wait()

    @classmethod
    def tearDownClass(self):
        self.servidor.w_s.shutdown()
        self.servidor.stop()
        self.servidor.join()

    def test_0(self):
        """
        Modo 1
        """
        self.servidor.mode = 1
        respuesta = self.peli.saludar()
        today = date.today()
        resultado = f"Hoy es {today} y es un gran día para ver una buena película"

        self.assertIn("status-code", respuesta)
        self.assertIn("saludo", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["saludo"], resultado)

    def test_1(self):
        """
        Modo 2
        """
        self.servidor.mode = 2
        respuesta = self.peli.saludar()
        today = date.today()
        resultado = f"Hoy es {today} y tengo ganas de ver una película"

        self.assertIn("status-code", respuesta)
        self.assertIn("saludo", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["saludo"], resultado)


if __name__ == '__main__':
    unittest.main(verbosity=2)