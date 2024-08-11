import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from peli import Peliculas
from api import Server


class TestVerificarInformacion(unittest.TestCase):

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
        Pelicula sí existe
        """
        pelicula = "Iron Man"

        respuesta = self.peli.verificar_informacion(pelicula)
        self.assertIsInstance(respuesta, bool)
        self.assertEqual(respuesta, True)

    def test_1(self):
        """
        Pelicula no existe
        """
        pelicula = "Black Panther"

        respuesta = self.peli.verificar_informacion(pelicula)
        self.assertIsInstance(respuesta, bool)
        self.assertEqual(respuesta, False)

    def test_2(self):
        """
        Pelicula sí existe
        """
        pelicula = "Monsters Inc"

        respuesta = self.peli.verificar_informacion(pelicula)
        self.assertIsInstance(respuesta, bool)
        self.assertEqual(respuesta, True)

    def test_3(self):
        """
        Pelicula sí existe
        """
        pelicula = "High School Musical"

        respuesta = self.peli.verificar_informacion(pelicula)
        self.assertIsInstance(respuesta, bool)
        self.assertEqual(respuesta, True)

    def test_4(self):
        """
        Pelicula no existe
        """
        pelicula = "High School Musical 2"

        respuesta = self.peli.verificar_informacion(pelicula)
        self.assertIsInstance(respuesta, bool)
        self.assertEqual(respuesta, False)

if __name__ == '__main__':
    unittest.main(verbosity=2)