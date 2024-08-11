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
            Peliculas(id=32718070, titulo='Inglourious Basterds', genero='Superhéroes', rating=8.9),
            Peliculas(id=63162203, titulo='The Departed', genero='Animación', rating=8.2),
            Peliculas(id=42103973, titulo="Schindler's List", genero='Fantasía', rating=9.3),
            Peliculas(id=76172796, titulo='Inception', genero='Ciencia Ficción', rating=8.8),
            Peliculas(id=34304754, titulo='Iron Man 3', genero='Animación', rating=7.1),
            Peliculas(id=71285784, titulo='Avengers: Age of Ultron', genero='Animación', rating=7.6),
            Peliculas(id=47377474, titulo='The Dark Knight Rises', genero='Bélico', rating=8.4),
            Peliculas(id=69065378, titulo='Black Panther', genero='Superhéroes', rating=8.0),
            Peliculas(id=11615401, titulo='The Princess Bride', genero='Aventura', rating=7.5),
            Peliculas(id=48119451, titulo='The Thirteenth Year', genero='Fantasía', rating=6.6),
            Peliculas(id=87114047, titulo='Jump In!', genero='Deportes', rating=5.4),
            Peliculas(id=49034902, titulo='The Godfather', genero='Crimen', rating=9.2),
            Peliculas(id=17287405, titulo='The Hunchback of Notre Dame', genero='Comedia', rating=6.9),
        ]
        expected_titulo = 'The Hunchback of Notre Dame'

        generador = (p for p in lista_peliculas)
        resultado = titulo_mas_largo(generador)
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, expected_titulo)

    def test_1(self):
        """
        Peliculas empatadas con el mismo largo
        """
        lista_peliculas = [
            Peliculas(id=70752273, titulo='Gladiator', genero='Crimen', rating=8.5),
            Peliculas(id=33896817, titulo='La La Land', genero='Musical', rating=8.0),
            Peliculas(id=45064961, titulo='Big Hero 6', genero='Animación', rating=7.8),
            Peliculas(id=62764502, titulo='Toy Story', genero='Animación', rating=8.3),
            Peliculas(id=57395306, titulo='Inuyasha', genero='Animación', rating=8.4),
            Peliculas(id=89587896, titulo='Whiplash', genero='Drama', rating=8.5),
            Peliculas(id=98811629, titulo='Braveheart', genero='Animación', rating=8.5),
            Peliculas(id=76172796, titulo='Inception', genero='Ciencia Ficción', rating=8.8),
            Peliculas(id=58643843, titulo='Iron Man 2', genero='Animación', rating=7.0),
            Peliculas(id=23678361, titulo='Scarface', genero='Crimen', rating=8.8),
            Peliculas(id=89737370, titulo='Iron Man', genero='Animación', rating=7.6),
            Peliculas(id=61384134, titulo='Mamma Mia', genero='Musical', rating=10.0),
            Peliculas(id=81744489, titulo='Cow Belles', genero='Comedia', rating=6.1),
            Peliculas(id=51151305, titulo='Pocahontas', genero='Fantasía', rating=7.8),
        ]

        expected_titulo = 'Braveheart'

        generador = (p for p in lista_peliculas)
        resultado = titulo_mas_largo(generador)
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, expected_titulo)

    def test_2(self):
        """
        Una pelicula con el título más largo
        """
        lista_peliculas = [
            Peliculas(id=99972342, titulo='The Cheetah Girls 2', genero='Comedia', rating=5.9),
            Peliculas(id=61161814, titulo='High School Musical', genero='Musical', rating=6.4),
            Peliculas(id=73079370, titulo='Thor: The Dark World', genero='Animación', rating=7.2),
            Peliculas(id=95817124, titulo='Fight Club', genero='Crimen', rating=8.8),
            Peliculas(id=71903918, titulo='Shrek', genero='Animación', rating=7.8),
        ]
        expected_titulo = 'Thor: The Dark World'

        generador = (p for p in lista_peliculas)
        resultado = titulo_mas_largo(generador)
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, expected_titulo)

    def test_3(self):
        """
        Peliculas empatadas con el mismo largo y el mismo rating
        """
        lista_peliculas = [
            Peliculas(id=58643843, titulo='Iron Man 2', genero='Animación', rating=7.0),
            Peliculas(id=55774654, titulo='The Pianist', genero='Superhéroes', rating=8.5),
            Peliculas(id=23653810, titulo='Reservoir Dogs', genero='Superhéroes', rating=8.3),
            Peliculas(id=59197164, titulo='Motocrossed', genero='Deportes', rating=6.6),
            Peliculas(id=32608840, titulo='Johnny Tsunami', genero='Deportes', rating=6.3),
            Peliculas(id=87538292, titulo='Monsters Inc.', genero='Animación', rating=8.1),
            Peliculas(id=52568632, titulo='Shutter Island', genero='Superhéroes', rating=8.5),
            Peliculas(id=69065378, titulo='Black Panther', genero='Superhéroes', rating=8.0),
            Peliculas(id=40873645, titulo='The Terminator', genero='Ciencia Ficción', rating=8.5),
            Peliculas(id=84580833, titulo='Wreck-It Ralph', genero='Animación', rating=8.5),
            Peliculas(id=42475848, titulo='Spirited Away', genero='Animación', rating=8.6),
            Peliculas(id=45064961, titulo='Big Hero 6', genero='Animación', rating=7.8),
            Peliculas(id=79145064, titulo='Forrest Gump', genero='Ciencia', rating=8.8),
            Peliculas(id=30060914, titulo='Get a Clue', genero='Comedia', rating=6.2),
        ]
        expected_titulo = 'Wreck-It Ralph'

        generador = (p for p in lista_peliculas)
        resultado = titulo_mas_largo(generador)
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, expected_titulo)

    def test_4(self):
        """
        Todas las peliculas del mismo largo y algunas con el mismo rating
        """
        lista_peliculas = [
            Peliculas(id=63162203, titulo='The Departed', genero='Animación', rating=8.2),
            Peliculas(id=79145064, titulo='Forrest Gump', genero='Ciencia', rating=8.8),
            Peliculas(id=40312799, titulo='Finding Nemo', genero='Misterio', rating=8.2),
            Peliculas(id=91153956, titulo='Blade Runner', genero='Ciencia Ficción', rating=8.8),
            Peliculas(id=34755557, titulo='The Notebook', genero='Western', rating=7.8),
            Peliculas(id=51512157, titulo='Pulp Fiction', genero='Crimen', rating=8.8),
            Peliculas(id=62863901, titulo='The Prestige', genero='Superhéroes', rating=8.6),
            Peliculas(id=11164686, titulo='Interstellar', genero='Ciencia Ficción', rating=8.6),
        ]
        expected_titulo = 'Pulp Fiction'

        generador = (p for p in lista_peliculas)
        resultado = titulo_mas_largo(generador)
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, expected_titulo)


if __name__ == '__main__':
    unittest.main(verbosity=2)
