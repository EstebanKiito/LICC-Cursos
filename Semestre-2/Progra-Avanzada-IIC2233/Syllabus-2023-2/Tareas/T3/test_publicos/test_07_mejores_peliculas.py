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
            Peliculas(83566857, 'The Usual Suspects', 'Superhéroes', 8.5),
            Peliculas(51418590, 'The Shawshank Redemption', 'Drama', 9.3),
            Peliculas(25035329, 'The Matrix', 'Ciencia Ficción', 8.8),
            Peliculas(58329437, 'My Neighbor Totoro', 'Animación', 8.6),
            Peliculas(79145064, 'Forrest Gump', 'Ciencia', 8.8),
            Peliculas(70752273, 'Gladiator', 'Crimen', 8.5),
            Peliculas(90803337, 'High School Musical 2', 'Musical', 6.1),
        ]
        expected_peliculas = [
            Peliculas(83566857, 'The Usual Suspects', 'Superhéroes', 8.5),
            Peliculas(51418590, 'The Shawshank Redemption', 'Drama', 9.3),
            Peliculas(25035329, 'The Matrix', 'Ciencia Ficción', 8.8),
            Peliculas(58329437, 'My Neighbor Totoro', 'Animación', 8.6),
            Peliculas(79145064, 'Forrest Gump', 'Ciencia', 8.8),
            Peliculas(70752273, 'Gladiator', 'Crimen', 8.5),
            Peliculas(90803337, 'High School Musical 2', 'Musical', 6.1),
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
            Peliculas(16359236, 'Mulan', 'Deportes', 7.8),
            Peliculas(19745617, 'The Dark Knight', 'Acción', 9.0),
            Peliculas(87210469, 'Doctor Strange', 'Superhéroes', 7.3),
            Peliculas(79145064, 'Forrest Gump', 'Ciencia', 8.8),
            Peliculas(91153956, 'Blade Runner', 'Ciencia Ficción', 8.1),
            Peliculas(11164686, 'Interstellar', 'Ciencia Ficción', 8.6),
            Peliculas(35100234, 'Terminator 2: Judgment Day', 'Animación', 8.5),
            Peliculas(17287405, 'The Hunchback of Notre Dame', 'Comedia', 6.9),
            Peliculas(95817124, 'Fight Club', 'Crimen', 8.8),
            Peliculas(96374386, 'The Lord of the Rings: The Two Towers', 'Animación', 8.7),
            Peliculas(51151305, 'Pocahontas', 'Fantasía', 7.8),
            Peliculas(69065378, 'Black Panther', 'Superhéroes', 8.0),
            Peliculas(21261768, 'The Jungle Book', 'Ciencia Ficción', 7.6),
            Peliculas(75203860, 'Kill Bill: Vol. 1', 'Superhéroes', 8.1),
            Peliculas(75259113, 'Up', 'Crimen', 8.4),
            Peliculas(46804999, 'Guardians of the Galaxy Vol. 2', 'Superhéroes', 7.1),
            Peliculas(78947971, 'Beauty and the Beast', 'Animación', 8.0),
            Peliculas(40312799, 'Finding Nemo', 'Misterio', 8.2),
            Peliculas(43516202, 'The Great Gatsby', 'Drama', 8.5),
            Peliculas(61234416, "Howl's Moving Castle", 'Animación', 8.9),
        ]
        expected_peliculas = [
            Peliculas(16359236, 'Mulan', 'Deportes', 7.8),
            Peliculas(19745617, 'The Dark Knight', 'Acción', 9.0),
            Peliculas(87210469, 'Doctor Strange', 'Superhéroes', 7.3),
            Peliculas(79145064, 'Forrest Gump', 'Ciencia', 8.8),
            Peliculas(91153956, 'Blade Runner', 'Ciencia Ficción', 8.1),
            Peliculas(11164686, 'Interstellar', 'Ciencia Ficción', 8.6),
            Peliculas(35100234, 'Terminator 2: Judgment Day', 'Animación', 8.5),
            Peliculas(17287405, 'The Hunchback of Notre Dame', 'Comedia', 6.9),
            Peliculas(95817124, 'Fight Club', 'Crimen', 8.8),
            Peliculas(96374386, 'The Lord of the Rings: The Two Towers', 'Animación', 8.7),
            Peliculas(51151305, 'Pocahontas', 'Fantasía', 7.8),
            Peliculas(69065378, 'Black Panther', 'Superhéroes', 8.0),
            Peliculas(21261768, 'The Jungle Book', 'Ciencia Ficción', 7.6),
            Peliculas(75203860, 'Kill Bill: Vol. 1', 'Superhéroes', 8.1),
            Peliculas(75259113, 'Up', 'Crimen', 8.4),
            Peliculas(46804999, 'Guardians of the Galaxy Vol. 2', 'Superhéroes', 7.1),
            Peliculas(78947971, 'Beauty and the Beast', 'Animación', 8.0),
            Peliculas(40312799, 'Finding Nemo', 'Misterio', 8.2),
            Peliculas(43516202, 'The Great Gatsby', 'Drama', 8.5),
            Peliculas(61234416, "Howl's Moving Castle", 'Animación', 8.9),
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
            Peliculas(16359236, 'Mulan', 'Deportes', 7.8),
            Peliculas(19745617, 'The Dark Knight', 'Acción', 9.0),
            Peliculas(42475848, 'Spirited Away', 'Animación', 8.6),
            Peliculas(32718070, 'Inglourious Basterds', 'Superhéroes', 8.9),
            Peliculas(58329437, 'My Neighbor Totoro', 'Animación', 8.6),
            Peliculas(73079370, 'Thor: The Dark World', 'Animación', 7.2),
            Peliculas(30060914, 'Get a Clue', 'Comedia', 6.2),
            Peliculas(11615401, 'The Princess Bride', 'Aventura', 7.5),
            Peliculas(25035329, 'The Matrix', 'Ciencia Ficción', 8.8),
            Peliculas(79963157, 'Django Unchained', 'Superhéroes', 8.5),
            Peliculas(89708109, 'Captain America: Civil War', 'Superhéroes', 8.0),
            Peliculas(61161814, 'High School Musical', 'Musical', 6.4),
            Peliculas(41115118, 'Avatar', 'Crimen', 7.8),
            Peliculas(38463448, 'Spider-Man: Homecoming', 'Superhéroes', 7.5),
            Peliculas(23678361, 'Scarface', 'Crimen', 8.8),
            Peliculas(98009659, 'Twitches', 'Fantasía', 6.7),
            Peliculas(49895401, 'Pixel Perfect', 'Ciencia Ficción', 6.0),
            Peliculas(51512157, 'Pulp Fiction', 'Crimen', 8.2),
            Peliculas(72588542, 'Frozen', 'Animación', 7.4),
            Peliculas(78376301, 'Smart House', 'Ciencia Ficción', 6.2),
            Peliculas(32152163, 'The Princess Diaries', 'Comedia', 6.2),
            Peliculas(67202232, 'Memento', 'Superhéroes', 8.5),
            Peliculas(48119451, 'The Thirteenth Year', 'Fantasía', 6.6),
            Peliculas(75259113, 'Up', 'Crimen', 8.4),
            Peliculas(54541808, 'Matilda', 'Comedia', 6.9),
        ]
        expected_peliculas = [
            Peliculas(19745617, 'The Dark Knight', 'Acción', 9.0),
            Peliculas(32718070, 'Inglourious Basterds', 'Superhéroes', 8.9),
            Peliculas(23678361, 'Scarface', 'Crimen', 8.8),
            Peliculas(25035329, 'The Matrix', 'Ciencia Ficción', 8.8),
            Peliculas(42475848, 'Spirited Away', 'Animación', 8.6),
            Peliculas(58329437, 'My Neighbor Totoro', 'Animación', 8.6),
            Peliculas(67202232, 'Memento', 'Superhéroes', 8.5),
            Peliculas(79963157, 'Django Unchained', 'Superhéroes', 8.5),
            Peliculas(75259113, 'Up', 'Crimen', 8.4),
            Peliculas(51512157, 'Pulp Fiction', 'Crimen', 8.2),
            Peliculas(89708109, 'Captain America: Civil War', 'Superhéroes', 8.0),
            Peliculas(16359236, 'Mulan', 'Deportes', 7.8),
            Peliculas(41115118, 'Avatar', 'Crimen', 7.8),
            Peliculas(11615401, 'The Princess Bride', 'Aventura', 7.5),
            Peliculas(38463448, 'Spider-Man: Homecoming', 'Superhéroes', 7.5),
            Peliculas(72588542, 'Frozen', 'Animación', 7.4),
            Peliculas(73079370, 'Thor: The Dark World', 'Animación', 7.2),
            Peliculas(54541808, 'Matilda', 'Comedia', 6.9),
            Peliculas(98009659, 'Twitches', 'Fantasía', 6.7),
            Peliculas(48119451, 'The Thirteenth Year', 'Fantasía', 6.6),
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
            Peliculas(51512157, 'Pulp Fiction', 'Crimen', 8.2),
            Peliculas(75660450, 'The Incredible Hulk', 'Animación', 6.7),
            Peliculas(23425933, 'The Revenant', 'Aventura', 8.0),
            Peliculas(73020923, 'Captain America: The First Avenger', 'Animación', 7.0),
            Peliculas(59197164, 'Motocrossed', 'Deportes', 6.6),
            Peliculas(75759551, 'The Lion King', 'Animación', 8.5),
            Peliculas(19177277, 'High School Musical 3', 'Musical', 6.9),
            Peliculas(42456754, 'The Matrix Reloaded', 'Fantasía', 7.2),
            Peliculas(85068287, 'Wendy Wu: Homecoming Warrior', 'Acción', 6.2),
            Peliculas(55774654, 'The Pianist', 'Superhéroes', 8.5),
            Peliculas(43516202, 'The Great Gatsby', 'Drama', 8.5),
            Peliculas(38937194, 'Tangled', 'Animación', 8.0),
            Peliculas(49895401, 'Pixel Perfect', 'Ciencia Ficción', 6.0),
            Peliculas(77439731, 'The Lord of the Rings: The Fellowship of the Ring', 'Animación', 8.4),
            Peliculas(91153956, 'Blade Runner', 'Ciencia Ficción', 8.1),
            Peliculas(82620795, 'Zenon: Girl of the 21st Century', 'Ciencia Ficción', 6.0),
            Peliculas(89737370, 'Iron Man', 'Animación', 7.6),
            Peliculas(42038936, 'The Matrix Revolutions', 'Fantasía', 7.3),
            Peliculas(76004798, 'Incredibles', 'Animación', 8.0),
            Peliculas(78947971, 'Beauty and the Beast', 'Animación', 8.0),
            Peliculas(48119451, 'The Thirteenth Year', 'Fantasía', 6.6),
            Peliculas(40267632, 'The Imitation Game', 'Drama', 9.6),
            Peliculas(17287405, 'The Hunchback of Notre Dame', 'Comedia', 6.9),
            Peliculas(20610700, 'The Princess and the Frog', 'Animación', 7.1),
            Peliculas(40312799, 'Finding Nemo', 'Misterio', 8.2),
            Peliculas(81169279, 'The Lord of the Rings: The Return of the King', 'Animación', 8.7),
            Peliculas(25227924, 'Kill Bill: Vol. 2', 'Western', 8.7),
            Peliculas(39971720, 'Ant-Man', 'Superhéroes', 7.5),
            Peliculas(59848286, 'The Silence of the Lambs', 'Suspense', 8.6),
            Peliculas(65976883, 'Titanic', 'Drama', 7.8),
            Peliculas(81187977, 'Moana', 'Animación', 8.0),
            Peliculas(75203860, 'Kill Bill: Vol. 1', 'Superhéroes', 8.1),
            Peliculas(44000862, 'American History X', 'Superhéroes', 8.5),
            Peliculas(52568632, 'Shutter Island', 'Superhéroes', 8.5),
            Peliculas(32152163, 'The Princess Diaries', 'Comedia', 6.2),
            Peliculas(87210469, 'Doctor Strange', 'Superhéroes', 7.3),
            Peliculas(61384134, 'Mamma Mia', 'Musical', 10.0),
            Peliculas(75901837, 'Akira', 'Animación', 8.6),
            Peliculas(92004621, 'Treasure Planet', 'Deportes', 7.7),
            Peliculas(42986062, 'The Lord of the Rings', 'Fantasía', 8.7),
        ]
        expected_peliculas = [
            Peliculas(61384134, 'Mamma Mia', 'Musical', 10.0),
            Peliculas(40267632, 'The Imitation Game', 'Drama', 9.6),
            Peliculas(25227924, 'Kill Bill: Vol. 2', 'Western', 8.7),
            Peliculas(42986062, 'The Lord of the Rings', 'Fantasía', 8.7),
            Peliculas(81169279, 'The Lord of the Rings: The Return of the King', 'Animación', 8.7),
            Peliculas(59848286, 'The Silence of the Lambs', 'Suspense', 8.6),
            Peliculas(75901837, 'Akira', 'Animación', 8.6),
            Peliculas(43516202, 'The Great Gatsby', 'Drama', 8.5),
            Peliculas(44000862, 'American History X', 'Superhéroes', 8.5),
            Peliculas(52568632, 'Shutter Island', 'Superhéroes', 8.5),
            Peliculas(55774654, 'The Pianist', 'Superhéroes', 8.5),
            Peliculas(75759551, 'The Lion King', 'Animación', 8.5),
            Peliculas(77439731, 'The Lord of the Rings: The Fellowship of the Ring', 'Animación', 8.4),
            Peliculas(40312799, 'Finding Nemo', 'Misterio', 8.2),
            Peliculas(51512157, 'Pulp Fiction', 'Crimen', 8.2),
            Peliculas(75203860, 'Kill Bill: Vol. 1', 'Superhéroes', 8.1),
            Peliculas(91153956, 'Blade Runner', 'Ciencia Ficción', 8.1),
            Peliculas(23425933, 'The Revenant', 'Aventura', 8.0),
            Peliculas(38937194, 'Tangled', 'Animación', 8.0),
            Peliculas(76004798, 'Incredibles', 'Animación', 8.0),
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
            Peliculas(51512157, 'Pulp Fiction', 'Crimen', 8.0),
            Peliculas(75660450, 'The Incredible Hulk', 'Animación', 8.0),
            Peliculas(23425933, 'The Revenant', 'Aventura', 8.0),
            Peliculas(73020923, 'Captain America: The First Avenger', 'Animación', 8.0),
            Peliculas(59197164, 'Motocrossed', 'Deportes', 8.0),
            Peliculas(75759551, 'The Lion King', 'Animación', 8.0),
            Peliculas(19177277, 'High School Musical 3', 'Musical', 8.0),
            Peliculas(42456754, 'The Matrix Reloaded', 'Fantasía', 8.0),
            Peliculas(85068287, 'Wendy Wu: Homecoming Warrior', 'Acción', 8.0),
            Peliculas(55774654, 'The Pianist', 'Superhéroes', 8.0),
            Peliculas(43516202, 'The Great Gatsby', 'Drama', 8.0),
            Peliculas(38937194, 'Tangled', 'Animación', 8.0),
            Peliculas(49895401, 'Pixel Perfect', 'Ciencia Ficción', 8.0),
            Peliculas(77439731, 'The Lord of the Rings: The Fellowship of the Ring', 'Animación', 8.0),
            Peliculas(91153956, 'Blade Runner', 'Ciencia Ficción', 8.0),
            Peliculas(82620795, 'Zenon: Girl of the 21st Century', 'Ciencia Ficción', 8.0),
            Peliculas(89737370, 'Iron Man', 'Animación', 8.0),
            Peliculas(42038936, 'The Matrix Revolutions', 'Fantasía', 8.0),
            Peliculas(76004798, 'Incredibles', 'Animación', 8.0),
            Peliculas(78947971, 'Beauty and the Beast', 'Animación', 8.0),
            Peliculas(48119451, 'The Thirteenth Year', 'Fantasía', 8.0),
            Peliculas(40267632, 'The Imitation Game', 'Drama', 8.0),
            Peliculas(17287405, 'The Hunchback of Notre Dame', 'Comedia', 8.0),
            Peliculas(20610700, 'The Princess and the Frog', 'Animación', 8.0),
            Peliculas(40312799, 'Finding Nemo', 'Misterio', 8.0),
            Peliculas(81169279, 'The Lord of the Rings: The Return of the King', 'Animación', 8.0),
            Peliculas(25227924, 'Kill Bill: Vol. 2', 'Western', 8.0),
            Peliculas(39971720, 'Ant-Man', 'Superhéroes', 8.0),
            Peliculas(59848286, 'The Silence of the Lambs', 'Suspense', 8.0),
            Peliculas(65976883, 'Titanic', 'Drama', 8.0),
            Peliculas(81187977, 'Moana', 'Animación', 8.0),
            Peliculas(75203860, 'Kill Bill: Vol. 1', 'Superhéroes', 8.0),
            Peliculas(44000862, 'American History X', 'Superhéroes', 8.0),
            Peliculas(52568632, 'Shutter Island', 'Superhéroes', 8.0),
            Peliculas(32152163, 'The Princess Diaries', 'Comedia', 8.0),
            Peliculas(87210469, 'Doctor Strange', 'Superhéroes', 8.0),
            Peliculas(61384134, 'Mamma Mia', 'Musical', 8.0),
            Peliculas(75901837, 'Akira', 'Animación', 8.0),
            Peliculas(92004621, 'Treasure Planet', 'Deportes', 8.0),
            Peliculas(42986062, 'The Lord of the Rings', 'Fantasía', 8.0),
        ]
        expected_peliculas = [
            Peliculas(id=17287405, titulo='The Hunchback of Notre Dame', genero='Comedia', rating=8.0),
            Peliculas(id=19177277, titulo='High School Musical 3', genero='Musical', rating=8.0),
            Peliculas(id=20610700, titulo='The Princess and the Frog', genero='Animación', rating=8.0),
            Peliculas(id=23425933, titulo='The Revenant', genero='Aventura', rating=8.0),
            Peliculas(id=25227924, titulo='Kill Bill: Vol. 2', genero='Western', rating=8.0),
            Peliculas(id=32152163, titulo='The Princess Diaries', genero='Comedia', rating=8.0),
            Peliculas(id=38937194, titulo='Tangled', genero='Animación', rating=8.0),
            Peliculas(id=39971720, titulo='Ant-Man', genero='Superhéroes', rating=8.0),
            Peliculas(id=40267632, titulo='The Imitation Game', genero='Drama', rating=8.0),
            Peliculas(id=40312799, titulo='Finding Nemo', genero='Misterio', rating=8.0),
            Peliculas(id=42038936, titulo='The Matrix Revolutions', genero='Fantasía', rating=8.0),
            Peliculas(id=42456754, titulo='The Matrix Reloaded', genero='Fantasía', rating=8.0),
            Peliculas(id=42986062, titulo='The Lord of the Rings', genero='Fantasía', rating=8.0),
            Peliculas(id=43516202, titulo='The Great Gatsby', genero='Drama', rating=8.0),
            Peliculas(id=44000862, titulo='American History X', genero='Superhéroes', rating=8.0),
            Peliculas(id=48119451, titulo='The Thirteenth Year', genero='Fantasía', rating=8.0),
            Peliculas(id=49895401, titulo='Pixel Perfect', genero='Ciencia Ficción', rating=8.0),
            Peliculas(id=51512157, titulo='Pulp Fiction', genero='Crimen', rating=8.0),
            Peliculas(id=52568632, titulo='Shutter Island', genero='Superhéroes', rating=8.0),
            Peliculas(id=55774654, titulo='The Pianist', genero='Superhéroes', rating=8.0),
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
            Peliculas(25227924, 'Kill Bill: Vol. 2', 'Western', 8.7),
        ]
        expected_peliculas = [
            Peliculas(25227924, 'Kill Bill: Vol. 2', 'Western', 8.7),
        ]

        generador = (p for p in peliculas)
        resultado = mejores_peliculas(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_peliculas)

if __name__ == '__main__':
    unittest.main(verbosity=2)