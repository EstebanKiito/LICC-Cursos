import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import genero_mas_transmitido
from utilidades import Peliculas, Funciones


class TestVacioGeneroMasTransmitido(unittest.TestCase):

    def test_0(self):
        """
        Sin funciones en la fecha
        """
        lista_peliculas = [
            Peliculas(id=20610700, titulo="The Princess and the Frog", genero="Animación", rating=7.1),
            Peliculas(id=78947971, titulo="Beauty and the Beast", genero="Animación", rating=8.0),
            Peliculas(id=21261768, titulo="The Jungle Book", genero="Ciencia Ficción", rating=7.6),
            Peliculas(id=42986062, titulo="The Lord of the Rings", genero="Fantasía", rating=8.7),
            Peliculas(id=41115118, titulo="Avatar", genero="Crimen", rating=7.8),
            Peliculas(id=72588542, titulo="Frozen", genero="Animación", rating=7.4),
            Peliculas(id=21803572, titulo="Avengers", genero="Acción", rating=8.0),
            Peliculas(id=34304754, titulo="Iron Man 3", genero="Animación", rating=7.1),
            Peliculas(id=59848286, titulo="The Silence of the Lambs", genero="Suspense", rating=8.6),
            Peliculas(id=42103973, titulo="Schindler's List", genero="Fantasía", rating=9.3),
            Peliculas(id=98009659, titulo="Twitches", genero="Fantasía", rating=6.7),
            Peliculas(id=44000862, titulo="American History X", genero="Superhéroes", rating=8.5),
            Peliculas(id=11615401, titulo="The Princess Bride", genero="Aventura", rating=7.5),
            Peliculas(id=38463448, titulo="Spider-Man: Homecoming", genero="Superhéroes", rating=7.5),
            Peliculas(id=23221543, titulo="Halloweentown", genero="Fantasía", rating=6.3),
            Peliculas(id=64787434, titulo="Casino", genero="Western", rating=8.5),
            Peliculas(id=83566857, titulo="The Usual Suspects", genero="Superhéroes", rating=8.5),
            Peliculas(id=90803337, titulo="High School Musical 2", genero="Musical", rating=6.1),
            Peliculas(id=83829256, titulo="Stuck in the Suburbs", genero="Comedia", rating=6.2),
            Peliculas(id=67202232, titulo="Memento", genero="Superhéroes", rating=8.5),
            Peliculas(id=43516202, titulo="The Great Gatsby", genero="Drama", rating=8.5),
            Peliculas(id=35100234, titulo="Terminator 2: Judgment Day", genero="Animación", rating=8.5),
            Peliculas(id=69065378, titulo="Black Panther", genero="Superhéroes", rating=8.0),
            Peliculas(id=35569845, titulo="The Princess Diaries 2", genero="Comedia", rating=5.8),
            Peliculas(id=57395306, titulo="Inuyasha", genero="Animación", rating=8.4),
            Peliculas(id=78376301, titulo="Smart House", genero="Ciencia Ficción", rating=6.2),
            Peliculas(id=87114047, titulo="Jump In!", genero="Deportes", rating=5.4),
            Peliculas(id=25227924, titulo="Kill Bill: Vol. 2", genero="Western", rating=8.7),
            Peliculas(id=75660450, titulo="The Incredible Hulk", genero="Animación", rating=6.7),
            Peliculas(id=38937194, titulo="Tangled", genero="Animación", rating=8.0),
        ]
        lista_funciones = [
            Funciones(id=2262, numero_sala=7, id_pelicula=11615401, horario=9, fecha="27-09-23"),
            Funciones(id=1011, numero_sala=9, id_pelicula=21803572, horario=1, fecha="25-09-23"),
            Funciones(id=2446, numero_sala=1, id_pelicula=90803337, horario=7, fecha="07-01-23"),
            Funciones(id=6429, numero_sala=8, id_pelicula=43516202, horario=8, fecha="09-12-23"),
            Funciones(id=9294, numero_sala=8, id_pelicula=25227924, horario=3, fecha="16-06-23"),
            Funciones(id=3569, numero_sala=2, id_pelicula=35100234, horario=2, fecha="21-07-23"),
            Funciones(id=5569, numero_sala=5, id_pelicula=75660450, horario=2, fecha="10-06-23"),
            Funciones(id=3370, numero_sala=5, id_pelicula=38463448, horario=5, fecha="15-12-23"),
            Funciones(id=6112, numero_sala=6, id_pelicula=20610700, horario=8, fecha="26-02-23"),
            Funciones(id=1836, numero_sala=7, id_pelicula=59848286, horario=4, fecha="10-07-23"),
            Funciones(id=9317, numero_sala=5, id_pelicula=42986062, horario=4, fecha="17-04-23"),
            Funciones(id=6369, numero_sala=3, id_pelicula=83829256, horario=5, fecha="04-04-23"),
            Funciones(id=1899, numero_sala=2, id_pelicula=20610700, horario=7, fecha="24-06-23"),
            Funciones(id=7142, numero_sala=2, id_pelicula=87114047, horario=5, fecha="23-03-23"),
            Funciones(id=5893, numero_sala=6, id_pelicula=64787434, horario=5, fecha="04-05-23"),
            Funciones(id=1408, numero_sala=3, id_pelicula=83829256, horario=5, fecha="16-04-23"),
            Funciones(id=5815, numero_sala=6, id_pelicula=59848286, horario=9, fecha="27-09-23"),
            Funciones(id=2080, numero_sala=2, id_pelicula=98009659, horario=2, fecha="14-02-23"),
            Funciones(id=2000, numero_sala=6, id_pelicula=23221543, horario=6, fecha="05-08-23"),
            Funciones(id=9123, numero_sala=6, id_pelicula=42103973, horario=3, fecha="18-10-23"),
            Funciones(id=8907, numero_sala=3, id_pelicula=23221543, horario=5, fecha="21-05-23"),
            Funciones(id=9084, numero_sala=6, id_pelicula=90803337, horario=4, fecha="18-09-23"),
            Funciones(id=2620, numero_sala=1, id_pelicula=67202232, horario=2, fecha="24-05-23"),
            Funciones(id=7994, numero_sala=1, id_pelicula=21261768, horario=6, fecha="20-02-23"),
            Funciones(id=1431, numero_sala=9, id_pelicula=87114047, horario=6, fecha="14-02-23"),
            Funciones(id=6679, numero_sala=7, id_pelicula=87114047, horario=6, fecha="03-03-23"),
            Funciones(id=8876, numero_sala=5, id_pelicula=25227924, horario=3, fecha="21-01-23"),
            Funciones(id=6410, numero_sala=4, id_pelicula=90803337, horario=9, fecha="17-09-23"),
            Funciones(id=9360, numero_sala=8, id_pelicula=23221543, horario=8, fecha="22-12-23"),
            Funciones(id=3920, numero_sala=1, id_pelicula=98009659, horario=1, fecha="14-02-23"),
        ]
        resultado = genero_mas_transmitido(iter(lista_peliculas), iter(lista_funciones), "26-02-1999")
        self.assertIsInstance(resultado, str)
        self.assertEqual(resultado, "")


if __name__ == '__main__':
    unittest.main(verbosity=2)
