import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import pelicula_genero_mayor_rating
from utilidades import Peliculas

class TestPeliculaGeneroMayorRating(unittest.TestCase):

    def test_0(self):
        """
        Test basico
        """
        lista_peliculas = [
            Peliculas(id=69065378, titulo="Black Panther", genero="Superhéroes", rating=8.0),
            Peliculas(id=76916171, titulo="Captain America: The Winter Soldier", genero="Animación", rating=7.8),
            Peliculas(id=87538292, titulo="Monsters Inc.", genero="Animación", rating=8.1),
            Peliculas(id=75203860, titulo="Kill Bill: Vol. 1", genero="Superhéroes", rating=8.1),
            Peliculas(id=42038936, titulo="The Matrix Revolutions", genero="Fantasía", rating=7.3),
            Peliculas(id=23653810, titulo="Reservoir Dogs", genero="Superhéroes", rating=8.3),
            Peliculas(id=66226007, titulo="The Godfather: Part II", genero="Ciencia Ficción", rating=9.0),
            Peliculas(id=64787434, titulo="Casino", genero="Western", rating=8.5),
            Peliculas(id=25227924, titulo="Kill Bill: Vol. 2", genero="Western", rating=8.7),
            Peliculas(id=40873645, titulo="The Terminator", genero="Ciencia Ficción", rating=8.5),
            Peliculas(id=61161814, titulo="High School Musical", genero="Musical", rating=6.4),
            Peliculas(id=38937194, titulo="Tangled", genero="Animación", rating=8.0),
            Peliculas(id=75421892, titulo="The Little Mermaid", genero="Aventura", rating=8.0),
            Peliculas(id=79145064, titulo="Forrest Gump", genero="Ciencia", rating=8.8),
            Peliculas(id=23221543, titulo="Halloweentown", genero="Fantasía", rating=6.3),
            Peliculas(id=87210469, titulo="Doctor Strange", genero="Superhéroes", rating=7.3),
            Peliculas(id=75901837, titulo="Akira", genero="Animación", rating=8.6),
            Peliculas(id=73020923, titulo="Captain America: The First Avenger", genero="Animación", rating=7.0),
            Peliculas(id=29533644, titulo="Saving Private Ryan", genero="Superhéroes", rating=8.6),
            Peliculas(id=42475848, titulo="Spirited Away", genero="Animación", rating=8.6),
            Peliculas(id=40312799, titulo="Finding Nemo", genero="Misterio", rating=8.2),
            Peliculas(id=81187977, titulo="Moana", genero="Animación", rating=8.0),
            Peliculas(id=27868789, titulo="Guardians of the Galaxy", genero="Animación", rating=7.5),
            Peliculas(id=58329437, titulo="My Neighbor Totoro", genero="Animación", rating=8.6),
            Peliculas(id=67202232, titulo="Memento", genero="Superhéroes", rating=8.5),
            Peliculas(id=96374386, titulo="The Lord of the Rings: The Two Towers", genero="Animación", rating=8.7),
            Peliculas(id=61234416, titulo="Howl's Moving Castle", genero="Animación", rating=8.9),
            Peliculas(id=78947971, titulo="Beauty and the Beast", genero="Animación", rating=8.9),
            Peliculas(id=43516202, titulo="The Great Gatsby", genero="Drama", rating=8.5),
            Peliculas(id=67027889, titulo="Seven Samurai", genero="Crimen", rating=9.0),
        ]

        resultado = pelicula_genero_mayor_rating(lista_peliculas, "Animación")

        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, "Howl's Moving Castle")


    def test_1(self):
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
            Peliculas(id=32608840, titulo="Johnny Tsunami", genero="Deportes", rating=6.3),
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
        resultado = pelicula_genero_mayor_rating(lista_peliculas, "Ciencia")

        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, "")

    def test_2(self):
        """
        Genero con una pelicula
        """
        lista_peliculas = [
            Peliculas(id=65976883, titulo="Titanic", genero="Drama", rating=7.8),
            Peliculas(id=73020923, titulo="Captain America: The First Avenger", genero="Animación", rating=7.0),
            Peliculas(id=69065378, titulo="Black Panther", genero="Superhéroes", rating=8.0),
            Peliculas(id=19177277, titulo="High School Musical 3", genero="Musical", rating=6.9),
            Peliculas(id=23221543, titulo="Halloweentown", genero="Fantasía", rating=6.3),
            Peliculas(id=62764502, titulo="Toy Story", genero="Animación", rating=8.3),
            Peliculas(id=27868789, titulo="Guardians of the Galaxy", genero="Animación", rating=7.5),
            Peliculas(id=32152163, titulo="The Princess Diaries", genero="Comedia", rating=6.2),
            Peliculas(id=34304754, titulo="Iron Man 3", genero="Animación", rating=7.1),
            Peliculas(id=81169279, titulo="The Lord of the Rings: The Return of the King", genero="Animación", rating=8.7),
            Peliculas(id=59848286, titulo="The Silence of the Lambs", genero="Suspense", rating=8.6),
            Peliculas(id=25035329, titulo="The Matrix", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=81591753, titulo="Zootopia", genero="Animación", rating=8.0),
            Peliculas(id=23653810, titulo="Reservoir Dogs", genero="Superhéroes", rating=8.3),
            Peliculas(id=63162203, titulo="The Departed", genero="Animación", rating=8.2),
            Peliculas(id=90803337, titulo="High School Musical 2", genero="Musical", rating=6.1),
            Peliculas(id=76004798, titulo="Incredibles", genero="Animación", rating=8.0),
            Peliculas(id=47191880, titulo="Thor", genero="Animación", rating=7.2),
            Peliculas(id=85032662, titulo="Aladdin", genero="Animación", rating=8.0),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=66226007, titulo="The Godfather: Part II", genero="Ciencia Ficción", rating=9.0),
            Peliculas(id=58643843, titulo="Iron Man 2", genero="Animación", rating=7.0),
            Peliculas(id=73079370, titulo="Thor: The Dark World", genero="Animación", rating=7.2),
            Peliculas(id=21803572, titulo="Avengers", genero="Acción", rating=8.0),
            Peliculas(id=11568343, titulo="The Social Network", genero="Drama", rating=7.7),
            Peliculas(id=87114047, titulo="Jump In!", genero="Deportes", rating=5.4),
            Peliculas(id=45745398, titulo="The Green Mile", genero="Animación", rating=8.2),
            Peliculas(id=67202232, titulo="Memento", genero="Superhéroes", rating=8.5),
            Peliculas(id=41068976, titulo="Cinderella", genero="Animación", rating=7.1),
            Peliculas(id=19745617, titulo="The Dark Knight", genero="Acción", rating=9.0),
        ]
        resultado = pelicula_genero_mayor_rating(lista_peliculas, "Deportes")

        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, "Jump In!")

    def test_3(self):
        """
        Dos peliculas con el mismo rating
        """
        lista_peliculas = [
            Peliculas(id=93369344, titulo="Avengers: Infinity War", genero="Superhéroes", rating=8.4),
            Peliculas(id=23678361, titulo="Scarface", genero="Crimen", rating=8.8),
            Peliculas(id=71903918, titulo="Shrek", genero="Animación", rating=7.8),
            Peliculas(id=39971720, titulo="Ant-Man", genero="Superhéroes", rating=7.5),
            Peliculas(id=75421892, titulo="The Little Mermaid", genero="Aventura", rating=8.0),
            Peliculas(id=85032662, titulo="Aladdin", genero="Animación", rating=8.0),
            Peliculas(id=41068976, titulo="Cinderella", genero="Animación", rating=7.1),
            Peliculas(id=21261768, titulo="The Jungle Book", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=75259113, titulo="Up", genero="Crimen", rating=8.4),
            Peliculas(id=84580833, titulo="Wreck-It Ralph", genero="Animación", rating=7.5),
            Peliculas(id=25227924, titulo="Kill Bill: Vol. 2", genero="Western", rating=8.7),
            Peliculas(id=45064961, titulo="Big Hero 6", genero="Animación", rating=7.8),
            Peliculas(id=87114047, titulo="Jump In!", genero="Deportes", rating=5.4),
            Peliculas(id=51151305, titulo="Pocahontas", genero="Fantasía", rating=7.8),
            Peliculas(id=89587896, titulo="Whiplash", genero="Drama", rating=8.5),
            Peliculas(id=52568632, titulo="Shutter Island", genero="Superhéroes", rating=8.5),
            Peliculas(id=46804999, titulo="Guardians of the Galaxy Vol. 2", genero="Superhéroes", rating=9.0),
            Peliculas(id=54090274, titulo="Cadet Kelly", genero="Comedia", rating=6.2),
            Peliculas(id=29533644, titulo="Saving Private Ryan", genero="Superhéroes", rating=9.0),
            Peliculas(id=89756869, titulo="The Emperor's New Groove", genero="Deportes", rating=6.9),
            Peliculas(id=99972342, titulo="The Cheetah Girls 2", genero="Comedia", rating=5.9),
            Peliculas(id=40873645, titulo="The Terminator", genero="Ciencia Ficción", rating=8.5),
            Peliculas(id=11615401, titulo="The Princess Bride", genero="Aventura", rating=7.5),
            Peliculas(id=35100234, titulo="Terminator 2: Judgment Day", genero="Animación", rating=8.5),
            Peliculas(id=34755557, titulo="The Notebook", genero="Western", rating=7.8),
            Peliculas(id=40312799, titulo="Finding Nemo", genero="Misterio", rating=8.2),
            Peliculas(id=42456754, titulo="The Matrix Reloaded", genero="Fantasía", rating=7.2),
            Peliculas(id=62863901, titulo="The Prestige", genero="Superhéroes", rating=9.0),
            Peliculas(id=48119451, titulo="The Thirteenth Year", genero="Fantasía", rating=6.6),
            Peliculas(id=55774654, titulo="The Pianist", genero="Superhéroes", rating=9.0),
        ]
        resultado = pelicula_genero_mayor_rating(lista_peliculas, "Superhéroes")

        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, "Guardians of the Galaxy Vol. 2")

    def test_4(self):
        """
        Dos peluculas
        """
        lista_peliculas = [
            Peliculas(id=25035329, titulo="The Matrix", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=78376301, titulo="Smart House", genero="Ciencia Ficción", rating=6.2),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
            Peliculas(id=71285784, titulo="Avengers: Age of Ultron", genero="Animación", rating=7.6),
            Peliculas(id=75421892, titulo="The Little Mermaid", genero="Aventura", rating=8.0),
            Peliculas(id=87538292, titulo="Monsters Inc.", genero="Animación", rating=8.1),
            Peliculas(id=89587896, titulo="Whiplash", genero="Drama", rating=8.5),
            Peliculas(id=61161814, titulo="High School Musical", genero="Musical", rating=6.4),
            Peliculas(id=49034902, titulo="The Godfather", genero="Crimen", rating=9.2),
            Peliculas(id=75203860, titulo="Kill Bill: Vol. 1", genero="Superhéroes", rating=8.1),
            Peliculas(id=21803572, titulo="Avengers", genero="Acción", rating=8.0),
            Peliculas(id=23425933, titulo="The Revenant", genero="Aventura", rating=8.0),
            Peliculas(id=73079370, titulo="Thor: The Dark World", genero="Animación", rating=7.2),
            Peliculas(id=23678361, titulo="Scarface", genero="Crimen", rating=8.8),
            Peliculas(id=58329437, titulo="My Neighbor Totoro", genero="Animación", rating=8.6),
            Peliculas(id=95230455, titulo="Your Name", genero="Animación", rating=8.4),
            Peliculas(id=62764502, titulo="Toy Story", genero="Animación", rating=8.3),
            Peliculas(id=45745398, titulo="The Green Mile", genero="Animación", rating=8.2),
            Peliculas(id=76004798, titulo="Incredibles", genero="Animación", rating=8.0),
            Peliculas(id=59848286, titulo="The Silence of the Lambs", genero="Suspense", rating=8.6),
            Peliculas(id=33896817, titulo="La La Land", genero="Musical", rating=8.0),
            Peliculas(id=16359236, titulo="Mulan", genero="Deportes", rating=7.8),
            Peliculas(id=34321575, titulo="Ant-Man and The Wasp", genero="Superhéroes", rating=7.1),
            Peliculas(id=98009659, titulo="Twitches", genero="Fantasía", rating=6.7),
            Peliculas(id=81169279, titulo="The Lord of the Rings: The Return of the King", genero="Animación", rating=8.7),
            Peliculas(id=61384134, titulo="Mamma Mia", genero="Musical", rating=10.0),
            Peliculas(id=96374386, titulo="The Lord of the Rings: The Two Towers", genero="Animación", rating=8.7),
            Peliculas(id=95054110, titulo="Thor: Ragnarok", genero="Superhéroes", rating=7.9),
            Peliculas(id=95413069, titulo="The Cheetah Girls", genero="Comedia", rating=5.8),
            Peliculas(id=99972342, titulo="The Cheetah Girls 2", genero="Comedia", rating=5.9),
        ]
        resultado = pelicula_genero_mayor_rating(lista_peliculas, "Comedia")

        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, "The Cheetah Girls 2")

if __name__ == '__main__':
    unittest.main(verbosity=2)