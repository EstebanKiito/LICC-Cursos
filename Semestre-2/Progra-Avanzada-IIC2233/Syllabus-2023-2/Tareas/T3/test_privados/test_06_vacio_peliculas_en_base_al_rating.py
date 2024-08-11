import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import peliculas_en_base_al_rating
from utilidades import Peliculas
from typing import Generator


class TestVacioPeliculasEnBaseAlRating(unittest.TestCase):

    def test_0(self):
        """
        Genero sin rating en el rango
        """
        lista_peliculas = [
            Peliculas(id=89587896, titulo="Whiplash", genero="Drama", rating=8.5),
            Peliculas(id=98811629, titulo="Braveheart", genero="Animación", rating=8.5),
            Peliculas(id=27868789, titulo="Guardians of the Galaxy", genero="Animación", rating=7.5),
            Peliculas(id=75259113, titulo="Up", genero="Crimen", rating=8.4),
            Peliculas(id=76172796, titulo="Inception", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=42456754, titulo="The Matrix Reloaded", genero="fantasía", rating=7.2),
            Peliculas(id=65976883, titulo="Titanic", genero="Drama", rating=7.8),
            Peliculas(id=83829256, titulo="Stuck in the Suburbs", genero="Comedia", rating=6.2),
            Peliculas(id=54090274, titulo="Cadet Kelly", genero="Comedia", rating=6.2),
            Peliculas(id=35100234, titulo="Terminator 2: Judgment Day", genero="Animación", rating=8.5),
            Peliculas(id=71903918, titulo="Shrek", genero="Animación", rating=7.8),
            Peliculas(id=78376301, titulo="Smart House", genero="Ciencia Ficción", rating=6.2),
            Peliculas(id=87114047, titulo="Jump In!", genero="Deportes", rating=5.4),
            Peliculas(id=35569845, titulo="The Princess Diaries 2", genero="Comedia", rating=5.8),
            Peliculas(id=89708109, titulo="Captain America: Civil War", genero="Superhéroes", rating=8.0),
            Peliculas(id=38937194, titulo="Tangled", genero="Animación", rating=8.0),
            Peliculas(id=16359236, titulo="Mulan", genero="Deportes", rating=7.8),
            Peliculas(id=66226007, titulo="The Godfather: Part II", genero="Ciencia Ficción", rating=9.0),
            Peliculas(id=75759551, titulo="The Lion King", genero="Animación", rating=8.5),
            Peliculas(id=40267632, titulo="The Imitation Game", genero="Drama", rating=9.6),
        ]

        expected_list_peliculas = []

        resultado = peliculas_en_base_al_rating(iter(lista_peliculas), "Comedia", 8.9, 9.9)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_list_peliculas)

    def test_1(self):
        """
        Genero sin peliculas
        """
        lista_peliculas = [
            Peliculas(id=58329437, titulo="My Neighbor Totoro", genero="Animación", rating=8.6),
            Peliculas(id=75901837, titulo="Akira", genero="Animación", rating=8.6),
            Peliculas(id=35569845, titulo="The Princess Diaries 2", genero="Comedia", rating=5.8),
            Peliculas(id=23653810, titulo="Reservoir Dogs", genero="Superhéroes", rating=8.3),
            Peliculas(id=33612645, titulo="Goodfellas", genero="Animación", rating=8.9),
            Peliculas(id=21261768, titulo="The Jungle Book", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=23678361, titulo="Scarface", genero="Crimen", rating=8.8),
            Peliculas(id=75421892, titulo="The Little Mermaid", genero="Aventura", rating=8.0),
            Peliculas(id=95054110, titulo="Thor: Ragnarok", genero="Superhéroes", rating=7.9),
            Peliculas(id=32608840, titulo="Johnny Tsunami", genero="Deportes", rating=6.3),
            Peliculas(id=82620795, titulo="Zenon: Girl of the 21st Century", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=72588542, titulo="Frozen", genero="Animación", rating=7.4),
            Peliculas(id=61234416, titulo="Howl's Moving Castle", genero="Animación", rating=8.9),
            Peliculas(id=95413069, titulo="The Cheetah Girls", genero="Comedia", rating=5.8),
            Peliculas(id=40873645, titulo="The Terminator", genero="Ciencia Ficción", rating=8.5),
            Peliculas(id=51151305, titulo="Pocahontas", genero="fantasía", rating=7.8),
            Peliculas(id=46804999, titulo="Guardians of the Galaxy Vol. 2", genero="Superhéroes", rating=7.1),
            Peliculas(id=87538292, titulo="Monsters Inc.", genero="Animación", rating=8.1),
            Peliculas(id=35100234, titulo="Terminator 2: Judgment Day", genero="Animación", rating=8.5),
            Peliculas(id=83566857, titulo="The Usual Suspects", genero="Superhéroes", rating=8.5),
        ]

        expected_list_peliculas = []

        resultado = peliculas_en_base_al_rating(iter(lista_peliculas), "Ciencia", 1.0, 9.0)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_list_peliculas)


if __name__ == '__main__':
    unittest.main(verbosity=2)
