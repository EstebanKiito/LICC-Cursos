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
            Reservas(id_persona=691734, id_funcion=2826, numero_butaca='C1'),
            Reservas(id_persona=781245, id_funcion=3566, numero_butaca='E1'),
            Reservas(id_persona=184926, id_funcion=3566, numero_butaca='A3'),
            Reservas(id_persona=852647, id_funcion=2826, numero_butaca='C9'),
            Reservas(id_persona=248765, id_funcion=9795, numero_butaca='C5'),
            Reservas(id_persona=917346, id_funcion=8386, numero_butaca='H4'),
            Reservas(id_persona=824156, id_funcion=8386, numero_butaca='G10'),
            Reservas(id_persona=138975, id_funcion=8386, numero_butaca='E6'),
            Reservas(id_persona=367591, id_funcion=3566, numero_butaca='F4'),
            Reservas(id_persona=654365, id_funcion=3566, numero_butaca='D3'),
            Reservas(id_persona=763215, id_funcion=2826, numero_butaca='B3'),
            Reservas(id_persona=149872, id_funcion=9795, numero_butaca='C6'),
            Reservas(id_persona=463518, id_funcion=5408, numero_butaca='H10'),
            Reservas(id_persona=573912, id_funcion=2826, numero_butaca='H8'),
            Reservas(id_persona=529874, id_funcion=5408, numero_butaca='D1'),
            Reservas(id_persona=951827, id_funcion=8386, numero_butaca='D7'),
            Reservas(id_persona=954362, id_funcion=2826, numero_butaca='G3'),
            Reservas(id_persona=518367, id_funcion=8386, numero_butaca='F6'),
        ]
        funciones = [
            Funciones(id=5408, numero_sala=2, id_pelicula=58329437, horario=1, fecha='02-12-23'),
            Funciones(id=9795, numero_sala=8, id_pelicula=95817124, horario=3, fecha='02-12-23'),
            Funciones(id=8386, numero_sala=7, id_pelicula=95817124, horario=5, fecha='01-12-23'),
            Funciones(id=3566, numero_sala=4, id_pelicula=95817124, horario=4, fecha='01-12-23'),
            Funciones(id=2826, numero_sala=1, id_pelicula=95817124, horario=2, fecha='02-12-23'),
        ]
        peliculas = [
            Peliculas(id=46804999, titulo='Guardians of the Galaxy Vol. 2', genero='Superhéroes', rating=7.1),
            Peliculas(id=59197164, titulo='Motocrossed', genero='Deportes', rating=6.6),
            Peliculas(id=29533644, titulo='Saving Private Ryan', genero='Superhéroes', rating=8.6),
            Peliculas(id=92004621, titulo='Treasure Planet', genero='Deportes', rating=7.7),
            Peliculas(id=58329437, titulo='My Neighbor Totoro', genero='Animación', rating=8.6),
            Peliculas(id=95817124, titulo='Fight Club', genero='Crimen', rating=8.8),
        ]
        fecha_funcion = '02-12-23'
        reservas_maximas = 5
        expected_horarios = [3]

        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = obtener_horarios_disponibles(gen_peliculas, gen_reservas, gen_funciones, 
                                              fecha_funcion, reservas_maximas)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_horarios)

    def test_1(self):
        """
        Ningun horario disponible

        - Dos funciones coinciden con la pelicula y la fecha, ninguna con butacas disponibles
        - Una función coincide con la pelicula pero no con la fecha
        - Una función coincide con la fecha pero no con la pelicula
        - Dos funciones no coinciden con la pelicula ni con la fecha
        """
        reservas = [
            Reservas(id_persona=745219, id_funcion=9795, numero_butaca='G10'),
            Reservas(id_persona=895642, id_funcion=4561, numero_butaca='H7'),
            Reservas(id_persona=428362, id_funcion=9400, numero_butaca='G9'),
            Reservas(id_persona=248765, id_funcion=9795, numero_butaca='A6'),
            Reservas(id_persona=534254, id_funcion=4736, numero_butaca='E5'),
            Reservas(id_persona=529874, id_funcion=4678, numero_butaca='A3'),
            Reservas(id_persona=765476, id_funcion=4736, numero_butaca='C3'),
            Reservas(id_persona=984723, id_funcion=9584, numero_butaca='H1'),
            Reservas(id_persona=184926, id_funcion=4561, numero_butaca='D10'),
            Reservas(id_persona=926342, id_funcion=4736, numero_butaca='B2'),
            Reservas(id_persona=278561, id_funcion=9795, numero_butaca='B4'),
            Reservas(id_persona=543254, id_funcion=9584, numero_butaca='C2'),
            Reservas(id_persona=186243, id_funcion=9584, numero_butaca='E1'),
            Reservas(id_persona=946353, id_funcion=4678, numero_butaca='B5'),
            Reservas(id_persona=645321, id_funcion=4561, numero_butaca='C5'),
        ]
        funciones = [
            Funciones(id=4678, numero_sala=2, id_pelicula=45245368, horario=6, fecha='02-12-23'),
            Funciones(id=9795, numero_sala=8, id_pelicula=49034902, horario=3, fecha='05-12-23'),
            Funciones(id=4561, numero_sala=2, id_pelicula=55774654, horario=5, fecha='01-12-23'),
            Funciones(id=9400, numero_sala=7, id_pelicula=49034902, horario=2, fecha='03-12-23'),
            Funciones(id=4736, numero_sala=4, id_pelicula=49034902, horario=2, fecha='05-12-23'),
            Funciones(id=9584, numero_sala=3, id_pelicula=84580833, horario=3, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=42475848, titulo='Spirited Away', genero='Animación', rating=8.6),
            Peliculas(id=84580833, titulo='Wreck-It Ralph', genero='Animación', rating=7.5),
            Peliculas(id=45245368, titulo='The Even Stevens Movie', genero='Comedia', rating=6.6),
            Peliculas(id=55774654, titulo='The Pianist', genero='Superhéroes', rating=8.5),
            Peliculas(id=49034902, titulo='The Godfather', genero='Crimen', rating=9.2),
        ]
        fecha_funcion = '05-12-23'
        reservas_maximas = 3
        expected_horarios = []

        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = obtener_horarios_disponibles(gen_peliculas, gen_reservas, gen_funciones, 
                                              fecha_funcion, reservas_maximas)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_horarios)

    def test_2(self):
        """
        Dos horarios disponibles

        - Dos funciones coinciden con la pelicula y la fecha, ambas con butacas disponibles
        - Una función coincide con la pelicula pero no con la fecha
        - Una función coincide con la fecha pero no con la pelicula
        - Una funcion no coincide con la pelicula ni con la fecha
        """
        reservas = [
            Reservas(id_persona=781245, id_funcion=9524, numero_butaca='B2'),
            Reservas(id_persona=245769, id_funcion=9524, numero_butaca='F4'),
            Reservas(id_persona=573849, id_funcion=7735, numero_butaca='A5'),
            Reservas(id_persona=596318, id_funcion=6237, numero_butaca='G10'),
            Reservas(id_persona=926342, id_funcion=9391, numero_butaca='F8'),
            Reservas(id_persona=543254, id_funcion=9391, numero_butaca='A4'),
            Reservas(id_persona=895642, id_funcion=7735, numero_butaca='H10'),
            Reservas(id_persona=735242, id_funcion=7735, numero_butaca='C8'),
            Reservas(id_persona=429186, id_funcion=9391, numero_butaca='A10'),
            Reservas(id_persona=317984, id_funcion=6237, numero_butaca='H1'),
        ]
        funciones = [
            Funciones(id=7777, numero_sala=6, id_pelicula=70752273, horario=5, fecha='05-12-23'),
            Funciones(id=9391, numero_sala=1, id_pelicula=87538292, horario=5, fecha='05-12-23'),
            Funciones(id=9524, numero_sala=5, id_pelicula=70752273, horario=2, fecha='01-12-23'),
            Funciones(id=6237, numero_sala=1, id_pelicula=95417284, horario=1, fecha='01-12-23'),
            Funciones(id=7735, numero_sala=3, id_pelicula=70752273, horario=4, fecha='01-12-23'),
        ]
        peliculas = [
            Peliculas(id=87538292, titulo='Monsters Inc.', genero='Animación', rating=8.1),
            Peliculas(id=95417284, titulo='Camp Rock', genero='Musical', rating=5.1),
            Peliculas(id=70752273, titulo='Gladiator', genero='Crimen', rating=8.5),
        ]
        fecha_funcion = '01-12-23'
        reservas_maximas = 5
        expected_horarios = [2, 4]

        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = obtener_horarios_disponibles(gen_peliculas, gen_reservas, gen_funciones, 
                                              fecha_funcion, reservas_maximas)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_horarios)

    def test_3(self):
        """
        Muchas funciones, dos horarios disponibles
        El horario 1 tiene butacas disponibles en dos salas 
        """
        reservas = [
            Reservas(id_persona=983156, id_funcion=8008, numero_butaca='B10'),
            Reservas(id_persona=781245, id_funcion=4293, numero_butaca='H7'),
            Reservas(id_persona=372615, id_funcion=9795, numero_butaca='H2'),
            Reservas(id_persona=367591, id_funcion=4211, numero_butaca='G2'),
            Reservas(id_persona=529874, id_funcion=5220, numero_butaca='A2'),
            Reservas(id_persona=825469, id_funcion=5220, numero_butaca='D9'),
            Reservas(id_persona=463518, id_funcion=9795, numero_butaca='F7'),
            Reservas(id_persona=946353, id_funcion=4293, numero_butaca='G3'),
            Reservas(id_persona=245769, id_funcion=9391, numero_butaca='G5'),
            Reservas(id_persona=836197, id_funcion=9391, numero_butaca='B9'),
        ]
        funciones = [
            Funciones(id=2826, numero_sala=1, id_pelicula=57395306, horario=4, fecha='05-12-23'),
            Funciones(id=9795, numero_sala=8, id_pelicula=41115118, horario=3, fecha='05-12-23'),
            Funciones(id=9391, numero_sala=1, id_pelicula=41115118, horario=5, fecha='05-12-23'),
            Funciones(id=4293, numero_sala=7, id_pelicula=57395306, horario=4, fecha='05-12-23'),
            Funciones(id=8008, numero_sala=6, id_pelicula=41115118, horario=6, fecha='01-12-23'),
            Funciones(id=3670, numero_sala=7, id_pelicula=57395306, horario=1, fecha='05-12-23'),
            Funciones(id=7617, numero_sala=8, id_pelicula=41115118, horario=2, fecha='04-12-23'),
            Funciones(id=5220, numero_sala=5, id_pelicula=57395306, horario=4, fecha='03-12-23'),
            Funciones(id=7777, numero_sala=6, id_pelicula=57395306, horario=1, fecha='05-12-23'),
            Funciones(id=4211, numero_sala=1, id_pelicula=98009659, horario=3, fecha='03-12-23'),
        ]
        peliculas = [
            Peliculas(id=41115118, titulo='Avatar', genero='Crimen', rating=7.8),
            Peliculas(id=57395306, titulo='Inuyasha', genero='Animación', rating=8.4),
            Peliculas(id=98009659, titulo='Twitches', genero='Fantasía', rating=6.7),
        ]
        fecha_funcion = '05-12-23'
        reservas_maximas = 2
        expected_horarios = [1, 4]

        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = obtener_horarios_disponibles(gen_peliculas, gen_reservas, gen_funciones, 
                                              fecha_funcion, reservas_maximas)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_horarios)

    def test_4(self):
        """
        Test grande, tres horarios disponibles
        """
        reservas = [
            Reservas(id_persona=317984, id_funcion=5181, numero_butaca='H10'),
            Reservas(id_persona=248765, id_funcion=4293, numero_butaca='G2'),
            Reservas(id_persona=245769, id_funcion=3224, numero_butaca='F6'),
            Reservas(id_persona=352429, id_funcion=7015, numero_butaca='E8'),
            Reservas(id_persona=691734, id_funcion=8008, numero_butaca='B6'),
            Reservas(id_persona=437219, id_funcion=1741, numero_butaca='F1'),
            Reservas(id_persona=463289, id_funcion=5181, numero_butaca='G5'),
            Reservas(id_persona=364298, id_funcion=3566, numero_butaca='D5'),
            Reservas(id_persona=312497, id_funcion=4582, numero_butaca='E9'),
            Reservas(id_persona=419725, id_funcion=5517, numero_butaca='F10'),
            Reservas(id_persona=463518, id_funcion=5408, numero_butaca='F3'),
            Reservas(id_persona=954362, id_funcion=3224, numero_butaca='C8'),
            Reservas(id_persona=836197, id_funcion=8008, numero_butaca='B2'),
            Reservas(id_persona=294176, id_funcion=2221, numero_butaca='H7'),
            Reservas(id_persona=534254, id_funcion=3566, numero_butaca='F2'),
            Reservas(id_persona=186243, id_funcion=1131, numero_butaca='G10'),
            Reservas(id_persona=763215, id_funcion=6566, numero_butaca='E6'),
            Reservas(id_persona=376581, id_funcion=3224, numero_butaca='B7'),
            Reservas(id_persona=946353, id_funcion=2221, numero_butaca='D10'),
            Reservas(id_persona=735242, id_funcion=2221, numero_butaca='E4'),
            Reservas(id_persona=367591, id_funcion=4293, numero_butaca='A10'),
            Reservas(id_persona=429186, id_funcion=5517, numero_butaca='A7'),
            Reservas(id_persona=739182, id_funcion=1910, numero_butaca='E7'),
            Reservas(id_persona=951827, id_funcion=8008, numero_butaca='C7'),
            Reservas(id_persona=573849, id_funcion=1131, numero_butaca='B5'),
            Reservas(id_persona=598127, id_funcion=6566, numero_butaca='B8'),
            Reservas(id_persona=529874, id_funcion=5517, numero_butaca='H4'),
            Reservas(id_persona=697413, id_funcion=5181, numero_butaca='H1'),
            Reservas(id_persona=926242, id_funcion=6566, numero_butaca='H2'),
        ]
        funciones = [
            Funciones(id=5181, numero_sala=6, id_pelicula=44000862, horario=3, fecha='03-12-23'),
            Funciones(id=1131, numero_sala=4, id_pelicula=71285784, horario=6, fecha='04-12-23'),
            Funciones(id=6566, numero_sala=1, id_pelicula=71285784, horario=4, fecha='04-12-23'),
            Funciones(id=1331, numero_sala=5, id_pelicula=71285784, horario=5, fecha='04-12-23'),
            Funciones(id=1910, numero_sala=6, id_pelicula=71285784, horario=1, fecha='01-12-23'),
            Funciones(id=3566, numero_sala=4, id_pelicula=44000862, horario=4, fecha='02-12-23'),
            Funciones(id=3224, numero_sala=8, id_pelicula=71285784, horario=5, fecha='04-12-23'),
            Funciones(id=5408, numero_sala=2, id_pelicula=44000862, horario=2, fecha='03-12-23'),
            Funciones(id=8008, numero_sala=6, id_pelicula=44000862, horario=6, fecha='01-12-23'),
            Funciones(id=4582, numero_sala=6, id_pelicula=71285784, horario=4, fecha='04-12-23'),
            Funciones(id=4293, numero_sala=7, id_pelicula=71285784, horario=4, fecha='05-12-23'),
            Funciones(id=1741, numero_sala=4, id_pelicula=44000862, horario=3, fecha='01-12-23'),
            Funciones(id=2221, numero_sala=4, id_pelicula=71285784, horario=1, fecha='04-12-23'),
            Funciones(id=7015, numero_sala=7, id_pelicula=71285784, horario=6, fecha='02-12-23'),
            Funciones(id=5517, numero_sala=3, id_pelicula=44000862, horario=5, fecha='02-12-23'),
        ]
        peliculas = [
            Peliculas(id=44000862, titulo='Avengers: Age of Ultron', genero='Animación', rating=7.6),
            Peliculas(id=71285784, titulo='American History X', genero='Superhéroes', rating=8.5),
        ]
        fecha_funcion = '04-12-23'
        reservas_maximas = 3
        expected_horarios = [4, 5, 6]

        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = obtener_horarios_disponibles(gen_peliculas, gen_reservas, gen_funciones, 
                                              fecha_funcion, reservas_maximas)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_horarios)

if __name__ == '__main__':
    unittest.main(verbosity=2)