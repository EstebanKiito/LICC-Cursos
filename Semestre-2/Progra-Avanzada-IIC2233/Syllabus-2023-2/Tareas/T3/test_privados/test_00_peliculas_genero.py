import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import peliculas_genero
from utilidades import Peliculas
from typing import Generator


class TestPeliculasGenero(unittest.TestCase):

    def test_0(self):
        """
        Varias peliculas son del genero a buscar
        """
        lista_peliculas = [
            Peliculas(id=67202232, titulo='Memento', genero='Superhéroes', rating=8.5),
            Peliculas(id=81169279, titulo='The Lord of the Rings: The Return of the King', genero='Animación', rating=8.7),
            Peliculas(id=54090274, titulo='Cadet Kelly', genero='Comedia', rating=6.2),
            Peliculas(id=23425933, titulo='The Revenant', genero='Aventura', rating=8.0),
            Peliculas(id=73020923, titulo='Captain America: The First Avenger', genero='Animación', rating=7.0),
            Peliculas(id=82620795, titulo='Zenon: Girl of the 21st Century', genero='Ciencia Ficción', rating=6.0),
            Peliculas(id=75759551, titulo='The Lion King', genero='Animación', rating=8.5),
            Peliculas(id=58329437, titulo='My Neighbor Totoro', genero='Animación', rating=8.6),
            Peliculas(id=39971720, titulo='Ant-Man', genero='Superhéroes', rating=7.5),
            Peliculas(id=23653810, titulo='Reservoir Dogs', genero='Superhéroes', rating=8.3),
        ]
        expected_lista_peliculas = [
            Peliculas(id=67202232, titulo='Memento', genero='Superhéroes', rating=8.5),
            Peliculas(id=39971720, titulo='Ant-Man', genero='Superhéroes', rating=7.5),
            Peliculas(id=23653810, titulo='Reservoir Dogs', genero='Superhéroes', rating=8.3),
        ]
        genero_a_buscar = 'Superhéroes'

        generador = (p for p in lista_peliculas)
        resultado = peliculas_genero(generador, genero_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_peliculas)

    def test_1(self):
        """
        Solo una pelicula es del genero a buscar
        """
        lista_peliculas = [
            Peliculas(id=34304754, titulo='Iron Man 3', genero='Animación', rating=7.1),
            Peliculas(id=27868789, titulo='Guardians of the Galaxy', genero='Animación', rating=7.5),
            Peliculas(id=76916171, titulo='Captain America: The Winter Soldier', genero='Animación', rating=7.8),
            Peliculas(id=25227924, titulo='Kill Bill: Vol. 2', genero='Western', rating=8.7),
            Peliculas(id=75203860, titulo='Kill Bill: Vol. 1', genero='Superhéroes', rating=8.1),
        ]
        expected_lista_peliculas = [
            Peliculas(id=75203860, titulo='Kill Bill: Vol. 1', genero='Superhéroes', rating=8.1),
        ]
        genero_a_buscar = 'Superhéroes'

        generador = (p for p in lista_peliculas)
        resultado = peliculas_genero(generador, genero_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_peliculas)

    def test_2(self):
        """
        Ninguna pelicula es del genero a buscar
        """
        lista_peliculas = [
            Peliculas(id=48119451, titulo='The Thirteenth Year', genero='Fantasía', rating=6.6),
            Peliculas(id=61234416, titulo="Howl's Moving Castle", genero='Animación', rating=8.9),
            Peliculas(id=52568632, titulo='Shutter Island', genero='Superhéroes', rating=8.5),
            Peliculas(id=59197164, titulo='Motocrossed', genero='Deportes', rating=6.6),
            Peliculas(id=58643843, titulo='Iron Man 2', genero='Animación', rating=7.0),
        ]
        expected_lista_peliculas = []
        genero_a_buscar = 'Crimen'

        generador = (p for p in lista_peliculas)
        resultado = peliculas_genero(generador, genero_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_peliculas)

    def test_3(self):
        """
        Peliculas de generos similares
        """
        lista_peliculas = [
            Peliculas(id=49895401, titulo='Pixel Perfect', genero='Ciencia Ficción', rating=6.0),
            Peliculas(id=76172796, titulo='Forrest Gump', genero='Ciencia', rating=8.0),
            Peliculas(id=66226007, titulo='The Godfather: Part II', genero='Ciencia Ficción', rating=9.0),
            Peliculas(id=25035329, titulo='The Matrix', genero='Ciencia Ficción', rating=8.8),
        ]
        expected_lista_peliculas = [
            Peliculas(id=76172796, titulo='Forrest Gump', genero='Ciencia', rating=8.0),
        ]
        genero_a_buscar = 'Ciencia'

        generador = (p for p in lista_peliculas)
        resultado = peliculas_genero(generador, genero_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_peliculas)

    def test_4(self):
        """
        Todas las peliculas son del genero a buscar
        """
        lista_peliculas = [
            Peliculas(id=62764502, titulo='Toy Story', genero='Animación', rating=8.3),
            Peliculas(id=45064961, titulo='Big Hero 6', genero='Animación', rating=7.8),
            Peliculas(id=41068976, titulo='Cinderella', genero='Animación', rating=7.1),
        ]
        expected_lista_peliculas = [
            Peliculas(id=62764502, titulo='Toy Story', genero='Animación', rating=8.3),
            Peliculas(id=45064961, titulo='Big Hero 6', genero='Animación', rating=7.8),
            Peliculas(id=41068976, titulo='Cinderella', genero='Animación', rating=7.1),
        ]
        genero_a_buscar = 'Animación'

        generador = (p for p in lista_peliculas)
        resultado = peliculas_genero(generador, genero_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_peliculas)


if __name__ == '__main__':
    unittest.main(verbosity=2)
