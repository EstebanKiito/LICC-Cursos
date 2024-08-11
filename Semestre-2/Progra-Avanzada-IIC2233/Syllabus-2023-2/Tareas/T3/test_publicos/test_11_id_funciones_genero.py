import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import id_funciones_genero
from utilidades import Peliculas, Funciones
from typing import Generator

class TestIdFuncionesGenero(unittest.TestCase):

    def test_0(self):
        """
        Test basico
        """
        lista_peliculas = [
            Peliculas(id=46804999, titulo="Guardians of the Galaxy Vol. 2", genero="Superhéroes", rating=7.1),
            Peliculas(id=81591753, titulo="Zootopia", genero="Animación", rating=8.0),
            Peliculas(id=69065378, titulo="Black Panther", genero="Superhéroes", rating=8.0),
            Peliculas(id=81744489, titulo="Cow Belles", genero="Comedia", rating=6.1),
            Peliculas(id=99972342, titulo="The Cheetah Girls 2", genero="Comedia", rating=5.9),
            Peliculas(id=73079370, titulo="Thor: The Dark World", genero="Animación", rating=7.2),
            Peliculas(id=39971720, titulo="Ant-Man", genero="Superhéroes", rating=7.5),
            Peliculas(id=49034902, titulo="The Godfather", genero="Crimen", rating=9.2),
            Peliculas(id=95817124, titulo="Fight Club", genero="Crimen", rating=8.8),
            Peliculas(id=30060914, titulo="Get a Clue", genero="Comedia", rating=6.2),
            Peliculas(id=47377474, titulo="The Dark Knight Rises", genero="Bélico", rating=8.4),
            Peliculas(id=59197164, titulo="Motocrossed", genero="Deportes", rating=6.6),
            Peliculas(id=29533644, titulo="Saving Private Ryan", genero="Superhéroes", rating=8.6),
            Peliculas(id=48119451, titulo="The Thirteenth Year", genero="Fantasía", rating=6.6),
            Peliculas(id=52568632, titulo="Shutter Island", genero="Superhéroes", rating=8.5),
            Peliculas(id=33612645, titulo="Goodfellas", genero="Animación", rating=8.9),
            Peliculas(id=95417284, titulo="Camp Rock", genero="Musical", rating=5.1),
            Peliculas(id=51418590, titulo="The Shawshank Redemption", genero="Drama", rating=9.3),
            Peliculas(id=61234416, titulo="Howl's Moving Castle", genero="Animación", rating=8.9),
            Peliculas(id=21803572, titulo="Avengers", genero="Acción", rating=8.0),
            Peliculas(id=40312799, titulo="Finding Nemo", genero="Misterio", rating=8.2),
            Peliculas(id=25035329, titulo="The Matrix", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=87114047, titulo="Jump In!", genero="Deportes", rating=5.4),
            Peliculas(id=75421892, titulo="The Little Mermaid", genero="Aventura", rating=8.0),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
            Peliculas(id=98811629, titulo="Braveheart", genero="Animación", rating=8.5),
            Peliculas(id=61161814, titulo="High School Musical", genero="Musical", rating=6.4),
            Peliculas(id=32568878, titulo="Harry Potter and the Sorcerer's Stone", genero="Bélico", rating=7.6),
            Peliculas(id=36540564, titulo="Tarzan", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
        ]
        lista_funciones = [
            Funciones(id=1765, numero_sala=6, id_pelicula=81744489, horario=6, fecha="21-04-23"),
            Funciones(id=8642, numero_sala=3, id_pelicula=39971720, horario=6, fecha="14-04-23"),
            Funciones(id=6189, numero_sala=4, id_pelicula=99972342, horario=4, fecha="07-10-23"),
            Funciones(id=9231, numero_sala=6, id_pelicula=95417284, horario=1, fecha="04-05-23"),
            Funciones(id=1536, numero_sala=8, id_pelicula=25035329, horario=5, fecha="05-10-23"),
            Funciones(id=4027, numero_sala=8, id_pelicula=51418590, horario=8, fecha="23-09-23"),
            Funciones(id=6499, numero_sala=8, id_pelicula=52568632, horario=3, fecha="20-03-23"),
            Funciones(id=1640, numero_sala=2, id_pelicula=25035329, horario=2, fecha="17-01-23"),
            Funciones(id=4504, numero_sala=7, id_pelicula=61161814, horario=9, fecha="04-06-23"),
            Funciones(id=2631, numero_sala=8, id_pelicula=95817124, horario=9, fecha="22-11-23"),
            Funciones(id=7335, numero_sala=1, id_pelicula=81591753, horario=2, fecha="18-10-23"),
            Funciones(id=9980, numero_sala=4, id_pelicula=61161814, horario=8, fecha="13-07-23"),
            Funciones(id=1090, numero_sala=3, id_pelicula=98811629, horario=4, fecha="20-03-23"),
            Funciones(id=9866, numero_sala=9, id_pelicula=32568878, horario=6, fecha="13-01-23"),
            Funciones(id=3343, numero_sala=4, id_pelicula=99972342, horario=2, fecha="16-11-23"),
            Funciones(id=9639, numero_sala=9, id_pelicula=81591753, horario=6, fecha="16-03-23"),
            Funciones(id=3443, numero_sala=2, id_pelicula=32568878, horario=4, fecha="01-02-23"),
            Funciones(id=2856, numero_sala=8, id_pelicula=21803572, horario=3, fecha="12-10-23"),
            Funciones(id=8404, numero_sala=5, id_pelicula=99972342, horario=3, fecha="06-02-23"),
            Funciones(id=3009, numero_sala=1, id_pelicula=30060914, horario=2, fecha="24-11-23"),
            Funciones(id=6711, numero_sala=6, id_pelicula=81591753, horario=4, fecha="26-03-23"),
            Funciones(id=3884, numero_sala=3, id_pelicula=95817124, horario=5, fecha="27-02-23"),
            Funciones(id=7508, numero_sala=3, id_pelicula=46804999, horario=8, fecha="21-07-23"),
            Funciones(id=1337, numero_sala=5, id_pelicula=25035329, horario=3, fecha="23-10-23"),
            Funciones(id=1553, numero_sala=3, id_pelicula=49034902, horario=7, fecha="27-09-23"),
            Funciones(id=8320, numero_sala=8, id_pelicula=87114047, horario=8, fecha="18-11-23"),
            Funciones(id=8862, numero_sala=2, id_pelicula=29533644, horario=3, fecha="15-11-23"),
            Funciones(id=9365, numero_sala=4, id_pelicula=40312799, horario=8, fecha="02-11-23"),
            Funciones(id=8461, numero_sala=9, id_pelicula=69065378, horario=5, fecha="23-05-23"),
            Funciones(id=7641, numero_sala=6, id_pelicula=32568878, horario=5, fecha="02-11-23"),
        ]
        lista_esperada = [8642, 6499, 7508, 8862, 8461]

        resultado = id_funciones_genero(iter(lista_peliculas), iter(lista_funciones), "Superhéroes")
        lista_resultado = list(resultado)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)

    def test_1(self):
        """
        Test basico
        """
        lista_peliculas = [
            Peliculas(id=42986062, titulo="The Lord of the Rings", genero="Fantasía", rating=8.7),
            Peliculas(id=98811629, titulo="Braveheart", genero="Animación", rating=8.5),
            Peliculas(id=23678361, titulo="Scarface", genero="Crimen", rating=8.8),
            Peliculas(id=27868789, titulo="Guardians of the Galaxy", genero="Animación", rating=7.5),
            Peliculas(id=64787434, titulo="Casino", genero="Western", rating=8.5),
            Peliculas(id=21803572, titulo="Avengers", genero="Acción", rating=8.0),
            Peliculas(id=20610700, titulo="The Princess and the Frog", genero="Animación", rating=7.1),
            Peliculas(id=91153956, titulo="Blade Runner", genero="Ciencia Ficción", rating=8.1),
            Peliculas(id=47377474, titulo="The Dark Knight Rises", genero="Bélico", rating=8.4),
            Peliculas(id=30060914, titulo="Get a Clue", genero="Comedia", rating=6.2),
            Peliculas(id=11615401, titulo="The Princess Bride", genero="Aventura", rating=7.5),
            Peliculas(id=87538292, titulo="Monsters Inc.", genero="Animación", rating=8.1),
            Peliculas(id=46804999, titulo="Guardians of the Galaxy Vol. 2", genero="Superhéroes", rating=7.1),
            Peliculas(id=73079370, titulo="Thor: The Dark World", genero="Animación", rating=7.2),
            Peliculas(id=95054110, titulo="Thor: Ragnarok", genero="Superhéroes", rating=7.9),
            Peliculas(id=33896817, titulo="La La Land", genero="Musical", rating=8.0),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=42456754, titulo="The Matrix Reloaded", genero="Fantasía", rating=7.2),
            Peliculas(id=85068287, titulo="Wendy Wu: Homecoming Warrior", genero="Acción", rating=6.2),
            Peliculas(id=39971720, titulo="Ant-Man", genero="Superhéroes", rating=7.5),
            Peliculas(id=62863901, titulo="The Prestige", genero="Superhéroes", rating=8.6),
            Peliculas(id=93369344, titulo="Avengers: Infinity War", genero="Superhéroes", rating=8.4),
            Peliculas(id=11568343, titulo="The Social Network", genero="Drama", rating=7.7),
            Peliculas(id=79145064, titulo="Forrest Gump", genero="Ciencia", rating=8.8),
            Peliculas(id=81187977, titulo="Moana", genero="Animación", rating=8.0),
            Peliculas(id=34755557, titulo="The Notebook", genero="Western", rating=7.8),
            Peliculas(id=59848286, titulo="The Silence of the Lambs", genero="Suspense", rating=8.6),
            Peliculas(id=92004621, titulo="Treasure Planet", genero="Deportes", rating=7.7),
            Peliculas(id=95230455, titulo="Your Name", genero="Animación", rating=8.4),
            Peliculas(id=44000862, titulo="American History X", genero="Superhéroes", rating=8.5),
        ]
        lista_funciones = [
            Funciones(id=3158, numero_sala=9, id_pelicula=44000862, horario=4, fecha="08-03-23"),
            Funciones(id=6538, numero_sala=2, id_pelicula=91153956, horario=6, fecha="02-12-23"),
            Funciones(id=7918, numero_sala=2, id_pelicula=44000862, horario=8, fecha="06-07-23"),
            Funciones(id=8367, numero_sala=3, id_pelicula=59848286, horario=1, fecha="03-08-23"),
            Funciones(id=4018, numero_sala=2, id_pelicula=21803572, horario=2, fecha="01-08-23"),
            Funciones(id=3509, numero_sala=1, id_pelicula=91153956, horario=2, fecha="04-10-23"),
            Funciones(id=1697, numero_sala=5, id_pelicula=44000862, horario=6, fecha="25-08-23"),
            Funciones(id=1016, numero_sala=8, id_pelicula=73079370, horario=6, fecha="21-01-23"),
            Funciones(id=4385, numero_sala=2, id_pelicula=49895401, horario=7, fecha="13-10-23"),
            Funciones(id=3379, numero_sala=5, id_pelicula=93369344, horario=3, fecha="23-12-23"),
            Funciones(id=2600, numero_sala=6, id_pelicula=64787434, horario=5, fecha="26-03-23"),
            Funciones(id=7498, numero_sala=2, id_pelicula=46804999, horario=9, fecha="16-09-23"),
            Funciones(id=9685, numero_sala=4, id_pelicula=47377474, horario=1, fecha="06-02-23"),
            Funciones(id=9769, numero_sala=9, id_pelicula=81187977, horario=7, fecha="18-03-23"),
            Funciones(id=3947, numero_sala=4, id_pelicula=91153956, horario=6, fecha="22-07-23"),
            Funciones(id=8987, numero_sala=7, id_pelicula=46804999, horario=1, fecha="17-04-23"),
            Funciones(id=5761, numero_sala=7, id_pelicula=11568343, horario=4, fecha="23-01-23"),
            Funciones(id=7214, numero_sala=6, id_pelicula=39971720, horario=9, fecha="02-05-23"),
            Funciones(id=6783, numero_sala=7, id_pelicula=23678361, horario=1, fecha="05-03-23"),
            Funciones(id=1396, numero_sala=1, id_pelicula=27868789, horario=5, fecha="28-12-23"),
            Funciones(id=9954, numero_sala=5, id_pelicula=44000862, horario=5, fecha="15-08-23"),
            Funciones(id=8217, numero_sala=8, id_pelicula=91153956, horario=6, fecha="14-06-23"),
            Funciones(id=2425, numero_sala=9, id_pelicula=44000862, horario=7, fecha="10-01-23"),
            Funciones(id=6055, numero_sala=6, id_pelicula=73079370, horario=8, fecha="11-01-23"),
            Funciones(id=8839, numero_sala=1, id_pelicula=42456754, horario=6, fecha="21-09-23"),
            Funciones(id=2849, numero_sala=9, id_pelicula=81187977, horario=6, fecha="06-04-23"),
            Funciones(id=7820, numero_sala=2, id_pelicula=95054110, horario=7, fecha="13-03-23"),
            Funciones(id=5753, numero_sala=6, id_pelicula=42456754, horario=9, fecha="13-04-23"),
            Funciones(id=2184, numero_sala=1, id_pelicula=95230455, horario=1, fecha="23-03-23"),
            Funciones(id=3385, numero_sala=8, id_pelicula=42456754, horario=6, fecha="19-06-23"),
        ]
        lista_esperada = [1016, 9769, 1396, 6055, 2849, 2184]

        resultado = id_funciones_genero(iter(lista_peliculas), iter(lista_funciones), "Animación")
        lista_resultado = list(resultado)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)

    def test_2(self):
        """
        Genero sin funciones
        """
        lista_peliculas = [
            Peliculas(id=40873645, titulo="The Terminator", genero="Ciencia Ficción", rating=8.5),
            Peliculas(id=96374386, titulo="The Lord of the Rings: The Two Towers", genero="Animación", rating=8.7),
            Peliculas(id=42475848, titulo="Spirited Away", genero="Animación", rating=8.6),
            Peliculas(id=45745398, titulo="The Green Mile", genero="Animación", rating=8.2),
            Peliculas(id=21261768, titulo="The Jungle Book", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=36540564, titulo="Tarzan", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=95054110, titulo="Thor: Ragnarok", genero="Superhéroes", rating=7.9),
            Peliculas(id=32568878, titulo="Harry Potter and the Sorcerer's Stone", genero="Bélico", rating=7.6),
            Peliculas(id=33896817, titulo="La La Land", genero="Musical", rating=8.0),
            Peliculas(id=87538292, titulo="Monsters Inc.", genero="Animación", rating=8.1),
            Peliculas(id=57395306, titulo="Inuyasha", genero="Animación", rating=8.4),
            Peliculas(id=20610700, titulo="The Princess and the Frog", genero="Animación", rating=7.1),
            Peliculas(id=25035329, titulo="The Matrix", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=83829256, titulo="Stuck in the Suburbs", genero="Comedia", rating=6.2),
            Peliculas(id=28527704, titulo="Princess Mononoke", genero="Animación", rating=8.4),
            Peliculas(id=11164686, titulo="Interstellar", genero="Ciencia Ficción", rating=8.6),
            Peliculas(id=39971720, titulo="Ant-Man", genero="Superhéroes", rating=7.5),
            Peliculas(id=40267632, titulo="The Imitation Game", genero="Drama", rating=9.6),
            Peliculas(id=46804999, titulo="Guardians of the Galaxy Vol. 2", genero="Superhéroes", rating=7.1),
            Peliculas(id=25227924, titulo="Kill Bill: Vol. 2", genero="Western", rating=8.7),
            Peliculas(id=75901837, titulo="Akira", genero="Animación", rating=8.6),
            Peliculas(id=51512157, titulo="Pulp Fiction", genero="Crimen", rating=8.2),
            Peliculas(id=87114047, titulo="Jump In!", genero="Deportes", rating=5.4),
            Peliculas(id=75660450, titulo="The Incredible Hulk", genero="Animación", rating=6.7),
            Peliculas(id=19745617, titulo="The Dark Knight", genero="Acción", rating=9.0),
            Peliculas(id=71285784, titulo="Avengers: Age of Ultron", genero="Animación", rating=7.6),
            Peliculas(id=42038936, titulo="The Matrix Revolutions", genero="Fantasía", rating=7.3),
            Peliculas(id=63162203, titulo="The Departed", genero="Animación", rating=8.2),
            Peliculas(id=34304754, titulo="Iron Man 3", genero="Animación", rating=7.1),
        ]
        lista_funciones = [
            Funciones(id=3081, numero_sala=5, id_pelicula=33896817, horario=7, fecha="07-04-23"),
            Funciones(id=1142, numero_sala=6, id_pelicula=40267632, horario=1, fecha="25-11-23"),
            Funciones(id=3879, numero_sala=2, id_pelicula=87538292, horario=7, fecha="12-12-23"),
            Funciones(id=5550, numero_sala=8, id_pelicula=20610700, horario=5, fecha="15-06-23"),
            Funciones(id=3591, numero_sala=5, id_pelicula=95054110, horario=7, fecha="01-10-23"),
            Funciones(id=5021, numero_sala=6, id_pelicula=45745398, horario=9, fecha="02-02-23"),
            Funciones(id=9943, numero_sala=4, id_pelicula=45745398, horario=8, fecha="13-10-23"),
            Funciones(id=8174, numero_sala=1, id_pelicula=75901837, horario=7, fecha="15-06-23"),
            Funciones(id=9398, numero_sala=2, id_pelicula=20610700, horario=1, fecha="15-09-23"),
            Funciones(id=7692, numero_sala=7, id_pelicula=32568878, horario=1, fecha="14-01-23"),
            Funciones(id=2340, numero_sala=3, id_pelicula=19745617, horario=2, fecha="01-07-23"),
            Funciones(id=8303, numero_sala=4, id_pelicula=46804999, horario=1, fecha="28-09-23"),
            Funciones(id=9672, numero_sala=8, id_pelicula=21261768, horario=9, fecha="19-10-23"),
            Funciones(id=7915, numero_sala=7, id_pelicula=57395306, horario=5, fecha="16-06-23"),
            Funciones(id=3126, numero_sala=5, id_pelicula=40267632, horario=6, fecha="25-06-23"),
            Funciones(id=3711, numero_sala=1, id_pelicula=11164686, horario=8, fecha="11-02-23"),
            Funciones(id=4814, numero_sala=5, id_pelicula=42038936, horario=1, fecha="25-11-23"),
            Funciones(id=5534, numero_sala=5, id_pelicula=45745398, horario=5, fecha="19-06-23"),
            Funciones(id=7663, numero_sala=4, id_pelicula=71285784, horario=4, fecha="25-08-23"),
            Funciones(id=6839, numero_sala=1, id_pelicula=36540564, horario=9, fecha="11-01-23"),
            Funciones(id=1060, numero_sala=4, id_pelicula=46804999, horario=3, fecha="13-03-23"),
            Funciones(id=4987, numero_sala=1, id_pelicula=45745398, horario=2, fecha="04-09-23"),
            Funciones(id=7348, numero_sala=1, id_pelicula=83829256, horario=6, fecha="03-07-23"),
            Funciones(id=1954, numero_sala=9, id_pelicula=21261768, horario=9, fecha="12-07-23"),
            Funciones(id=4632, numero_sala=5, id_pelicula=19745617, horario=7, fecha="13-06-23"),
            Funciones(id=4645, numero_sala=1, id_pelicula=39971720, horario=4, fecha="26-06-23"),
            Funciones(id=5320, numero_sala=9, id_pelicula=96374386, horario=1, fecha="13-09-23"),
            Funciones(id=2889, numero_sala=9, id_pelicula=25035329, horario=1, fecha="08-01-23"),
            Funciones(id=3720, numero_sala=3, id_pelicula=71285784, horario=8, fecha="04-01-23"),
            Funciones(id=5062, numero_sala=1, id_pelicula=63162203, horario=5, fecha="19-02-23"),
        ]
        lista_esperada = []

        resultado = id_funciones_genero(iter(lista_peliculas), iter(lista_funciones), "Ciencia")
        lista_resultado = list(resultado)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)

    def test_3(self):
        """
        Genero no existe
        """
        lista_peliculas = [
            Peliculas(id=89737370, titulo="Iron Man", genero="Animación", rating=7.6),
            Peliculas(id=75660450, titulo="The Incredible Hulk", genero="Animación", rating=6.7),
            Peliculas(id=38937194, titulo="Tangled", genero="Animación", rating=8.0),
            Peliculas(id=34755557, titulo="The Notebook", genero="Western", rating=7.8),
            Peliculas(id=93369344, titulo="Avengers: Infinity War", genero="Superhéroes", rating=8.4),
            Peliculas(id=19745617, titulo="The Dark Knight", genero="Acción", rating=9.0),
            Peliculas(id=95413069, titulo="The Cheetah Girls", genero="Comedia", rating=5.8),
            Peliculas(id=20610700, titulo="The Princess and the Frog", genero="Animación", rating=7.1),
            Peliculas(id=77439731, titulo="The Lord of the Rings: The Fellowship of the Ring", genero="Animación", rating=8.4),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
            Peliculas(id=95817124, titulo="Fight Club", genero="Crimen", rating=8.8),
            Peliculas(id=70752273, titulo="Gladiator", genero="Crimen", rating=8.5),
            Peliculas(id=29533644, titulo="Saving Private Ryan", genero="Superhéroes", rating=8.6),
            Peliculas(id=67027889, titulo="Seven Samurai", genero="Crimen", rating=9.0),
            Peliculas(id=89708109, titulo="Captain America: Civil War", genero="Superhéroes", rating=8.0),
            Peliculas(id=47191880, titulo="Thor", genero="Animación", rating=7.2),
            Peliculas(id=30060914, titulo="Get a Clue", genero="Comedia", rating=6.2),
            Peliculas(id=23221543, titulo="Halloweentown", genero="Fantasía", rating=6.3),
            Peliculas(id=11615401, titulo="The Princess Bride", genero="Aventura", rating=7.5),
            Peliculas(id=89756869, titulo="The Emperor's New Groove", genero="Deportes", rating=6.9),
            Peliculas(id=84580833, titulo="Wreck-It Ralph", genero="Animación", rating=7.5),
            Peliculas(id=75203860, titulo="Kill Bill: Vol. 1", genero="Superhéroes", rating=8.1),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=78376301, titulo="Smart House", genero="Ciencia Ficción", rating=6.2),
            Peliculas(id=61384134, titulo="Mamma Mia", genero="Musical", rating=10.0),
            Peliculas(id=62764502, titulo="Toy Story", genero="Animación", rating=8.3),
            Peliculas(id=75259113, titulo="Up", genero="Crimen", rating=8.4),
            Peliculas(id=85032662, titulo="Aladdin", genero="Animación", rating=8.0),
            Peliculas(id=87114047, titulo="Jump In!", genero="Deportes", rating=5.4),
            Peliculas(id=25035329, titulo="The Matrix", genero="Ciencia Ficción", rating=8.8),
        ]
        lista_funciones = [
            Funciones(id=8467, numero_sala=3, id_pelicula=34755557, horario=8, fecha="17-06-23"),
            Funciones(id=4552, numero_sala=2, id_pelicula=11615401, horario=9, fecha="11-04-23"),
            Funciones(id=3633, numero_sala=4, id_pelicula=89708109, horario=2, fecha="18-08-23"),
            Funciones(id=3418, numero_sala=4, id_pelicula=49895401, horario=9, fecha="24-04-23"),
            Funciones(id=1154, numero_sala=1, id_pelicula=75259113, horario=2, fecha="20-02-23"),
            Funciones(id=8811, numero_sala=5, id_pelicula=30060914, horario=1, fecha="24-10-23"),
            Funciones(id=9641, numero_sala=7, id_pelicula=77439731, horario=6, fecha="17-08-23"),
            Funciones(id=1200, numero_sala=7, id_pelicula=20610700, horario=3, fecha="15-07-23"),
            Funciones(id=3912, numero_sala=8, id_pelicula=87114047, horario=7, fecha="16-07-23"),
            Funciones(id=5058, numero_sala=6, id_pelicula=42103973, horario=6, fecha="23-09-23"),
            Funciones(id=9784, numero_sala=8, id_pelicula=62764502, horario=8, fecha="04-01-23"),
            Funciones(id=3839, numero_sala=4, id_pelicula=49895401, horario=4, fecha="22-04-23"),
            Funciones(id=1354, numero_sala=3, id_pelicula=67027889, horario=1, fecha="23-09-23"),
            Funciones(id=9063, numero_sala=8, id_pelicula=20610700, horario=2, fecha="23-09-23"),
            Funciones(id=2997, numero_sala=9, id_pelicula=11615401, horario=1, fecha="25-04-23"),
            Funciones(id=3793, numero_sala=9, id_pelicula=30060914, horario=5, fecha="11-04-23"),
            Funciones(id=2708, numero_sala=2, id_pelicula=93369344, horario=2, fecha="23-05-23"),
            Funciones(id=6527, numero_sala=5, id_pelicula=89737370, horario=2, fecha="12-01-23"),
            Funciones(id=4576, numero_sala=7, id_pelicula=75259113, horario=2, fecha="06-05-23"),
            Funciones(id=8674, numero_sala=3, id_pelicula=67027889, horario=9, fecha="28-02-23"),
            Funciones(id=1848, numero_sala=7, id_pelicula=89756869, horario=5, fecha="17-01-23"),
            Funciones(id=3307, numero_sala=5, id_pelicula=67027889, horario=4, fecha="28-10-23"),
            Funciones(id=8884, numero_sala=4, id_pelicula=11615401, horario=1, fecha="27-11-23"),
            Funciones(id=3454, numero_sala=6, id_pelicula=61384134, horario=7, fecha="10-06-23"),
            Funciones(id=3043, numero_sala=7, id_pelicula=78376301, horario=8, fecha="07-11-23"),
            Funciones(id=4787, numero_sala=6, id_pelicula=95413069, horario=9, fecha="13-02-23"),
            Funciones(id=9778, numero_sala=1, id_pelicula=93369344, horario=4, fecha="13-07-23"),
            Funciones(id=7883, numero_sala=6, id_pelicula=89756869, horario=5, fecha="18-01-23"),
            Funciones(id=2567, numero_sala=8, id_pelicula=29533644, horario=1, fecha="26-09-23"),
            Funciones(id=1297, numero_sala=9, id_pelicula=38937194, horario=5, fecha="09-02-23"),
        ]
        lista_esperada = []

        resultado = id_funciones_genero(iter(lista_peliculas), iter(lista_funciones), "Crimen 2")
        lista_resultado = list(resultado)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)

    def test_4(self):
        """
        Una pelicula con varias funciones
        """
        lista_peliculas = [
            Peliculas(id=41115118, titulo="Avatar", genero="Crimen", rating=7.8),
            Peliculas(id=75421892, titulo="The Little Mermaid", genero="Aventura", rating=8.0),
            Peliculas(id=36540564, titulo="Tarzan", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=99972342, titulo="The Cheetah Girls 2", genero="Comedia", rating=5.9),
            Peliculas(id=34304754, titulo="Iron Man 3", genero="Animación", rating=7.1),
            Peliculas(id=11568343, titulo="The Social Network", genero="Drama", rating=7.7),
            Peliculas(id=89737370, titulo="Iron Man", genero="Animación", rating=7.6),
            Peliculas(id=23678361, titulo="Scarface", genero="Crimen", rating=8.8),
            Peliculas(id=95230455, titulo="Your Name", genero="Animación", rating=8.4),
            Peliculas(id=19177277, titulo="High School Musical 3", genero="Musical", rating=6.9),
            Peliculas(id=40873645, titulo="The Terminator", genero="Ciencia Ficción", rating=8.5),
            Peliculas(id=95054110, titulo="Thor: Ragnarok", genero="Superhéroes", rating=7.9),
            Peliculas(id=87538292, titulo="Monsters Inc.", genero="Animación", rating=8.1),
            Peliculas(id=69065378, titulo="Black Panther", genero="Superhéroes", rating=8.0),
            Peliculas(id=57395306, titulo="Inuyasha", genero="Animación", rating=8.4),
            Peliculas(id=75259113, titulo="Up", genero="Crimen", rating=8.4),
            Peliculas(id=35569845, titulo="The Princess Diaries 2", genero="Comedia", rating=5.8),
            Peliculas(id=32152163, titulo="The Princess Diaries", genero="Comedia", rating=6.2),
            Peliculas(id=55774654, titulo="The Pianist", genero="Superhéroes", rating=8.5),
            Peliculas(id=25227924, titulo="Kill Bill: Vol. 2", genero="Western", rating=8.7),
            Peliculas(id=75759551, titulo="The Lion King", genero="Animación", rating=8.5),
            Peliculas(id=81744489, titulo="Cow Belles", genero="Comedia", rating=6.1),
            Peliculas(id=76172796, titulo="Inception", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=25035329, titulo="The Matrix", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=81591753, titulo="Zootopia", genero="Animación", rating=8.0),
            Peliculas(id=77439731, titulo="The Lord of the Rings: The Fellowship of the Ring", genero="Animación", rating=8.4),
            Peliculas(id=72588542, titulo="Frozen", genero="Animación", rating=7.4),
            Peliculas(id=34755557, titulo="The Notebook", genero="Western", rating=7.8),
            Peliculas(id=30060914, titulo="Get a Clue", genero="Comedia", rating=6.2),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
        ]
        lista_funciones = [
            Funciones(id=4162, numero_sala=2, id_pelicula=23678361, horario=1, fecha="27-06-23"),
            Funciones(id=6444, numero_sala=9, id_pelicula=95230455, horario=7, fecha="08-07-23"),
            Funciones(id=8511, numero_sala=4, id_pelicula=95054110, horario=3, fecha="13-01-23"),
            Funciones(id=8295, numero_sala=3, id_pelicula=75759551, horario=4, fecha="06-09-23"),
            Funciones(id=8460, numero_sala=4, id_pelicula=69065378, horario=4, fecha="19-09-23"),
            Funciones(id=9354, numero_sala=4, id_pelicula=25227924, horario=2, fecha="04-04-23"),
            Funciones(id=2522, numero_sala=1, id_pelicula=23678361, horario=7, fecha="15-06-23"),
            Funciones(id=3009, numero_sala=9, id_pelicula=75421892, horario=8, fecha="03-02-23"),
            Funciones(id=3163, numero_sala=8, id_pelicula=69065378, horario=1, fecha="04-02-23"),
            Funciones(id=3109, numero_sala=1, id_pelicula=25035329, horario=4, fecha="10-11-23"),
            Funciones(id=4099, numero_sala=7, id_pelicula=55774654, horario=5, fecha="16-07-23"),
            Funciones(id=5335, numero_sala=2, id_pelicula=42103973, horario=8, fecha="01-10-23"),
            Funciones(id=8839, numero_sala=2, id_pelicula=41115118, horario=2, fecha="18-11-23"),
            Funciones(id=6789, numero_sala=3, id_pelicula=76172796, horario=8, fecha="18-10-23"),
            Funciones(id=6833, numero_sala=9, id_pelicula=72588542, horario=5, fecha="15-09-23"),
            Funciones(id=5071, numero_sala=6, id_pelicula=34755557, horario=2, fecha="19-12-23"),
            Funciones(id=7295, numero_sala=8, id_pelicula=36540564, horario=4, fecha="12-10-23"),
            Funciones(id=9491, numero_sala=9, id_pelicula=75759551, horario=3, fecha="14-03-23"),
            Funciones(id=9126, numero_sala=9, id_pelicula=34755557, horario=6, fecha="16-10-23"),
            Funciones(id=8735, numero_sala=2, id_pelicula=30060914, horario=8, fecha="09-12-23"),
            Funciones(id=5468, numero_sala=3, id_pelicula=23678361, horario=8, fecha="10-08-23"),
            Funciones(id=7403, numero_sala=6, id_pelicula=87538292, horario=6, fecha="02-05-23"),
            Funciones(id=8152, numero_sala=8, id_pelicula=72588542, horario=8, fecha="18-06-23"),
            Funciones(id=4395, numero_sala=9, id_pelicula=40873645, horario=1, fecha="07-12-23"),
            Funciones(id=6703, numero_sala=3, id_pelicula=55774654, horario=4, fecha="19-07-23"),
            Funciones(id=5368, numero_sala=8, id_pelicula=30060914, horario=1, fecha="16-03-23"),
            Funciones(id=3789, numero_sala=9, id_pelicula=75421892, horario=7, fecha="01-05-23"),
            Funciones(id=2997, numero_sala=8, id_pelicula=34304754, horario=7, fecha="04-08-23"),
            Funciones(id=6632, numero_sala=4, id_pelicula=99972342, horario=2, fecha="22-05-23"),
            Funciones(id=6153, numero_sala=7, id_pelicula=34755557, horario=4, fecha="23-09-23"),
        ]
        lista_esperada = [3009, 3789]

        resultado = id_funciones_genero(iter(lista_peliculas), iter(lista_funciones), "Aventura")
        lista_resultado = list(resultado)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        for n in lista_esperada:
            self.assertIn(n, lista_resultado)
        for n in lista_resultado:
            self.assertIn(n, lista_esperada)

if __name__ == '__main__':
    unittest.main(verbosity=2)