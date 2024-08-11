import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import edad_promedio
from utilidades import Personas, Peliculas, Funciones, Reservas


class TestEdadPromedio(unittest.TestCase):

    def test_0(self):
        """
        Promedio 56 exacto
        """
        personas = [
            Personas(id=193453, nombre='José', genero='Femenino', edad=81),
            Personas(id=551792, nombre='Hernán', genero='Masculino', edad=35),
            Personas(id=589077, nombre='Andrés', genero='Femenino', edad=92),
            Personas(id=423989, nombre='Nicolás', genero='Masculino', edad=56),
            Personas(id=591515, nombre='Gabriel', genero='Femenino', edad=44),
            Personas(id=255048, nombre='Manuel', genero='No binario', edad=89),
        ]
        reservas = [
            Reservas(id_persona=551792, id_funcion=4479, numero_butaca='F3'),
            Reservas(id_persona=423989, id_funcion=1523, numero_butaca='E9'),
            Reservas(id_persona=423989, id_funcion=4479, numero_butaca='A5'),
            Reservas(id_persona=591515, id_funcion=4479, numero_butaca='H1'),
            Reservas(id_persona=591515, id_funcion=1523, numero_butaca='D5'),
            Reservas(id_persona=591515, id_funcion=7603, numero_butaca='B6'),
            Reservas(id_persona=255048, id_funcion=4479, numero_butaca='H10'),
            Reservas(id_persona=255048, id_funcion=7603, numero_butaca='G9'),
        ]
        funciones = [
            Funciones(id=4479, numero_sala=2, id_pelicula=246255299, horario=5, fecha='04-12-23'),
            Funciones(id=7603, numero_sala=7, id_pelicula=283343146, horario=6, fecha='01-12-23'),
            Funciones(id=1523, numero_sala=7, id_pelicula=259829780, horario=8, fecha='03-12-23'),
        ]
        peliculas = [
            Peliculas(id=246255299, titulo='Shutter Island', genero='Animación', rating=8.6),
            Peliculas(id=283343146, titulo='The Princess Diaries 2', genero='Musical', rating=5.1),
            Peliculas(id=259829780, titulo='The Pianist', genero='Animación', rating=7.8),
        ]

        id_funcion = 4479
        titulo = 'Shutter Island'
        promedio = 56

        expected_str = "En la función {} de la película {} la edad promedio del público es {}."
        expected_str = expected_str.format(id_funcion, titulo, promedio)
        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = edad_promedio(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_str)

    def test_1(self):
        """
        Promedio 17.3333 aproximado a 18
        """
        personas = [
            Personas(id=788596, nombre='Andrés', genero='Masculino', edad=98),
            Personas(id=662059, nombre='Victoria', genero='Masculino', edad=24),
            Personas(id=355736, nombre='Teresa', genero='Femenino', edad=13),
            Personas(id=852596, nombre='Teresa', genero='Femenino', edad=25),
            Personas(id=202443, nombre='Tomás', genero='Masculino', edad=14),
        ]
        reservas = [
            Reservas(id_persona=788596, id_funcion=6446, numero_butaca='E8'),
            Reservas(id_persona=662059, id_funcion=6446, numero_butaca='E9'),
            Reservas(id_persona=355736, id_funcion=6386, numero_butaca='G2'),
            Reservas(id_persona=355736, id_funcion=6446, numero_butaca='B5'),
            Reservas(id_persona=852596, id_funcion=6386, numero_butaca='A5'),
            Reservas(id_persona=202443, id_funcion=6386, numero_butaca='F10'),
            Reservas(id_persona=202443, id_funcion=6446, numero_butaca='H6'),
        ]
        funciones = [
            Funciones(id=6446, numero_sala=6, id_pelicula=263930660, horario=6, fecha='05-12-23'),
            Funciones(id=6386, numero_sala=8, id_pelicula=228994838, horario=5, fecha='01-12-23'),
        ]
        peliculas = [
            Peliculas(id=263930660, titulo='Captain America: The First Avenger', genero='Animación', rating=8.0),
            Peliculas(id=228994838, titulo='The Lord of the Rings: The Return of the King', genero='Animación', rating=7.1),
        ]

        id_funcion = 6386
        titulo = 'The Lord of the Rings: The Return of the King'
        promedio = 18

        expected_str = "En la función {} de la película {} la edad promedio del público es {}."
        expected_str = expected_str.format(id_funcion, titulo, promedio)
        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = edad_promedio(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_str)

    def test_2(self):
        """
        Promedio 40.6 aproximado a 41
        """
        personas = [
            Personas(id=523275, nombre='Felipe', genero='No binario', edad=55),
            Personas(id=971631, nombre='Pedro', genero='Masculino', edad=16),
            Personas(id=571081, nombre='Teresa', genero='Femenino', edad=16),
            Personas(id=777689, nombre='Alejandro', genero='Femenino', edad=79),
            Personas(id=254224, nombre='Diego', genero='Masculino', edad=44),
            Personas(id=143846, nombre='Juampi', genero='Masculino', edad=31),
            Personas(id=678509, nombre='Rodrigo', genero='No binario', edad=24),
            Personas(id=970731, nombre='Martín', genero='Masculino', edad=22),
            Personas(id=289380, nombre='María', genero='Femenino', edad=57),
            Personas(id=245587, nombre='Teresita', genero='Femenino', edad=9),
        ]
        reservas = [
            Reservas(id_persona=777689, id_funcion=2270, numero_butaca='C6'),
            Reservas(id_persona=143846, id_funcion=2270, numero_butaca='A7'),
            Reservas(id_persona=523275, id_funcion=2270, numero_butaca='E3'),
            Reservas(id_persona=254224, id_funcion=1685, numero_butaca='F10'),
            Reservas(id_persona=970731, id_funcion=2270, numero_butaca='C10'),
            Reservas(id_persona=777689, id_funcion=1685, numero_butaca='G9'),
            Reservas(id_persona=523275, id_funcion=1685, numero_butaca='C5'),
            Reservas(id_persona=971631, id_funcion=2270, numero_butaca='C9'),
        ]
        funciones = [
            Funciones(id=2270, numero_sala=5, id_pelicula=266302163, horario=5, fecha='03-12-23'),
            Funciones(id=1685, numero_sala=5, id_pelicula=266302163, horario=6, fecha='04-12-23'),
        ]
        peliculas = [
            Peliculas(id=266302163, titulo='Moana', genero='Ciencia Ficción', rating=6.2),
        ]

        id_funcion = 2270
        titulo = 'Moana'
        promedio = 41

        expected_str = "En la función {} de la película {} la edad promedio del público es {}."
        expected_str = expected_str.format(id_funcion, titulo, promedio)
        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = edad_promedio(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_str)

    def test_3(self):
        """
        Promedio 52.75 aproximado a 53
        """
        personas = [
            Personas(id=852596, nombre='Teresa', genero='Femenino', edad=23),
            Personas(id=422180, nombre='Luis', genero='Masculino', edad=80),
            Personas(id=517596, nombre='Juampi', genero='Masculino', edad=8),
            Personas(id=193453, nombre='José', genero='Femenino', edad=79),
            Personas(id=369116, nombre='Jimena', genero='Masculino', edad=64),
            Personas(id=551792, nombre='Hernán', genero='Masculino', edad=33),
            Personas(id=178291, nombre='Jorge', genero='Masculino', edad=44),
            Personas(id=678509, nombre='Rodrigo', genero='No binario', edad=24),
            Personas(id=480227, nombre='Hernán', genero='Masculino', edad=53),
            Personas(id=355736, nombre='Teresa', genero='Femenino', edad=11),
        ]
        reservas = [
            Reservas(id_persona=422180, id_funcion=1540, numero_butaca='H7'),
            Reservas(id_persona=517596, id_funcion=1540, numero_butaca='F9'),
            Reservas(id_persona=193453, id_funcion=1540, numero_butaca='A1'),
            Reservas(id_persona=178291, id_funcion=1540, numero_butaca='B9'),
        ]
        funciones = [
            Funciones(id=1540, numero_sala=5, id_pelicula=199090548, horario=9, fecha='02-12-23'),
        ]
        peliculas = [
            Peliculas(id=199090548, titulo='Guardians of the Galaxy', genero='Ciencia Ficción', rating=8.6),
        ]

        id_funcion = 1540
        titulo = 'Guardians of the Galaxy'
        promedio = 53

        expected_str = "En la función {} de la película {} la edad promedio del público es {}."
        expected_str = expected_str.format(id_funcion, titulo, promedio)
        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = edad_promedio(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_str)

    def test_4(self):
        """
        Promedio 47 exacto
        """
        personas = [
            Personas(id=971631, nombre='Pedro', genero='Masculino', edad=16),
            Personas(id=104423, nombre='Tomás', genero='Masculino', edad=37),
            Personas(id=547446, nombre='Andrés', genero='Masculino', edad=57),
        ]
        reservas = [
            Reservas(id_persona=104423, id_funcion=1685, numero_butaca='D5'),
            Reservas(id_persona=104423, id_funcion=8109, numero_butaca='F8'),
            Reservas(id_persona=971631, id_funcion=4597, numero_butaca='A2'),
            Reservas(id_persona=547446, id_funcion=8109, numero_butaca='F3'),
            Reservas(id_persona=547446, id_funcion=6253, numero_butaca='F9'),
            Reservas(id_persona=547446, id_funcion=1423, numero_butaca='B1'),
            Reservas(id_persona=547446, id_funcion=6993, numero_butaca='B9'),
            Reservas(id_persona=547446, id_funcion=4597, numero_butaca='A4'),
            Reservas(id_persona=971631, id_funcion=6253, numero_butaca='H2'),
            Reservas(id_persona=104423, id_funcion=4528, numero_butaca='E10'),
            Reservas(id_persona=547446, id_funcion=9428, numero_butaca='C7'),
            Reservas(id_persona=104423, id_funcion=3244, numero_butaca='E8'),
            Reservas(id_persona=547446, id_funcion=8396, numero_butaca='F7'),
            Reservas(id_persona=104423, id_funcion=8396, numero_butaca='H3'),
            Reservas(id_persona=104423, id_funcion=6993, numero_butaca='A3'),
            Reservas(id_persona=547446, id_funcion=1685, numero_butaca='E6'),
            Reservas(id_persona=104423, id_funcion=9428, numero_butaca='G8'),
            Reservas(id_persona=104423, id_funcion=6253, numero_butaca='A8'),
            Reservas(id_persona=104423, id_funcion=1423, numero_butaca='A7'),
            Reservas(id_persona=104423, id_funcion=4597, numero_butaca='D9'),
            Reservas(id_persona=547446, id_funcion=3244, numero_butaca='D10'),
            Reservas(id_persona=547446, id_funcion=4528, numero_butaca='E3'),
        ]
        funciones = [
            Funciones(id=6993, numero_sala=7, id_pelicula=235117742, horario=9, fecha='04-12-23'),
            Funciones(id=1685, numero_sala=5, id_pelicula=229964798, horario=6, fecha='04-12-23'),
            Funciones(id=1423, numero_sala=5, id_pelicula=229964798, horario=8, fecha='01-12-23'),
            Funciones(id=4528, numero_sala=2, id_pelicula=228994838, horario=4, fecha='03-12-23'),
            Funciones(id=8396, numero_sala=6, id_pelicula=230911924, horario=9, fecha='03-12-23'),
            Funciones(id=9428, numero_sala=7, id_pelicula=242467670, horario=7, fecha='02-12-23'),
            Funciones(id=4597, numero_sala=6, id_pelicula=242467670, horario=7, fecha='01-12-23'),
            Funciones(id=6253, numero_sala=4, id_pelicula=230911924, horario=8, fecha='05-12-23'),
            Funciones(id=8109, numero_sala=5, id_pelicula=229964798, horario=7, fecha='05-12-23'),
            Funciones(id=3244, numero_sala=6, id_pelicula=229964798, horario=5, fecha='04-12-23'),
        ]
        peliculas = [
            Peliculas(id=235117742, titulo='Frozen', genero='Animación', rating=7.2),
            Peliculas(id=229964798, titulo='The Jungle Book', genero='Fantasía', rating=7.3),
            Peliculas(id=230911924, titulo='Doctor Strange', genero='Fantasía', rating=8.7),
            Peliculas(id=242467670, titulo='Avatar', genero='Comedia', rating=6.9),
            Peliculas(id=228994838, titulo='The Lord of the Rings: The Return of the King', genero='Animación', rating=7.1),
        ]

        id_funcion = 9428
        titulo = 'Avatar'
        promedio = 47

        expected_str = "En la función {} de la película {} la edad promedio del público es {}."
        expected_str = expected_str.format(id_funcion, titulo, promedio)
        gen_personas = (p for p in personas)
        gen_peliculas = (p for p in peliculas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        result = edad_promedio(gen_personas, gen_peliculas, gen_reservas, gen_funciones, id_funcion)
        self.assertIsInstance(result, str)
        self.assertEqual(result, expected_str)


if __name__ == '__main__':
    unittest.main(verbosity=2)
