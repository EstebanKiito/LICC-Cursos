import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import obtener_horarios_disponibles
from utilidades import Personas, Peliculas, Funciones, Reservas
from typing import Generator


class TestVacioObtenerHorariosDisponibles(unittest.TestCase):

    def test_0(self):
        """
        Ningun horario disponible

        - Dos funciones coinciden con la pelicula y la fecha, ninguna con butacas disponibles
        - Una función coincide con la pelicula pero no con la fecha
        - Una función coincide con la fecha pero no con la pelicula
        - Dos funciones no coinciden con la pelicula ni con la fecha
        """
        reservas = [
            Reservas(id_persona=571081, id_funcion=6657, numero_butaca='G10'),
            Reservas(id_persona=721504, id_funcion=1423, numero_butaca='H7'),
            Reservas(id_persona=254224, id_funcion=6262, numero_butaca='G9'),
            Reservas(id_persona=974627, id_funcion=6657, numero_butaca='A6'),
            Reservas(id_persona=360116, id_funcion=1598, numero_butaca='E5'),
            Reservas(id_persona=355736, id_funcion=1540, numero_butaca='A3'),
            Reservas(id_persona=591338, id_funcion=1598, numero_butaca='C3'),
            Reservas(id_persona=810585, id_funcion=6446, numero_butaca='H1'),
            Reservas(id_persona=910788, id_funcion=1423, numero_butaca='D10'),
            Reservas(id_persona=752204, id_funcion=1598, numero_butaca='B2'),
            Reservas(id_persona=104423, id_funcion=6657, numero_butaca='B4'),
            Reservas(id_persona=369116, id_funcion=6446, numero_butaca='C2'),
            Reservas(id_persona=912105, id_funcion=6446, numero_butaca='E1'),
            Reservas(id_persona=772215, id_funcion=1540, numero_butaca='B5'),
            Reservas(id_persona=471183, id_funcion=1423, numero_butaca='C5'),
        ]
        funciones = [
            Funciones(id=1540, numero_sala=5, id_pelicula=53171230, horario=9, fecha='02-10-22'),
            Funciones(id=6657, numero_sala=2, id_pelicula=56960764, horario=6, fecha='05-10-22'),
            Funciones(id=1423, numero_sala=5, id_pelicula=63700516, horario=8, fecha='01-10-22'),
            Funciones(id=6262, numero_sala=1, id_pelicula=56960764, horario=5, fecha='03-10-22'),
            Funciones(id=1598, numero_sala=7, id_pelicula=56960764, horario=5, fecha='05-10-22'),
            Funciones(id=6446, numero_sala=6, id_pelicula=92506695, horario=6, fecha='05-10-22'),
        ]
        peliculas = [
            Peliculas(id=50401710, titulo='The Dark Knight', genero='Animación', rating=8.6),
            Peliculas(id=92506695, titulo='Gladiator', genero='Animación', rating=7.5),
            Peliculas(id=53171230, titulo='The Green Mile', genero='Comedia', rating=6.6),
            Peliculas(id=63700516, titulo='Iron Man', genero='Superhéroes', rating=8.5),
            Peliculas(id=56960764, titulo='Motocrossed', genero='Crimen', rating=9.2),
        ]
        fecha_funcion = '05-10-22'
        reservas_maximas = 3
        expected_horarios = []

        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = obtener_horarios_disponibles(gen_peliculas, gen_reservas, gen_funciones, 
                                              fecha_funcion, reservas_maximas)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(result, expected_horarios)


if __name__ == '__main__':
    unittest.main(verbosity=2)
