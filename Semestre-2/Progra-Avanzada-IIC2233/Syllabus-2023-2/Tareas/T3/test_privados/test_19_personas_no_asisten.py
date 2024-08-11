import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import personas_no_asisten
from utilidades import Personas, Funciones, Reservas
from typing import Generator


class TestPersonasNoAsisten(unittest.TestCase):

    def test_0(self):
        """
        Cada persona hace a lo más una reserva
        """
        personas = [
            Personas(id=737153, nombre='Luis', genero='Masculino', edad=84),
            Personas(id=596318, nombre='Martín', genero='Masculino', edad=81),
            Personas(id=463919, nombre='Juampi', genero='Masculino', edad=24),
            Personas(id=240871, nombre='Martina', genero='Femenino', edad=36),
            Personas(id=372615, nombre='Jimena', genero='Masculino', edad=72),
            Personas(id=404091, nombre='Elena', genero='Femenino', edad=39),
            Personas(id=356133, nombre='Carmen', genero='Femenino', edad=17),
            Personas(id=312497, nombre='Valentina', genero='Femenino', edad=69),
            Personas(id=957719, nombre='Felipe', genero='No binario', edad=19),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=80),
        ]
        reservas = [
            Reservas(id_persona=404091, id_funcion=9721, numero_butaca='G9'),
            Reservas(id_persona=240871, id_funcion=7617, numero_butaca='B1'),
            Reservas(id_persona=596318, id_funcion=7617, numero_butaca='D1'),
            Reservas(id_persona=372615, id_funcion=7617, numero_butaca='G7'),
            Reservas(id_persona=312497, id_funcion=4293, numero_butaca='B7'),
            Reservas(id_persona=356133, id_funcion=9721, numero_butaca='E6'),
            Reservas(id_persona=951827, id_funcion=6237, numero_butaca='C5'),
            Reservas(id_persona=463919, id_funcion=4293, numero_butaca='A3'),
        ]
        funciones = [
            Funciones(id=4283, numero_sala=7, id_pelicula=23101123, horario=2, fecha='03-09-22'),
            Funciones(id=9761, numero_sala=2, id_pelicula=16908968, horario=5, fecha='01-09-22'),
            Funciones(id=4293, numero_sala=6, id_pelicula=16412480, horario=3, fecha='03-09-22'),
            Funciones(id=6237, numero_sala=8, id_pelicula=19177277, horario=5, fecha='02-09-22'),
            Funciones(id=7617, numero_sala=5, id_pelicula=62764502, horario=4, fecha='03-09-22'),
            Funciones(id=7117, numero_sala=7, id_pelicula=32568878, horario=1, fecha='02-09-22'),
            Funciones(id=7517, numero_sala=6, id_pelicula=11615401, horario=5, fecha='05-09-22'),
            Funciones(id=9721, numero_sala=6, id_pelicula=16412480, horario=6, fecha='01-09-22'),
        ]

        expected_personas = [
            Personas(id=404091, nombre='Elena', genero='Femenino', edad=39),
            Personas(id=356133, nombre='Carmen', genero='Femenino', edad=17),
            Personas(id=737153, nombre='Luis', genero='Masculino', edad=84),
            Personas(id=957719, nombre='Felipe', genero='No binario', edad=19),
        ]
        fecha_inicio = "02-09-2022"
        fecha_termino = "03-09-2022"

        gen_personas = (p for p in personas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        resultado = personas_no_asisten(gen_personas, gen_reservas, gen_funciones, fecha_inicio,
                                        fecha_termino)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_personas)

    def test_1(self):
        """
        Una persona hace reservas dentro y fuera del rango de fechas
        """
        personas = [
            Personas(id=900504, nombre='Isidora', genero='Femenino', edad=65),
            Personas(id=750958, nombre='Adriana', genero='Femenino', edad=60),
            Personas(id=926342, nombre='Magdalena', genero='Femenino', edad=67),
            Personas(id=606728, nombre='Alex', genero='Masculino', edad=42),
            Personas(id=132093, nombre='Isidora', genero='Femenino', edad=40),
        ]
        reservas = [
            Reservas(id_persona=926342, id_funcion=4823, numero_butaca='H10'),
            Reservas(id_persona=900504, id_funcion=4736, numero_butaca='C7'),
            Reservas(id_persona=900504, id_funcion=5517, numero_butaca='D5'),
            Reservas(id_persona=926342, id_funcion=4736, numero_butaca='A2'),
            Reservas(id_persona=606728, id_funcion=5181, numero_butaca='E5'),
        ]
        funciones = [
            Funciones(id=5181, numero_sala=6, id_pelicula=16412480, horario=3, fecha='01-06-21'),
            Funciones(id=5517, numero_sala=3, id_pelicula=84580833, horario=5, fecha='02-06-21'),
            Funciones(id=4736, numero_sala=4, id_pelicula=28527704, horario=2, fecha='07-06-21'),
            Funciones(id=4823, numero_sala=2, id_pelicula=34304754, horario=3, fecha='05-06-21'),
        ]
        expected_personas = [
            Personas(id=900504, nombre='Isidora', genero='Femenino', edad=65),
            Personas(id=750958, nombre='Adriana', genero='Femenino', edad=60),
            Personas(id=606728, nombre='Alex', genero='Masculino', edad=42),
            Personas(id=132093, nombre='Isidora', genero='Femenino', edad=40),
        ]
        fecha_inicio = "03-06-2021"
        fecha_termino = "05-06-2021"

        gen_personas = (p for p in personas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        resultado = personas_no_asisten(gen_personas, gen_reservas, gen_funciones, fecha_inicio,
                                        fecha_termino)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_personas)

    def test_2(self):
        """
        Varias personas hacen multiples reservas
        """
        personas = [
            Personas(id=962734, nombre='Renata', genero='Masculino', edad=57),
            Personas(id=896748, nombre='Valentina', genero='Femenino', edad=55),
            Personas(id=596318, nombre='Martín', genero='Masculino', edad=81),
            Personas(id=903952, nombre='Isabel', genero='Femenino', edad=40),
            Personas(id=113860, nombre='Andrés', genero='Femenino', edad=43),
            Personas(id=903104, nombre='Daniel', genero='Masculino', edad=50),
        ]
        reservas = [
            Reservas(id_persona=903104, id_funcion=8579, numero_butaca='H1'),
            Reservas(id_persona=903952, id_funcion=2515, numero_butaca='H6'),
            Reservas(id_persona=903104, id_funcion=9505, numero_butaca='H5'),
            Reservas(id_persona=596318, id_funcion=9505, numero_butaca='E9'),
            Reservas(id_persona=896748, id_funcion=4211, numero_butaca='C2'),
            Reservas(id_persona=596318, id_funcion=2515, numero_butaca='E6'),
            Reservas(id_persona=962734, id_funcion=2515, numero_butaca='E1'),
            Reservas(id_persona=903952, id_funcion=4211, numero_butaca='B6'),
        ]
        funciones = [
            Funciones(id=9505, numero_sala=4, id_pelicula=75985837, horario=4, fecha='15-10-11'),
            Funciones(id=8579, numero_sala=1, id_pelicula=85303162, horario=4, fecha='27-10-11'),
            Funciones(id=2515, numero_sala=3, id_pelicula=41243961, horario=6, fecha='21-10-11'),
            Funciones(id=4211, numero_sala=1, id_pelicula=35528845, horario=3, fecha='17-10-11'),
            Funciones(id=8386, numero_sala=7, id_pelicula=23101123, horario=7, fecha='06-08-11'),
        ]
        expected_personas = [
            Personas(id=113860, nombre='Andrés', genero='Femenino', edad=43),
            Personas(id=903104, nombre='Daniel', genero='Masculino', edad=50),
        ]
        fecha_inicio = "17-10-2011"
        fecha_termino = "22-10-2011"

        gen_personas = (p for p in personas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        resultado = personas_no_asisten(gen_personas, gen_reservas, gen_funciones, fecha_inicio,
                                        fecha_termino)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_personas)

    def test_3(self):
        """
        Rango amplio de fechas, siglo 20 y 21
        """
        personas = [
            Personas(id=287565, nombre='Valeria', genero='Femenino', edad=39),
            Personas(id=903104, nombre='Pablo', genero='Femenino', edad=50),
            Personas(id=149872, nombre='Tomás', genero='Masculino', edad=61),
            Personas(id=737153, nombre='Luis', genero='Masculino', edad=84),
            Personas(id=824156, nombre='Gabriel', genero='Femenino', edad=33),
            Personas(id=278561, nombre='Hernán', genero='Masculino', edad=38),
            Personas(id=463919, nombre='Juampi', genero='Masculino', edad=24),
            Personas(id=687423, nombre='Victoria', genero='Masculino', edad=49),
            Personas(id=926342, nombre='Magdalena', genero='Femenino', edad=67),
            Personas(id=419725, nombre='Antonio', genero='Femenino', edad=10),
            Personas(id=697413, nombre='Andrés', genero='Masculino', edad=56),
            Personas(id=252837, nombre='Alex', genero='No binario', edad=15),
        ]
        reservas = [
            Reservas(id_persona=287565, id_funcion=7015, numero_butaca='H9'),
            Reservas(id_persona=903104, id_funcion=1331, numero_butaca='E2'),
            Reservas(id_persona=149872, id_funcion=7617, numero_butaca='E1'),
            Reservas(id_persona=737153, id_funcion=3566, numero_butaca='A8'),
            Reservas(id_persona=824156, id_funcion=4252, numero_butaca='D8'),
            Reservas(id_persona=278561, id_funcion=4736, numero_butaca='F8'),
            Reservas(id_persona=463919, id_funcion=5408, numero_butaca='C6'),
            Reservas(id_persona=687423, id_funcion=2548, numero_butaca='B1'),
            Reservas(id_persona=926342, id_funcion=5517, numero_butaca='B7'),
            Reservas(id_persona=419725, id_funcion=4211, numero_butaca='D5'),
            Reservas(id_persona=697413, id_funcion=7777, numero_butaca='B9'),
            Reservas(id_persona=252837, id_funcion=1131, numero_butaca='B3'),
        ]
        funciones = [
            Funciones(id=7015, numero_sala=7, id_pelicula=19257655, horario=6, fecha='28-11-97'),
            Funciones(id=1331, numero_sala=5, id_pelicula=56436564, horario=5, fecha='28-05-09'),
            Funciones(id=7617, numero_sala=8, id_pelicula=19173455, horario=2, fecha='04-03-11'),
            Funciones(id=3566, numero_sala=4, id_pelicula=75901837, horario=4, fecha='28-04-11'),
            Funciones(id=4252, numero_sala=1, id_pelicula=35553845, horario=6, fecha='25-06-11'),
            Funciones(id=4736, numero_sala=4, id_pelicula=28365704, horario=2, fecha='05-09-11'),
            Funciones(id=5408, numero_sala=2, id_pelicula=62568755, horario=2, fecha='24-07-15'),
            Funciones(id=2548, numero_sala=7, id_pelicula=74537553, horario=3, fecha='04-02-19'),
            Funciones(id=5517, numero_sala=3, id_pelicula=84580533, horario=5, fecha='25-09-19'),
            Funciones(id=4211, numero_sala=1, id_pelicula=35560945, horario=3, fecha='20-10-19'),
            Funciones(id=7777, numero_sala=6, id_pelicula=11634501, horario=5, fecha='05-12-19'),
            Funciones(id=1131, numero_sala=4, id_pelicula=57967306, horario=6, fecha='11-10-22'),
        ]
        expected_personas = [
            Personas(id=287565, nombre='Valeria', genero='Femenino', edad=39),
            Personas(id=903104, nombre='Pablo', genero='Femenino', edad=50),
            Personas(id=149872, nombre='Tomás', genero='Masculino', edad=61),
            Personas(id=737153, nombre='Luis', genero='Masculino', edad=84),
            Personas(id=697413, nombre='Andrés', genero='Masculino', edad=56),
            Personas(id=252837, nombre='Alex', genero='No binario', edad=15),
        ]
        fecha_inicio = "25-06-2011"
        fecha_termino = "20-10-2019"

        gen_personas = (p for p in personas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        resultado = personas_no_asisten(gen_personas, gen_reservas, gen_funciones, fecha_inicio,
                                        fecha_termino)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_personas)

    def test_4(self):
        """
        Fechas siglo 20
        """
        personas = [
            Personas(id=315403, nombre='Juana', genero='Femenino', edad=23),
            Personas(id=750958, nombre='Isabel', genero='Femenino', edad=86),
            Personas(id=721584, nombre='Leonardo', genero='Masculino', edad=58),
            Personas(id=836197, nombre='Camila', genero='Femenino', edad=23),
            Personas(id=278561, nombre='Gabriel', genero='Masculino', edad=38),
            Personas(id=315896, nombre='Antonio', genero='Femenino', edad=10),
        ]
        reservas = [
            Reservas(id_persona=750958, id_funcion=4638, numero_butaca='F1'),
            Reservas(id_persona=315896, id_funcion=4718, numero_butaca='B3'),
            Reservas(id_persona=836197, id_funcion=1741, numero_butaca='C1'),
            Reservas(id_persona=836197, id_funcion=3670, numero_butaca='D10'),
            Reservas(id_persona=750958, id_funcion=6382, numero_butaca='G1'),
            Reservas(id_persona=315403, id_funcion=4638, numero_butaca='C8'),
            Reservas(id_persona=315896, id_funcion=1741, numero_butaca='B4'),
            Reservas(id_persona=721584, id_funcion=4718, numero_butaca='D8'),
        ]
        funciones = [
            Funciones(id=1741, numero_sala=4, id_pelicula=57395306, horario=6, fecha='15-01-85'),
            Funciones(id=8008, numero_sala=5, id_pelicula=16412480, horario=6, fecha='05-05-88'),
            Funciones(id=4718, numero_sala=9, id_pelicula=32152163, horario=2, fecha='06-10-88'),
            Funciones(id=4638, numero_sala=5, id_pelicula=90803337, horario=3, fecha='27-06-88'),
            Funciones(id=3670, numero_sala=2, id_pelicula=32568878, horario=2, fecha='17-06-88'),
            Funciones(id=6382, numero_sala=1, id_pelicula=84580833, horario=2, fecha='23-09-90'),
        ]
        expected_personas = [
            Personas(id=836197, nombre='Camila', genero='Femenino', edad=23),
            Personas(id=278561, nombre='Gabriel', genero='Masculino', edad=38),
        ]
        fecha_inicio = "20-06-1988"
        fecha_termino = "01-11-1988"

        gen_personas = (p for p in personas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        resultado = personas_no_asisten(gen_personas, gen_reservas, gen_funciones, fecha_inicio,
                                        fecha_termino)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_personas)

    def test_5(self):
        """
        Rango de fechas desde el siglo 20 al 21
        """
        personas = [
            Personas(id=983156, nombre='Hernán', genero='Masculino', edad=39),
            Personas(id=903104, nombre='Pablo', genero='Femenino', edad=50),
            Personas(id=149872, nombre='Pietro', genero='Masculino', edad=61),
            Personas(id=737153, nombre='Luis', genero='No binario', edad=84),
            Personas(id=824156, nombre='Gabriel', genero='Femenino', edad=33),
            Personas(id=278561, nombre='Hernán', genero='Masculino', edad=38),
            Personas(id=463919, nombre='Juampi', genero='Masculino', edad=24),
            Personas(id=687423, nombre='Victoria', genero='Masculino', edad=49),
            Personas(id=926342, nombre='Magdalena', genero='Femenino', edad=67),
            Personas(id=419725, nombre='Antonio', genero='Femenino', edad=10),
            Personas(id=697413, nombre='Andrés', genero='Masculino', edad=56),
            Personas(id=781245, nombre='Leonardo', genero='Femenino', edad=15),
        ]
        reservas = [
            Reservas(id_persona=983156, id_funcion=7015, numero_butaca='H9'),
            Reservas(id_persona=903104, id_funcion=1331, numero_butaca='E3'),
            Reservas(id_persona=149872, id_funcion=7617, numero_butaca='E2'),
            Reservas(id_persona=824156, id_funcion=4252, numero_butaca='D8'),
            Reservas(id_persona=278561, id_funcion=4736, numero_butaca='F8'),
            Reservas(id_persona=463919, id_funcion=5408, numero_butaca='C6'),
            Reservas(id_persona=781245, id_funcion=1131, numero_butaca='B3'),
            Reservas(id_persona=737153, id_funcion=3566, numero_butaca='A7'),
            Reservas(id_persona=419725, id_funcion=4211, numero_butaca='D5'),
            Reservas(id_persona=926342, id_funcion=5517, numero_butaca='B7'),
            Reservas(id_persona=687423, id_funcion=2548, numero_butaca='B1'),
            Reservas(id_persona=697413, id_funcion=7777, numero_butaca='A9'),
        ]
        funciones = [
            Funciones(id=7015, numero_sala=7, id_pelicula=70752273, horario=6, fecha='28-11-83'),
            Funciones(id=1331, numero_sala=5, id_pelicula=75759551, horario=5, fecha='28-05-85'),
            Funciones(id=7617, numero_sala=8, id_pelicula=19177277, horario=2, fecha='04-03-96'),
            Funciones(id=3566, numero_sala=4, id_pelicula=75901837, horario=4, fecha='28-04-96'),
            Funciones(id=4252, numero_sala=1, id_pelicula=35569845, horario=6, fecha='25-06-96'),
            Funciones(id=4736, numero_sala=4, id_pelicula=28527704, horario=2, fecha='05-09-96'),
            Funciones(id=5408, numero_sala=2, id_pelicula=16908968, horario=2, fecha='24-07-98'),
            Funciones(id=2548, numero_sala=7, id_pelicula=70752273, horario=3, fecha='04-02-08'),
            Funciones(id=5517, numero_sala=3, id_pelicula=84580833, horario=5, fecha='25-09-08'),
            Funciones(id=4211, numero_sala=1, id_pelicula=35569845, horario=3, fecha='20-10-08'),
            Funciones(id=7777, numero_sala=6, id_pelicula=11615401, horario=5, fecha='05-12-08'),
            Funciones(id=1131, numero_sala=4, id_pelicula=57395306, horario=6, fecha='11-10-10'),
        ]
        expected_personas = [
            Personas(id=983156, nombre='Hernán', genero='Masculino', edad=39),
            Personas(id=903104, nombre='Pablo', genero='Femenino', edad=50),
            Personas(id=149872, nombre='Pietro', genero='Masculino', edad=61),
            Personas(id=737153, nombre='Luis', genero='No binario', edad=84),
            Personas(id=697413, nombre='Andrés', genero='Masculino', edad=56),
            Personas(id=781245, nombre='Leonardo', genero='Femenino', edad=15),
        ]
        fecha_inicio = "25-06-1996"
        fecha_termino = "20-10-2008"

        gen_personas = (p for p in personas)
        gen_reservas = (r for r in reservas)
        gen_funciones = (f for f in funciones)
        resultado = personas_no_asisten(gen_personas, gen_reservas, gen_funciones, fecha_inicio,
                                        fecha_termino)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_personas)


if __name__ == '__main__':
    unittest.main(verbosity=2)
