import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import id_funciones_genero
from utilidades import Peliculas, Funciones
from typing import Generator


class TestVacioIdFuncionesGenero(unittest.TestCase):

    def test_0(self):
        """
        Genero sin funciones
        """
        lista_peliculas = [
            Peliculas(id=96374386, titulo="The Lord of the Rings: The Two Towers", genero="Animación", rating=8.7),
            Peliculas(id=32568878, titulo="Harry Potter and the Sorcerer's Stone", genero="Bélico", rating=7.6),
            Peliculas(id=46804999, titulo="Guardians of the Galaxy Vol. 2", genero="Superhéroes", rating=7.1),
            Peliculas(id=20610700, titulo="The Princess and the Frog", genero="Animación", rating=7.1),
            Peliculas(id=21261768, titulo="The Jungle Book", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=40873645, titulo="The Terminator", genero="Ciencia Ficción", rating=8.5),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=83829256, titulo="Stuck in the Suburbs", genero="Comedia", rating=6.2),
            Peliculas(id=11164686, titulo="Interstellar", genero="Ciencia Ficción", rating=8.6),
            Peliculas(id=28527704, titulo="Princess Mononoke", genero="Animación", rating=8.4),
            Peliculas(id=95054110, titulo="Thor: Ragnarok", genero="Superhéroes", rating=7.9),
            Peliculas(id=25035329, titulo="The Matrix", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=25227924, titulo="Kill Bill: Vol. 2", genero="Western", rating=8.7),
            Peliculas(id=45745398, titulo="The Green Mile", genero="Animación", rating=8.2),
            Peliculas(id=40267632, titulo="The Imitation Game", genero="Drama", rating=9.6),
            Peliculas(id=42475848, titulo="Spirited Away", genero="Animación", rating=8.6),
            Peliculas(id=87538292, titulo="Monsters Inc.", genero="Animación", rating=8.1),
            Peliculas(id=36540564, titulo="Tarzan", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=51512157, titulo="Pulp Fiction", genero="Crimen", rating=8.2),
            Peliculas(id=39971720, titulo="Ant-Man", genero="Superhéroes", rating=7.5),
            Peliculas(id=57395306, titulo="Inuyasha", genero="Animación", rating=8.4),
            Peliculas(id=33896817, titulo="La La Land", genero="Musical", rating=8.0),
            Peliculas(id=75901837, titulo="Akira", genero="Animación", rating=8.6),
            Peliculas(id=87114047, titulo="Jump In!", genero="Deportes", rating=5.4),
            Peliculas(id=34304754, titulo="Iron Man 3", genero="Animación", rating=7.1),
            Peliculas(id=63162203, titulo="The Departed", genero="Animación", rating=8.2),
            Peliculas(id=19745617, titulo="The Dark Knight", genero="Acción", rating=9.0),
            Peliculas(id=75660450, titulo="The Incredible Hulk", genero="Animación", rating=6.7),
            Peliculas(id=42038936, titulo="The Matrix Revolutions", genero="Fantasía", rating=7.3),
            Peliculas(id=71285784, titulo="Avengers: Age of Ultron", genero="Animación", rating=7.6),
        ]
        lista_funciones = [
            Funciones(id=3081, numero_sala=5, id_pelicula=33896817, horario=7, fecha="07-04-23"),
            Funciones(id=4814, numero_sala=5, id_pelicula=42038936, horario=1, fecha="25-11-23"),
            Funciones(id=5534, numero_sala=5, id_pelicula=45745398, horario=5, fecha="19-06-23"),
            Funciones(id=7663, numero_sala=4, id_pelicula=71285784, horario=4, fecha="25-08-23"),
            Funciones(id=6839, numero_sala=1, id_pelicula=36540564, horario=9, fecha="11-01-23"),
            Funciones(id=1060, numero_sala=4, id_pelicula=46804999, horario=3, fecha="13-03-23"),
            Funciones(id=4987, numero_sala=1, id_pelicula=45745398, horario=2, fecha="04-09-23"),
            Funciones(id=7348, numero_sala=1, id_pelicula=83827256, horario=6, fecha="03-07-23"),
            Funciones(id=1954, numero_sala=9, id_pelicula=21261768, horario=9, fecha="12-07-23"),
            Funciones(id=5550, numero_sala=8, id_pelicula=20610700, horario=5, fecha="15-06-23"),
            Funciones(id=3879, numero_sala=2, id_pelicula=87538292, horario=7, fecha="12-12-23"),
            Funciones(id=8303, numero_sala=4, id_pelicula=46804999, horario=1, fecha="28-09-23"),
            Funciones(id=9672, numero_sala=8, id_pelicula=21261768, horario=9, fecha="19-10-23"),
            Funciones(id=7915, numero_sala=7, id_pelicula=57395306, horario=5, fecha="16-06-23"),
            Funciones(id=3126, numero_sala=5, id_pelicula=40267632, horario=6, fecha="25-06-23"),
            Funciones(id=3711, numero_sala=1, id_pelicula=11164686, horario=8, fecha="11-02-23"),
            Funciones(id=3720, numero_sala=3, id_pelicula=71285784, horario=8, fecha="04-01-23"),
            Funciones(id=5062, numero_sala=1, id_pelicula=63162203, horario=5, fecha="19-02-23"),
            Funciones(id=4632, numero_sala=5, id_pelicula=19745617, horario=7, fecha="13-06-23"),
            Funciones(id=2889, numero_sala=9, id_pelicula=25035329, horario=1, fecha="08-01-23"),
            Funciones(id=3591, numero_sala=5, id_pelicula=95054110, horario=7, fecha="01-10-23"),
            Funciones(id=5021, numero_sala=6, id_pelicula=45745398, horario=9, fecha="02-02-23"),
            Funciones(id=9943, numero_sala=4, id_pelicula=45745398, horario=8, fecha="13-10-23"),
            Funciones(id=8174, numero_sala=1, id_pelicula=75901837, horario=7, fecha="15-06-23"),
            Funciones(id=9398, numero_sala=2, id_pelicula=20610700, horario=1, fecha="15-09-23"),
            Funciones(id=7692, numero_sala=7, id_pelicula=32568878, horario=1, fecha="14-01-23"),
            Funciones(id=2340, numero_sala=3, id_pelicula=19745617, horario=2, fecha="01-07-23"),
            Funciones(id=4645, numero_sala=1, id_pelicula=39971720, horario=4, fecha="26-06-23"),
            Funciones(id=5320, numero_sala=9, id_pelicula=96374386, horario=1, fecha="13-09-23"),
            Funciones(id=1142, numero_sala=6, id_pelicula=40267632, horario=1, fecha="25-11-23"),
        ]
        lista_esperada = []

        resultado = id_funciones_genero(iter(lista_peliculas), iter(lista_funciones), "Comedia")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), lista_esperada)

    def test_1(self):
        """
        Genero no existe
        """
        lista_peliculas = [
            Peliculas(id=75259113, titulo="Up", genero="Crimen", rating=8.4),
            Peliculas(id=47191880, titulo="Thor", genero="Animación", rating=7.2),
            Peliculas(id=70752273, titulo="Gladiator", genero="Crimen", rating=8.5),
            Peliculas(id=87114047, titulo="Jump In!", genero="Western", rating=5.4),
            Peliculas(id=95817124, titulo="Fight Club", genero="Crimen", rating=8.8),
            Peliculas(id=85032662, titulo="Aladdin", genero="Animación", rating=8.0),
            Peliculas(id=38937194, titulo="Tangled", genero="Animación", rating=8.0),
            Peliculas(id=89737370, titulo="Iron Man", genero="Animación", rating=7.6),
            Peliculas(id=61384134, titulo="Mamma Mia", genero="Musical", rating=10.0),
            Peliculas(id=30060914, titulo="Get a Clue", genero="Comedia", rating=6.2),
            Peliculas(id=62764502, titulo="Toy Story", genero="Animación", rating=8.3),
            Peliculas(id=67027889, titulo="Seven Samurai", genero="Crimen", rating=9.0),
            Peliculas(id=34755557, titulo="The Notebook", genero="Western", rating=7.8),
            Peliculas(id=23221543, titulo="Halloweentown", genero="Fantasía", rating=6.3),
            Peliculas(id=19745617, titulo="The Dark Knight", genero="Acción", rating=9.0),
            Peliculas(id=84580833, titulo="Wreck-It Ralph", genero="Animación", rating=7.5),
            Peliculas(id=95413069, titulo="The Cheetah Girls", genero="Comedia", rating=5.8),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
            Peliculas(id=25035329, titulo="The Matrix", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=78376301, titulo="Smart House", genero="Ciencia Ficción", rating=6.2),
            Peliculas(id=11615401, titulo="The Princess Bride", genero="Aventura", rating=7.5),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=75660450, titulo="The Incredible Hulk", genero="Animación", rating=6.7),
            Peliculas(id=75203860, titulo="Kill Bill: Vol. 1", genero="Superhéroes", rating=8.1),
            Peliculas(id=29533644, titulo="Saving Private Ryan", genero="Superhéroes", rating=8.6),
            Peliculas(id=89756869, titulo="The Emperor's New Groove", genero="Western", rating=6.9),
            Peliculas(id=93369344, titulo="Avengers: Infinity War", genero="Superhéroes", rating=8.4),
            Peliculas(id=20610700, titulo="The Princess and the Frog", genero="Animación", rating=7.1),
            Peliculas(id=89708109, titulo="Captain America: Civil War", genero="Superhéroes", rating=8.0),
            Peliculas(id=77439731, titulo="The Lord of the Rings: The Fellowship of the Ring", genero="Animación", rating=8.4),
        ]
        lista_funciones = [
            Funciones(id=8467, numero_sala=3, id_pelicula=34755557, horario=8, fecha="17-06-23"),
            Funciones(id=9641, numero_sala=7, id_pelicula=77439731, horario=6, fecha="17-08-23"),
            Funciones(id=1200, numero_sala=7, id_pelicula=20610700, horario=3, fecha="15-07-23"),
            Funciones(id=3912, numero_sala=8, id_pelicula=87114047, horario=7, fecha="16-07-23"),
            Funciones(id=3839, numero_sala=4, id_pelicula=49895401, horario=4, fecha="22-04-23"),
            Funciones(id=1354, numero_sala=3, id_pelicula=67027889, horario=1, fecha="23-09-23"),
            Funciones(id=7883, numero_sala=6, id_pelicula=89756869, horario=5, fecha="18-01-23"),
            Funciones(id=1848, numero_sala=7, id_pelicula=89756869, horario=5, fecha="17-01-23"),
            Funciones(id=3307, numero_sala=5, id_pelicula=67027889, horario=4, fecha="28-10-23"),
            Funciones(id=2708, numero_sala=2, id_pelicula=93369344, horario=2, fecha="23-05-23"),
            Funciones(id=6527, numero_sala=5, id_pelicula=89737370, horario=2, fecha="12-01-23"),
            Funciones(id=5058, numero_sala=6, id_pelicula=42103973, horario=6, fecha="23-09-23"),
            Funciones(id=8884, numero_sala=4, id_pelicula=11615401, horario=1, fecha="27-11-23"),
            Funciones(id=3454, numero_sala=6, id_pelicula=61384134, horario=7, fecha="10-06-23"),
            Funciones(id=3043, numero_sala=7, id_pelicula=78376301, horario=8, fecha="07-11-23"),
            Funciones(id=4552, numero_sala=2, id_pelicula=11615401, horario=9, fecha="11-04-23"),
            Funciones(id=3633, numero_sala=4, id_pelicula=89708109, horario=2, fecha="18-08-23"),
            Funciones(id=9784, numero_sala=8, id_pelicula=62764502, horario=8, fecha="04-01-23"),
            Funciones(id=9778, numero_sala=1, id_pelicula=93369344, horario=4, fecha="13-07-23"),
            Funciones(id=4787, numero_sala=6, id_pelicula=95413069, horario=9, fecha="13-02-23"),
            Funciones(id=3418, numero_sala=4, id_pelicula=49895401, horario=9, fecha="24-04-23"),
            Funciones(id=1154, numero_sala=1, id_pelicula=75259113, horario=2, fecha="20-02-23"),
            Funciones(id=8811, numero_sala=5, id_pelicula=30060914, horario=1, fecha="24-10-23"),
            Funciones(id=9063, numero_sala=8, id_pelicula=20610700, horario=2, fecha="23-09-23"),
            Funciones(id=2997, numero_sala=9, id_pelicula=11615401, horario=1, fecha="25-04-23"),
            Funciones(id=1297, numero_sala=9, id_pelicula=38937194, horario=5, fecha="09-02-23"),
            Funciones(id=2567, numero_sala=8, id_pelicula=29533644, horario=1, fecha="26-09-23"),
            Funciones(id=4576, numero_sala=7, id_pelicula=75259113, horario=2, fecha="06-05-23"),
            Funciones(id=8674, numero_sala=3, id_pelicula=67027889, horario=9, fecha="28-02-23"),
            Funciones(id=3793, numero_sala=9, id_pelicula=30060914, horario=5, fecha="11-04-23"),
        ]
        lista_esperada = []

        resultado = id_funciones_genero(iter(lista_peliculas), iter(lista_funciones), "Deportes")
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), lista_esperada)


if __name__ == '__main__':
    unittest.main(verbosity=2)
