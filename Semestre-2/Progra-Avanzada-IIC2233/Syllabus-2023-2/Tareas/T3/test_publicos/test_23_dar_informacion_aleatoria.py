import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from peli import Peliculas
from api import Server


class TestDarInformacionAleatoria(unittest.TestCase):
    
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
        Modo 0
        """
        self.servidor.mode = 0
        respuesta = self.peli.dar_informacion_aleatoria()
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(len(respuesta), 2)
        self.assertEqual(respuesta['status-code'], 200)
        self.assertEqual(respuesta['mensaje'], self.servidor.database[list(self.servidor.database.keys())[-1]])

    def test_1(self):
        """
        Modo 1
        """
        self.servidor.mode = 1
        respuesta = self.peli.dar_informacion_aleatoria()
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(len(respuesta), 2)
        self.assertEqual(respuesta['status-code'], 200)
        self.assertEqual(respuesta['mensaje'], self.servidor.database[list(self.servidor.database.keys())[0]])

    def test_2(self):
        """
        Modo 3
        """
        self.servidor.mode = 3
        respuesta = self.peli.dar_informacion_aleatoria()
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(len(respuesta), 2)
        self.assertEqual(respuesta['status-code'], 500)
        self.assertEqual(respuesta['mensaje'], 'ups, no pude')


if __name__ == '__main__':
    unittest.main(verbosity=2)