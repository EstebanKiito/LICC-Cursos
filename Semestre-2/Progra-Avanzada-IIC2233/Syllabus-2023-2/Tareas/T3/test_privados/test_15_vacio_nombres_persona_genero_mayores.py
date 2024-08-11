import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import nombres_persona_genero_mayores
from utilidades import Personas, Peliculas, Funciones, Reservas
from typing import Generator


class TestVacioNombresPersonaGeneroMayores(unittest.TestCase):

    def test_0(self):
        """
        Ninguna persona cumple las condiciones
        """
        personas = [
            Personas(id=971631, nombre='Pedro', genero='No binario', edad=14),
            Personas(id=662059, nombre='Victoria', genero='Masculino', edad=20),
            Personas(id=752104, nombre='Isidora', genero='No binario', edad=33),
            Personas(id=289151, nombre='Leonardo', genero='No binario', edad=21),
            Personas(id=193453, nombre='José', genero='Masculino', edad=77),
            Personas(id=650018, nombre='Daniel', genero='No binario', edad=30),
            Personas(id=185689, nombre='Esteban', genero='Femenino', edad=81),
            Personas(id=143846, nombre='Juampi', genero='No binario', edad=29),
            Personas(id=743208, nombre='Pietro', genero='No binario', edad=66),
            Personas(id=368840, nombre='Valeria', genero='Femenino', edad=22),
            Personas(id=752204, nombre='Paula', genero='No binario', edad=64),
        ]
        reservas = [
            Reservas(id_persona=193453, id_funcion=8109, numero_butaca='G1'),
            Reservas(id_persona=143846, id_funcion=1685, numero_butaca='F10'),
            Reservas(id_persona=193453, id_funcion=1685, numero_butaca='A6'),
            Reservas(id_persona=143846, id_funcion=4870, numero_butaca='D7'),
            Reservas(id_persona=971631, id_funcion=8109, numero_butaca='H2'),
            Reservas(id_persona=143846, id_funcion=8109, numero_butaca='G5'),
            Reservas(id_persona=743208, id_funcion=8109, numero_butaca='A5'),
            Reservas(id_persona=368840, id_funcion=4870, numero_butaca='B1'),
            Reservas(id_persona=185689, id_funcion=1685, numero_butaca='G7'),
            Reservas(id_persona=368840, id_funcion=8109, numero_butaca='B10'),
            Reservas(id_persona=650018, id_funcion=1685, numero_butaca='H6'),
            Reservas(id_persona=368840, id_funcion=6262, numero_butaca='C10'),
            Reservas(id_persona=752104, id_funcion=4870, numero_butaca='B3'),
            Reservas(id_persona=143846, id_funcion=6262, numero_butaca='H7'),
        ]
        funciones = [
            Funciones(id=6262, numero_sala=1, id_pelicula=50911924, horario=5, fecha='03-12-23'),
            Funciones(id=4870, numero_sala=9, id_pelicula=29729434, horario=9, fecha='01-12-23'),
            Funciones(id=1685, numero_sala=5, id_pelicula=50911924, horario=6, fecha='04-12-23'),
            Funciones(id=8109, numero_sala=5, id_pelicula=50911924, horario=7, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=79211646, titulo='The Silence of the Lambs', genero='Animación', rating=7.6),
            Peliculas(id=50911924, titulo='The Godfather: Part II', genero='Fantasía', rating=8.7),
            Peliculas(id=63700516, titulo='Iron Man', genero='Superhéroes', rating=8.5),
            Peliculas(id=29729434, titulo='The Princess Diaries 2', genero='Acción', rating=8.0),
        ]

        pelicula = 'The Godfather: Part II'
        genero = 'No binario'
        edad = 67
        expected_nombres = []

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
