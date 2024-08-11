import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import genero_mas_transmitido
from utilidades import Peliculas, Funciones


class TestGeneroMasTransmitido(unittest.TestCase):

    def test_0(self):
        """
        Test basico
        """
        lista_peliculas = [
            Peliculas(id=41068976, titulo="Cinderella", genero="Animación", rating=7.1),
            Peliculas(id=89756869, titulo="The Emperor's New Groove", genero="Deportes", rating=6.9),
            Peliculas(id=40873645, titulo="The Terminator", genero="Ciencia Ficción", rating=8.5),
            Peliculas(id=91153956, titulo="Blade Runner", genero="Ciencia Ficción", rating=8.1),
            Peliculas(id=42475848, titulo="Spirited Away", genero="Animación", rating=8.6),
            Peliculas(id=78376301, titulo="Smart House", genero="Ciencia Ficción", rating=6.2),
            Peliculas(id=47191880, titulo="Thor", genero="Animación", rating=7.2),
            Peliculas(id=45064961, titulo="Big Hero 6", genero="Animación", rating=7.8),
            Peliculas(id=70752273, titulo="Gladiator", genero="Crimen", rating=8.5),
            Peliculas(id=54541808, titulo="Matilda", genero="Comedia", rating=6.9),
            Peliculas(id=87114047, titulo="Jump In!", genero="Deportes", rating=5.4),
            Peliculas(id=19745617, titulo="The Dark Knight", genero="Acción", rating=9.0),
            Peliculas(id=85068287, titulo="Wendy Wu: Homecoming Warrior", genero="Acción", rating=6.2),
            Peliculas(id=11615401, titulo="The Princess Bride", genero="Aventura", rating=7.5),
            Peliculas(id=58643843, titulo="Iron Man 2", genero="Animación", rating=7.0),
            Peliculas(id=75259113, titulo="Up", genero="Crimen", rating=8.4),
            Peliculas(id=34321575, titulo="Ant-Man and The Wasp", genero="Superhéroes", rating=7.1),
            Peliculas(id=75759551, titulo="The Lion King", genero="Animación", rating=8.5),
            Peliculas(id=93369344, titulo="Avengers: Infinity War", genero="Superhéroes", rating=8.4),
            Peliculas(id=25035329, titulo="The Matrix", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=85032662, titulo="Aladdin", genero="Animación", rating=8.0),
            Peliculas(id=35569845, titulo="The Princess Diaries 2", genero="Comedia", rating=5.8),
            Peliculas(id=32152163, titulo="The Princess Diaries", genero="Comedia", rating=6.2),
            Peliculas(id=95230455, titulo="Your Name", genero="Animación", rating=8.4),
            Peliculas(id=61161814, titulo="High School Musical", genero="Musical", rating=6.4),
            Peliculas(id=51512157, titulo="Pulp Fiction", genero="Crimen", rating=8.2),
            Peliculas(id=95417284, titulo="Camp Rock", genero="Musical", rating=5.1),
            Peliculas(id=38937194, titulo="Tangled", genero="Animación", rating=8.0),
            Peliculas(id=19177277, titulo="High School Musical 3", genero="Musical", rating=6.9),
            Peliculas(id=42038936, titulo="The Matrix Revolutions", genero="Fantasía", rating=7.3),
        ]
        lista_funciones = [
            Funciones(id=4971, numero_sala=7, id_pelicula=91153956, horario=7, fecha="25-08-23"),
            Funciones(id=1709, numero_sala=1, id_pelicula=40873645, horario=9, fecha="08-11-23"),
            Funciones(id=5507, numero_sala=6, id_pelicula=91153956, horario=1, fecha="24-06-23"),
            Funciones(id=4899, numero_sala=5, id_pelicula=40873645, horario=4, fecha="28-08-23"),
            Funciones(id=1677, numero_sala=7, id_pelicula=54541808, horario=6, fecha="08-11-23"),
            Funciones(id=2630, numero_sala=9, id_pelicula=25035329, horario=5, fecha="16-12-23"),
            Funciones(id=2789, numero_sala=3, id_pelicula=40873645, horario=6, fecha="24-06-23"),
            Funciones(id=7821, numero_sala=2, id_pelicula=78376301, horario=9, fecha="23-02-23"),
            Funciones(id=2358, numero_sala=4, id_pelicula=25035329, horario=2, fecha="24-06-23"),
            Funciones(id=3967, numero_sala=5, id_pelicula=95417284, horario=4, fecha="08-11-23"),
            Funciones(id=4743, numero_sala=8, id_pelicula=78376301, horario=7, fecha="01-07-23"),
            Funciones(id=2227, numero_sala=5, id_pelicula=91153956, horario=3, fecha="24-06-23"),
            Funciones(id=7196, numero_sala=8, id_pelicula=47191880, horario=5, fecha="24-06-23"),
            Funciones(id=2514, numero_sala=6, id_pelicula=78376301, horario=9, fecha="07-11-23"),
            Funciones(id=6432, numero_sala=5, id_pelicula=25035329, horario=9, fecha="24-06-23"),
            Funciones(id=5941, numero_sala=9, id_pelicula=35569845, horario=4, fecha="08-11-23"),
            Funciones(id=3598, numero_sala=4, id_pelicula=78376301, horario=4, fecha="01-10-23"),
            Funciones(id=6028, numero_sala=5, id_pelicula=58643843, horario=1, fecha="18-11-23"),
            Funciones(id=4164, numero_sala=2, id_pelicula=91153956, horario=8, fecha="19-10-23"),
            Funciones(id=8900, numero_sala=6, id_pelicula=40873645, horario=7, fecha="08-11-23"),
            Funciones(id=9901, numero_sala=8, id_pelicula=25035329, horario=4, fecha="27-01-23"),
            Funciones(id=8498, numero_sala=3, id_pelicula=95230455, horario=3, fecha="24-06-23"),
            Funciones(id=6376, numero_sala=8, id_pelicula=91153956, horario=3, fecha="08-11-23"),
            Funciones(id=9281, numero_sala=1, id_pelicula=47191880, horario=3, fecha="08-11-23"),
            Funciones(id=8019, numero_sala=1, id_pelicula=25035329, horario=9, fecha="24-06-23"),
            Funciones(id=1311, numero_sala=3, id_pelicula=42038936, horario=2, fecha="17-04-23"),
            Funciones(id=1688, numero_sala=3, id_pelicula=78376301, horario=9, fecha="08-11-23"),
            Funciones(id=3443, numero_sala=6, id_pelicula=87114047, horario=8, fecha="24-06-23"),
            Funciones(id=8434, numero_sala=3, id_pelicula=25035329, horario=9, fecha="18-03-23"),
            Funciones(id=5169, numero_sala=6, id_pelicula=91153956, horario=6, fecha="08-11-23"),
        ]

        resultado = genero_mas_transmitido(iter(lista_peliculas), iter(lista_funciones), "08-11-2023")
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, "Ciencia Ficción")

    def test_1(self):
        """
        Solo una funcion en la fecha
        """
        lista_peliculas = [
            Peliculas(id=45245368, titulo="The Even Stevens Movie", genero="Comedia", rating=6.6),
            Peliculas(id=42456754, titulo="The Matrix Reloaded", genero="Fantasía", rating=7.2),
            Peliculas(id=81169279, titulo="The Lord of the Rings: The Return of the King", genero="Animación", rating=8.7),
            Peliculas(id=11568343, titulo="The Social Network", genero="Drama", rating=7.7),
            Peliculas(id=23678361, titulo="Scarface", genero="Crimen", rating=8.8),
            Peliculas(id=75259113, titulo="Up", genero="Crimen", rating=8.4),
            Peliculas(id=89708109, titulo="Captain America: Civil War", genero="Superhéroes", rating=8.0),
            Peliculas(id=75203860, titulo="Kill Bill: Vol. 1", genero="Superhéroes", rating=8.1),
            Peliculas(id=69065378, titulo="Black Panther", genero="Superhéroes", rating=8.0),
            Peliculas(id=87210469, titulo="Doctor Strange", genero="Superhéroes", rating=7.3),
            Peliculas(id=23221543, titulo="Halloweentown", genero="Fantasía", rating=6.3),
            Peliculas(id=19745617, titulo="The Dark Knight", genero="Acción", rating=9.0),
            Peliculas(id=98009659, titulo="Twitches", genero="Fantasía", rating=6.7),
            Peliculas(id=34321575, titulo="Ant-Man and The Wasp", genero="Superhéroes", rating=7.1),
            Peliculas(id=71285784, titulo="Avengers: Age of Ultron", genero="Animación", rating=7.6),
            Peliculas(id=66226007, titulo="The Godfather: Part II", genero="Ciencia Ficción", rating=9.0),
            Peliculas(id=29533644, titulo="Saving Private Ryan", genero="Superhéroes", rating=8.6),
            Peliculas(id=20610700, titulo="The Princess and the Frog", genero="Animación", rating=7.1),
            Peliculas(id=90803337, titulo="High School Musical 2", genero="Musical", rating=6.1),
            Peliculas(id=42475848, titulo="Spirited Away", genero="Animación", rating=8.6),
            Peliculas(id=39971720, titulo="Ant-Man", genero="Superhéroes", rating=7.5),
            Peliculas(id=81187977, titulo="Moana", genero="Animación", rating=8.0),
            Peliculas(id=76004798, titulo="Incredibles", genero="Animación", rating=8.0),
            Peliculas(id=71903918, titulo="Shrek", genero="Animación", rating=7.8),
            Peliculas(id=73020923, titulo="Captain America: The First Avenger", genero="Animación", rating=7.0),
            Peliculas(id=63162203, titulo="The Departed", genero="Animación", rating=8.2),
            Peliculas(id=17287405, titulo="The Hunchback of Notre Dame", genero="Comedia", rating=6.9),
            Peliculas(id=51151305, titulo="Pocahontas", genero="Fantasía", rating=7.8),
            Peliculas(id=70752273, titulo="Gladiator", genero="Crimen", rating=8.5),
            Peliculas(id=95817124, titulo="Fight Club", genero="Crimen", rating=8.8),
        ]
        lista_funciones = [
            Funciones(id=8457, numero_sala=4, id_pelicula=29533644, horario=8, fecha="17-05-23"),
            Funciones(id=3343, numero_sala=6, id_pelicula=42456754, horario=2, fecha="14-10-23"),
            Funciones(id=6318, numero_sala=9, id_pelicula=75203860, horario=8, fecha="27-08-23"),
            Funciones(id=2447, numero_sala=3, id_pelicula=45245368, horario=1, fecha="07-03-23"),
            Funciones(id=8276, numero_sala=6, id_pelicula=73020923, horario=5, fecha="21-08-23"),
            Funciones(id=1505, numero_sala=9, id_pelicula=70752273, horario=9, fecha="17-02-23"),
            Funciones(id=4701, numero_sala=4, id_pelicula=73020923, horario=2, fecha="08-06-23"),
            Funciones(id=5874, numero_sala=5, id_pelicula=17287405, horario=9, fecha="11-12-23"),
            Funciones(id=4050, numero_sala=6, id_pelicula=95817124, horario=8, fecha="21-02-23"),
            Funciones(id=4233, numero_sala=1, id_pelicula=70752273, horario=6, fecha="18-11-23"),
            Funciones(id=5348, numero_sala=9, id_pelicula=71285784, horario=7, fecha="09-12-23"),
            Funciones(id=1731, numero_sala=1, id_pelicula=66226007, horario=3, fecha="28-01-23"),
            Funciones(id=9655, numero_sala=1, id_pelicula=90803337, horario=3, fecha="22-10-23"),
            Funciones(id=3096, numero_sala=8, id_pelicula=95817124, horario=6, fecha="04-10-23"),
            Funciones(id=7514, numero_sala=8, id_pelicula=29533644, horario=3, fecha="25-02-23"),
            Funciones(id=6240, numero_sala=9, id_pelicula=20610700, horario=8, fecha="20-11-23"),
            Funciones(id=9604, numero_sala=5, id_pelicula=45245368, horario=6, fecha="02-07-23"),
            Funciones(id=8520, numero_sala=7, id_pelicula=70752273, horario=2, fecha="18-08-23"),
            Funciones(id=4749, numero_sala=2, id_pelicula=81169279, horario=8, fecha="13-10-23"),
            Funciones(id=4804, numero_sala=3, id_pelicula=45245368, horario=5, fecha="07-06-23"),
            Funciones(id=1523, numero_sala=8, id_pelicula=17287405, horario=5, fecha="09-06-23"),
            Funciones(id=5261, numero_sala=2, id_pelicula=87210469, horario=4, fecha="13-09-23"),
            Funciones(id=9014, numero_sala=6, id_pelicula=75259113, horario=4, fecha="27-01-23"),
            Funciones(id=5721, numero_sala=4, id_pelicula=29533644, horario=9, fecha="07-06-23"),
            Funciones(id=7080, numero_sala=2, id_pelicula=39971720, horario=9, fecha="16-04-23"),
            Funciones(id=7209, numero_sala=9, id_pelicula=87210469, horario=7, fecha="01-03-23"),
            Funciones(id=2386, numero_sala=9, id_pelicula=20610700, horario=7, fecha="01-07-23"),
            Funciones(id=7709, numero_sala=9, id_pelicula=23678361, horario=8, fecha="01-10-23"),
            Funciones(id=4846, numero_sala=9, id_pelicula=51151305, horario=4, fecha="03-07-23"),
            Funciones(id=6840, numero_sala=4, id_pelicula=66226007, horario=9, fecha="23-08-23"),
        ]
        resultado = genero_mas_transmitido(iter(lista_peliculas), iter(lista_funciones), "21-02-2023")
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, "Crimen")

    def test_2(self):
        """
        Solo dos generos con la misma cantidad de funciones
        """
        lista_peliculas = [
            Peliculas(id=20610700, titulo="The Princess and the Frog", genero="Animación", rating=7.1),
            Peliculas(id=23678361, titulo="Scarface", genero="Crimen", rating=8.8),
            Peliculas(id=75203860, titulo="Kill Bill: Vol. 1", genero="Superhéroes", rating=8.1),
            Peliculas(id=42038936, titulo="The Matrix Revolutions", genero="Fantasía", rating=7.3),
            Peliculas(id=61234416, titulo="Howl's Moving Castle", genero="Animación", rating=8.9),
            Peliculas(id=57395306, titulo="Inuyasha", genero="Animación", rating=8.4),
            Peliculas(id=89756869, titulo="The Emperor's New Groove", genero="Deportes", rating=6.9),
            Peliculas(id=83829256, titulo="Stuck in the Suburbs", genero="Comedia", rating=6.2),
            Peliculas(id=32608840, titulo="Johnny Tsunami", genero="Deportes", rating=6.3),
            Peliculas(id=75421892, titulo="The Little Mermaid", genero="Aventura", rating=8.0),
            Peliculas(id=33896817, titulo="La La Land", genero="Musical", rating=8.0),
            Peliculas(id=30060914, titulo="Get a Clue", genero="Comedia", rating=6.2),
            Peliculas(id=11615401, titulo="The Princess Bride", genero="Aventura", rating=7.5),
            Peliculas(id=62764502, titulo="Toy Story", genero="Animación", rating=8.3),
            Peliculas(id=42986062, titulo="The Lord of the Rings", genero="Fantasía", rating=8.7),
            Peliculas(id=73079370, titulo="Thor: The Dark World", genero="Animación", rating=7.2),
            Peliculas(id=87210469, titulo="Doctor Strange", genero="Superhéroes", rating=7.3),
            Peliculas(id=41068976, titulo="Cinderella", genero="Animación", rating=7.1),
            Peliculas(id=32152163, titulo="The Princess Diaries", genero="Comedia", rating=6.2),
            Peliculas(id=55774654, titulo="The Pianist", genero="Superhéroes", rating=8.5),
            Peliculas(id=41115118, titulo="Avatar", genero="Crimen", rating=7.8),
            Peliculas(id=42456754, titulo="The Matrix Reloaded", genero="Fantasía", rating=7.2),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
            Peliculas(id=75259113, titulo="Up", genero="Crimen", rating=8.4),
            Peliculas(id=75660450, titulo="The Incredible Hulk", genero="Superhéroes", rating=6.7),
            Peliculas(id=89708109, titulo="Captain America: Civil War", genero="Superhéroes", rating=8.0),
            Peliculas(id=49034902, titulo="The Godfather", genero="Crimen", rating=9.2),
            Peliculas(id=16359236, titulo="Mulan", genero="Deportes", rating=7.8),
            Peliculas(id=49895401, titulo="Pixel Perfect", genero="Ciencia Ficción", rating=6.0),
            Peliculas(id=76172796, titulo="Inception", genero="Ciencia Ficción", rating=8.8),
        ]
        lista_funciones = [
            Funciones(id=6262, numero_sala=5, id_pelicula=76172796, horario=9, fecha="22-06-23"),
            Funciones(id=2739, numero_sala=7, id_pelicula=42456754, horario=9, fecha="08-08-23"),
            Funciones(id=4988, numero_sala=3, id_pelicula=42456754, horario=9, fecha="12-06-23"),
            Funciones(id=8651, numero_sala=3, id_pelicula=41068976, horario=9, fecha="02-01-24"),
            Funciones(id=3915, numero_sala=8, id_pelicula=32608840, horario=3, fecha="27-10-23"),
            Funciones(id=6281, numero_sala=9, id_pelicula=75660450, horario=5, fecha="01-01-24"),
            Funciones(id=9054, numero_sala=5, id_pelicula=76172796, horario=4, fecha="14-06-23"),
            Funciones(id=1435, numero_sala=1, id_pelicula=75660450, horario=8, fecha="01-01-24"),
            Funciones(id=5776, numero_sala=4, id_pelicula=73079370, horario=4, fecha="06-01-23"),
            Funciones(id=6019, numero_sala=9, id_pelicula=41068976, horario=9, fecha="01-01-24"),
            Funciones(id=5377, numero_sala=7, id_pelicula=30060914, horario=4, fecha="17-03-23"),
            Funciones(id=3480, numero_sala=7, id_pelicula=73079370, horario=8, fecha="25-10-23"),
            Funciones(id=9324, numero_sala=8, id_pelicula=75660450, horario=2, fecha="01-01-24"),
            Funciones(id=3560, numero_sala=8, id_pelicula=89708109, horario=1, fecha="10-04-23"),
            Funciones(id=6494, numero_sala=5, id_pelicula=75660450, horario=7, fecha="01-01-24"),
            Funciones(id=3489, numero_sala=9, id_pelicula=55774654, horario=1, fecha="26-04-23"),
            Funciones(id=5704, numero_sala=8, id_pelicula=41068976, horario=7, fecha="01-01-24"),
            Funciones(id=6797, numero_sala=3, id_pelicula=41068976, horario=2, fecha="01-01-24"),
            Funciones(id=4354, numero_sala=8, id_pelicula=42986062, horario=3, fecha="27-03-23"),
            Funciones(id=5129, numero_sala=1, id_pelicula=61234416, horario=6, fecha="02-12-23"),
            Funciones(id=7540, numero_sala=2, id_pelicula=75660450, horario=2, fecha="01-01-24"),
            Funciones(id=2782, numero_sala=8, id_pelicula=41068976, horario=8, fecha="24-03-23"),
            Funciones(id=3568, numero_sala=1, id_pelicula=41068976, horario=3, fecha="01-01-24"),
            Funciones(id=2592, numero_sala=6, id_pelicula=42456754, horario=4, fecha="27-03-23"),
            Funciones(id=4341, numero_sala=1, id_pelicula=49895401, horario=3, fecha="02-08-23"),
            Funciones(id=6347, numero_sala=8, id_pelicula=33896817, horario=7, fecha="18-09-23"),
            Funciones(id=9609, numero_sala=8, id_pelicula=41068976, horario=7, fecha="01-01-24"),
            Funciones(id=2310, numero_sala=7, id_pelicula=75259113, horario=6, fecha="09-10-23"),
            Funciones(id=4742, numero_sala=3, id_pelicula=75660450, horario=9, fecha="02-01-24"),
            Funciones(id=9768, numero_sala=2, id_pelicula=41068976, horario=3, fecha="12-11-23"),
        ]
        resultado = genero_mas_transmitido(iter(lista_peliculas), iter(lista_funciones), "02-01-1924")
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, "Animación")

    def test_3(self):
        """
        Dos generos con misma cantidad de funciones y otros
        """
        lista_peliculas = [
            Peliculas(id=77439731, titulo="The Lord of the Rings: The Fellowship of the Ring", genero="Animación", rating=8.4),
            Peliculas(id=70752273, titulo="Gladiator", genero="Crimen", rating=8.5),
            Peliculas(id=98811629, titulo="Braveheart", genero="Animación", rating=8.5),
            Peliculas(id=25227924, titulo="Kill Bill: Vol. 2", genero="Western", rating=8.7),
            Peliculas(id=58643843, titulo="Iron Man 2", genero="Animación", rating=7.0),
            Peliculas(id=67027889, titulo="Seven Samurai", genero="Crimen", rating=9.0),
            Peliculas(id=11568343, titulo="The Social Network", genero="Drama", rating=7.7),
            Peliculas(id=89587896, titulo="Whiplash", genero="Drama", rating=8.5),
            Peliculas(id=76172796, titulo="Inception", genero="Ciencia Ficción", rating=8.8),
            Peliculas(id=23221543, titulo="Halloweentown", genero="Fantasía", rating=6.3),
            Peliculas(id=51512157, titulo="Pulp Fiction", genero="Crimen", rating=8.2),
            Peliculas(id=49034902, titulo="The Godfather", genero="Crimen", rating=9.2),
            Peliculas(id=78147558, titulo="Se7en", genero="Superhéroes", rating=8.6),
            Peliculas(id=92004621, titulo="Treasure Planet", genero="Deportes", rating=7.7),
            Peliculas(id=51151305, titulo="Pocahontas", genero="Fantasía", rating=7.8),
            Peliculas(id=42475848, titulo="Spirited Away", genero="Animación", rating=8.6),
            Peliculas(id=32608840, titulo="Johnny Tsunami", genero="Deportes", rating=6.3),
            Peliculas(id=90803337, titulo="High School Musical 2", genero="Musical", rating=6.1),
            Peliculas(id=47191880, titulo="Thor", genero="Animación", rating=7.2),
            Peliculas(id=99972342, titulo="The Cheetah Girls 2", genero="Comedia", rating=5.9),
            Peliculas(id=79145064, titulo="Forrest Gump", genero="Ciencia", rating=8.8),
            Peliculas(id=83566857, titulo="The Usual Suspects", genero="Superhéroes", rating=8.5),
            Peliculas(id=33612645, titulo="Goodfellas", genero="Animación", rating=8.9),
            Peliculas(id=75660450, titulo="The Incredible Hulk", genero="Animación", rating=6.7),
            Peliculas(id=81187977, titulo="Moana", genero="Animación", rating=8.0),
            Peliculas(id=42986062, titulo="The Lord of the Rings", genero="Fantasía", rating=8.7),
            Peliculas(id=78376301, titulo="Smart House", genero="Ciencia Ficción", rating=6.2),
            Peliculas(id=19177277, titulo="High School Musical 3", genero="Musical", rating=6.9),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
            Peliculas(id=34755557, titulo="The Notebook", genero="Western", rating=7.8),
        ]
        lista_funciones = [
            Funciones(id=6947, numero_sala=2, id_pelicula=23221543, horario=1, fecha="09-08-24"),
            Funciones(id=2704, numero_sala=6, id_pelicula=23221543, horario=8, fecha="09-08-24"),
            Funciones(id=3971, numero_sala=3, id_pelicula=42986062, horario=3, fecha="09-04-23"),
            Funciones(id=9431, numero_sala=8, id_pelicula=83566857, horario=7, fecha="09-08-24"),
            Funciones(id=1798, numero_sala=1, id_pelicula=78376301, horario=9, fecha="10-11-23"),
            Funciones(id=6969, numero_sala=4, id_pelicula=83566857, horario=1, fecha="09-08-24"),
            Funciones(id=8099, numero_sala=1, id_pelicula=89587896, horario=9, fecha="11-07-23"),
            Funciones(id=2801, numero_sala=6, id_pelicula=90803337, horario=6, fecha="09-08-24"),
            Funciones(id=1132, numero_sala=6, id_pelicula=49034902, horario=2, fecha="05-05-23"),
            Funciones(id=2246, numero_sala=1, id_pelicula=89587896, horario=9, fecha="01-04-23"),
            Funciones(id=3918, numero_sala=4, id_pelicula=89587896, horario=4, fecha="01-04-23"),
            Funciones(id=5454, numero_sala=1, id_pelicula=90803337, horario=9, fecha="09-08-24"),
            Funciones(id=9501, numero_sala=6, id_pelicula=67027889, horario=6, fecha="09-12-23"),
            Funciones(id=9714, numero_sala=6, id_pelicula=51512157, horario=3, fecha="09-08-24"),
            Funciones(id=3827, numero_sala=1, id_pelicula=79145064, horario=9, fecha="26-10-23"),
            Funciones(id=5486, numero_sala=7, id_pelicula=51512157, horario=2, fecha="09-08-24"),
            Funciones(id=4213, numero_sala=2, id_pelicula=75660450, horario=7, fecha="20-10-23"),
            Funciones(id=9846, numero_sala=3, id_pelicula=51512157, horario=9, fecha="09-08-24"),
            Funciones(id=4588, numero_sala=1, id_pelicula=99972342, horario=8, fecha="01-04-23"),
            Funciones(id=2781, numero_sala=3, id_pelicula=99972342, horario=2, fecha="01-04-23"),
            Funciones(id=9516, numero_sala=2, id_pelicula=78147558, horario=2, fecha="22-03-23"),
            Funciones(id=2063, numero_sala=2, id_pelicula=99972342, horario=5, fecha="01-04-23"),
            Funciones(id=2742, numero_sala=9, id_pelicula=51512157, horario=3, fecha="09-08-24"),
            Funciones(id=5907, numero_sala=3, id_pelicula=49034902, horario=4, fecha="17-12-23"),
            Funciones(id=9137, numero_sala=6, id_pelicula=99972342, horario=5, fecha="01-04-23"),
            Funciones(id=6406, numero_sala=6, id_pelicula=23221543, horario=8, fecha="09-08-24"),
            Funciones(id=8148, numero_sala=3, id_pelicula=99972342, horario=8, fecha="01-04-23"),
            Funciones(id=6899, numero_sala=5, id_pelicula=23221543, horario=2, fecha="09-08-24"),
            Funciones(id=9449, numero_sala=7, id_pelicula=51512157, horario=3, fecha="09-08-24"),
            Funciones(id=7917, numero_sala=5, id_pelicula=23221543, horario=1, fecha="09-08-24"),
        ]
        resultado = genero_mas_transmitido(iter(lista_peliculas), iter(lista_funciones), "09-08-1924")
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, "Fantasía")


if __name__ == '__main__':
    unittest.main(verbosity=2)
