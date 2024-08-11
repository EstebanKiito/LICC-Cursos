import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import nombres_persona_genero_mayores
from utilidades import Personas, Peliculas, Funciones, Reservas
from typing import Generator

class TestNombresPersonaGeneroMayores(unittest.TestCase):

    def test_0(self):
        """
        Solo una función de la pelicula a buscar
        Una persona con la edad exacta a buscar
        """
        personas = personas = [
            Personas(id=294176, nombre='Diego', genero='Femenino', edad=38),
            Personas(id=138975, nombre='Daniel', genero='Masculino', edad=66),
            Personas(id=376581, nombre='José', genero='Femenino', edad=13),
            Personas(id=765653, nombre='Arturo', genero='Masculino', edad=43),
            Personas(id=721584, nombre='Leonardo', genero='Masculino', edad=58),
            Personas(id=917346, nombre='Andrés', genero='Femenino', edad=69),
            Personas(id=352429, nombre='Jorge', genero='Masculino', edad=45),
            Personas(id=926342, nombre='Magdalena', genero='No binario', edad=67),
            Personas(id=359827, nombre='Luis', genero='Masculino', edad=84),
            Personas(id=278561, nombre='Hernán', genero='Masculino', edad=38),
        ]
        reservas = [
            Reservas(id_persona=294176, id_funcion=3224, numero_butaca='F6'),
            Reservas(id_persona=376581, id_funcion=3224, numero_butaca='G6'),
            Reservas(id_persona=926342, id_funcion=3224, numero_butaca='H3'),
            Reservas(id_persona=138975, id_funcion=3224, numero_butaca='B4'),
            Reservas(id_persona=917346, id_funcion=3224, numero_butaca='E2'),
            Reservas(id_persona=765653, id_funcion=3224, numero_butaca='F5'),
        ]
        funciones = [
            Funciones(id=3224, numero_sala=8, id_pelicula=21803572, horario=5, fecha='02-12-23'),
        ]
        peliculas = [
            Peliculas(id=21803572, titulo='Avengers', genero='Acción', rating=8.0),
        ]

        pelicula = 'Avengers'
        genero = 'Femenino'
        edad = 38
        expected_nombres = [
            'Diego',
            'Andrés',
        ]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_persona_genero_mayores(gen_personas, gen_peliculas, gen_reservas,
                                                gen_funciones, pelicula, genero, edad)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_nombres)

    def test_1(self):
        """
        Varias peliculas y varias funciones
        Algunas personas vieron la pelicula más de una vez
        """
        personas = [
            Personas(id=518367, nombre='Mateo', genero='Femenino', edad=77),
            Personas(id=463289, nombre='Teresita', genero='Femenino', edad=24),
            Personas(id=186243, nombre='Pablo', genero='Femenino', edad=50),
            Personas(id=428362, nombre='Emma', genero='Masculino', edad=45),
            Personas(id=954362, nombre='Isabel', genero='Femenino', edad=86),
            Personas(id=645321, nombre='Diego', genero='Masculino', edad=39),
            Personas(id=654365, nombre='Isidora', genero='Femenino', edad=54),
            Personas(id=244869, nombre='Matias', genero='Masculino', edad=23),
            Personas(id=763215, nombre='Carmen', genero='Femenino', edad=91),
            Personas(id=725930, nombre='Adela', genero='Femenino', edad=34),
        ]
        reservas = [
            Reservas(id_persona=186243, id_funcion=2247, numero_butaca='G5'),
            Reservas(id_persona=654365, id_funcion=2247, numero_butaca='F7'),
            Reservas(id_persona=725930, id_funcion=9524, numero_butaca='F2'),
            Reservas(id_persona=954362, id_funcion=2221, numero_butaca='G9'),
            Reservas(id_persona=763215, id_funcion=2221, numero_butaca='A4'),
            Reservas(id_persona=244869, id_funcion=9524, numero_butaca='H7'),
            Reservas(id_persona=463289, id_funcion=2221, numero_butaca='G2'),
            Reservas(id_persona=463289, id_funcion=2247, numero_butaca='A5'),
            Reservas(id_persona=518367, id_funcion=2247, numero_butaca='H5'),
            Reservas(id_persona=244869, id_funcion=2221, numero_butaca='E1'),
            Reservas(id_persona=954362, id_funcion=2247, numero_butaca='E8'),
            Reservas(id_persona=244869, id_funcion=2247, numero_butaca='F1'),
            Reservas(id_persona=654365, id_funcion=2221, numero_butaca='D2'),
            Reservas(id_persona=428362, id_funcion=9524, numero_butaca='D3'),
            Reservas(id_persona=645321, id_funcion=2221, numero_butaca='A6'),
            Reservas(id_persona=463289, id_funcion=9524, numero_butaca='D4'),
            Reservas(id_persona=954362, id_funcion=9524, numero_butaca='E3'),
            Reservas(id_persona=654365, id_funcion=9524, numero_butaca='B7'),
        ]
        funciones = [
            Funciones(id=2247, numero_sala=2, id_pelicula=16359236, horario=4, fecha='05-12-23'),
            Funciones(id=2221, numero_sala=4, id_pelicula=41115118, horario=1, fecha='04-12-23'),
            Funciones(id=9524, numero_sala=5, id_pelicula=16359236, horario=2, fecha='01-12-23'),
        ]
        peliculas = [
            Peliculas(id=16359236, titulo='Mulan', genero='Deportes', rating=7.8),
            Peliculas(id=41115118, titulo='Avatar', genero='Crimen', rating=7.8),
        ]

        pelicula = 'Mulan'
        genero = 'Masculino'
        edad = 20
        expected_nombres = [
            'Emma',
            'Matias',
        ]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_persona_genero_mayores(gen_personas, gen_peliculas, gen_reservas,
                                                gen_funciones, pelicula, genero, edad)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_nombres)

    def test_2(self):
        """
        Solo una persona del genero
        """
        personas = [
            Personas(id=278561, nombre='Hernán', genero='Masculino', edad=38),
            Personas(id=573849, nombre='María', genero='Femenino', edad=12),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=80),
            Personas(id=529874, nombre='Pedro', genero='Masculino', edad=12),
            Personas(id=184926, nombre='Andrea', genero='No binario', edad=47),
        ]
        reservas = [
            Reservas(id_persona=184926, id_funcion=7777, numero_butaca='C3'),
            Reservas(id_persona=529874, id_funcion=8512, numero_butaca='F8'),
            Reservas(id_persona=951827, id_funcion=8512, numero_butaca='G3'),
            Reservas(id_persona=278561, id_funcion=8512, numero_butaca='C7'),
            Reservas(id_persona=951827, id_funcion=7777, numero_butaca='E3'),
            Reservas(id_persona=573849, id_funcion=8512, numero_butaca='A5'),
            Reservas(id_persona=278561, id_funcion=7777, numero_butaca='B8'),
        ]
        funciones = [
            Funciones(id=7777, numero_sala=6, id_pelicula=45745398, horario=5, fecha='05-12-23'),
            Funciones(id=8512, numero_sala=3, id_pelicula=62863901, horario=1, fecha='03-12-23'),
        ]
        peliculas = [
            Peliculas(id=45745398, titulo='The Green Mile', genero='Animación', rating=8.2),
            Peliculas(id=62863901, titulo='The Prestige', genero='Superhéroes', rating=8.6),
        ]

        pelicula = 'The Green Mile'
        genero = 'No binario'
        edad = 40
        expected_nombres = [
            'Andrea',
        ]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_persona_genero_mayores(gen_personas, gen_peliculas, gen_reservas,
                                                gen_funciones, pelicula, genero, edad)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_nombres)

    def test_3(self):
        """
        Ninguna persona cumple las condiciones
        """
        personas = [
            Personas(id=245769, nombre='Natalia', genero='Femenino', edad=17),
            Personas(id=836197, nombre='Julia', genero='No binario', edad=23),
            Personas(id=926242, nombre='Martina', genero='Femenino', edad=36),
            Personas(id=463289, nombre='Teresita', genero='Femenino', edad=24),
            Personas(id=367591, nombre='Rodrigo', genero='No binario', edad=80),
            Personas(id=824156, nombre='Gabriel', genero='Femenino', edad=33),
            Personas(id=359827, nombre='Luis', genero='Masculino', edad=84),
            Personas(id=317984, nombre='Lucía', genero='Femenino', edad=32),
            Personas(id=917346, nombre='Andrés', genero='Femenino', edad=69),
            Personas(id=542978, nombre='Isabella', genero='Masculino', edad=25),
            Personas(id=926342, nombre='Magdalena', genero='Femenino', edad=67),
        ]
        reservas = [
            Reservas(id_persona=367591, id_funcion=2247, numero_butaca='G1'),
            Reservas(id_persona=317984, id_funcion=4823, numero_butaca='F10'),
            Reservas(id_persona=367591, id_funcion=4823, numero_butaca='A6'),
            Reservas(id_persona=317984, id_funcion=8008, numero_butaca='D7'),
            Reservas(id_persona=245769, id_funcion=2247, numero_butaca='H2'),
            Reservas(id_persona=317984, id_funcion=2247, numero_butaca='G5'),
            Reservas(id_persona=917346, id_funcion=2247, numero_butaca='A5'),
            Reservas(id_persona=542978, id_funcion=8008, numero_butaca='B1'),
            Reservas(id_persona=359827, id_funcion=4823, numero_butaca='G7'),
            Reservas(id_persona=542978, id_funcion=2247, numero_butaca='B10'),
            Reservas(id_persona=824156, id_funcion=4823, numero_butaca='H6'),
            Reservas(id_persona=542978, id_funcion=9400, numero_butaca='C10'),
            Reservas(id_persona=926242, id_funcion=8008, numero_butaca='B3'),
            Reservas(id_persona=317984, id_funcion=9400, numero_butaca='H7'),
        ]
        funciones = [
            Funciones(id=9400, numero_sala=7, id_pelicula=42986062, horario=2, fecha='03-12-23'),
            Funciones(id=8008, numero_sala=6, id_pelicula=21803572, horario=6, fecha='01-12-23'),
            Funciones(id=4823, numero_sala=2, id_pelicula=42986062, horario=3, fecha='04-12-23'),
            Funciones(id=2247, numero_sala=2, id_pelicula=42986062, horario=4, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=71285784, titulo='Avengers: Age of Ultron', genero='Animación', rating=7.6),
            Peliculas(id=42986062, titulo='The Lord of the Rings', genero='Fantasía', rating=8.7),
            Peliculas(id=55774654, titulo='The Pianist', genero='Superhéroes', rating=8.5),
            Peliculas(id=21803572, titulo='Avengers', genero='Acción', rating=8.0),
        ]

        pelicula = 'The Lord of the Rings'
        genero = 'Femenino'
        edad = 70
        expected_nombres = []

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_persona_genero_mayores(gen_personas, gen_peliculas, gen_reservas,
                                                gen_funciones, pelicula, genero, edad)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_nombres)

    def test_4(self):
        """
        Muchas funciones de la misma pelicula
        """
        personas = [
            Personas(id=463289, nombre='Teresita', genero='Femenino', edad=24),
            Personas(id=645321, nombre='Diego', genero='Masculino', edad=39),
            Personas(id=278561, nombre='Hernán', genero='Masculino', edad=38),
            Personas(id=852647, nombre='Santiago', genero='Femenino', edad=25),
            Personas(id=621438, nombre='Sofía', genero='No binario', edad=14),
            Personas(id=765653, nombre='Arturo', genero='Masculino', edad=43),
            Personas(id=312497, nombre='Valentina', genero='Femenino', edad=69),
            Personas(id=367591, nombre='Rodrigo', genero='No binario', edad=80),
            Personas(id=518367, nombre='Mateo', genero='Femenino', edad=77),
            Personas(id=463518, nombre='Esteban', genero='Femenino', edad=58),
            Personas(id=245769, nombre='Natalia', genero='Femenino', edad=17),
        ]
        reservas = [
            Reservas(id_persona=367591, id_funcion=6237, numero_butaca='C7'),
            Reservas(id_persona=518367, id_funcion=3592, numero_butaca='B9'),
            Reservas(id_persona=245769, id_funcion=6237, numero_butaca='H1'),
            Reservas(id_persona=463518, id_funcion=6237, numero_butaca='B2'),
            Reservas(id_persona=312497, id_funcion=4293, numero_butaca='G5'),
            Reservas(id_persona=312497, id_funcion=6237, numero_butaca='A6'),
            Reservas(id_persona=852647, id_funcion=3592, numero_butaca='A8'),
            Reservas(id_persona=463518, id_funcion=4293, numero_butaca='H10'),
            Reservas(id_persona=852647, id_funcion=6237, numero_butaca='B10'),
            Reservas(id_persona=463289, id_funcion=3592, numero_butaca='F5'),
            Reservas(id_persona=852647, id_funcion=4293, numero_butaca='E1'),
            Reservas(id_persona=765653, id_funcion=3592, numero_butaca='E10'),
            Reservas(id_persona=245769, id_funcion=4293, numero_butaca='B5'),
            Reservas(id_persona=312497, id_funcion=3592, numero_butaca='D9'),
            Reservas(id_persona=765653, id_funcion=4293, numero_butaca='A9'),
            Reservas(id_persona=518367, id_funcion=4293, numero_butaca='E5'),
            Reservas(id_persona=367591, id_funcion=4293, numero_butaca='D3'),
            Reservas(id_persona=518367, id_funcion=6237, numero_butaca='H2'),
            Reservas(id_persona=463289, id_funcion=6237, numero_butaca='C6'),
            Reservas(id_persona=463289, id_funcion=4293, numero_butaca='G7'),
            Reservas(id_persona=245769, id_funcion=3592, numero_butaca='D6'),
            Reservas(id_persona=621438, id_funcion=4293, numero_butaca='H8'),
            Reservas(id_persona=367591, id_funcion=3592, numero_butaca='F8'),
            Reservas(id_persona=765653, id_funcion=6237, numero_butaca='A4'),
            Reservas(id_persona=645321, id_funcion=6237, numero_butaca='F2'),
        ]
        funciones = [
            Funciones(id=3592, numero_sala=6, id_pelicula=61384134, horario=2, fecha='02-12-23'),
            Funciones(id=4293, numero_sala=7, id_pelicula=61384134, horario=4, fecha='05-12-23'),
            Funciones(id=6237, numero_sala=1, id_pelicula=61384134, horario=1, fecha='01-12-23'),
        ]
        peliculas = [
            Peliculas(id=61384134, titulo='Mamma Mia', genero='Musical', rating=10.0),
        ]

        pelicula = 'Mamma Mia'
        genero = 'Femenino'
        edad = 20
        expected_nombres = [
            'Teresita',
            'Santiago',
            'Valentina',
            'Mateo',
            'Esteban',
        ]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_persona_genero_mayores(gen_personas, gen_peliculas, gen_reservas,
                                                gen_funciones, pelicula, genero, edad)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_nombres)

if __name__ == '__main__':
    unittest.main(verbosity=2)