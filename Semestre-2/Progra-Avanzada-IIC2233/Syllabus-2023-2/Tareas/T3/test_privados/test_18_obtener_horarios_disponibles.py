import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import obtener_horarios_disponibles
from utilidades import Personas, Peliculas, Funciones, Reservas
from typing import Generator


class TestObtenerHorariosDisponibles(unittest.TestCase):

    def test_0(self):
        """
        Solo un horario disponible

        - Dos funciones coinciden con la pelicula y la fecha, una con butacas disponibles
        - Dos funciones coinciden con la pelicula pero no con la fecha
        - Una función coincide con la fecha pero no con la pelicula
        """
        reservas = [
            Reservas(id_persona=517596, id_funcion=8688, numero_butaca='C1'),
            Reservas(id_persona=607107, id_funcion=9428, numero_butaca='E1'),
            Reservas(id_persona=910788, id_funcion=9428, numero_butaca='A3'),
            Reservas(id_persona=678509, id_funcion=8688, numero_butaca='C9'),
            Reservas(id_persona=974627, id_funcion=6657, numero_butaca='C5'),
            Reservas(id_persona=743208, id_funcion=5248, numero_butaca='H4'),
            Reservas(id_persona=650018, id_funcion=5248, numero_butaca='G10'),
            Reservas(id_persona=864837, id_funcion=5248, numero_butaca='E6'),
            Reservas(id_persona=193453, id_funcion=9428, numero_butaca='F4'),
            Reservas(id_persona=480227, id_funcion=9428, numero_butaca='D3'),
            Reservas(id_persona=589077, id_funcion=8688, numero_butaca='B3'),
            Reservas(id_persona=875734, id_funcion=6657, numero_butaca='C6'),
            Reservas(id_persona=289380, id_funcion=2270, numero_butaca='H10'),
            Reservas(id_persona=399774, id_funcion=8688, numero_butaca='H8'),
            Reservas(id_persona=355736, id_funcion=2270, numero_butaca='D1'),
            Reservas(id_persona=777689, id_funcion=5248, numero_butaca='D7'),
            Reservas(id_persona=780224, id_funcion=8688, numero_butaca='G3'),
            Reservas(id_persona=344229, id_funcion=5248, numero_butaca='F6'),
        ]
        funciones = [
            Funciones(id=2270, numero_sala=5, id_pelicula=66255299, horario=4, fecha='02-07-23'),
            Funciones(id=6657, numero_sala=2, id_pelicula=13742986, horario=6, fecha='02-07-23'),
            Funciones(id=5248, numero_sala=1, id_pelicula=13742986, horario=8, fecha='01-07-23'),
            Funciones(id=9428, numero_sala=7, id_pelicula=13742986, horario=7, fecha='01-07-23'),
            Funciones(id=8688, numero_sala=4, id_pelicula=13742986, horario=5, fecha='02-07-23'),
        ]
        peliculas = [
            Peliculas(id=54730861, titulo='Avengers: Age of Ultron', genero='Superhéroes', rating=7.1),
            Peliculas(id=67123026, titulo='Spider-Man: Homecoming', genero='Deportes', rating=6.6),
            Peliculas(id=37459506, titulo='The Dark Knight', genero='Superhéroes', rating=8.6),
            Peliculas(id=99930483, titulo='Akira', genero='Deportes', rating=7.7),
            Peliculas(id=66255299, titulo='Inception', genero='Animación', rating=8.6),
            Peliculas(id=13742986, titulo='Braveheart', genero='Crimen', rating=8.8),
        ]
        fecha_funcion = '02-07-23'
        reservas_maximas = 5
        expected_horarios = [6]

        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = obtener_horarios_disponibles(gen_peliculas, gen_reservas, gen_funciones,
                                              fecha_funcion, reservas_maximas)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_horarios)

    def test_1(self):
        """
        Dos horarios disponibles

        - Dos funciones coinciden con la pelicula y la fecha, ambas con butacas disponibles
        - Una función coincide con la pelicula pero no con la fecha
        - Una función coincide con la fecha pero no con la pelicula
        - Una funcion no coincide con la pelicula ni con la fecha
        """
        reservas = [
            Reservas(id_persona=607107, id_funcion=6386, numero_butaca='B2'),
            Reservas(id_persona=971631, id_funcion=6386, numero_butaca='F4'),
            Reservas(id_persona=399711, id_funcion=4597, numero_butaca='A5'),
            Reservas(id_persona=422180, id_funcion=3099, numero_butaca='G10'),
            Reservas(id_persona=752204, id_funcion=6253, numero_butaca='F8'),
            Reservas(id_persona=369116, id_funcion=6253, numero_butaca='A4'),
            Reservas(id_persona=721504, id_funcion=4597, numero_butaca='H10'),
            Reservas(id_persona=561104, id_funcion=4597, numero_butaca='C8'),
            Reservas(id_persona=255048, id_funcion=6253, numero_butaca='A10'),
            Reservas(id_persona=143846, id_funcion=3099, numero_butaca='H1'),
        ]
        funciones = [
            Funciones(id=4639, numero_sala=9, id_pelicula=78678135, horario=8, fecha='05-01-14'),
            Funciones(id=6253, numero_sala=4, id_pelicula=95464154, horario=8, fecha='05-01-14'),
            Funciones(id=6386, numero_sala=8, id_pelicula=78678135, horario=5, fecha='01-01-14'),
            Funciones(id=3099, numero_sala=4, id_pelicula=13343146, horario=4, fecha='01-01-14'),
            Funciones(id=4597, numero_sala=6, id_pelicula=78678135, horario=7, fecha='01-01-14'),
        ]
        peliculas = [
            Peliculas(id=95464154, titulo='Avatar', genero='Animación', rating=8.1),
            Peliculas(id=13343146, titulo='Se7en', genero='Musical', rating=5.1),
            Peliculas(id=78678135, titulo='Reservoir Dogs', genero='Crimen', rating=8.5),
        ]
        fecha_funcion = '01-01-14'
        reservas_maximas = 5
        expected_horarios = [5, 7]

        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = obtener_horarios_disponibles(gen_peliculas, gen_reservas, gen_funciones,
                                              fecha_funcion, reservas_maximas)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_horarios)

    def test_2(self):
        """
        Muchas funciones, dos horarios disponibles
        El horario 1 tiene butacas disponibles en dos salas
        """
        reservas = [
            Reservas(id_persona=809018, id_funcion=4870, numero_butaca='B10'),
            Reservas(id_persona=607107, id_funcion=1155, numero_butaca='H7'),
            Reservas(id_persona=198477, id_funcion=6657, numero_butaca='H2'),
            Reservas(id_persona=193453, id_funcion=1073, numero_butaca='G2'),
            Reservas(id_persona=355736, id_funcion=2082, numero_butaca='A2'),
            Reservas(id_persona=651331, id_funcion=2082, numero_butaca='D9'),
            Reservas(id_persona=289380, id_funcion=6657, numero_butaca='F7'),
            Reservas(id_persona=772215, id_funcion=1155, numero_butaca='G3'),
            Reservas(id_persona=971631, id_funcion=6253, numero_butaca='G5'),
            Reservas(id_persona=662059, id_funcion=6253, numero_butaca='B9'),
        ]
        funciones = [
            Funciones(id=8688, numero_sala=4, id_pelicula=65321168, horario=7, fecha='05-12-20'),
            Funciones(id=6657, numero_sala=2, id_pelicula=49040980, horario=6, fecha='05-12-20'),
            Funciones(id=6253, numero_sala=4, id_pelicula=49040980, horario=8, fecha='05-12-20'),
            Funciones(id=1155, numero_sala=1, id_pelicula=65321168, horario=7, fecha='05-12-20'),
            Funciones(id=4870, numero_sala=9, id_pelicula=49040980, horario=9, fecha='01-12-20'),
            Funciones(id=9532, numero_sala=1, id_pelicula=65321168, horario=4, fecha='05-12-20'),
            Funciones(id=4479, numero_sala=2, id_pelicula=49040980, horario=5, fecha='04-12-20'),
            Funciones(id=2082, numero_sala=8, id_pelicula=65321168, horario=7, fecha='03-12-20'),
            Funciones(id=4639, numero_sala=9, id_pelicula=65321168, horario=4, fecha='05-12-20'),
            Funciones(id=1073, numero_sala=4, id_pelicula=15935521, horario=6, fecha='03-12-20'),
        ]
        peliculas = [
            Peliculas(id=49040980, titulo='The Hunchback of Notre Dame', genero='Crimen', rating=7.8),
            Peliculas(id=65321168, titulo='Forrest Gump', genero='Animación', rating=8.4),
            Peliculas(id=15935521, titulo='Big Hero 6', genero='Fantasía', rating=6.7),
        ]
        fecha_funcion = '05-12-20'
        reservas_maximas = 2
        expected_horarios = [4, 7]

        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = obtener_horarios_disponibles(gen_peliculas, gen_reservas, gen_funciones,
                                              fecha_funcion, reservas_maximas)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_horarios)

    def test_3(self):
        """
        Test grande, tres horarios disponibles
        """
        reservas = [
            Reservas(id_persona=143846, id_funcion=2043, numero_butaca='H10'),
            Reservas(id_persona=974627, id_funcion=1155, numero_butaca='G2'),
            Reservas(id_persona=971631, id_funcion=9086, numero_butaca='F6'),
            Reservas(id_persona=178291, id_funcion=3877, numero_butaca='E8'),
            Reservas(id_persona=517596, id_funcion=4870, numero_butaca='B6'),
            Reservas(id_persona=263081, id_funcion=7603, numero_butaca='F1'),
            Reservas(id_persona=289151, id_funcion=2043, numero_butaca='G5'),
            Reservas(id_persona=190160, id_funcion=9428, numero_butaca='D5'),
            Reservas(id_persona=138359, id_funcion=1444, numero_butaca='E9'),
            Reservas(id_persona=245587, id_funcion=2379, numero_butaca='F10'),
            Reservas(id_persona=289380, id_funcion=2270, numero_butaca='F3'),
            Reservas(id_persona=780224, id_funcion=9086, numero_butaca='C8'),
            Reservas(id_persona=662059, id_funcion=4870, numero_butaca='B2'),
            Reservas(id_persona=120038, id_funcion=8083, numero_butaca='H7'),
            Reservas(id_persona=360116, id_funcion=9428, numero_butaca='F2'),
            Reservas(id_persona=912105, id_funcion=6993, numero_butaca='G10'),
            Reservas(id_persona=589077, id_funcion=3428, numero_butaca='E6'),
            Reservas(id_persona=202443, id_funcion=9086, numero_butaca='B7'),
            Reservas(id_persona=772215, id_funcion=8083, numero_butaca='D10'),
            Reservas(id_persona=561104, id_funcion=8083, numero_butaca='E4'),
            Reservas(id_persona=193453, id_funcion=1155, numero_butaca='A10'),
            Reservas(id_persona=255048, id_funcion=2379, numero_butaca='A7'),
            Reservas(id_persona=565044, id_funcion=7772, numero_butaca='E7'),
            Reservas(id_persona=777689, id_funcion=4870, numero_butaca='C7'),
            Reservas(id_persona=399711, id_funcion=6993, numero_butaca='B5'),
            Reservas(id_persona=423989, id_funcion=3428, numero_butaca='B8'),
            Reservas(id_persona=355736, id_funcion=2379, numero_butaca='H4'),
            Reservas(id_persona=523275, id_funcion=2043, numero_butaca='H1'),
            Reservas(id_persona=752104, id_funcion=3428, numero_butaca='H2'),
        ]
        funciones = [
            Funciones(id=2043, numero_sala=9, id_pelicula=51926724, horario=6, fecha='03-05-20'),
            Funciones(id=6993, numero_sala=7, id_pelicula=79211646, horario=9, fecha='04-05-20'),
            Funciones(id=3428, numero_sala=4, id_pelicula=79211646, horario=7, fecha='04-05-20'),
            Funciones(id=7193, numero_sala=8, id_pelicula=79211646, horario=8, fecha='04-05-20'),
            Funciones(id=7772, numero_sala=9, id_pelicula=79211646, horario=4, fecha='01-05-20'),
            Funciones(id=9428, numero_sala=7, id_pelicula=51926724, horario=7, fecha='02-05-20'),
            Funciones(id=9086, numero_sala=2, id_pelicula=79211646, horario=8, fecha='04-05-20'),
            Funciones(id=2270, numero_sala=5, id_pelicula=51926724, horario=5, fecha='03-05-20'),
            Funciones(id=4870, numero_sala=9, id_pelicula=51926724, horario=9, fecha='01-05-20'),
            Funciones(id=1444, numero_sala=9, id_pelicula=79211646, horario=7, fecha='04-05-20'),
            Funciones(id=1155, numero_sala=1, id_pelicula=79211646, horario=7, fecha='05-05-20'),
            Funciones(id=7603, numero_sala=7, id_pelicula=51926724, horario=6, fecha='01-05-20'),
            Funciones(id=8083, numero_sala=7, id_pelicula=79211646, horario=4, fecha='04-05-20'),
            Funciones(id=3877, numero_sala=1, id_pelicula=79211646, horario=9, fecha='02-05-20'),
            Funciones(id=2379, numero_sala=6, id_pelicula=51926724, horario=8, fecha='02-05-20'),
        ]
        peliculas = [
            Peliculas(id=51926724, titulo='The Dark Knight Rises', genero='Animación', rating=7.6),
            Peliculas(id=79211646, titulo='The Silence of the Lambs', genero='Superhéroes', rating=8.5),
        ]
        fecha_funcion = '04-05-20'
        reservas_maximas = 3
        expected_horarios = [7, 8, 9]

        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = obtener_horarios_disponibles(gen_peliculas, gen_reservas, gen_funciones, 
                                              fecha_funcion, reservas_maximas)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_horarios)


if __name__ == '__main__':
    unittest.main(verbosity=2)
