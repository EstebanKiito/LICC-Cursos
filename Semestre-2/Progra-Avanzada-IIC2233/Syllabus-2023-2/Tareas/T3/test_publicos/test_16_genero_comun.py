import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import genero_comun
from utilidades import Personas, Peliculas, Funciones, Reservas


class TestGeneroComun(unittest.TestCase):

    def setUp(self):
        self.str1 = "En la función {} de la película {} la mayor parte del público es {}."
        self.str2 = "En la función {} de la película {} se obtiene que la mayor parte del público es de {} y {} con la misma cantidad de personas."
        self.str3 = "En la función {} de la película {} se obtiene que la cantidad de personas es igual para todos los géneros."

    def test_0(self):
        """
        Un solo género es el más común
        """
        personas = [
            Personas(id=781245, nombre='Alex', genero='No binario', edad=15),
            Personas(id=518367, nombre='Mateo', genero='Femenino', edad=77),
            Personas(id=654365, nombre='Isidora', genero='Femenino', edad=54),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=80),
            Personas(id=745219, nombre='Camila', genero='Masculino', edad=17),
            Personas(id=983156, nombre='Valeria', genero='Femenino', edad=39),
            Personas(id=429186, nombre='Paula', genero='Masculino', edad=88),
            Personas(id=962734, nombre='Renata', genero='Masculino', edad=97),
            Personas(id=735242, nombre='Juana', genero='Femenino', edad=23),
            Personas(id=836197, nombre='Julia', genero='No binario', edad=23),
        ]
        reservas = [
            Reservas(id_persona=781245, id_funcion=2660, numero_butaca='F6'),
            Reservas(id_persona=518367, id_funcion=2660, numero_butaca='B7'),
            Reservas(id_persona=983156, id_funcion=2660, numero_butaca='F5'),
            Reservas(id_persona=745219, id_funcion=2660, numero_butaca='G2'),
            Reservas(id_persona=951827, id_funcion=2660, numero_butaca='D7'),
            Reservas(id_persona=735242, id_funcion=2660, numero_butaca='F4'),
            Reservas(id_persona=836197, id_funcion=2660, numero_butaca='F8'),
            Reservas(id_persona=962734, id_funcion=2660, numero_butaca='F7'),
            Reservas(id_persona=654365, id_funcion=2660, numero_butaca='F9'),
            Reservas(id_persona=429186, id_funcion=2660, numero_butaca='H4'),
        ]
        funciones = [
            Funciones(id=2660, numero_sala=5, id_pelicula=19177277, horario=6, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=19177277, titulo='High School Musical 3', genero='Musical', rating=6.9),
        ]
        id_funcion = 2660
        titulo = 'High School Musical 3'
        expected_strings = [self.str1.format(id_funcion, titulo, 'Femenino')]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = genero_comun(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertIn(result, expected_strings)

    def test_1(self):
        """
        Dos géneros son los más comunes
        """
        personas = [
            Personas(id=765653, nombre='Arturo', genero='No binario', edad=43),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=80),
            Personas(id=126734, nombre='Juampi', genero='Masculino', edad=24),
            Personas(id=184926, nombre='Andrea', genero='No binario', edad=47),
            Personas(id=138975, nombre='Daniel', genero='Masculino', edad=66),
            Personas(id=654365, nombre='Isidora', genero='Femenino', edad=54),
            Personas(id=278561, nombre='Hernán', genero='Masculino', edad=38),
            Personas(id=244869, nombre='Renata', genero='Femenino', edad=23),
            Personas(id=463289, nombre='Teresita', genero='Femenino', edad=24),
            Personas(id=352429, nombre='Jorge', genero='Masculino', edad=45),
        ]
        reservas = [
            Reservas(id_persona=352429, id_funcion=2247, numero_butaca='H2'),
            Reservas(id_persona=654365, id_funcion=2247, numero_butaca='A8'),
            Reservas(id_persona=184926, id_funcion=2247, numero_butaca='B6'),
            Reservas(id_persona=765653, id_funcion=2247, numero_butaca='E5'),
            Reservas(id_persona=138975, id_funcion=2247, numero_butaca='B1'),
            Reservas(id_persona=126734, id_funcion=2247, numero_butaca='A5'),
            Reservas(id_persona=244869, id_funcion=2247, numero_butaca='E2'),
            Reservas(id_persona=463289, id_funcion=2247, numero_butaca='E9'),
            Reservas(id_persona=951827, id_funcion=2247, numero_butaca='F1'),
            Reservas(id_persona=278561, id_funcion=2247, numero_butaca='D10'),
        ]
        funciones = [
            Funciones(id=2247, numero_sala=2, id_pelicula=73020923, horario=4, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=73020923, titulo='Captain America: The First Avenger', genero='Animación', rating=7.0),
        ]

        id_funcion = 2247
        titulo = 'Captain America: The First Avenger'
        expected_strings = [
            self.str2.format(id_funcion, titulo, 'Femenino', 'Masculino'),
            self.str2.format(id_funcion, titulo, 'Masculino', 'Femenino'),
        ]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = genero_comun(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertIn(result, expected_strings)

    def test_2(self):
        """
        Todos los géneros son igual de comunes
        """
        personas = [
            Personas(id=429186, nombre='Paula', genero='Masculino', edad=88),
            Personas(id=149872, nombre='Tomás', genero='Masculino', edad=61),
            Personas(id=917346, nombre='Andrés', genero='Femenino', edad=69),
            Personas(id=983156, nombre='Valeria', genero='Femenino', edad=39),
            Personas(id=926342, nombre='Magdalena', genero='Femenino', edad=67),
            Personas(id=654365, nombre='Isidora', genero='No binario', edad=54),
            Personas(id=673894, nombre='Felipe', genero='No binario', edad=19),
            Personas(id=278561, nombre='Hernán', genero='Masculino', edad=38),
            Personas(id=184926, nombre='Andrea', genero='No binario', edad=47),
        ]
        reservas = [
            Reservas(id_persona=149872, id_funcion=2534, numero_butaca='E9'),
            Reservas(id_persona=278561, id_funcion=2534, numero_butaca='F8'),
            Reservas(id_persona=926342, id_funcion=2534, numero_butaca='H4'),
            Reservas(id_persona=184926, id_funcion=2534, numero_butaca='B10'),
            Reservas(id_persona=954362, id_funcion=2534, numero_butaca='B2'),
            Reservas(id_persona=917346, id_funcion=2534, numero_butaca='A8'),
            Reservas(id_persona=429186, id_funcion=2534, numero_butaca='F3'),
            Reservas(id_persona=673894, id_funcion=2534, numero_butaca='E1'),
            Reservas(id_persona=654365, id_funcion=2534, numero_butaca='A3'),
            Reservas(id_persona=983156, id_funcion=2534, numero_butaca='B5'),
        ]
        funciones = [
            Funciones(id=2534, numero_sala=3, id_pelicula=25227924, horario=6, fecha='03-12-23'),
        ]
        peliculas = [
            Peliculas(id=25227924, titulo='Kill Bill: Vol. 2', genero='Western', rating=8.7),
        ]

        id_funcion = 2534
        titulo = 'Kill Bill: Vol. 2'
        expected_strings = [self.str3.format(id_funcion, titulo)]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = genero_comun(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertIn(result, expected_strings)

    def test_3(self):
        """
        Varias peliculas y funciones, algunas personas fueron a más de una función
        Un solo género es el más común 
        """
        personas = [
            Personas(id=529874, nombre='Pedro', genero='Masculino', edad=12),
            Personas(id=765653, nombre='Arturo', genero='Masculino', edad=43),
            Personas(id=186243, nombre='Pablo', genero='Femenino', edad=50),
            Personas(id=691734, nombre='Raúl', genero='No binario', edad=9),
            Personas(id=654365, nombre='Isidora', genero='Femenino', edad=54),
            Personas(id=654546, nombre='Alberto', genero='Masculino', edad=76),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=80),
            Personas(id=598127, nombre='Valentina', genero='Masculino', edad=55),
            Personas(id=697413, nombre='Andrés', genero='Masculino', edad=56),
            Personas(id=367591, nombre='Rodrigo', genero='No binario', edad=80),
        ]
        reservas = [
            Reservas(id_persona=691734, id_funcion=8008, numero_butaca='G7'),
            Reservas(id_persona=765653, id_funcion=9729, numero_butaca='F3'),
            Reservas(id_persona=765653, id_funcion=8008, numero_butaca='H7'),
            Reservas(id_persona=951827, id_funcion=4823, numero_butaca='E4'),
            Reservas(id_persona=654546, id_funcion=4823, numero_butaca='G10'),
            Reservas(id_persona=654365, id_funcion=9729, numero_butaca='F7'),
            Reservas(id_persona=765653, id_funcion=4823, numero_butaca='C4'),
            Reservas(id_persona=529874, id_funcion=9729, numero_butaca='A4'),
            Reservas(id_persona=654546, id_funcion=8008, numero_butaca='B8'),
        ]
        funciones = [
            Funciones(id=9729, numero_sala=2, id_pelicula=98811629, horario=1, fecha='02-12-23'),
            Funciones(id=8008, numero_sala=6, id_pelicula=11568343, horario=6, fecha='01-12-23'),
            Funciones(id=4823, numero_sala=2, id_pelicula=11568343, horario=3, fecha='04-12-23'),
        ]
        peliculas = [
            Peliculas(id=11568343, titulo='The Social Network', genero='Drama', rating=7.7),
            Peliculas(id=98811629, titulo='Braveheart', genero='Animación', rating=8.5),
        ]

        id_funcion = 8008
        titulo = 'The Social Network'
        expected_strings = [self.str1.format(id_funcion, titulo, 'Masculino')]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = genero_comun(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertIn(result, expected_strings)

    def test_4(self):
        """
        Varias peliculas y funciones, algunas personas fueron a más de una función
        Dos géneros son los más comunes 
        """
        personas = [
            Personas(id=244869, nombre='Matias', genero='Masculino', edad=23),
            Personas(id=765653, nombre='Arturo', genero='Masculino', edad=43),
            Personas(id=573849, nombre='María', genero='Femenino', edad=12),
            Personas(id=691734, nombre='Raúl', genero='No binario', edad=9),
            Personas(id=836197, nombre='Julia', genero='No binario', edad=23),
            Personas(id=781245, nombre='Alex', genero='No binario', edad=15),
            Personas(id=367591, nombre='Rodrigo', genero='No binario', edad=80),
            Personas(id=573912, nombre='Carla', genero='Masculino', edad=12),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=80),
            Personas(id=739182, nombre='Beatriz', genero='Femenino', edad=77),
            Personas(id=419725, nombre='Antonio', genero='Femenino', edad=10),
            Personas(id=596318, nombre='Martín', genero='Masculino', edad=81),
            Personas(id=645321, nombre='Diego', genero='Masculino', edad=39),
        ]
        reservas = [
            Reservas(id_persona=951827, id_funcion=6566, numero_butaca='H3'),
            Reservas(id_persona=691734, id_funcion=4211, numero_butaca='A3'),
            Reservas(id_persona=419725, id_funcion=4211, numero_butaca='F5'),
            Reservas(id_persona=573849, id_funcion=4211, numero_butaca='E3'),
            Reservas(id_persona=739182, id_funcion=4211, numero_butaca='D7'),
            Reservas(id_persona=596318, id_funcion=4211, numero_butaca='D4'),
            Reservas(id_persona=573849, id_funcion=6566, numero_butaca='G5'),
            Reservas(id_persona=244869, id_funcion=4211, numero_butaca='B4'),
            Reservas(id_persona=367591, id_funcion=4211, numero_butaca='C4'),
            Reservas(id_persona=951827, id_funcion=4211, numero_butaca='E8'),
            Reservas(id_persona=781245, id_funcion=4211, numero_butaca='A5'),
            Reservas(id_persona=367591, id_funcion=6566, numero_butaca='D1'),
            Reservas(id_persona=645321, id_funcion=4211, numero_butaca='B8'),
            Reservas(id_persona=419725, id_funcion=6566, numero_butaca='A2'),
            Reservas(id_persona=836197, id_funcion=4211, numero_butaca='C10'),
            Reservas(id_persona=739182, id_funcion=6566, numero_butaca='H1'),
            Reservas(id_persona=836197, id_funcion=6566, numero_butaca='H10'),
        ]
        funciones = [
            Funciones(id=4211, numero_sala=1, id_pelicula=83829256, horario=3, fecha='03-12-23'),
            Funciones(id=6566, numero_sala=1, id_pelicula=83829256, horario=4, fecha='04-12-23'),
        ]
        peliculas = [
            Peliculas(id=49895401, titulo='Pixel Perfect', genero='Ciencia Ficción', rating=6.0),
            Peliculas(id=75421892, titulo='The Little Mermaid', genero='Aventura', rating=8.0),
            Peliculas(id=83829256, titulo='Stuck in the Suburbs', genero='Comedia', rating=6.2),
        ]

        id_funcion = 4211
        titulo = 'Stuck in the Suburbs'
        expected_strings = [
            self.str2.format(id_funcion, titulo, 'Femenino', 'No binario'),
            self.str2.format(id_funcion, titulo, 'No binario', 'Femenino'),
        ]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = genero_comun(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertIn(result, expected_strings)

    def test_5(self):
        """
        Todas las personas son del mismo género
        """
        personas = [
            Personas(id=543254, nombre='Teresa', genero='Femenino', edad=65),
            Personas(id=419725, nombre='Antonio', genero='Femenino', edad=10),
            Personas(id=376581, nombre='José', genero='Femenino', edad=13),
            Personas(id=824156, nombre='Gabriel', genero='Femenino', edad=33),
            Personas(id=463289, nombre='Teresita', genero='Femenino', edad=24),
        ]
        reservas = [
            Reservas(id_persona=543254, id_funcion=5220, numero_butaca='B4'),
            Reservas(id_persona=824156, id_funcion=5220, numero_butaca='G3'),
            Reservas(id_persona=463289, id_funcion=5220, numero_butaca='A6'),
        ]
        funciones = [
            Funciones(id=5220, numero_sala=5, id_pelicula=67202232, horario=4, fecha='03-12-23'),
        ]
        peliculas = [
            Peliculas(id=67202232, titulo='Memento', genero='Superhéroes', rating=8.5),
            Peliculas(id=32608840, titulo='Johnny Tsunami', genero='Deportes', rating=6.3),
        ]

        id_funcion = 5220
        titulo = 'Memento'
        expected_strings = [self.str1.format(id_funcion, titulo, 'Femenino')]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = genero_comun(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertIn(result, expected_strings)

if __name__ == '__main__':
    unittest.main(verbosity=2)