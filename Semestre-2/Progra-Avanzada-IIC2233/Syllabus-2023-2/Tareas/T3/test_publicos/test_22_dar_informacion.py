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
        pelicula = "Avengers"
        resultado = "Superhéroes luchan contra villanos poderosos"

        respuesta = self.peli.dar_informacion(pelicula)
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["mensaje"], resultado)

    def test_1(self):
        """
        Pelicula no existe (status code 400)
        """
        pelicula = "High School Musical 2"
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
        pelicula = "High School Musical"
        resultado = "Drama musical adolescente en la escuela East High"

        respuesta = self.peli.dar_informacion(pelicula)
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["mensaje"], resultado)

    def test_3(self):
        """
        Pelicula en la base de datos
        """
        pelicula = "Tarzan"
        resultado = "Hombre criado por simios en la jungla"

        respuesta = self.peli.dar_informacion(pelicula)
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["mensaje"], resultado)

    def test_4(self):
        """
        Pelicula en la base de datos
        """
        pelicula = "Mamma Mia"
        resultado = "Comedia musical con ABBA"

        respuesta = self.peli.dar_informacion(pelicula)
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["mensaje"], resultado)

if __name__ == '__main__':
    unittest.main(verbosity=2)