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
        personas = [
            Personas(id=120038, nombre='Valentina', genero='Masculino', edad=40),
            Personas(id=864837, nombre='Andrea', genero='No binario', edad=68),
            Personas(id=202443, nombre='Tomás', genero='Masculino', edad=15),
            Personas(id=591515, nombre='Gabriel', genero='No binario', edad=45),
            Personas(id=547446, nombre='Andrés', genero='No binario', edad=60),
            Personas(id=743208, nombre='Pietro', genero='Masculino', edad=71),
            Personas(id=178291, nombre='Jorge', genero='No binario', edad=47),
            Personas(id=752204, nombre='Paula', genero='Femenino', edad=69),
            Personas(id=185689, nombre='Esteban', genero='No binario', edad=86),
            Personas(id=104423, nombre='Tomás', genero='No binario', edad=40),
        ]
        reservas = [
            Reservas(id_persona=120038, id_funcion=9086, numero_butaca='F6'),
            Reservas(id_persona=202443, id_funcion=9086, numero_butaca='G6'),
            Reservas(id_persona=752204, id_funcion=9086, numero_butaca='H3'),
            Reservas(id_persona=864837, id_funcion=9086, numero_butaca='B4'),
            Reservas(id_persona=743208, id_funcion=9086, numero_butaca='E2'),
            Reservas(id_persona=591515, id_funcion=9086, numero_butaca='F5'),
        ]
        funciones = [
            Funciones(id=9086, numero_sala=2, id_pelicula=29729434, horario=8, fecha='02-12-23'),
        ]
        peliculas = [
            Peliculas(id=29729434, titulo='The Princess Diaries 2', genero='Acción', rating=8.0),
        ]

        pelicula = 'The Princess Diaries 2'
        genero = 'Masculino'
        edad = 40
        expected_nombres = [
            'Valentina',
            'Pietro',
        ]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_persona_genero_mayores(gen_personas, gen_peliculas, gen_reservas,
                                                gen_funciones, pelicula, genero, edad)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_nombres)

    def test_1(self):
        """
        Varias peliculas y varias funciones
        Algunas personas vieron la pelicula más de una vez
        """
        personas = [
            Personas(id=344229, nombre='Isidora', genero='Masculino', edad=79),
            Personas(id=289151, nombre='Leonardo', genero='Masculino', edad=26),
            Personas(id=912105, nombre='Felipe', genero='Masculino', edad=52),
            Personas(id=254224, nombre='Diego', genero='No binario', edad=47),
            Personas(id=780224, nombre='Alejandro', genero='Masculino', edad=88),
            Personas(id=471183, nombre='Pietro', genero='No binario', edad=41),
            Personas(id=480227, nombre='Hernán', genero='Masculino', edad=56),
            Personas(id=970731, nombre='Martín', genero='No binario', edad=25),
            Personas(id=589077, nombre='Andrés', genero='Masculino', edad=93),
            Personas(id=551792, nombre='Hernán', genero='Masculino', edad=36),
        ]
        reservas = [
            Reservas(id_persona=912105, id_funcion=8109, numero_butaca='G5'),
            Reservas(id_persona=480227, id_funcion=8109, numero_butaca='F7'),
            Reservas(id_persona=551792, id_funcion=6386, numero_butaca='F2'),
            Reservas(id_persona=780224, id_funcion=8083, numero_butaca='G9'),
            Reservas(id_persona=589077, id_funcion=8083, numero_butaca='A4'),
            Reservas(id_persona=970731, id_funcion=6386, numero_butaca='H7'),
            Reservas(id_persona=289151, id_funcion=8083, numero_butaca='G2'),
            Reservas(id_persona=289151, id_funcion=8109, numero_butaca='A5'),
            Reservas(id_persona=344229, id_funcion=8109, numero_butaca='H5'),
            Reservas(id_persona=970731, id_funcion=8083, numero_butaca='E1'),
            Reservas(id_persona=780224, id_funcion=8109, numero_butaca='E8'),
            Reservas(id_persona=970731, id_funcion=8109, numero_butaca='F1'),
            Reservas(id_persona=480227, id_funcion=8083, numero_butaca='D2'),
            Reservas(id_persona=254224, id_funcion=6386, numero_butaca='D3'),
            Reservas(id_persona=471183, id_funcion=8083, numero_butaca='A6'),
            Reservas(id_persona=289151, id_funcion=6386, numero_butaca='D4'),
            Reservas(id_persona=780224, id_funcion=6386, numero_butaca='E3'),
            Reservas(id_persona=480227, id_funcion=6386, numero_butaca='B7'),
        ]
        funciones = [
            Funciones(id=8109, numero_sala=5, id_pelicula=24285098, horario=7, fecha='05-12-23'),
            Funciones(id=8083, numero_sala=7, id_pelicula=49040980, horario=4, fecha='04-12-23'),
            Funciones(id=6386, numero_sala=8, id_pelicula=24285098, horario=5, fecha='01-12-23'),
        ]
        peliculas = [
            Peliculas(id=24285098, titulo='Frozen', genero='Deportes', rating=7.8),
            Peliculas(id=49040980, titulo='The Hunchback of Notre Dame', genero='Crimen', rating=7.8),
        ]

        pelicula = 'Frozen'
        genero = 'No binario'
        edad = 22
        expected_nombres = [
            'Diego',
            'Martín',
        ]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_persona_genero_mayores(gen_personas, gen_peliculas, gen_reservas,
                                                gen_funciones, pelicula, genero, edad)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_nombres)

    def test_2(self):
        """
        Solo una persona del genero
        """
        personas = [
            Personas(id=104423, nombre='Tomás', genero='No binario', edad=40),
            Personas(id=399711, nombre='Renata', genero='Masculino', edad=14),
            Personas(id=777689, nombre='Alejandro', genero='Masculino', edad=82),
            Personas(id=355736, nombre='Teresa', genero='No binario', edad=14),
            Personas(id=910788, nombre='Carmen', genero='Femenino', edad=49),
        ]
        reservas = [
            Reservas(id_persona=910788, id_funcion=4639, numero_butaca='C3'),
            Reservas(id_persona=355736, id_funcion=5374, numero_butaca='F8'),
            Reservas(id_persona=777689, id_funcion=5374, numero_butaca='G3'),
            Reservas(id_persona=104423, id_funcion=5374, numero_butaca='C7'),
            Reservas(id_persona=777689, id_funcion=4639, numero_butaca='E3'),
            Reservas(id_persona=399711, id_funcion=5374, numero_butaca='A5'),
            Reservas(id_persona=104423, id_funcion=4639, numero_butaca='B8'),
        ]
        funciones = [
            Funciones(id=4639, numero_sala=9, id_pelicula=53671260, horario=8, fecha='05-12-23'),
            Funciones(id=5374, numero_sala=6, id_pelicula=70789763, horario=4, fecha='03-12-23'),
        ]
        peliculas = [
            Peliculas(id=53671260, titulo='Memento', genero='Animación', rating=8.2),
            Peliculas(id=70789763, titulo='Inception', genero='Superhéroes', rating=8.6),
        ]

        pelicula = 'Memento'
        genero = 'Femenino'
        edad = 42
        expected_nombres = [
            'Carmen',
        ]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_persona_genero_mayores(gen_personas, gen_peliculas, gen_reservas,
                                                gen_funciones, pelicula, genero, edad)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_nombres)

    def test_3(self):
        """
        Muchas funciones de la misma pelicula
        """
        personas = [
            Personas(id=289151, nombre='Leonardo', genero='Masculino', edad=21),
            Personas(id=471183, nombre='Pietro', genero='No binario', edad=36),
            Personas(id=104423, nombre='Tomás', genero='No binario', edad=35),
            Personas(id=678509, nombre='Rodrigo', genero='Masculino', edad=22),
            Personas(id=447300, nombre='Diego', genero='Femenino', edad=11),
            Personas(id=591515, nombre='Gabriel', genero='No binario', edad=40),
            Personas(id=138359, nombre='Valentina', genero='Masculino', edad=66),
            Personas(id=193453, nombre='José', genero='Femenino', edad=77),
            Personas(id=344229, nombre='Isidora', genero='Masculino', edad=74),
            Personas(id=289380, nombre='María', genero='Masculino', edad=55),
            Personas(id=971631, nombre='Pedro', genero='Masculino', edad=14),
        ]
        reservas = [
            Reservas(id_persona=193453, id_funcion=3099, numero_butaca='C7'),
            Reservas(id_persona=344229, id_funcion=9454, numero_butaca='B9'),
            Reservas(id_persona=971631, id_funcion=3099, numero_butaca='H1'),
            Reservas(id_persona=289380, id_funcion=3099, numero_butaca='B2'),
            Reservas(id_persona=138359, id_funcion=1155, numero_butaca='G5'),
            Reservas(id_persona=138359, id_funcion=3099, numero_butaca='A6'),
            Reservas(id_persona=678509, id_funcion=9454, numero_butaca='A8'),
            Reservas(id_persona=289380, id_funcion=1155, numero_butaca='H10'),
            Reservas(id_persona=678509, id_funcion=3099, numero_butaca='B10'),
            Reservas(id_persona=289151, id_funcion=9454, numero_butaca='F5'),
            Reservas(id_persona=678509, id_funcion=1155, numero_butaca='E1'),
            Reservas(id_persona=591515, id_funcion=9454, numero_butaca='E10'),
            Reservas(id_persona=971631, id_funcion=1155, numero_butaca='B5'),
            Reservas(id_persona=138359, id_funcion=9454, numero_butaca='D9'),
            Reservas(id_persona=591515, id_funcion=1155, numero_butaca='A9'),
            Reservas(id_persona=344229, id_funcion=1155, numero_butaca='E5'),
            Reservas(id_persona=193453, id_funcion=1155, numero_butaca='D3'),
            Reservas(id_persona=344229, id_funcion=3099, numero_butaca='H2'),
            Reservas(id_persona=289151, id_funcion=3099, numero_butaca='C6'),
            Reservas(id_persona=289151, id_funcion=1155, numero_butaca='G7'),
            Reservas(id_persona=971631, id_funcion=9454, numero_butaca='D6'),
            Reservas(id_persona=447300, id_funcion=1155, numero_butaca='H8'),
            Reservas(id_persona=193453, id_funcion=9454, numero_butaca='F8'),
            Reservas(id_persona=591515, id_funcion=3099, numero_butaca='A4'),
            Reservas(id_persona=471183, id_funcion=3099, numero_butaca='F2'),
        ]
        funciones = [
            Funciones(id=9454, numero_sala=9, id_pelicula=69309996, horario=5, fecha='02-12-23'),
            Funciones(id=1155, numero_sala=1, id_pelicula=69309996, horario=7, fecha='05-12-23'),
            Funciones(id=3099, numero_sala=4, id_pelicula=69309996, horario=4, fecha='01-12-23'),
        ]
        peliculas = [
            Peliculas(id=69309996, titulo='Guardians of the Galaxy', genero='Musical', rating=10.0),
        ]

        pelicula = 'Guardians of the Galaxy'
        genero = 'Masculino'
        edad = 17
        expected_nombres = [
            'Leonardo',
            'Rodrigo',
            'Valentina',
            'Isidora',
            'María',
        ]

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_persona_genero_mayores(gen_personas, gen_peliculas, gen_reservas,
                                                gen_funciones, pelicula, genero, edad)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_nombres)


if __name__ == '__main__':
    unittest.main(verbosity=2)
