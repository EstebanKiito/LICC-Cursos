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
            Personas(id=739182, nombre='Beatriz', genero='Femenino', edad=77),
            Personas(id=962734, nombre='Renata', genero='Masculino', edad=97),
            Personas(id=781245, nombre='Alex', genero='No binario', edad=15),
            Personas(id=126734, nombre='Juampi', genero='Masculino', edad=24),
            Personas(id=687423, nombre='Victoria', genero='Masculino', edad=49),
            Personas(id=186243, nombre='Pablo', genero='Femenino', edad=50),
            Personas(id=654365, nombre='Isidora', genero='Femenino', edad=54),
            Personas(id=954362, nombre='Isabel', genero='Femenino', edad=86),
            Personas(id=518367, nombre='Mateo', genero='Femenino', edad=77),
            Personas(id=836197, nombre='Julia', genero='No binario', edad=23),
        ]
        reservas = [
            Reservas(id_persona=126734, id_funcion=3592, numero_butaca='A1'),
            Reservas(id_persona=654365, id_funcion=3592, numero_butaca='H4'),
            Reservas(id_persona=954362, id_funcion=3592, numero_butaca='C5'),
            Reservas(id_persona=962734, id_funcion=3592, numero_butaca='C1'),
            Reservas(id_persona=186243, id_funcion=3592, numero_butaca='F10'),
            Reservas(id_persona=518367, id_funcion=3592, numero_butaca='F2'),
        ]
        funciones = [
            Funciones(id=3592, numero_sala=6, id_pelicula=95230455, horario=2, fecha='02-12-23'),
        ]
        peliculas = [
            Peliculas(id=95230455, titulo='Your Name', genero='Animación', rating=8.4),
        ]

        pelicula = 'Your Name'
        horario = 2
        expected_nombres = ['Juampi', 'Isidora', 'Isabel', 'Renata', 'Pablo', 'Mateo']

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_butacas_altas(gen_personas, gen_peliculas, gen_reservas, gen_funciones,
                                        pelicula, horario)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_nombres)

    def test_1(self):
        """
        Varias funciones de la pelicula, pero solo una en el horario
        """
        personas = [
            Personas(id=372615, nombre='Jimena', genero='Masculino', edad=72),
            Personas(id=463518, nombre='Esteban', genero='Femenino', edad=58),
            Personas(id=765476, nombre='Rachel', genero='Femenino', edad=43),
            Personas(id=745219, nombre='Camila', genero='Masculino', edad=17),
            Personas(id=645321, nombre='Diego', genero='Masculino', edad=39),
            Personas(id=926242, nombre='Martina', genero='Femenino', edad=36),
            Personas(id=245769, nombre='Natalia', genero='Femenino', edad=17),
            Personas(id=543254, nombre='Teresa', genero='Femenino', edad=65),
            Personas(id=534254, nombre='Manuel', genero='No binario', edad=76),
            Personas(id=463289, nombre='Teresita', genero='Femenino', edad=24),
        ]
        reservas = [
            Reservas(id_persona=645321, id_funcion=2247, numero_butaca='F8'),
            Reservas(id_persona=645321, id_funcion=4582, numero_butaca='A3'),
            Reservas(id_persona=463518, id_funcion=4582, numero_butaca='G8'),
            Reservas(id_persona=926242, id_funcion=4582, numero_butaca='F2'),
            Reservas(id_persona=926242, id_funcion=2247, numero_butaca='B3'),
            Reservas(id_persona=745219, id_funcion=2247, numero_butaca='F6'),
        ]
        funciones = [
            Funciones(id=4582, numero_sala=6, id_pelicula=72588542, horario=4, fecha='04-12-23'),
            Funciones(id=2247, numero_sala=2, id_pelicula=72588542, horario=5, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=72588542, titulo='Frozen', genero='Animación', rating=7.4),
        ]

        pelicula = 'Frozen'
        horario = 4
        expected_nombres = ['Esteban', 'Diego', 'Martina']

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_butacas_altas(gen_personas, gen_peliculas, gen_reservas, gen_funciones,
                                        pelicula, horario)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_nombres)

    def test_2(self):
        """
        Varias funciones en el horario, pero de distintas peliculas
        """
        personas = [
            Personas(id=825469, nombre='Elena', genero='Masculino', edad=14),
            Personas(id=691734, nombre='Raúl', genero='No binario', edad=9),
            Personas(id=543254, nombre='Teresa', genero='Femenino', edad=65),
            Personas(id=895642, nombre='Isabel', genero='Femenino', edad=36),
            Personas(id=962734, nombre='Renata', genero='Masculino', edad=97),
            Personas(id=244869, nombre='Matias', genero='Masculino', edad=23),
            Personas(id=312497, nombre='Valentina', genero='Femenino', edad=69),
            Personas(id=278561, nombre='Hernán', genero='Masculino', edad=38),
            Personas(id=824156, nombre='Gabriel', genero='Femenino', edad=33),
            Personas(id=248765, nombre='Lucas', genero='Masculino', edad=45),
        ]
        reservas = [
            Reservas(id_persona=543254, id_funcion=2247, numero_butaca='E8'),
            Reservas(id_persona=962734, id_funcion=2247, numero_butaca='H1'),
            Reservas(id_persona=248765, id_funcion=7617, numero_butaca='H3'),
            Reservas(id_persona=244869, id_funcion=7617, numero_butaca='G1'),
            Reservas(id_persona=825469, id_funcion=7617, numero_butaca='G7'),
            Reservas(id_persona=895642, id_funcion=7617, numero_butaca='D9'),
            Reservas(id_persona=824156, id_funcion=2247, numero_butaca='B9'),
            Reservas(id_persona=278561, id_funcion=2247, numero_butaca='H6'),
            Reservas(id_persona=312497, id_funcion=7617, numero_butaca='A2'),
            Reservas(id_persona=691734, id_funcion=2247, numero_butaca='D7'),
        ]
        funciones = [
            Funciones(id=2247, numero_sala=2, id_pelicula=20610700, horario=3, fecha='05-12-23'),
            Funciones(id=7617, numero_sala=8, id_pelicula=59848286, horario=3, fecha='04-12-23'),
        ]
        peliculas = [
            Peliculas(id=20610700, titulo='The Princess and the Frog', genero='Animación', rating=7.1),
            Peliculas(id=59848286, titulo='The Silence of the Lambs', genero='Suspense', rating=8.6),
        ]

        pelicula = 'The Silence of the Lambs'
        horario = 3
        expected_nombres = ['Elena', 'Matias', 'Valentina', 'Lucas', 'Isabel']

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_butacas_altas(gen_personas, gen_peliculas, gen_reservas, gen_funciones,
                                        pelicula, horario)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_nombres)

    def test_3(self):
        """
        Varias funciones y peliculas en distintos horarios
        Una persona vio la pelicula más de una vez en el horaio solicitado
        """
        personas = [
            Personas(id=954362, nombre='Isabel', genero='Femenino', edad=86),
            Personas(id=697413, nombre='Andrés', genero='Masculino', edad=56),
            Personas(id=824156, nombre='Gabriel', genero='Femenino', edad=33),
            Personas(id=518367, nombre='Mateo', genero='Femenino', edad=77),
            Personas(id=962734, nombre='Renata', genero='Masculino', edad=97),
            Personas(id=895642, nombre='Isabel', genero='Femenino', edad=36),
            Personas(id=573912, nombre='Carla', genero='Masculino', edad=12),
            Personas(id=317984, nombre='Lucía', genero='Femenino', edad=32),
        ]
        reservas = [
            Reservas(id_persona=954362, id_funcion=8008, numero_butaca='F7'),
            Reservas(id_persona=962734, id_funcion=6237, numero_butaca='E2'),
            Reservas(id_persona=518367, id_funcion=2534, numero_butaca='B6'),
            Reservas(id_persona=962734, id_funcion=3592, numero_butaca='C2'),
            Reservas(id_persona=895642, id_funcion=8008, numero_butaca='E1'),
            Reservas(id_persona=518367, id_funcion=5220, numero_butaca='F9'),
            Reservas(id_persona=962734, id_funcion=2534, numero_butaca='A2'),
            Reservas(id_persona=697413, id_funcion=2221, numero_butaca='G2'),
            Reservas(id_persona=518367, id_funcion=6237, numero_butaca='H5'),
            Reservas(id_persona=697413, id_funcion=6237, numero_butaca='A7'),
            Reservas(id_persona=697413, id_funcion=4293, numero_butaca='E8'),
        ]
        funciones = [
            Funciones(id=6566, numero_sala=1, id_pelicula=87114047, horario=4, fecha='04-12-23'),
            Funciones(id=6237, numero_sala=1, id_pelicula=87114047, horario=1, fecha='01-12-23'),
            Funciones(id=2534, numero_sala=3, id_pelicula=87114047, horario=6, fecha='03-12-23'),
            Funciones(id=8008, numero_sala=6, id_pelicula=78376301, horario=6, fecha='01-12-23'),
            Funciones(id=9524, numero_sala=5, id_pelicula=62863901, horario=2, fecha='01-12-23'),
            Funciones(id=2221, numero_sala=4, id_pelicula=87114047, horario=1, fecha='04-12-23'),
            Funciones(id=2247, numero_sala=2, id_pelicula=62863901, horario=4, fecha='05-12-23'),
            Funciones(id=5220, numero_sala=5, id_pelicula=62863901, horario=4, fecha='03-12-23'),
            Funciones(id=3592, numero_sala=6, id_pelicula=87114047, horario=2, fecha='02-12-23'),
            Funciones(id=4293, numero_sala=7, id_pelicula=62863901, horario=4, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=78376301, titulo='Smart House', genero='Ciencia Ficción', rating=6.2),
            Peliculas(id=62863901, titulo='The Prestige', genero='Superhéroes', rating=8.6),
            Peliculas(id=83829256, titulo='Stuck in the Suburbs', genero='Comedia', rating=6.2),
            Peliculas(id=49034902, titulo='The Godfather', genero='Crimen', rating=9.2),
            Peliculas(id=87114047, titulo='Jump In!', genero='Deportes', rating=5.4),
        ]

        pelicula = 'Jump In!'
        horario = 1
        expected_nombres = ['Andrés', 'Mateo', 'Renata']

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_butacas_altas(gen_personas, gen_peliculas, gen_reservas, gen_funciones,
                                        pelicula, horario)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_nombres)

    def test_4(self):
        """
        Varias funciones y peliculas en distintos horarios
        Algunas personas vieron la pelicula más de una vez, pero en distintos horarios
        """
        personas = [
            Personas(id=763215, nombre='Carmen', genero='Femenino', edad=91),
            Personas(id=518367, nombre='Mateo', genero='Femenino', edad=77),
            Personas(id=697413, nombre='Andrés', genero='Masculino', edad=56),
            Personas(id=437219, nombre='Carlos', genero='Masculino', edad=71),
            Personas(id=621438, nombre='Sofía', genero='No binario', edad=14),
            Personas(id=983156, nombre='Valeria', genero='Femenino', edad=39),
            Personas(id=721584, nombre='Leonardo', genero='Masculino', edad=58),
            Personas(id=542978, nombre='Isabella', genero='Masculino', edad=25),
            Personas(id=126734, nombre='Juampi', genero='Masculino', edad=24),
        ]
        reservas = [
            Reservas(id_persona=983156, id_funcion=1131, numero_butaca='D10'),
            Reservas(id_persona=697413, id_funcion=7777, numero_butaca='C2'),
            Reservas(id_persona=763215, id_funcion=1131, numero_butaca='G6'),
            Reservas(id_persona=437219, id_funcion=1131, numero_butaca='G4'),
            Reservas(id_persona=621438, id_funcion=1131, numero_butaca='H8'),
            Reservas(id_persona=126734, id_funcion=7777, numero_butaca='G10'),
            Reservas(id_persona=621438, id_funcion=9391, numero_butaca='E3'),
            Reservas(id_persona=983156, id_funcion=9391, numero_butaca='F1'),
            Reservas(id_persona=763215, id_funcion=9584, numero_butaca='H3'),
            Reservas(id_persona=697413, id_funcion=1131, numero_butaca='H6'),
            Reservas(id_persona=763215, id_funcion=9391, numero_butaca='H10'),
            Reservas(id_persona=763215, id_funcion=7777, numero_butaca='F8'),
            Reservas(id_persona=721584, id_funcion=9584, numero_butaca='C5'),
            Reservas(id_persona=983156, id_funcion=7777, numero_butaca='F10'),
            Reservas(id_persona=126734, id_funcion=1131, numero_butaca='F2'),
            Reservas(id_persona=518367, id_funcion=9584, numero_butaca='D7'),
            Reservas(id_persona=983156, id_funcion=9584, numero_butaca='C7'),
            Reservas(id_persona=621438, id_funcion=7777, numero_butaca='A4'),
            Reservas(id_persona=697413, id_funcion=9391, numero_butaca='E9'),
        ]
        funciones = [
            Funciones(id=9584, numero_sala=3, id_pelicula=87210469, horario=3, fecha='05-12-23'),
            Funciones(id=9391, numero_sala=1, id_pelicula=11568343, horario=5, fecha='05-12-23'),
            Funciones(id=1131, numero_sala=4, id_pelicula=11568343, horario=6, fecha='04-12-23'),
            Funciones(id=7777, numero_sala=6, id_pelicula=87210469, horario=5, fecha='05-12-23'),
        ]
        peliculas = [
            Peliculas(id=87210469, titulo='Doctor Strange', genero='Superhéroes', rating=7.3),
            Peliculas(id=11568343, titulo='The Social Network', genero='Drama', rating=7.7),
        ]

        pelicula = 'Doctor Strange'
        horario = 5
        expected_nombres = ['Carmen', 'Andrés', 'Sofía', 'Valeria', 'Juampi']

        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = nombres_butacas_altas(gen_personas, gen_peliculas, gen_reservas, gen_funciones,
                                        pelicula, horario)
        self.assertIsInstance(result, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(result), expected_nombres)

if __name__ == '__main__':
    unittest.main(verbosity=2)