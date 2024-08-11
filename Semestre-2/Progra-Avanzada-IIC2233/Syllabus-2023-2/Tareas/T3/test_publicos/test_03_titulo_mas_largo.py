import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import titulo_mas_largo
from utilidades import Peliculas


class TestTituloMasLargo(unittest.TestCase):

    def test_0(self):
        """
        Una pelicula con el título más largo
        """
        lista_peliculas = [
            Peliculas(id=23221543, titulo='Halloweentown', genero='Fantasía', rating=6.3),
            Peliculas(id=27868789, titulo='Guardians of the Galaxy', genero='Animación', rating=7.5),
            Peliculas(id=69065378, titulo='Black Panther', genero='Superhéroes', rating=8.0),
            Peliculas(id=28527704, titulo='Princess Mononoke', genero='Animación', rating=8.4),
            Peliculas(id=64787434, titulo='Inuyasha', genero='Animación', rating=8.5),
            Peliculas(id=58329437, titulo='My Neighbor Totoro', genero='Animación', rating=8.6),
            Peliculas(id=89756869, titulo="The Emperor's New Groove", genero='Deportes', rating=6.9),
            Peliculas(id=84580833, titulo='Wreck-It Ralph', genero='Animación', rating=7.5),
            Peliculas(id=77439731, titulo='The Lord of the Rings: The Fellowship of the Ring', genero='Animación', rating=8.4),
            Peliculas(id=75259113, titulo='Up', genero='Crimen', rating=8.4),
            Peliculas(id=43516202, titulo='The Great Gatsby', genero='Drama', rating=8.5),
            Peliculas(id=71285784, titulo='Avengers: Age of Ultron', genero='Animación', rating=7.6),
            Peliculas(id=61384134, titulo='Mamma Mia', genero='Musical', rating=10.0),
        ]
        expected_titulo = 'The Lord of the Rings: The Fellowship of the Ring'

        generador = (p for p in lista_peliculas)
        resultado = titulo_mas_largo(generador)
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, expected_titulo)

    def test_1(self):
        """
        Peliculas empatadas con el mismo largo
        """
        lista_peliculas = [
            Peliculas(id=54541808, titulo='Matilda', genero='Comedia', rating=6.9),
            Peliculas(id=98811629, titulo='Braveheart', genero='Animación', rating=8.5),
            Peliculas(id=98009659, titulo='Twitches', genero='Fantasía', rating=6.7),
            Peliculas(id=51151305, titulo='Pocahontas', genero='Fantasía', rating=7.8),
            Peliculas(id=45064961, titulo='Big Hero 6', genero='Animación', rating=7.8),
            Peliculas(id=95417284, titulo='Camp Rock', genero='Musical', rating=5.1),
            Peliculas(id=41068976, titulo='Cinderella', genero='Animación', rating=7.1),
            Peliculas(id=58643843, titulo='Iron Man 2', genero='Animación', rating=7.0),
            Peliculas(id=39971720, titulo='Inuyasha', genero='Superhéroes', rating=7.5),
            Peliculas(id=33612645, titulo='Goodfellas', genero='Animación', rating=8.9),
            Peliculas(id=34304754, titulo='Iron Man 3', genero='Animación', rating=7.1),
            Peliculas(id=87114047, titulo='Jump In!', genero='Deportes', rating=5.4),
            Peliculas(id=30060914, titulo='Get a Clue', genero='Comedia', rating=6.2),
            Peliculas(id=81744489, titulo='Cow Belles', genero='Comedia', rating=6.1),
        ]

        expected_titulo = 'Goodfellas'

        generador = (p for p in lista_peliculas)
        resultado = titulo_mas_largo(generador)
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, expected_titulo)

    def test_2(self):
        """
        Una pelicula con el título más largo
        """
        lista_peliculas = [
            Peliculas(id=95054110, titulo='Thor: Ragnarok', genero='Superhéroes', rating=7.9),
            Peliculas(id=46804999, titulo='Guardians of the Galaxy Vol. 2', genero='Superhéroes', rating=7.1),
            Peliculas(id=81744489, titulo='Cow Belles', genero='Comedia', rating=6.1),
            Peliculas(id=16359236, titulo='Mulan', genero='Deportes', rating=7.8),
            Peliculas(id=32152163, titulo='The Princess Diaries', genero='Comedia', rating=6.2),
        ]
        expected_titulo = 'Guardians of the Galaxy Vol. 2'

        generador = (p for p in lista_peliculas)
        resultado = titulo_mas_largo(generador)
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, expected_titulo)

    def test_3(self):
        """
        Peliculas empatadas con el mismo largo y el mismo rating
        """
        lista_peliculas = [
            Peliculas(id=23678361, titulo='Scarface', genero='Crimen', rating=8.8),
            Peliculas(id=45745398, titulo='The Green Mile', genero='Animación', rating=8.2),
            Peliculas(id=51151305, titulo='Pocahontas', genero='Fantasía', rating=7.8),
            Peliculas(id=40873645, titulo='The Terminator', genero='Ciencia Ficción', rating=8.5),
            Peliculas(id=23653810, titulo='Reservoir Dogs', genero='Superhéroes', rating=8.3),
            Peliculas(id=49034902, titulo='The Godfather', genero='Crimen', rating=9.2),
            Peliculas(id=84580833, titulo='Wreck-It Ralph', genero='Animación', rating=7.5),
            Peliculas(id=32608840, titulo='Johnny Tsunami', genero='Deportes', rating=6.3),
            Peliculas(id=89737370, titulo='Iron Man', genero='Animación', rating=7.6),
            Peliculas(id=87210469, titulo='Doctor Strange', genero='Superhéroes', rating=7.3),
            Peliculas(id=52568632, titulo='Shutter Island', genero='Superhéroes', rating=8.5),
            Peliculas(id=65976883, titulo='Titanic', genero='Drama', rating=7.8),
            Peliculas(id=95054110, titulo='Thor: Ragnarok', genero='Superhéroes', rating=7.9),
        ]
        expected_titulo = 'Shutter Island'

        generador = (p for p in lista_peliculas)
        resultado = titulo_mas_largo(generador)
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, expected_titulo)

    def test_4(self):
        """
        Todas las peliculas del mismo largo y algunas con el mismo rating
        """
        lista_peliculas = [
            Peliculas(id=87538292, titulo='Monsters Inc.', genero='Animación', rating=8.1),
            Peliculas(id=75759551, titulo='The Lion King', genero='Animación', rating=9.2),
            Peliculas(id=49034902, titulo='The Godfather', genero='Crimen', rating=9.2),
            Peliculas(id=42475848, titulo='Spirited Away', genero='Animación', rating=8.6),
            Peliculas(id=69065378, titulo='Black Panther', genero='Superhéroes', rating=8.0),
            Peliculas(id=23221543, titulo='Halloweentown', genero='Fantasía', rating=6.3),
            Peliculas(id=67027889, titulo='Seven Samurai', genero='Crimen', rating=9.2),
            Peliculas(id=49895401, titulo='Pixel Perfect', genero='Ciencia Ficción', rating=6.0),
        ]
        expected_titulo = 'Seven Samurai'

        generador = (p for p in lista_peliculas)
        resultado = titulo_mas_largo(generador)
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, expected_titulo)

if __name__ == '__main__':
    unittest.main(verbosity=2)