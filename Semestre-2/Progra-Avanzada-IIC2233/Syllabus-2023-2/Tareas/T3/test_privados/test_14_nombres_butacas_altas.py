import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import nombres_butacas_altas
from utilidades import Personas, Peliculas, Funciones, Reservas
from typing import Generator


class TestNombresButacasAltas(unittest.TestCase):

    def test_0(self):
        """
        Una función de la pelicula
        Solo algunas personas hicieron reserva
        """
        personas = [
            Personas(id=565044, nombre='Adriana', genero='Masculino', edad=77),
            Personas(id=788596, nombre='Rachel', genero='No binario', edad=97),
            Personas(id=607107, nombre='Luis', genero='Femenino', edad=15),
            Personas(id=852596, nombre='Victoria', genero='No binario', edad=24),
            Personas(id=513285, nombre='Laura', genero='No binario', edad=49),
            Personas(id=912105, nombre='Lucas', genero='Masculino', edad=50),
            Personas(id=480227, nombre='Isidora', genero='Masculino', edad=54),
            Personas(id=780224, nombre='Lucía', genero='Masculino', edad=86),
            Personas(id=344229, nombre='Andrés', genero='Masculino', edad=77),
            Personas(id=662059, nombre='Jorge', genero='Femenino', edad=23),
        ]
        reservas = [
            Reservas(id_persona=852596, id_funcion=9454, numero_butaca='A1'),
            Reservas(id_persona=480227, id_funcion=9454, numero_butaca='H4'),
            Reservas(id_persona=780224, id_funcion=9454, numero_butaca='C5'),
            Reservas(id_persona=788596, id_funcion=9454, numero_butaca='C1'),
            Reservas(id_persona=912105, id_funcion=9454, numero_butaca='F10'),
            Reservas(id_persona=344229, id_funcion=9454, numero_butaca='F2'),
        ]
        funciones = [
            Funciones(id=9454, numero_sala=9, id_pelicula=13156317, horario=5, fecha='02-12-23'),
        ]
        peliculas = [
            Peliculas(id=13156317, titulo='Titanic', genero='Animación', rating=8.4),
        ]

        pelicula = 'Titanic'
        horario = 5
        expected_nombres = ['Victoria', 'Isidora', 'Lucía', 'Rachel', 'Lucas', 'Andrés']

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_butacas_altas(gen_personas, gen_peliculas, gen_reservas, gen_funciones,
                                       pelicula, horario)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_nombres)

    def test_1(self):
        """
        Varias funciones de la pelicula, pero solo una en el horario
        """
        personas = [
            Personas(id=198477, nombre='Nicolás', genero='No binario', edad=72),
            Personas(id=289380, nombre='Tomás', genero='Masculino', edad=58),
            Personas(id=591338, nombre='Alex', genero='Masculino', edad=43),
            Personas(id=571081, nombre='Victoria', genero='No binario', edad=17),
            Personas(id=471183, nombre='Felipe', genero='No binario', edad=39),
            Personas(id=752104, nombre='Luis', genero='Masculino', edad=36),
            Personas(id=971631, nombre='Isabella', genero='Masculino', edad=17),
            Personas(id=369116, nombre='Andrea', genero='Masculino', edad=65),
            Personas(id=360116, nombre='Lucas', genero='Femenino', edad=76),
            Personas(id=289151, nombre='Carla', genero='Masculino', edad=24),
        ]
        reservas = [
            Reservas(id_persona=471183, id_funcion=8109, numero_butaca='F8'),
            Reservas(id_persona=471183, id_funcion=1444, numero_butaca='A3'),
            Reservas(id_persona=289380, id_funcion=1444, numero_butaca='G8'),
            Reservas(id_persona=752104, id_funcion=1444, numero_butaca='F2'),
            Reservas(id_persona=752104, id_funcion=8109, numero_butaca='B3'),
            Reservas(id_persona=571081, id_funcion=8109, numero_butaca='F6'),
        ]
        funciones = [
            Funciones(id=1444, numero_sala=9, id_pelicula=80514404, horario=7, fecha='04-12-23'),
            Funciones(id=8109, numero_sala=5, id_pelicula=80514404, horario=8, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=80514404, titulo='Pocahontas', genero='Animación', rating=7.4),
        ]

        pelicula = 'Pocahontas'
        horario = 7
        expected_nombres = ['Tomás', 'Felipe', 'Luis']

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_butacas_altas(gen_personas, gen_peliculas, gen_reservas, gen_funciones,
                                       pelicula, horario)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_nombres)

    def test_2(self):
        """
        Varias funciones en el horario, pero de distintas peliculas
        """
        personas = [
            Personas(id=651331, nombre='Lucía', genero='No binario', edad=14),
            Personas(id=517596, nombre='Carla', genero='Femenino', edad=9),
            Personas(id=369116, nombre='Andrea', genero='Masculino', edad=65),
            Personas(id=721504, nombre='Tomás', genero='Masculino', edad=36),
            Personas(id=788596, nombre='Rachel', genero='No binario', edad=97),
            Personas(id=970731, nombre='Martina', genero='No binario', edad=23),
            Personas(id=138359, nombre='Valentina', genero='Masculino', edad=69),
            Personas(id=104423, nombre='Rodrigo', genero='No binario', edad=38),
            Personas(id=650018, nombre='Alberto', genero='Masculino', edad=33),
            Personas(id=974627, nombre='Julia', genero='No binario', edad=45),
        ]
        reservas = [
            Reservas(id_persona=369116, id_funcion=8109, numero_butaca='E8'),
            Reservas(id_persona=788596, id_funcion=8109, numero_butaca='H1'),
            Reservas(id_persona=974627, id_funcion=4479, numero_butaca='H3'),
            Reservas(id_persona=970731, id_funcion=4479, numero_butaca='G1'),
            Reservas(id_persona=651331, id_funcion=4479, numero_butaca='G7'),
            Reservas(id_persona=721504, id_funcion=4479, numero_butaca='D9'),
            Reservas(id_persona=650018, id_funcion=8109, numero_butaca='B9'),
            Reservas(id_persona=104423, id_funcion=8109, numero_butaca='H6'),
            Reservas(id_persona=138359, id_funcion=4479, numero_butaca='A2'),
            Reservas(id_persona=517596, id_funcion=8109, numero_butaca='D7'),
        ]
        funciones = [
            Funciones(id=8109, numero_sala=5, id_pelicula=28536562, horario=6, fecha='05-12-23'),
            Funciones(id=4479, numero_sala=2, id_pelicula=67774148, horario=6, fecha='04-12-23'),
        ]
        peliculas = [
            Peliculas(id=28536562, titulo='The Godfather', genero='Animación', rating=7.1),
            Peliculas(id=67774148, titulo='Seven Samurai', genero='Suspense', rating=8.6),
        ]

        pelicula = 'Seven Samurai'
        horario = 6
        expected_nombres = ['Lucía', 'Martina', 'Valentina', 'Julia', 'Tomás']

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_butacas_altas(gen_personas, gen_peliculas, gen_reservas, gen_funciones,
                                       pelicula, horario)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_nombres)

    def test_3(self):
        """
        Varias funciones y peliculas en distintos horarios
        Una persona vio la pelicula más de una vez en el horaio solicitado
        """
        personas = [
            Personas(id=780224, nombre='Lucía', genero='Masculino', edad=86),
            Personas(id=523275, nombre='Emma', genero='No binario', edad=56),
            Personas(id=650018, nombre='Alberto', genero='Masculino', edad=33),
            Personas(id=344229, nombre='Andrés', genero='Masculino', edad=77),
            Personas(id=788596, nombre='Rachel', genero='No binario', edad=97),
            Personas(id=721504, nombre='Tomás', genero='Masculino', edad=36),
            Personas(id=399774, nombre='Mateo', genero='No binario', edad=12),
            Personas(id=143846, nombre='Arturo', genero='Masculino', edad=32),
        ]
        reservas = [
            Reservas(id_persona=780224, id_funcion=4870, numero_butaca='F7'),
            Reservas(id_persona=788596, id_funcion=3099, numero_butaca='E2'),
            Reservas(id_persona=344229, id_funcion=8396, numero_butaca='B6'),
            Reservas(id_persona=788596, id_funcion=9454, numero_butaca='C2'),
            Reservas(id_persona=721504, id_funcion=4870, numero_butaca='E1'),
            Reservas(id_persona=344229, id_funcion=2082, numero_butaca='F9'),
            Reservas(id_persona=788596, id_funcion=8396, numero_butaca='A2'),
            Reservas(id_persona=523275, id_funcion=8083, numero_butaca='G2'),
            Reservas(id_persona=344229, id_funcion=3099, numero_butaca='H5'),
            Reservas(id_persona=523275, id_funcion=3099, numero_butaca='A7'),
            Reservas(id_persona=523275, id_funcion=1155, numero_butaca='E8'),
        ]
        funciones = [
            Funciones(id=3428, numero_sala=4, id_pelicula=95039909, horario=7, fecha='04-12-23'),
            Funciones(id=3099, numero_sala=4, id_pelicula=95039909, horario=4, fecha='01-12-23'),
            Funciones(id=8396, numero_sala=6, id_pelicula=95039909, horario=9, fecha='03-12-23'),
            Funciones(id=4870, numero_sala=9, id_pelicula=86302163, horario=9, fecha='01-12-23'),
            Funciones(id=6386, numero_sala=8, id_pelicula=70789763, horario=5, fecha='01-12-23'),
            Funciones(id=8083, numero_sala=7, id_pelicula=95039909, horario=4, fecha='04-12-23'),
            Funciones(id=8109, numero_sala=5, id_pelicula=70789763, horario=7, fecha='05-12-23'),
            Funciones(id=2082, numero_sala=8, id_pelicula=70789763, horario=7, fecha='03-12-23'),
            Funciones(id=9454, numero_sala=9, id_pelicula=95039909, horario=5, fecha='02-12-23'),
            Funciones(id=1155, numero_sala=1, id_pelicula=70789763, horario=7, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=86302163, titulo='The Notebook', genero='Ciencia Ficción', rating=6.2),
            Peliculas(id=70789763, titulo='Inception', genero='Superhéroes', rating=8.6),
            Peliculas(id=91755118, titulo='Braveheart', genero='Comedia', rating=6.2),
            Peliculas(id=56960764, titulo='Motocrossed', genero='Crimen', rating=9.2),
            Peliculas(id=95039909, titulo='The Matrix Reloaded', genero='Deportes', rating=5.4),
        ]

        pelicula = 'The Matrix Reloaded'
        horario = 4
        expected_nombres = ['Emma', 'Andrés', 'Rachel']

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_butacas_altas(gen_personas, gen_peliculas, gen_reservas, gen_funciones,
                                       pelicula, horario)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_nombres)

    def test_4(self):
        """
        Varias funciones y peliculas en distintos horarios
        Algunas personas vieron la pelicula más de una vez, pero en distintos horarios
        """
        personas = [
            Personas(id=589077, nombre='Adela', genero='Masculino', edad=91),
            Personas(id=344229, nombre='Andrés', genero='Masculino', edad=77),
            Personas(id=523275, nombre='Emma', genero='No binario', edad=56),
            Personas(id=263081, nombre='Rachel', genero='No binario', edad=71),
            Personas(id=447300, nombre='Pietro', genero='Femenino', edad=14),
            Personas(id=809018, nombre='Magdalena', genero='Masculino', edad=39),
            Personas(id=547446, nombre='Leonardo', genero='No binario', edad=58),
            Personas(id=368840, nombre='Lucía', genero='No binario', edad=25),
            Personas(id=852596, nombre='Victoria', genero='No binario', edad=24),
        ]
        reservas = [
            Reservas(id_persona=809018, id_funcion=6993, numero_butaca='D10'),
            Reservas(id_persona=523275, id_funcion=4639, numero_butaca='C2'),
            Reservas(id_persona=589077, id_funcion=6993, numero_butaca='G6'),
            Reservas(id_persona=263081, id_funcion=6993, numero_butaca='G4'),
            Reservas(id_persona=447300, id_funcion=6993, numero_butaca='H8'),
            Reservas(id_persona=852596, id_funcion=4639, numero_butaca='G10'),
            Reservas(id_persona=447300, id_funcion=6253, numero_butaca='E3'),
            Reservas(id_persona=809018, id_funcion=6253, numero_butaca='F1'),
            Reservas(id_persona=589077, id_funcion=6446, numero_butaca='H3'),
            Reservas(id_persona=523275, id_funcion=6993, numero_butaca='H6'),
            Reservas(id_persona=589077, id_funcion=6253, numero_butaca='H10'),
            Reservas(id_persona=589077, id_funcion=4639, numero_butaca='F8'),
            Reservas(id_persona=547446, id_funcion=6446, numero_butaca='C5'),
            Reservas(id_persona=809018, id_funcion=4639, numero_butaca='F10'),
            Reservas(id_persona=852596, id_funcion=6993, numero_butaca='F2'),
            Reservas(id_persona=344229, id_funcion=6446, numero_butaca='D7'),
            Reservas(id_persona=809018, id_funcion=6446, numero_butaca='C7'),
            Reservas(id_persona=447300, id_funcion=4639, numero_butaca='A4'),
            Reservas(id_persona=523275, id_funcion=6253, numero_butaca='E9'),
        ]
        funciones = [
            Funciones(id=6446, numero_sala=6, id_pelicula=95136331, horario=6, fecha='05-12-23'),
            Funciones(id=6253, numero_sala=4, id_pelicula=19494205, horario=8, fecha='05-12-23'),
            Funciones(id=6993, numero_sala=7, id_pelicula=19494205, horario=9, fecha='04-12-23'),
            Funciones(id=4639, numero_sala=9, id_pelicula=95136331, horario=8, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=95136331, titulo='Thor: Ragnarok', genero='Superhéroes', rating=7.3),
            Peliculas(id=19494205, titulo='The Lord of the Rings: The Two Towers', genero='Drama', rating=7.7),
        ]

        pelicula = 'Thor: Ragnarok'
        horario = 8
        expected_nombres = ['Adela', 'Emma', 'Pietro', 'Magdalena', 'Victoria']

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_butacas_altas(gen_personas, gen_peliculas, gen_reservas, gen_funciones,
                                       pelicula, horario)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_nombres)


if __name__ == '__main__':
    unittest.main(verbosity=2)
