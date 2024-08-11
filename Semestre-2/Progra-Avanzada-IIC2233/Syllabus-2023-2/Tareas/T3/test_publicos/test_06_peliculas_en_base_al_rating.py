import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import peliculas_en_base_al_rating
from utilidades import Peliculas
from typing import Generator

class TestPeliculasEnBaseAlRating(unittest.TestCase):

    def test_0(self):
        """
        Test basico
        """
        lista_peliculas = [
            Peliculas(id=21261768, titulo="The Jungle Book", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=75759551, titulo="The Lion King", genero="Animación", rating=8.5),
            Peliculas(id=47191880, titulo="Thor", genero="Animación", rating=7.2),
            Peliculas(id=51512157, titulo="Pulp Fiction", genero="Crimen", rating=8.2),
            Peliculas(id=36540564, titulo="Tarzan", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=76916171, titulo="Captain America: The Winter Soldier", genero="Animación", rating=7.8),
            Peliculas(id=51151305, titulo="Pocahontas", genero="fantasía", rating=7.8),
            Peliculas(id=34321575, titulo="Ant-Man and The Wasp", genero="Superhéroes", rating=7.1),
            Peliculas(id=70752273, titulo="Gladiator", genero="Crimen", rating=8.5),
            Peliculas(id=90803337, titulo="High School Musical 2", genero="Musical", rating=6.1),
            Peliculas(id=19177277, titulo="High School Musical 3", genero="Musical", rating=6.9),
            Peliculas(id=11568343, titulo="The Social Network", genero="Drama", rating=7.7),
            Peliculas(id=38463448, titulo="Spider-Man: Homecoming", genero="Superhéroes", rating=7.5),
            Peliculas(id=28527704, titulo="Princess Mononoke", genero="Animación", rating=8.4),
            Peliculas(id=52568632, titulo="Shutter Island", genero="Superhéroes", rating=8.5),
            Peliculas(id=89737370, titulo="Iron Man", genero="Animación", rating=7.6),
            Peliculas(id=83566857, titulo="The Usual Suspects", genero="Superhéroes", rating=8.5),
            Peliculas(id=58643843, titulo="Iron Man 2", genero="Animación", rating=7.0),
            Peliculas(id=75901837, titulo="Akira", genero="Animación", rating=8.6),
            Peliculas(id=32152163, titulo="The Princess Diaries", genero="Comedia", rating=6.2),
        ]

        expected_list_peliculas = [
            Peliculas(id=75759551, titulo='The Lion King', genero='Animación', rating=8.5),
            Peliculas(id=47191880, titulo='Thor', genero='Animación', rating=7.2),
            Peliculas(id=76916171, titulo='Captain America: The Winter Soldier', genero='Animación', rating=7.8),
            Peliculas(id=28527704, titulo='Princess Mononoke', genero='Animación', rating=8.4),
            Peliculas(id=89737370, titulo='Iron Man', genero='Animación', rating=7.6),
            Peliculas(id=58643843, titulo='Iron Man 2', genero='Animación', rating=7.0),
            Peliculas(id=75901837, titulo='Akira', genero='Animación', rating=8.6)
        ]

        resultado = peliculas_en_base_al_rating(iter(lista_peliculas), "Animación", 7.0, 8.6)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        list_resultado = list(resultado)
        for n in expected_list_peliculas:
            self.assertIn(n, list_resultado)
        for n in list_resultado:
            self.assertIn(n, expected_list_peliculas)


    def test_1(self):
        """
        Genero sin rating en el rango
        """
        lista_peliculas = [
            Peliculas(id=89587896, titulo="Whiplash", genero="Drama", rating=8.5),
            Peliculas(id=16359236, titulo="Mulan", genero="Deportes", rating=7.8),
            Peliculas(id=87114047, titulo="Jump In!", genero="Deportes", rating=5.4),
            Peliculas(id=75259113, titulo="Up", genero="Crimen", rating=8.4),
            Peliculas(id=76172796, titulo="Inception", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=42456754, titulo="The Matrix Reloaded", genero="fantasía", rating=7.2),
            Peliculas(id=65976883, titulo="Titanic", genero="Drama", rating=7.8),
            Peliculas(id=83829256, titulo="Stuck in the Suburbs", genero="Comedia", rating=6.2),
            Peliculas(id=35100234, titulo="Terminator 2: Judgment Day", genero="Animación", rating=8.5),
            Peliculas(id=35569845, titulo="The Princess Diaries 2", genero="Comedia", rating=5.8),
            Peliculas(id=71903918, titulo="Shrek", genero="Animación", rating=7.8),
            Peliculas(id=98811629, titulo="Braveheart", genero="Animación", rating=8.5),
            Peliculas(id=78376301, titulo="Smart House", genero="Ciencia Ficción", rating=6.2),
            Peliculas(id=54090274, titulo="Cadet Kelly", genero="Comedia", rating=6.2),
            Peliculas(id=89708109, titulo="Captain America: Civil War", genero="Superhéroes", rating=8.0),
            Peliculas(id=38937194, titulo="Tangled", genero="Animación", rating=8.0),
            Peliculas(id=75759551, titulo="The Lion King", genero="Animación", rating=8.5),
            Peliculas(id=66226007, titulo="The Godfather: Part II", genero="Ciencia Ficción", rating=9.0),
            Peliculas(id=40267632, titulo="The Imitation Game", genero="Drama", rating=9.6),
            Peliculas(id=27868789, titulo="Guardians of the Galaxy", genero="Animación", rating=7.5),
        ]

        expected_list_peliculas = []

        expected_filter_peliculas = filter(lambda pelicula: True, expected_list_peliculas)
        resultado = peliculas_en_base_al_rating(iter(lista_peliculas), "Animación", 8.9, 9.9)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(resultado, expected_filter_peliculas)

    def test_2(self):
        """
        Rating en el limite
        """
        lista_peliculas = [
            Peliculas(id=69065378, titulo="Black Panther", genero="Superhéroes", rating=8.0),
            Peliculas(id=28527704, titulo="Princess Mononoke", genero="Animación", rating=8.4),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=79145064, titulo="Forrest Gump", genero="Ciencia", rating=8.8),
            Peliculas(id=29533644, titulo="Saving Private Ryan", genero="Superhéroes", rating=8.6),
            Peliculas(id=75901837, titulo="Akira", genero="Animación", rating=8.6),
            Peliculas(id=51418590, titulo="The Shawshank Redemption", genero="Drama", rating=9.3),
            Peliculas(id=75759551, titulo="The Lion King", genero="Animación", rating=8.5),
            Peliculas(id=16359236, titulo="Mulan", genero="Deportes", rating=7.8),
            Peliculas(id=95817124, titulo="Fight Club", genero="Crimen", rating=8.8),
            Peliculas(id=21803572, titulo="Avengers", genero="Acción", rating=8.0),
            Peliculas(id=98811629, titulo="Braveheart", genero="Animación", rating=8.5),
            Peliculas(id=54090274, titulo="Cadet Kelly", genero="Comedia", rating=6.2),
            Peliculas(id=42475848, titulo="Spirited Away", genero="Animación", rating=8.6),
            Peliculas(id=96374386, titulo="The Lord of the Rings: The Two Towers", genero="Animación", rating=8.7),
            Peliculas(id=54541808, titulo="Matilda", genero="Comedia", rating=6.9),
            Peliculas(id=64787434, titulo="Casino", genero="Western", rating=8.5),
            Peliculas(id=27868789, titulo="Guardians of the Galaxy", genero="Animación", rating=7.5),
            Peliculas(id=78376301, titulo="Smart House", genero="Ciencia Ficción", rating=6.2),
            Peliculas(id=93369344, titulo="Avengers: Infinity War", genero="Superhéroes", rating=8.4),
        ]

        expected_list_peliculas = [Peliculas(id=49895401, titulo='Pixel Perfect', genero='Ciencia Ficción', rating=6.0)]

        resultado = peliculas_en_base_al_rating(iter(lista_peliculas), "Ciencia Ficción", 5.0, 6.0)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        list_resultado = list(resultado)
        for n in expected_list_peliculas:
            self.assertIn(n, list_resultado)
        for n in list_resultado:
            self.assertIn(n, expected_list_peliculas)

    def test_3(self):
        """
        Solo una pelicula con rating en el limite
        """
        lista_peliculas = [
            Peliculas(id=72588542, titulo="Frozen", genero="Animación", rating=7.4),
            Peliculas(id=89756869, titulo="The Emperor's New Groove", genero="Deportes", rating=6.9),
            Peliculas(id=79145064, titulo="Forrest Gump", genero="Ciencia", rating=8.8),
            Peliculas(id=16359236, titulo="Mulan", genero="Deportes", rating=7.8),
            Peliculas(id=71903918, titulo="Shrek", genero="Animación", rating=7.8),
            Peliculas(id=63162203, titulo="The Departed", genero="Animación", rating=8.2),
            Peliculas(id=19745617, titulo="The Dark Knight", genero="Acción", rating=9.0),
            Peliculas(id=95230455, titulo="Your Name", genero="Animación", rating=8.4),
            Peliculas(id=58329437, titulo="My Neighbor Totoro", genero="Animación", rating=8.6),
            Peliculas(id=76916171, titulo="Captain America: The Winter Soldier", genero="Animación", rating=7.8),
            Peliculas(id=75259113, titulo="Up", genero="Crimen", rating=8.4),
            Peliculas(id=51151305, titulo="Pocahontas", genero="fantasía", rating=7.8),
            Peliculas(id=84580833, titulo="Wreck-It Ralph", genero="Animación", rating=7.5),
            Peliculas(id=73079370, titulo="Thor: The Dark World", genero="Animación", rating=7.2),
            Peliculas(id=47377474, titulo="The Dark Knight Rises", genero="Bélico", rating=8.4),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=11164686, titulo="Interstellar", genero="Ciencia Ficción", rating=8.6),
            Peliculas(id=67027889, titulo="Seven Samurai", genero="Crimen", rating=9.0),
            Peliculas(id=36540564, titulo="Tarzan", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=65976883, titulo="Titanic", genero="Drama", rating=7.8),
        ]

        expected_list_peliculas = [Peliculas(id=19745617, titulo='The Dark Knight', genero='Acción', rating=9.0)]

        resultado = peliculas_en_base_al_rating(iter(lista_peliculas), "Acción", 6.9, 9.0)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        list_resultado = list(resultado)
        for n in expected_list_peliculas:
            self.assertIn(n, list_resultado)
        for n in list_resultado:
            self.assertIn(n, expected_list_peliculas)

    def test_4(self):
        """
        Genero sin peliculas
        """
        lista_peliculas = [
            Peliculas(id=61234416, titulo="Howl's Moving Castle", genero="Animación", rating=8.9),
            Peliculas(id=75901837, titulo="Akira", genero="Animación", rating=8.6),
            Peliculas(id=35569845, titulo="The Princess Diaries 2", genero="Comedia", rating=5.8),
            Peliculas(id=40873645, titulo="The Terminator", genero="Ciencia Ficción", rating=8.5),
            Peliculas(id=33612645, titulo="Goodfellas", genero="Animación", rating=8.9),
            Peliculas(id=21261768, titulo="The Jungle Book", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=23678361, titulo="Scarface", genero="Crimen", rating=8.8),
            Peliculas(id=75421892, titulo="The Little Mermaid", genero="Aventura", rating=8.0),
            Peliculas(id=95054110, titulo="Thor: Ragnarok", genero="Superhéroes", rating=7.9),
            Peliculas(id=32608840, titulo="Johnny Tsunami", genero="Deportes", rating=6.3),
            Peliculas(id=82620795, titulo="Zenon: Girl of the 21st Century", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=72588542, titulo="Frozen", genero="Animación", rating=7.4),
            Peliculas(id=23653810, titulo="Reservoir Dogs", genero="Superhéroes", rating=8.3),
            Peliculas(id=95413069, titulo="The Cheetah Girls", genero="Comedia", rating=5.8),
            Peliculas(id=51151305, titulo="Pocahontas", genero="fantasía", rating=7.8),
            Peliculas(id=46804999, titulo="Guardians of the Galaxy Vol. 2", genero="Superhéroes", rating=7.1),
            Peliculas(id=87538292, titulo="Monsters Inc.", genero="Animación", rating=8.1),
            Peliculas(id=35100234, titulo="Terminator 2: Judgment Day", genero="Animación", rating=8.5),
            Peliculas(id=83566857, titulo="The Usual Suspects", genero="Superhéroes", rating=8.5),
            Peliculas(id=58329437, titulo="My Neighbor Totoro", genero="Animación", rating=8.6),
        ]

        expected_list_peliculas = []

        expected_filter_peliculas = filter(lambda pelicula: True, expected_list_peliculas)
        resultado = peliculas_en_base_al_rating(iter(lista_peliculas), "Ciencia", 5.0, 5.7)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(resultado, expected_filter_peliculas)

if __name__ == '__main__':
    unittest.main(verbosity=2)