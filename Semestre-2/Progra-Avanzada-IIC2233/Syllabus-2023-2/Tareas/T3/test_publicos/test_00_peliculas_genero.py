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
            Peliculas(id=32608840, titulo='Johnny Tsunami', genero='Deportes', rating=6.3),
            Peliculas(id=83829256, titulo='Stuck in the Suburbs', genero='Comedia', rating=6.2),
            Peliculas(id=89587896, titulo='Whiplash', genero='Drama', rating=8.5),
            Peliculas(id=16359236, titulo='Mulan', genero='Deportes', rating=7.8),
            Peliculas(id=34321575, titulo='Ant-Man and The Wasp', genero='Superhéroes', rating=7.1),
            Peliculas(id=73079370, titulo='Thor: The Dark World', genero='Animación', rating=7.2),
            Peliculas(id=98009659, titulo='Twitches', genero='Fantasía', rating=6.7),
            Peliculas(id=75759551, titulo='The Lion King', genero='Animación', rating=8.5),
            Peliculas(id=81169279, titulo='The Lord of the Rings: The Return of the King', genero='Animación', rating=8.7),
            Peliculas(id=23221543, titulo='Halloweentown', genero='Fantasía', rating=6.3),
        ]
        expected_lista_peliculas = [
            Peliculas(id=73079370, titulo='Thor: The Dark World', genero='Animación', rating=7.2),
            Peliculas(id=75759551, titulo='The Lion King', genero='Animación', rating=8.5),
            Peliculas(id=81169279, titulo='The Lord of the Rings: The Return of the King', genero='Animación', rating=8.7),
        ]
        genero_a_buscar = 'Animación'

        generador = (p for p in lista_peliculas)
        resultado = peliculas_genero(generador, genero_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_peliculas)

    def test_1(self):
        """
        Solo una pelicula es del genero a buscar
        """
        lista_peliculas = [
            Peliculas(id=59197164, titulo='Motocrossed', genero='Deportes', rating=6.6),
            Peliculas(id=89708109, titulo='Captain America: Civil War', genero='Superhéroes', rating=8.0),
            Peliculas(id=51418590, titulo='The Shawshank Redemption', genero='Drama', rating=9.3),
            Peliculas(id=25227924, titulo='Kill Bill: Vol. 2', genero='Western', rating=8.7),
            Peliculas(id=95817124, titulo='Fight Club', genero='Crimen', rating=8.8),
        ]
        expected_lista_peliculas = [
            Peliculas(id=25227924, titulo='Kill Bill: Vol. 2', genero='Western', rating=8.7),
        ]
        genero_a_buscar = 'Western'

        generador = (p for p in lista_peliculas)
        resultado = peliculas_genero(generador, genero_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_peliculas)


    def test_2(self):
        """
        Ninguna pelicula es del genero a buscar
        """
        lista_peliculas = [
            Peliculas(id=59197164, titulo='Motocrossed', genero='Deportes', rating=6.6),
            Peliculas(id=89708109, titulo='Captain America: Civil War', genero='Superhéroes', rating=8.0),
            Peliculas(id=51418590, titulo='The Shawshank Redemption', genero='Drama', rating=9.3),
            Peliculas(id=25227924, titulo='Kill Bill: Vol. 2', genero='Western', rating=8.7),
            Peliculas(id=95817124, titulo='Fight Club', genero='Crimen', rating=8.8),
        ]
        expected_lista_peliculas = []
        genero_a_buscar = 'Animación'

        generador = (p for p in lista_peliculas)
        resultado = peliculas_genero(generador, genero_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_peliculas)

    def test_3(self):
        """
        Peliculas de generos similares
        """
        lista_peliculas = [
            Peliculas(id=78376301, titulo='Smart House', genero='Ciencia Ficción', rating=6.2),
            Peliculas(id=36540564, titulo='Tarzan', genero='Ciencia Ficción', rating=7.6),
            Peliculas(id=79145064, titulo='Forrest Gump', genero='Ciencia', rating=8.8),
            Peliculas(id=49895401, titulo='Pixel Perfect', genero='Ciencia Ficción', rating=6.0),
        ]
        expected_lista_peliculas = [
            Peliculas(id=79145064, titulo='Forrest Gump', genero='Ciencia', rating=8.8),
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
            Peliculas(id=38463448, titulo='Spider-Man: Homecoming', genero='Superhéroes', rating=7.5),
            Peliculas(id=52568632, titulo='Shutter Island', genero='Superhéroes', rating=8.5),
            Peliculas(id=44000862, titulo='American History X', genero='Superhéroes', rating=8.5),
        ]
        expected_lista_peliculas = [
            Peliculas(id=38463448, titulo='Spider-Man: Homecoming', genero='Superhéroes', rating=7.5),
            Peliculas(id=52568632, titulo='Shutter Island', genero='Superhéroes', rating=8.5),
            Peliculas(id=44000862, titulo='American History X', genero='Superhéroes', rating=8.5),
        ]
        genero_a_buscar = 'Superhéroes'

        generador = (p for p in lista_peliculas)
        resultado = peliculas_genero(generador, genero_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_peliculas)

if __name__ == '__main__':
    unittest.main(verbosity=2)