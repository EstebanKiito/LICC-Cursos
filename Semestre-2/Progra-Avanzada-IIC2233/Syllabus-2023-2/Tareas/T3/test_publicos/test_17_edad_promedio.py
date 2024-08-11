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
        Promedio 55 exacto
        """
        personas = [
            Personas(id=367591, nombre='Rodrigo', genero='No binario', edad=80),
            Personas(id=725930, nombre='Adela', genero='Femenino', edad=34),
            Personas(id=763215, nombre='Carmen', genero='Femenino', edad=91),
            Personas(id=598127, nombre='Valentina', genero='Masculino', edad=55),
            Personas(id=765653, nombre='Arturo', genero='Masculino', edad=43),
            Personas(id=429186, nombre='Paula', genero='Masculino', edad=88),
        ]
        reservas = [
            Reservas(id_persona=725930, id_funcion=7617, numero_butaca='F3'),
            Reservas(id_persona=598127, id_funcion=4661, numero_butaca='E9'),
            Reservas(id_persona=598127, id_funcion=7617, numero_butaca='A5'),
            Reservas(id_persona=765653, id_funcion=7617, numero_butaca='H1'),
            Reservas(id_persona=765653, id_funcion=4661, numero_butaca='D5'),
            Reservas(id_persona=765653, id_funcion=1741, numero_butaca='B6'),
            Reservas(id_persona=429186, id_funcion=7617, numero_butaca='H10'),
            Reservas(id_persona=429186, id_funcion=1741, numero_butaca='G9'),
        ]
        funciones = [
            Funciones(id=7617, numero_sala=8, id_pelicula=58329437, horario=2, fecha='04-12-23'),
            Funciones(id=1741, numero_sala=4, id_pelicula=95417284, horario=3, fecha='01-12-23'),
            Funciones(id=4661, numero_sala=4, id_pelicula=71903918, horario=5, fecha='03-12-23'),
        ]
        peliculas = [
            Peliculas(id=58329437, titulo='My Neighbor Totoro', genero='Animación', rating=8.6),
            Peliculas(id=95417284, titulo='Camp Rock', genero='Musical', rating=5.1),
            Peliculas(id=71903918, titulo='Shrek', genero='Animación', rating=7.8),
        ]

        id_funcion = 7617
        titulo = 'My Neighbor Totoro'
        promedio = 55
        
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
        Promedio 16.3333 aproximado a 17
        """
        personas = [
            Personas(id=962734, nombre='Renata', genero='Masculino', edad=97),
            Personas(id=836197, nombre='Julia', genero='No binario', edad=23),
            Personas(id=529874, nombre='Pedro', genero='Masculino', edad=12),
            Personas(id=126734, nombre='Juampi', genero='Masculino', edad=24),
            Personas(id=376581, nombre='José', genero='Femenino', edad=13),
        ]
        reservas = [
            Reservas(id_persona=962734, id_funcion=9584, numero_butaca='E8'),
            Reservas(id_persona=836197, id_funcion=9584, numero_butaca='E9'),
            Reservas(id_persona=529874, id_funcion=9524, numero_butaca='G2'),
            Reservas(id_persona=529874, id_funcion=9584, numero_butaca='B5'),
            Reservas(id_persona=126734, id_funcion=9524, numero_butaca='A5'),
            Reservas(id_persona=376581, id_funcion=9524, numero_butaca='F10'),
            Reservas(id_persona=376581, id_funcion=9584, numero_butaca='H6'),
        ]
        funciones = [
            Funciones(id=9584, numero_sala=3, id_pelicula=76004798, horario=3, fecha='05-12-23'),
            Funciones(id=9524, numero_sala=5, id_pelicula=41068976, horario=2, fecha='01-12-23'),
        ]
        peliculas = [
            Peliculas(id=76004798, titulo='Incredibles', genero='Animación', rating=8.0),
            Peliculas(id=41068976, titulo='Cinderella', genero='Animación', rating=7.1),
        ]

        id_funcion = 9524
        titulo = 'Cinderella'
        promedio = 17
        
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
        Promedio 41.6 aproximado a 42
        """
        personas = [
            Personas(id=697413, nombre='Andrés', genero='Masculino', edad=56),
            Personas(id=245769, nombre='Natalia', genero='Femenino', edad=17),
            Personas(id=745219, nombre='Camila', genero='Masculino', edad=17),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=80),
            Personas(id=428362, nombre='Emma', genero='Masculino', edad=45),
            Personas(id=317984, nombre='Lucía', genero='Femenino', edad=32),
            Personas(id=852647, nombre='Santiago', genero='Femenino', edad=25),
            Personas(id=244869, nombre='Matias', genero='Masculino', edad=23),
            Personas(id=463518, nombre='Esteban', genero='Femenino', edad=58),
            Personas(id=419725, nombre='Antonio', genero='Femenino', edad=10),
        ]
        reservas = [
            Reservas(id_persona=951827, id_funcion=5408, numero_butaca='C6'),
            Reservas(id_persona=317984, id_funcion=5408, numero_butaca='A7'),
            Reservas(id_persona=697413, id_funcion=5408, numero_butaca='E3'),
            Reservas(id_persona=428362, id_funcion=4823, numero_butaca='F10'),
            Reservas(id_persona=244869, id_funcion=5408, numero_butaca='C10'),
            Reservas(id_persona=951827, id_funcion=4823, numero_butaca='G9'),
            Reservas(id_persona=697413, id_funcion=4823, numero_butaca='C5'),
            Reservas(id_persona=245769, id_funcion=5408, numero_butaca='C9'),
        ]
        funciones = [
            Funciones(id=5408, numero_sala=2, id_pelicula=78376301, horario=2, fecha='03-12-23'),
            Funciones(id=4823, numero_sala=2, id_pelicula=78376301, horario=3, fecha='04-12-23'),
        ]
        peliculas = [
            Peliculas(id=78376301, titulo='Smart House', genero='Ciencia Ficción', rating=6.2),
        ]

        id_funcion = 5408
        titulo = 'Smart House'
        promedio = 42
        
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
        Promedio 53.75 aproximado a 54
        """
        personas = [
            Personas(id=126734, nombre='Juampi', genero='Masculino', edad=24),
            Personas(id=596318, nombre='Martín', genero='Masculino', edad=81),
            Personas(id=691734, nombre='Raúl', genero='No binario', edad=9),
            Personas(id=367591, nombre='Rodrigo', genero='No binario', edad=80),
            Personas(id=543254, nombre='Teresa', genero='Femenino', edad=65),
            Personas(id=725930, nombre='Adela', genero='Femenino', edad=34),
            Personas(id=352429, nombre='Jorge', genero='Masculino', edad=45),
            Personas(id=852647, nombre='Santiago', genero='Femenino', edad=25),
            Personas(id=654365, nombre='Isidora', genero='Femenino', edad=54),
            Personas(id=529874, nombre='Pedro', genero='Masculino', edad=12),
        ]
        reservas = [
            Reservas(id_persona=596318, id_funcion=4678, numero_butaca='H7'),
            Reservas(id_persona=691734, id_funcion=4678, numero_butaca='F9'),
            Reservas(id_persona=367591, id_funcion=4678, numero_butaca='A1'),
            Reservas(id_persona=352429, id_funcion=4678, numero_butaca='B9'),
        ]
        funciones = [
            Funciones(id=4678, numero_sala=2, id_pelicula=11164686, horario=6, fecha='02-12-23'),
        ]
        peliculas = [
            Peliculas(id=11164686, titulo='Interstellar', genero='Ciencia Ficción', rating=8.6),
        ]

        id_funcion = 4678
        titulo = 'Interstellar'
        promedio = 54
        
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
        Promedio 48 exacto
        """
        personas = [
            Personas(id=245769, nombre='Natalia', genero='Femenino', edad=17),
            Personas(id=278561, nombre='Hernán', genero='Masculino', edad=38),
            Personas(id=721584, nombre='Leonardo', genero='Masculino', edad=58),
        ]
        reservas = [
            Reservas(id_persona=278561, id_funcion=4823, numero_butaca='D5'),
            Reservas(id_persona=278561, id_funcion=2247, numero_butaca='F8'),
            Reservas(id_persona=245769, id_funcion=7735, numero_butaca='A2'),
            Reservas(id_persona=721584, id_funcion=2247, numero_butaca='F3'),
            Reservas(id_persona=721584, id_funcion=9391, numero_butaca='F9'),
            Reservas(id_persona=721584, id_funcion=4561, numero_butaca='B1'),
            Reservas(id_persona=721584, id_funcion=1131, numero_butaca='B9'),
            Reservas(id_persona=721584, id_funcion=7735, numero_butaca='A4'),
            Reservas(id_persona=245769, id_funcion=9391, numero_butaca='H2'),
            Reservas(id_persona=278561, id_funcion=7666, numero_butaca='E10'),
            Reservas(id_persona=721584, id_funcion=3566, numero_butaca='C7'),
            Reservas(id_persona=278561, id_funcion=6382, numero_butaca='E8'),
            Reservas(id_persona=721584, id_funcion=2534, numero_butaca='F7'),
            Reservas(id_persona=278561, id_funcion=2534, numero_butaca='H3'),
            Reservas(id_persona=278561, id_funcion=1131, numero_butaca='A3'),
            Reservas(id_persona=721584, id_funcion=4823, numero_butaca='E6'),
            Reservas(id_persona=278561, id_funcion=3566, numero_butaca='G8'),
            Reservas(id_persona=278561, id_funcion=9391, numero_butaca='A8'),
            Reservas(id_persona=278561, id_funcion=4561, numero_butaca='A7'),
            Reservas(id_persona=278561, id_funcion=7735, numero_butaca='D9'),
            Reservas(id_persona=721584, id_funcion=6382, numero_butaca='D10'),
            Reservas(id_persona=721584, id_funcion=7666, numero_butaca='E3'),
        ]
        funciones = [
            Funciones(id=1131, numero_sala=4, id_pelicula=47191880, horario=6, fecha='04-12-23'),
            Funciones(id=4823, numero_sala=2, id_pelicula=42038936, horario=3, fecha='04-12-23'),
            Funciones(id=4561, numero_sala=2, id_pelicula=42038936, horario=5, fecha='01-12-23'),
            Funciones(id=7666, numero_sala=8, id_pelicula=41068976, horario=1, fecha='03-12-23'),
            Funciones(id=2534, numero_sala=3, id_pelicula=42986062, horario=6, fecha='03-12-23'),
            Funciones(id=3566, numero_sala=4, id_pelicula=54541808, horario=4, fecha='02-12-23'),
            Funciones(id=7735, numero_sala=3, id_pelicula=54541808, horario=4, fecha='01-12-23'),
            Funciones(id=9391, numero_sala=1, id_pelicula=42986062, horario=5, fecha='05-12-23'),
            Funciones(id=2247, numero_sala=2, id_pelicula=42038936, horario=4, fecha='05-12-23'),
            Funciones(id=6382, numero_sala=3, id_pelicula=42038936, horario=2, fecha='04-12-23'),
        ]
        peliculas = [
            Peliculas(id=47191880, titulo='Thor', genero='Animación', rating=7.2),
            Peliculas(id=42038936, titulo='The Matrix Revolutions', genero='Fantasía', rating=7.3),
            Peliculas(id=42986062, titulo='The Lord of the Rings', genero='Fantasía', rating=8.7),
            Peliculas(id=54541808, titulo='Matilda', genero='Comedia', rating=6.9),
            Peliculas(id=41068976, titulo='Cinderella', genero='Animación', rating=7.1),
        ]

        id_funcion = 3566
        titulo = 'Matilda'
        promedio = 48
        
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