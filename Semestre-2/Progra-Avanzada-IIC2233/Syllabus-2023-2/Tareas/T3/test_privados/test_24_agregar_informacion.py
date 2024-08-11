import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from peli import Peliculas
from api import Server


class TestAgregarInformacion(unittest.TestCase):

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
            "Spiderman 2": "Chico es mordido por una araña y obtiene super poderes",
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
        Pelicula no existe y token valido
        """
        pelicula = "Hulk"
        sinopsis = "Hombre se convierte en un monstruo verde"

        self.servidor.mode = 0
        respuesta = self.peli.agregar_informacion(pelicula, sinopsis, "juampiiic2233")
        self.assertIsInstance(respuesta, str)
        self.assertIn(pelicula, self.servidor.database)
        self.assertEqual(respuesta, "La base de la API ha sido actualizada")

    def test_1(self):
        """
        Pelicula no existe y token no valido
        """
        pelicula = "Truan y Cattan"
        sinopsis = "Dos almas destinadas a cruzar sus caminos en medio de la oscuridad"

        self.servidor.mode = 1
        respuesta = self.peli.agregar_informacion(pelicula, sinopsis, "juampiiic2233")
        self.assertIsInstance(respuesta, str)
        self.assertNotIn(pelicula, self.servidor.database)
        self.assertEqual(respuesta, "Agregar pelicula no autorizado")

    def test_2(self):
        """
        Pelicula no existe y token valido
        """
        pelicula = "Spiderman"
        sinopsis = "El asombroso hombre araña"

        self.servidor.mode = 1
        respuesta = self.peli.agregar_informacion(pelicula, sinopsis, "tereiic2233")
        self.assertIsInstance(respuesta, str)
        self.assertIn(pelicula, self.servidor.database)
        self.assertEqual(respuesta, "La base de la API ha sido actualizada")

    def test_3(self):
        """
        Pelicula existe y token no valido
        """
        pelicula = "Spiderman 2"
        sinopsis = "Chico y araña, ¿qué puede salir mal?"

        self.servidor.mode = 1
        respuesta = self.peli.agregar_informacion(pelicula, sinopsis, "juampiiic2233")
        self.assertIsInstance(respuesta, str)
        self.assertIn(pelicula, self.servidor.database)
        self.assertEqual(respuesta, "Agregar pelicula no autorizado")

    def test_4(self):
        """
        Pelicula existe y token valido
        """
        pelicula = "High School Musical"
        sinopsis = "Drama musical adolescente en la escuela East High"

        self.servidor.mode = 1
        respuesta = self.peli.agregar_informacion(pelicula, sinopsis, "tereiic2233")
        self.assertIsInstance(respuesta, str)
        self.assertIn(pelicula, self.servidor.database)
        self.assertEqual(respuesta, "La pelicula ya existe, no puedes modificarlo")


if __name__ == '__main__':
    unittest.main(verbosity=2)
