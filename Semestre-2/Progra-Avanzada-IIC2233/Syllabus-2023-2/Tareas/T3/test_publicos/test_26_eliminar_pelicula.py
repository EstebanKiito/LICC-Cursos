import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from peli import Peliculas
from api import Server


class TestEliminarPelicula(unittest.TestCase):

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
        Pelicula existe y el token es valido
        """
        pelicula = "Tarzan"

        self.servidor.mode = 0
        respuesta = self.peli.eliminar_pelicula(pelicula, "juampiiic2233")
        self.assertIsInstance(respuesta, str)
        self.assertNotIn(pelicula, self.servidor.database.keys())
        self.assertEqual(respuesta, "La base de la API ha sido actualizada")

    def test_1(self):
        """
        Pelicula existe y el token es valido
        """
        pelicula = "Iron Man"

        self.servidor.mode = 1
        respuesta = self.peli.eliminar_pelicula(pelicula, "tereiic2233")
        self.assertIsInstance(respuesta, str)
        self.assertNotIn(pelicula, self.servidor.database.keys())
        self.assertEqual(respuesta, "La base de la API ha sido actualizada")

    def test_2(self):
        """
        Pelicula existe y el token no es valido
        """
        pelicula = "Iron Man"

        self.servidor.mode = 0
        respuesta = self.peli.eliminar_pelicula(pelicula, "tereiic2233")
        self.assertIsInstance(respuesta, str)
        self.assertNotIn(pelicula, self.servidor.database.keys())
        self.assertEqual(respuesta, "Eliminar pelicula no autorizado")

    def test_3(self):
        """
        Pelicula no existe y el token es valido
        """
        pelicula = "Titanic 2"

        self.servidor.mode = 0
        respuesta = self.peli.eliminar_pelicula(pelicula, "juampiiic2233")
        self.assertIsInstance(respuesta, str)
        self.assertNotIn(pelicula, self.servidor.database.keys())
        self.assertEqual(respuesta, "La pelicula no existe")

    def test_4(self):
        """
        Pelicula no existe y el token no es valido
        """
        pelicula = "Iron Man 2"

        self.servidor.mode = 1
        respuesta = self.peli.eliminar_pelicula(pelicula, "juampiiic2233")
        self.assertIsInstance(respuesta, str)
        self.assertNotIn(pelicula, self.servidor.database.keys())
        self.assertEqual(respuesta, "Eliminar pelicula no autorizado")

if __name__ == '__main__':
    unittest.main(verbosity=2)