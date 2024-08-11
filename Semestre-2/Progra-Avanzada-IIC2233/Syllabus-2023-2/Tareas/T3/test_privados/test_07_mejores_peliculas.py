import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import mejores_peliculas
from utilidades import Peliculas
from typing import Generator


class TestMejoresPeliculas(unittest.TestCase):

    def test_0(self):
        """
        Menos de 20 peliculas
        """
        peliculas = [
            Peliculas(id=83619224, titulo='Iron Man 2', genero='Superhéroes', rating=8.4),
            Peliculas(id=51470957, titulo='Titanic', genero='Drama', rating=9.2),
            Peliculas(id=25087696, titulo='Inuyasha', genero='Ciencia Ficción', rating=8.7),
            Peliculas(id=58381804, titulo='Zootopia', genero='Animación', rating=8.5),
            Peliculas(id=79197431, titulo='The Little Mermaid', genero='Ciencia', rating=8.7),
            Peliculas(id=70804640, titulo='The Usual Suspects', genero='Crimen', rating=8.4),
            Peliculas(id=90855704, titulo='The Princess Diaries 2', genero='Musical', rating=6.0),
        ]
        expected_peliculas = [
            Peliculas(id=83619224, titulo='Iron Man 2', genero='Superhéroes', rating=8.4),
            Peliculas(id=51470957, titulo='Titanic', genero='Drama', rating=9.2),
            Peliculas(id=25087696, titulo='Inuyasha', genero='Ciencia Ficción', rating=8.7),
            Peliculas(id=58381804, titulo='Zootopia', genero='Animación', rating=8.5),
            Peliculas(id=79197431, titulo='The Little Mermaid', genero='Ciencia', rating=8.7),
            Peliculas(id=70804640, titulo='The Usual Suspects', genero='Crimen', rating=8.4),
            Peliculas(id=90855704, titulo='The Princess Diaries 2', genero='Musical', rating=6.0),
        ]

        generador = (p for p in peliculas)
        resultado = mejores_peliculas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_peliculas)

    def test_1(self):
        """
        Exactamente 20 peliculas
        """
        peliculas = [
            Peliculas(id=16411603, titulo='American History X', genero='Deportes', rating=7.7),
            Peliculas(id=19797984, titulo='Big Hero 6', genero='Acción', rating=8.9),
            Peliculas(id=87262836, titulo='Seven Samurai', genero='Superhéroes', rating=7.2),
            Peliculas(id=79197431, titulo='The Little Mermaid', genero='Ciencia', rating=8.7),
            Peliculas(id=91206323, titulo='Inglourious Basterds', genero='Ciencia Ficción', rating=8.0),
            Peliculas(id=11217053, titulo='The Departed', genero='Ciencia Ficción', rating=8.5),
            Peliculas(id=35152601, titulo='Django Unchained', genero='Animación', rating=8.4),
            Peliculas(id=17339772, titulo='Iron Man', genero='Comedia', rating=6.8),
            Peliculas(id=95869491, titulo='Your Name', genero='Crimen', rating=8.7),
            Peliculas(id=96426753, titulo='Inception', genero='Animación', rating=8.6),
            Peliculas(id=51203672, titulo='Captain America: The Winter Soldier', genero='Fantasía', rating=7.7),
            Peliculas(id=69117745, titulo='The Lord of the Rings: The Two Towers', genero='Superhéroes', rating=7.9),
            Peliculas(id=21314135, titulo='The Matrix Revolutions', genero='Ciencia Ficción', rating=7.5),
            Peliculas(id=75256227, titulo='Frozen', genero='Superhéroes', rating=8.0),
            Peliculas(id=75311480, titulo='Black Panther', genero='Crimen', rating=8.3),
            Peliculas(id=46857366, titulo='High School Musical', genero='Superhéroes', rating=7.0),
            Peliculas(id=79000338, titulo='Frozen', genero='Animación', rating=7.9),
            Peliculas(id=40365166, titulo='Shrek', genero='Misterio', rating=8.1),
            Peliculas(id=43568569, titulo='Kill Bill: Vol. 2', genero='Drama', rating=8.4),
            Peliculas(id=61286783, titulo='Shrek', genero='Animación', rating=8.8),
        ]
        expected_peliculas = [
            Peliculas(id=16411603, titulo='American History X', genero='Deportes', rating=7.7),
            Peliculas(id=19797984, titulo='Big Hero 6', genero='Acción', rating=8.9),
            Peliculas(id=87262836, titulo='Seven Samurai', genero='Superhéroes', rating=7.2),
            Peliculas(id=79197431, titulo='The Little Mermaid', genero='Ciencia', rating=8.7),
            Peliculas(id=91206323, titulo='Inglourious Basterds', genero='Ciencia Ficción', rating=8.0),
            Peliculas(id=11217053, titulo='The Departed', genero='Ciencia Ficción', rating=8.5),
            Peliculas(id=35152601, titulo='Django Unchained', genero='Animación', rating=8.4),
            Peliculas(id=17339772, titulo='Iron Man', genero='Comedia', rating=6.8),
            Peliculas(id=95869491, titulo='Your Name', genero='Crimen', rating=8.7),
            Peliculas(id=96426753, titulo='Inception', genero='Animación', rating=8.6),
            Peliculas(id=51203672, titulo='Captain America: The Winter Soldier', genero='Fantasía', rating=7.7),
            Peliculas(id=69117745, titulo='The Lord of the Rings: The Two Towers', genero='Superhéroes', rating=7.9),
            Peliculas(id=21314135, titulo='The Matrix Revolutions', genero='Ciencia Ficción', rating=7.5),
            Peliculas(id=75256227, titulo='Frozen', genero='Superhéroes', rating=8.0),
            Peliculas(id=75311480, titulo='Black Panther', genero='Crimen', rating=8.3),
            Peliculas(id=46857366, titulo='High School Musical', genero='Superhéroes', rating=7.0),
            Peliculas(id=79000338, titulo='Frozen', genero='Animación', rating=7.9),
            Peliculas(id=40365166, titulo='Shrek', genero='Misterio', rating=8.1),
            Peliculas(id=43568569, titulo='Kill Bill: Vol. 2', genero='Drama', rating=8.4),
            Peliculas(id=61286783, titulo='Shrek', genero='Animación', rating=8.8),
        ]

        generador = (p for p in peliculas)
        resultado = mejores_peliculas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_peliculas)

    def test_2(self):
        """
        Más de 20 peliculas sin empate de rating
        """
        peliculas = [
            Peliculas(id=16411603, titulo='American History X', genero='Deportes', rating=8.0),
            Peliculas(id=19797984, titulo='Big Hero 6', genero='Acción', rating=9.2),
            Peliculas(id=42528215, titulo='Cadet Kelly', genero='Animación', rating=8.8),
            Peliculas(id=32770437, titulo='The Lion King', genero='Superhéroes', rating=9.1),
            Peliculas(id=58381804, titulo='Zootopia', genero='Animación', rating=8.8),
            Peliculas(id=73131737, titulo='Braveheart', genero='Animación', rating=7.4),
            Peliculas(id=30113281, titulo='The Lord of the Rings: The Two Towers', genero='Comedia', rating=6.4),
            Peliculas(id=11667768, titulo='Stuck in the Suburbs', genero='Aventura', rating=7.7),
            Peliculas(id=25087696, titulo='Inuyasha', genero='Ciencia Ficción', rating=9.0),
            Peliculas(id=80015524, titulo="Howl's Moving Castle", genero='Superhéroes', rating=8.7),
            Peliculas(id=89760476, titulo='Inglourious Basterds', genero='Superhéroes', rating=8.2),
            Peliculas(id=61214181, titulo='Camp Rock', genero='Musical', rating=6.6),
            Peliculas(id=41167485, titulo='Pocahontas', genero='Crimen', rating=8.0),
            Peliculas(id=38515815, titulo='Zenon: Girl of the 21st Century', genero='Superhéroes', rating=7.7),
            Peliculas(id=23730728, titulo="The Emperor's New Groove", genero='Crimen', rating=9.0),
            Peliculas(id=98062026, titulo='Inception', genero='Fantasía', rating=6.9),
            Peliculas(id=49947768, titulo='Iron Man', genero='Ciencia Ficción', rating=6.2),
            Peliculas(id=51564524, titulo='The Matrix Revolutions', genero='Crimen', rating=8.4),
            Peliculas(id=72640909, titulo='Captain America: Civil War', genero='Animación', rating=7.6),
            Peliculas(id=78428668, titulo='Princess Mononoke', genero='Ciencia Ficción', rating=6.4),
            Peliculas(id=32204530, titulo='My Neighbor Totoro', genero='Comedia', rating=6.4),
            Peliculas(id=67254599, titulo='Smart House', genero='Superhéroes', rating=8.7),
            Peliculas(id=48171818, titulo='Avengers: Infinity War', genero='Fantasía', rating=6.8),
            Peliculas(id=75311480, titulo='Black Panther', genero='Crimen', rating=8.6),
            Peliculas(id=54594175, titulo='The Pianist', genero='Comedia', rating=7.1),
        ]
        expected_peliculas = [
            Peliculas(id=19797984, titulo='Big Hero 6', genero='Acción', rating=9.2),
            Peliculas(id=32770437, titulo='The Lion King', genero='Superhéroes', rating=9.1),
            Peliculas(id=23730728, titulo="The Emperor's New Groove", genero='Crimen', rating=9.0),
            Peliculas(id=25087696, titulo='Inuyasha', genero='Ciencia Ficción', rating=9.0),
            Peliculas(id=42528215, titulo='Cadet Kelly', genero='Animación', rating=8.8),
            Peliculas(id=58381804, titulo='Zootopia', genero='Animación', rating=8.8),
            Peliculas(id=67254599, titulo='Smart House', genero='Superhéroes', rating=8.7),
            Peliculas(id=80015524, titulo="Howl's Moving Castle", genero='Superhéroes', rating=8.7),
            Peliculas(id=75311480, titulo='Black Panther', genero='Crimen', rating=8.6),
            Peliculas(id=51564524, titulo='The Matrix Revolutions', genero='Crimen', rating=8.4),
            Peliculas(id=89760476, titulo='Inglourious Basterds', genero='Superhéroes', rating=8.2),
            Peliculas(id=16411603, titulo='American History X', genero='Deportes', rating=8.0),
            Peliculas(id=41167485, titulo='Pocahontas', genero='Crimen', rating=8.0),
            Peliculas(id=11667768, titulo='Stuck in the Suburbs', genero='Aventura', rating=7.7),
            Peliculas(id=38515815, titulo='Zenon: Girl of the 21st Century', genero='Superhéroes', rating=7.7),
            Peliculas(id=72640909, titulo='Captain America: Civil War', genero='Animación', rating=7.6),
            Peliculas(id=73131737, titulo='Braveheart', genero='Animación', rating=7.4),
            Peliculas(id=54594175, titulo='The Pianist', genero='Comedia', rating=7.1),
            Peliculas(id=98062026, titulo='Inception', genero='Fantasía', rating=6.9),
            Peliculas(id=48171818, titulo='Avengers: Infinity War', genero='Fantasía', rating=6.8),
        ]

        generador = (p for p in peliculas)
        resultado = mejores_peliculas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_peliculas)

    def test_3(self):
        """
        Más de 20 peliculas, algunas con empate de rating
        """
        peliculas = [
            Peliculas(id=51564524, titulo='Pulp Fiction', genero='Crimen', rating=7.8),
            Peliculas(id=75712817, titulo='The Incredible Hulk', genero='Animación', rating=6.3),
            Peliculas(id=23478300, titulo='The Revenant', genero='Aventura', rating=7.6),
            Peliculas(id=73073290, titulo='Captain America: The First Avenger', genero='Animación', rating=6.6),
            Peliculas(id=59249531, titulo='Motocrossed', genero='Deportes', rating=6.2),
            Peliculas(id=75811918, titulo='The Lion King', genero='Animación', rating=8.1),
            Peliculas(id=19229644, titulo='High School Musical 3', genero='Musical', rating=6.5),
            Peliculas(id=42509121, titulo='The Matrix Reloaded', genero='Fantasía', rating=6.8),
            Peliculas(id=85120654, titulo='Wendy Wu: Homecoming Warrior', genero='Acción', rating=5.8),
            Peliculas(id=55827021, titulo='The Pianist', genero='Superhéroes', rating=8.1),
            Peliculas(id=43568569, titulo='The Great Gatsby', genero='Drama', rating=8.1),
            Peliculas(id=38989561, titulo='Tangled', genero='Animación', rating=7.6),
            Peliculas(id=49947768, titulo='Pixel Perfect', genero='Ciencia Ficción', rating=5.6),
            Peliculas(id=77492098, titulo='The Lord of the Rings: The Fellowship of the Ring', genero='Animación', rating=8.0),
            Peliculas(id=91206323, titulo='Blade Runner', genero='Ciencia Ficción', rating=7.7),
            Peliculas(id=82673162, titulo='Zenon: Girl of the 21st Century', genero='Ciencia Ficción', rating=5.6),
            Peliculas(id=89789737, titulo='Iron Man', genero='Animación', rating=7.2),
            Peliculas(id=42091303, titulo='The Matrix Revolutions', genero='Fantasía', rating=6.9),
            Peliculas(id=76057165, titulo='Incredibles', genero='Animación', rating=7.6),
            Peliculas(id=79000338, titulo='Beauty and the Beast', genero='Animación', rating=7.6),
            Peliculas(id=48171818, titulo='The Thirteenth Year', genero='Fantasía', rating=6.2),
            Peliculas(id=40319999, titulo='The Imitation Game', genero='Drama', rating=9.2),
            Peliculas(id=17339772, titulo='The Hunchback of Notre Dame', genero='Comedia', rating=6.5),
            Peliculas(id=20663067, titulo='The Princess and the Frog', genero='Animación', rating=6.7),
            Peliculas(id=40365166, titulo='Finding Nemo', genero='Misterio', rating=7.8),
            Peliculas(id=81221646, titulo='The Lord of the Rings: The Return of the King', genero='Animación', rating=8.3),
            Peliculas(id=25280291, titulo='Kill Bill: Vol. 2', genero='Western', rating=8.3),
            Peliculas(id=40024087, titulo='Ant-Man', genero='Superhéroes', rating=7.1),
            Peliculas(id=59900653, titulo='The Silence of the Lambs', genero='Suspense', rating=8.2),
            Peliculas(id=66029250, titulo='Titanic', genero='Drama', rating=7.4),
            Peliculas(id=81240344, titulo='Moana', genero='Animación', rating=7.6),
            Peliculas(id=75256227, titulo='Kill Bill: Vol. 1', genero='Superhéroes', rating=7.7),
            Peliculas(id=44053229, titulo='American History X', genero='Superhéroes', rating=8.1),
            Peliculas(id=52620999, titulo='Shutter Island', genero='Superhéroes', rating=8.1),
            Peliculas(id=32204530, titulo='The Princess Diaries', genero='Comedia', rating=5.8),
            Peliculas(id=87262836, titulo='Doctor Strange', genero='Superhéroes', rating=6.9),
            Peliculas(id=61436501, titulo='Mamma Mia', genero='Musical', rating=9.6),
            Peliculas(id=75954204, titulo='Akira', genero='Animación', rating=8.2),
            Peliculas(id=92056988, titulo='Treasure Planet', genero='Deportes', rating=7.3),
            Peliculas(id=43038429, titulo='The Lord of the Rings', genero='Fantasía', rating=8.3),
        ]
        expected_peliculas = [
            Peliculas(id=61436501, titulo='Mamma Mia', genero='Musical', rating=9.6),
            Peliculas(id=40319999, titulo='The Imitation Game', genero='Drama', rating=9.2),
            Peliculas(id=25280291, titulo='Kill Bill: Vol. 2', genero='Western', rating=8.3),
            Peliculas(id=43038429, titulo='The Lord of the Rings', genero='Fantasía', rating=8.3),
            Peliculas(id=81221646, titulo='The Lord of the Rings: The Return of the King', genero='Animación', rating=8.3),
            Peliculas(id=59900653, titulo='The Silence of the Lambs', genero='Suspense', rating=8.2),
            Peliculas(id=75954204, titulo='Akira', genero='Animación', rating=8.2),
            Peliculas(id=43568569, titulo='The Great Gatsby', genero='Drama', rating=8.1),
            Peliculas(id=44053229, titulo='American History X', genero='Superhéroes', rating=8.1),
            Peliculas(id=52620999, titulo='Shutter Island', genero='Superhéroes', rating=8.1),
            Peliculas(id=55827021, titulo='The Pianist', genero='Superhéroes', rating=8.1),
            Peliculas(id=75811918, titulo='The Lion King', genero='Animación', rating=8.1),
            Peliculas(id=77492098, titulo='The Lord of the Rings: The Fellowship of the Ring', genero='Animación', rating=8.0),
            Peliculas(id=40365166, titulo='Finding Nemo', genero='Misterio', rating=7.8),
            Peliculas(id=51564524, titulo='Pulp Fiction', genero='Crimen', rating=7.8),
            Peliculas(id=75256227, titulo='Kill Bill: Vol. 1', genero='Superhéroes', rating=7.7),
            Peliculas(id=91206323, titulo='Blade Runner', genero='Ciencia Ficción', rating=7.7),
            Peliculas(id=23478300, titulo='The Revenant', genero='Aventura', rating=7.6),
            Peliculas(id=38989561, titulo='Tangled', genero='Animación', rating=7.6),
            Peliculas(id=76057165, titulo='Incredibles', genero='Animación', rating=7.6),
        ]

        generador = (p for p in peliculas)
        resultado = mejores_peliculas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_peliculas)

    def test_4(self):
        """
        Más de 20 peliculas, todas con empate de rating
        """
        peliculas = [
            Peliculas(id=51564524, titulo='Pulp Fiction', genero='Crimen', rating=8.3),
            Peliculas(id=75712817, titulo='The Incredible Hulk', genero='Animación', rating=8.3),
            Peliculas(id=23478300, titulo='The Revenant', genero='Aventura', rating=8.3),
            Peliculas(id=73073290, titulo='Captain America: The First Avenger', genero='Animación', rating=8.3),
            Peliculas(id=59249531, titulo='Motocrossed', genero='Deportes', rating=8.3),
            Peliculas(id=75811918, titulo='The Lion King', genero='Animación', rating=8.3),
            Peliculas(id=19229644, titulo='High School Musical 3', genero='Musical', rating=8.3),
            Peliculas(id=42509121, titulo='The Matrix Reloaded', genero='Fantasía', rating=8.3),
            Peliculas(id=85120654, titulo='Wendy Wu: Homecoming Warrior', genero='Acción', rating=8.3),
            Peliculas(id=55827021, titulo='The Pianist', genero='Superhéroes', rating=8.3),
            Peliculas(id=43568569, titulo='The Great Gatsby', genero='Drama', rating=8.3),
            Peliculas(id=38989561, titulo='Tangled', genero='Animación', rating=8.3),
            Peliculas(id=49947768, titulo='Pixel Perfect', genero='Ciencia Ficción', rating=8.3),
            Peliculas(id=77492098, titulo='The Lord of the Rings: The Fellowship of the Ring', genero='Animación', rating=8.3),
            Peliculas(id=91206323, titulo='Blade Runner', genero='Ciencia Ficción', rating=8.3),
            Peliculas(id=82673162, titulo='Zenon: Girl of the 21st Century', genero='Ciencia Ficción', rating=8.3),
            Peliculas(id=89789737, titulo='Iron Man', genero='Animación', rating=8.3),
            Peliculas(id=42091303, titulo='The Matrix Revolutions', genero='Fantasía', rating=8.3),
            Peliculas(id=76057165, titulo='Incredibles', genero='Animación', rating=8.3),
            Peliculas(id=79000338, titulo='Beauty and the Beast', genero='Animación', rating=8.3),
            Peliculas(id=48171818, titulo='The Thirteenth Year', genero='Fantasía', rating=8.3),
            Peliculas(id=40319999, titulo='The Imitation Game', genero='Drama', rating=8.3),
            Peliculas(id=17339772, titulo='The Hunchback of Notre Dame', genero='Comedia', rating=8.3),
            Peliculas(id=20663067, titulo='The Princess and the Frog', genero='Animación', rating=8.3),
            Peliculas(id=40365166, titulo='Finding Nemo', genero='Misterio', rating=8.3),
            Peliculas(id=81221646, titulo='The Lord of the Rings: The Return of the King', genero='Animación', rating=8.3),
            Peliculas(id=25280291, titulo='Kill Bill: Vol. 2', genero='Western', rating=8.3),
            Peliculas(id=40024087, titulo='Ant-Man', genero='Superhéroes', rating=8.3),
            Peliculas(id=59900653, titulo='The Silence of the Lambs', genero='Suspense', rating=8.3),
            Peliculas(id=66029250, titulo='Titanic', genero='Drama', rating=8.3),
            Peliculas(id=81240344, titulo='Moana', genero='Animación', rating=8.3),
            Peliculas(id=75256227, titulo='Kill Bill: Vol. 1', genero='Superhéroes', rating=8.3),
            Peliculas(id=44053229, titulo='American History X', genero='Superhéroes', rating=8.3),
            Peliculas(id=52620999, titulo='Shutter Island', genero='Superhéroes', rating=8.3),
            Peliculas(id=32204530, titulo='The Princess Diaries', genero='Comedia', rating=8.3),
            Peliculas(id=87262836, titulo='Doctor Strange', genero='Superhéroes', rating=8.3),
            Peliculas(id=61436501, titulo='Mamma Mia', genero='Musical', rating=8.3),
            Peliculas(id=75954204, titulo='Akira', genero='Animación', rating=8.3),
            Peliculas(id=92056988, titulo='Treasure Planet', genero='Deportes', rating=8.3),
            Peliculas(id=43038429, titulo='The Lord of the Rings', genero='Fantasía', rating=8.3),
        ]
        expected_peliculas = [
            Peliculas(id=17339772, titulo='The Hunchback of Notre Dame', genero='Comedia', rating=8.3),
            Peliculas(id=19229644, titulo='High School Musical 3', genero='Musical', rating=8.3),
            Peliculas(id=20663067, titulo='The Princess and the Frog', genero='Animación', rating=8.3),
            Peliculas(id=23478300, titulo='The Revenant', genero='Aventura', rating=8.3),
            Peliculas(id=25280291, titulo='Kill Bill: Vol. 2', genero='Western', rating=8.3),
            Peliculas(id=32204530, titulo='The Princess Diaries', genero='Comedia', rating=8.3),
            Peliculas(id=38989561, titulo='Tangled', genero='Animación', rating=8.3),
            Peliculas(id=40024087, titulo='Ant-Man', genero='Superhéroes', rating=8.3),
            Peliculas(id=40319999, titulo='The Imitation Game', genero='Drama', rating=8.3),
            Peliculas(id=40365166, titulo='Finding Nemo', genero='Misterio', rating=8.3),
            Peliculas(id=42091303, titulo='The Matrix Revolutions', genero='Fantasía', rating=8.3),
            Peliculas(id=42509121, titulo='The Matrix Reloaded', genero='Fantasía', rating=8.3),
            Peliculas(id=43038429, titulo='The Lord of the Rings', genero='Fantasía', rating=8.3),
            Peliculas(id=43568569, titulo='The Great Gatsby', genero='Drama', rating=8.3),
            Peliculas(id=44053229, titulo='American History X', genero='Superhéroes', rating=8.3),
            Peliculas(id=48171818, titulo='The Thirteenth Year', genero='Fantasía', rating=8.3),
            Peliculas(id=49947768, titulo='Pixel Perfect', genero='Ciencia Ficción', rating=8.3),
            Peliculas(id=51564524, titulo='Pulp Fiction', genero='Crimen', rating=8.3),
            Peliculas(id=52620999, titulo='Shutter Island', genero='Superhéroes', rating=8.3),
            Peliculas(id=55827021, titulo='The Pianist', genero='Superhéroes', rating=8.3),
        ]

        generador = (p for p in peliculas)
        resultado = mejores_peliculas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_peliculas)

    def test_5(self):
        """
        Solo una pelicula
        """
        peliculas = [
            Peliculas(id=25280291, titulo='The Departed', genero='Western', rating=9.0),
        ]
        expected_peliculas = [
            Peliculas(id=25280291, titulo='The Departed', genero='Western', rating=9.0),
        ]

        generador = (p for p in peliculas)
        resultado = mejores_peliculas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_peliculas)


if __name__ == '__main__':
    unittest.main(verbosity=2)
