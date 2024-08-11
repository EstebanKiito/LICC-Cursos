import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import pelicula_genero_mayor_rating
from utilidades import Peliculas


class TestVacioPeliculaGeneroMayorRating(unittest.TestCase):

    def test_0(self):
        """
        Genero sin peliculas
        """
        lista_peliculas = [
            Peliculas(id=98811629, titulo="Braveheart", genero="Animación", rating=8.5),
            Peliculas(id=17287405, titulo="The Hunchback of Notre Dame", genero="Comedia", rating=6.9),
            Peliculas(id=61234416, titulo="Howl's Moving Castle", genero="Animación", rating=8.9),
            Peliculas(id=61384134, titulo="Mamma Mia", genero="Musical", rating=10.0),
            Peliculas(id=42038936, titulo="The Matrix Revolutions", genero="Fantasía", rating=7.3),
            Peliculas(id=23653810, titulo="Reservoir Dogs", genero="Superhéroes", rating=8.3),
            Peliculas(id=95413069, titulo="The Cheetah Girls", genero="Comedia", rating=5.8),
            Peliculas(id=89737370, titulo="Iron Man", genero="Animación", rating=7.6),
            Peliculas(id=34321575, titulo="Ant-Man and The Wasp", genero="Superhéroes", rating=7.1),
            Peliculas(id=41068976, titulo="Cinderella", genero="Animación", rating=7.1),
            Peliculas(id=64787434, titulo="Casino", genero="Western", rating=8.5),
            Peliculas(id=81744489, titulo="Cow Belles", genero="Comedia", rating=6.1),
            Peliculas(id=84580833, titulo="Wreck-It Ralph", genero="Animación", rating=7.5),
            Peliculas(id=40312799, titulo="Finding Nemo", genero="Misterio", rating=8.2),
            Peliculas(id=75660450, titulo="The Incredible Hulk", genero="Animación", rating=6.7),
            Peliculas(id=21261768, titulo="The Jungle Book", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=78947971, titulo="Beauty and the Beast", genero="Animación", rating=8.0),
            Peliculas(id=54541808, titulo="Matilda", genero="Comedia", rating=6.9),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=43516202, titulo="The Great Gatsby", genero="Drama", rating=8.5),
            Peliculas(id=32608840, titulo="Johnny Tsunami", genero="Comedia", rating=6.3),
            Peliculas(id=95054110, titulo="Thor: Ragnarok", genero="Superhéroes", rating=7.9),
            Peliculas(id=71285784, titulo="Avengers: Age of Ultron", genero="Animación", rating=7.6),
            Peliculas(id=11568343, titulo="The Social Network", genero="Drama", rating=7.7),
            Peliculas(id=78147558, titulo="Se7en", genero="Superhéroes", rating=8.6),
            Peliculas(id=96374386, titulo="The Lord of the Rings: The Two Towers", genero="Animación", rating=8.7),
            Peliculas(id=89587896, titulo="Whiplash", genero="Drama", rating=8.5),
            Peliculas(id=54090274, titulo="Cadet Kelly", genero="Comedia", rating=6.2),
            Peliculas(id=21803572, titulo="Avengers", genero="Acción", rating=8.0),
            Peliculas(id=35569845, titulo="The Princess Diaries 2", genero="Comedia", rating=5.8),
        ]
        resultado = pelicula_genero_mayor_rating(lista_peliculas, "Deportes")

        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, "")


if __name__ == '__main__':
    unittest.main(verbosity=2)
