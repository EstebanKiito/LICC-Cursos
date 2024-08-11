import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import personas_mayores
from utilidades import Personas
from typing import Generator


class TestPersonasMayores(unittest.TestCase):

    def test_0(self):
        """
        Varias personas son mayores a la edad a buscar
        """
        lista_personas = [
            Personas(id=745219, nombre='Camila', genero='Masculino', edad=17),
            Personas(id=429186, nombre='Paula', genero='Masculino', edad=88),
            Personas(id=654365, nombre='Isidora', genero='Femenino', edad=54),
            Personas(id=857474, nombre='Nicolás', genero='Masculino', edad=23),
            Personas(id=765653, nombre='Arturo', genero='Masculino', edad=43),
            Personas(id=312497, nombre='Valentina', genero='Femenino', edad=69),
            Personas(id=573849, nombre='María', genero='Femenino', edad=12),
            Personas(id=529874, nombre='Pedro', genero='Masculino', edad=12),
            Personas(id=278561, nombre='Hernán', genero='Masculino', edad=38),
            Personas(id=697413, nombre='Andrés', genero='Masculino', edad=56),
        ]
        expected_lista_personas = [
            Personas(id=429186, nombre='Paula', genero='Masculino', edad=88),
            Personas(id=654365, nombre='Isidora', genero='Femenino', edad=54),
            Personas(id=312497, nombre='Valentina', genero='Femenino', edad=69),
            Personas(id=697413, nombre='Andrés', genero='Masculino', edad=56),
        ]
        edad_a_buscar = 51

        generador = (p for p in lista_personas)
        resultado = personas_mayores(generador, edad_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_personas)

    def test_1(self):
        """
        Todas las personas son mayores a la edad a buscar
        """
        lista_personas = [
            Personas(id=596318, nombre='Martín', genero='Masculino', edad=81),
            Personas(id=781245, nombre='Alex', genero='No binario', edad=15),
            Personas(id=419725, nombre='Antonio', genero='Femenino', edad=12),
            Personas(id=184926, nombre='Andrea', genero='No binario', edad=47),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=80),
        ]
        expected_lista_personas = [
            Personas(id=596318, nombre='Martín', genero='Masculino', edad=81),
            Personas(id=781245, nombre='Alex', genero='No binario', edad=15),
            Personas(id=419725, nombre='Antonio', genero='Femenino', edad=12),
            Personas(id=184926, nombre='Andrea', genero='No binario', edad=47),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=80),
        ]
        edad_a_buscar = 10

        generador = (p for p in lista_personas)
        resultado = personas_mayores(generador, edad_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_personas)

    def test_2(self):
        """
        Ninguna persona es mayor a la edad a buscar
        """
        lista_personas = [
            Personas(id=926342, nombre='Magdalena', genero='Femenino', edad=67),
            Personas(id=654365, nombre='Isidora', genero='Femenino', edad=54),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=75),
            Personas(id=149872, nombre='Tomás', genero='Masculino', edad=61),
            Personas(id=543254, nombre='Teresa', genero='Femenino', edad=65),
        ]
        expected_lista_personas = []
        edad_a_buscar = 80

        generador = (p for p in lista_personas)
        resultado = personas_mayores(generador, edad_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_personas)

    def test_3(self):
        """
        Persona con edad igual a la edad a buscar
        """
        lista_personas = [
            Personas(id=852647, nombre='Santiago', genero='Femenino', edad=25),
            Personas(id=621438, nombre='Sofía', genero='No binario', edad=14),
            Personas(id=244869, nombre='Matias', genero='Masculino', edad=23),
            Personas(id=598127, nombre='Valentina', genero='Masculino', edad=55),
            Personas(id=372615, nombre='Jimena', genero='Masculino', edad=72),
            Personas(id=763215, nombre='Carmen', genero='Femenino', edad=91),
            Personas(id=534254, nombre='Manuel', genero='No binario', edad=76),
            Personas(id=419725, nombre='Antonio', genero='Femenino', edad=10),
        ]
        expected_lista_personas = [
            Personas(id=372615, nombre='Jimena', genero='Masculino', edad=72),
            Personas(id=763215, nombre='Carmen', genero='Femenino', edad=91),
            Personas(id=534254, nombre='Manuel', genero='No binario', edad=76),
        ]
        edad_a_buscar = 72

        generador = (p for p in lista_personas)
        resultado = personas_mayores(generador, edad_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_personas)

    def test_4(self):
        """
        Personas con el mismo nombre
        """
        lista_personas = [
            Personas(id=184926, nombre='Andrea', genero='No binario', edad=47),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=80),
            Personas(id=824156, nombre='Adriana', genero='Femenino', edad=33),
            Personas(id=946353, nombre='Pietro', genero='Masculino', edad=42),
        ]
        expected_lista_personas = [
            Personas(id=184926, nombre='Andrea', genero='No binario', edad=47),
            Personas(id=951827, nombre='Adriana', genero='Femenino', edad=80),
        ]
        edad_a_buscar = 46

        generador = (p for p in lista_personas)
        resultado = personas_mayores(generador, edad_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_personas)


if __name__ == '__main__':
    unittest.main(verbosity=2)
