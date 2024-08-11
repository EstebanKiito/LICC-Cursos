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
            Personas(id=607107, nombre='Hernán', genero='Femenino', edad=15),
            Personas(id=344229, nombre='Isidora', genero='Masculino', edad=77),
            Personas(id=480227, nombre='Hernán', genero='Masculino', edad=54),
            Personas(id=777689, nombre='Alejandro', genero='Masculino', edad=80),
            Personas(id=571081, nombre='Teresa', genero='No binario', edad=17),
            Personas(id=809018, nombre='Camila', genero='Masculino', edad=39),
            Personas(id=255048, nombre='Manuel', genero='No binario', edad=88),
            Personas(id=788596, nombre='Andrés', genero='No binario', edad=97),
            Personas(id=561104, nombre='Paula', genero='Masculino', edad=23),
            Personas(id=662059, nombre='Victoria', genero='Femenino', edad=23),
        ]
        reservas = [
            Reservas(id_persona=607107, id_funcion=8522, numero_butaca='F6'),
            Reservas(id_persona=344229, id_funcion=8522, numero_butaca='B7'),
            Reservas(id_persona=809018, id_funcion=8522, numero_butaca='F5'),
            Reservas(id_persona=571081, id_funcion=8522, numero_butaca='G2'),
            Reservas(id_persona=777689, id_funcion=8522, numero_butaca='D7'),
            Reservas(id_persona=561104, id_funcion=8522, numero_butaca='F4'),
            Reservas(id_persona=662059, id_funcion=8522, numero_butaca='F8'),
            Reservas(id_persona=788596, id_funcion=8522, numero_butaca='F7'),
            Reservas(id_persona=480227, id_funcion=8522, numero_butaca='F9'),
            Reservas(id_persona=255048, id_funcion=8522, numero_butaca='H4'),
        ]
        funciones = [
            Funciones(id=8522, numero_sala=8, id_pelicula=20710313, horario=9, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=20710313, titulo='Your Name', genero='Musical', rating=6.9),
        ]
        id_funcion = 8522
        titulo = 'Your Name'
        expected_strings = [self.str1.format(id_funcion, titulo, 'Masculino')]

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
            Personas(id=591515, nombre='Gabriel', genero='Masculino', edad=43),
            Personas(id=777689, nombre='Alejandro', genero='No binario', edad=80),
            Personas(id=852596, nombre='Teresa', genero='Femenino', edad=24),
            Personas(id=910788, nombre='Carmen', genero='Masculino', edad=47),
            Personas(id=864837, nombre='Andrea', genero='Femenino', edad=66),
            Personas(id=480227, nombre='Hernán', genero='No binario', edad=54),
            Personas(id=104423, nombre='Tomás', genero='Femenino', edad=38),
            Personas(id=970731, nombre='Martín', genero='No binario', edad=23),
            Personas(id=289151, nombre='Leonardo', genero='No binario', edad=24),
            Personas(id=178291, nombre='Jorge', genero='Femenino', edad=45),
        ]
        reservas = [
            Reservas(id_persona=178291, id_funcion=8109, numero_butaca='H2'),
            Reservas(id_persona=480227, id_funcion=8109, numero_butaca='A8'),
            Reservas(id_persona=910788, id_funcion=8109, numero_butaca='B6'),
            Reservas(id_persona=591515, id_funcion=8109, numero_butaca='E5'),
            Reservas(id_persona=864837, id_funcion=8109, numero_butaca='B1'),
            Reservas(id_persona=852596, id_funcion=8109, numero_butaca='A5'),
            Reservas(id_persona=970731, id_funcion=8109, numero_butaca='E2'),
            Reservas(id_persona=289151, id_funcion=8109, numero_butaca='E9'),
            Reservas(id_persona=777689, id_funcion=8109, numero_butaca='F1'),
            Reservas(id_persona=104423, id_funcion=8109, numero_butaca='D10'),
        ]
        funciones = [
            Funciones(id=8109, numero_sala=5, id_pelicula=26094678, horario=7, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=26094678, titulo='Tarzan', genero='Animación', rating=7.0),
        ]

        id_funcion = 8109
        titulo = 'Tarzan'
        expected_strings = [
            self.str2.format(id_funcion, titulo, 'No binario', 'Femenino'),
            self.str2.format(id_funcion, titulo, 'Femenino', 'No binario'),
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
            Personas(id=255048, nombre='Manuel', genero='No binario', edad=88),
            Personas(id=875734, nombre='Isidora', genero='No binario', edad=61),
            Personas(id=743208, nombre='Pietro', genero='Masculino', edad=69),
            Personas(id=809018, nombre='Camila', genero='Masculino', edad=39),
            Personas(id=752204, nombre='Paula', genero='Masculino', edad=67),
            Personas(id=480227, nombre='Hernán', genero='Femenino', edad=54),
            Personas(id=499756, nombre='Carla', genero='Femenino', edad=19),
            Personas(id=104423, nombre='Tomás', genero='No binario', edad=38),
            Personas(id=910788, nombre='Carmen', genero='Femenino', edad=47),
        ]
        reservas = [
            Reservas(id_persona=875734, id_funcion=8396, numero_butaca='E9'),
            Reservas(id_persona=104423, id_funcion=8396, numero_butaca='F8'),
            Reservas(id_persona=752204, id_funcion=8396, numero_butaca='H4'),
            Reservas(id_persona=910788, id_funcion=8396, numero_butaca='B10'),
            Reservas(id_persona=780224, id_funcion=8396, numero_butaca='B2'),
            Reservas(id_persona=743208, id_funcion=8396, numero_butaca='A8'),
            Reservas(id_persona=255048, id_funcion=8396, numero_butaca='F3'),
            Reservas(id_persona=499756, id_funcion=8396, numero_butaca='E1'),
            Reservas(id_persona=480227, id_funcion=8396, numero_butaca='A3'),
            Reservas(id_persona=809018, id_funcion=8396, numero_butaca='B5'),
        ]
        funciones = [
            Funciones(id=8396, numero_sala=6, id_pelicula=21315378, horario=9, fecha='03-12-23'),
        ]
        peliculas = [
            Peliculas(id=21315378, titulo='American History X', genero='Western', rating=8.7),
        ]

        id_funcion = 8396
        titulo = 'American History X'
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
            Personas(id=355736, nombre='Teresa', genero='No binario', edad=12),
            Personas(id=591515, nombre='Gabriel', genero='No binario', edad=43),
            Personas(id=912105, nombre='Felipe', genero='Masculino', edad=50),
            Personas(id=517596, nombre='Juampi', genero='Femenino', edad=9),
            Personas(id=480227, nombre='Hernán', genero='Masculino', edad=54),
            Personas(id=480408, nombre='Arturo', genero='No binario', edad=76),
            Personas(id=777689, nombre='Alejandro', genero='Masculino', edad=80),
            Personas(id=423989, nombre='Nicolás', genero='No binario', edad=55),
            Personas(id=523275, nombre='Felipe', genero='No binario', edad=56),
            Personas(id=193453, nombre='José', genero='Femenino', edad=80),
        ]
        reservas = [
            Reservas(id_persona=517596, id_funcion=4870, numero_butaca='G7'),
            Reservas(id_persona=591515, id_funcion=6591, numero_butaca='F3'),
            Reservas(id_persona=591515, id_funcion=4870, numero_butaca='H7'),
            Reservas(id_persona=777689, id_funcion=1685, numero_butaca='E4'),
            Reservas(id_persona=480408, id_funcion=1685, numero_butaca='G10'),
            Reservas(id_persona=480227, id_funcion=6591, numero_butaca='F7'),
            Reservas(id_persona=591515, id_funcion=1685, numero_butaca='C4'),
            Reservas(id_persona=355736, id_funcion=6591, numero_butaca='A4'),
            Reservas(id_persona=480408, id_funcion=4870, numero_butaca='B8'),
        ]
        funciones = [
            Funciones(id=6591, numero_sala=5, id_pelicula=16737491, horario=4, fecha='02-12-23'),
            Funciones(id=4870, numero_sala=9, id_pelicula=19494205, horario=9, fecha='01-12-23'),
            Funciones(id=1685, numero_sala=5, id_pelicula=19494205, horario=6, fecha='04-12-23'),
        ]
        peliculas = [
            Peliculas(id=19494205, titulo='The Lord of the Rings: The Two Towers', genero='Drama', rating=7.7),
            Peliculas(id=16737491, titulo='Your Name', genero='Animación', rating=8.5),
        ]

        id_funcion = 4870
        titulo = 'The Lord of the Rings: The Two Towers'
        expected_strings = [self.str1.format(id_funcion, titulo, 'No binario')]

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
            Personas(id=970731, nombre='Martín', genero='No binario', edad=23),
            Personas(id=591515, nombre='Gabriel', genero='No binario', edad=43),
            Personas(id=399711, nombre='Renata', genero='Masculino', edad=12),
            Personas(id=517596, nombre='Juampi', genero='Femenino', edad=9),
            Personas(id=662059, nombre='Victoria', genero='Femenino', edad=23),
            Personas(id=607107, nombre='Hernán', genero='Femenino', edad=15),
            Personas(id=193453, nombre='José', genero='Femenino', edad=80),
            Personas(id=399774, nombre='Paula', genero='No binario', edad=12),
            Personas(id=777689, nombre='Alejandro', genero='Masculino', edad=80),
            Personas(id=565044, nombre='Martina', genero='Masculino', edad=77),
            Personas(id=245587, nombre='Teresita', genero='Masculino', edad=10),
            Personas(id=422180, nombre='Luis', genero='No binario', edad=81),
            Personas(id=471183, nombre='Pietro', genero='No binario', edad=39),
        ]
        reservas = [
            Reservas(id_persona=777689, id_funcion=3428, numero_butaca='H3'),
            Reservas(id_persona=517596, id_funcion=1073, numero_butaca='A3'),
            Reservas(id_persona=245587, id_funcion=1073, numero_butaca='F5'),
            Reservas(id_persona=399711, id_funcion=1073, numero_butaca='E3'),
            Reservas(id_persona=565044, id_funcion=1073, numero_butaca='D7'),
            Reservas(id_persona=422180, id_funcion=1073, numero_butaca='D4'),
            Reservas(id_persona=399711, id_funcion=3428, numero_butaca='G5'),
            Reservas(id_persona=970731, id_funcion=1073, numero_butaca='B4'),
            Reservas(id_persona=193453, id_funcion=1073, numero_butaca='C4'),
            Reservas(id_persona=777689, id_funcion=1073, numero_butaca='E8'),
            Reservas(id_persona=607107, id_funcion=1073, numero_butaca='A5'),
            Reservas(id_persona=193453, id_funcion=3428, numero_butaca='D1'),
            Reservas(id_persona=471183, id_funcion=1073, numero_butaca='B8'),
            Reservas(id_persona=245587, id_funcion=3428, numero_butaca='A2'),
            Reservas(id_persona=662059, id_funcion=1073, numero_butaca='C10'),
            Reservas(id_persona=565044, id_funcion=3428, numero_butaca='H1'),
            Reservas(id_persona=662059, id_funcion=3428, numero_butaca='H10'),
        ]
        funciones = [
            Funciones(id=1073, numero_sala=4, id_pelicula=91755118, horario=6, fecha='03-12-23'),
            Funciones(id=3428, numero_sala=4, id_pelicula=91755118, horario=7, fecha='04-12-23'),
        ]
        peliculas = [
            Peliculas(id=57821263, titulo='The Luck of the Irish', genero='Ciencia Ficción', rating=6.0),
            Peliculas(id=83347754, titulo='The Lord of the Rings: The Return of the King', genero='Aventura', rating=8.0),
            Peliculas(id=91755118, titulo='Braveheart', genero='Comedia', rating=6.2),
        ]

        id_funcion = 1073
        titulo = 'Braveheart'
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

    def test_5(self):
        """
        Todas las personas son del mismo género
        """
        personas = [
            Personas(id=369116, nombre='Jimena', genero='Masculino', edad=65),
            Personas(id=245587, nombre='Teresita', genero='Masculino', edad=10),
            Personas(id=202443, nombre='Tomás', genero='Masculino', edad=13),
            Personas(id=650018, nombre='Daniel', genero='Masculino', edad=33),
            Personas(id=289151, nombre='Leonardo', genero='Masculino', edad=24),
        ]
        reservas = [
            Reservas(id_persona=369116, id_funcion=2082, numero_butaca='B4'),
            Reservas(id_persona=650018, id_funcion=2082, numero_butaca='G3'),
            Reservas(id_persona=289151, id_funcion=2082, numero_butaca='A6'),
        ]
        funciones = [
            Funciones(id=2082, numero_sala=8, id_pelicula=75128094, horario=7, fecha='03-12-23'),
        ]
        peliculas = [
            Peliculas(id=75128094, titulo='The Silence of the Lambs', genero='Superhéroes', rating=8.5),
            Peliculas(id=40534702, titulo='The Godfather', genero='Deportes', rating=6.3),
        ]

        id_funcion = 2082
        titulo = 'The Silence of the Lambs'
        expected_strings = [self.str1.format(id_funcion, titulo, 'Masculino')]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = genero_comun(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertIn(result, expected_strings)


if __name__ == '__main__':
    unittest.main(verbosity=2)
