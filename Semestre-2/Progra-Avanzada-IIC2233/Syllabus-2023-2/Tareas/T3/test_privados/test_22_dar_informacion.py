import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from peli import Peliculas
from api import Server


class TestDarInformacion(unittest.TestCase):

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
            "Spider Man": "Chico es mordido por una araña y obtiene super poderes",
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
        Pelicula en la base de datos
        """
        pelicula = "Spider Man"
        resultado = "Chico es mordido por una araña y obtiene super poderes"

        respuesta = self.peli.dar_informacion(pelicula)
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["mensaje"], resultado)

    def test_1(self):
        """
        Pelicula no existe (status code 400)
        """
        pelicula = "Spider Man 2"
        resultado = "La pelicula no existe"

        respuesta = self.peli.dar_informacion(pelicula)
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)
        self.assertEqual(respuesta["status-code"], 400)
        self.assertEqual(respuesta["mensaje"], resultado)

    def test_2(self):
        """
        Pelicula en la base de datos
        """
        pelicula = "The Princess Diaries"
        resultado = "Joven descubre que es princesa de Genovia"

        respuesta = self.peli.dar_informacion(pelicula)
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["mensaje"], resultado)

    def test_3(self):
        """
        Pelicula en la base de datos
        """
        pelicula = "The Pianist"
        resultado = "Músico judío sobrevive en Varsovia durante el Holocausto"

        respuesta = self.peli.dar_informacion(pelicula)
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["mensaje"], resultado)

    def test_4(self):
        """
        Pelicula en la base de datos
        """
        pelicula = "Akira"
        resultado = "Ciencia ficción japonesa con poderes psíquicos"

        respuesta = self.peli.dar_informacion(pelicula)
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["mensaje"], resultado)


if __name__ == '__main__':
    unittest.main(verbosity=2)
