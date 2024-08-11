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
            Personas(id=824156, nombre='Gabriel', genero='Femenino', edad=33),
            Personas(id=781245, nombre='Alex', genero='No binario', edad=15),
            Personas(id=248765, nombre='Lucas', genero='Masculino', edad=45),
            Personas(id=765653, nombre='Arturo', genero='Masculino', edad=43),
            Personas(id=596318, nombre='Martín', genero='Masculino', edad=81),
            Personas(id=352429, nombre='Jorge', genero='Masculino', edad=45),
            Personas(id=534254, nombre='Manuel', genero='No binario', edad=76),
            Personas(id=962734, nombre='Renata', genero='Masculino', edad=97),
            Personas(id=372615, nombre='Jimena', genero='Masculino', edad=72),
            Personas(id=926242, nombre='Martina', genero='Femenino', edad=36),
        ]
        expected_lista_personas = [
            Personas(id=596318, nombre='Martín', genero='Masculino', edad=81),
            Personas(id=534254, nombre='Manuel', genero='No binario', edad=76),
            Personas(id=962734, nombre='Renata', genero='Masculino', edad=97),
            Personas(id=372615, nombre='Jimena', genero='Masculino', edad=72),
        ]
        edad_a_buscar = 50

        generador = (p for p in lista_personas)
        resultado = personas_mayores(generador, edad_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_personas)

    def test_1(self):
        """
        Todas las personas son mayores a la edad a buscar
        """
        lista_personas = [
            Personas(id=317984, nombre='Lucía', genero='Femenino', edad=32),
            Personas(id=437219, nombre='Carlos', genero='Masculino', edad=71),
            Personas(id=543254, nombre='Teresa', genero='Femenino', edad=65),
            Personas(id=244869, nombre='Matias', genero='Masculino', edad=23),
            Personas(id=983156, nombre='Valeria', genero='Femenino', edad=39),
        ]
        expected_lista_personas = [
            Personas(id=317984, nombre='Lucía', genero='Femenino', edad=32),
            Personas(id=437219, nombre='Carlos', genero='Masculino', edad=71),
            Personas(id=543254, nombre='Teresa', genero='Femenino', edad=65),
            Personas(id=244869, nombre='Matias', genero='Masculino', edad=23),
            Personas(id=983156, nombre='Valeria', genero='Femenino', edad=39),
        ]
        edad_a_buscar = 20

        generador = (p for p in lista_personas)
        resultado = personas_mayores(generador, edad_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_personas)

    def test_2(self):
        """
        Ninguna persona es mayor a la edad a buscar
        """
        lista_personas = [
            Personas(id=317984, nombre='Lucía', genero='Femenino', edad=32),
            Personas(id=437219, nombre='Carlos', genero='Masculino', edad=71),
            Personas(id=543254, nombre='Teresa', genero='Femenino', edad=65),
            Personas(id=244869, nombre='Matias', genero='Masculino', edad=23),
            Personas(id=983156, nombre='Valeria', genero='Femenino', edad=39),
        ]
        expected_lista_personas = []
        edad_a_buscar = 75

        generador = (p for p in lista_personas)
        resultado = personas_mayores(generador, edad_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_personas)

    def test_3(self):
        """
        Persona con edad igual a la edad a buscar
        """
        lista_personas = [
            Personas(id=429186, nombre='Paula', genero='Masculino', edad=88),
            Personas(id=926242, nombre='Martina', genero='Femenino', edad=36),
            Personas(id=138975, nombre='Daniel', genero='Masculino', edad=66),
            Personas(id=186243, nombre='Pablo', genero='Femenino', edad=50),
            Personas(id=673894, nombre='Felipe', genero='No binario', edad=19),
            Personas(id=824156, nombre='Gabriel', genero='Femenino', edad=33),
            Personas(id=126734, nombre='Juampi', genero='Masculino', edad=24),
            Personas(id=245769, nombre='Natalia', genero='Femenino', edad=17),
        ]
        expected_lista_personas = [
            Personas(id=429186, nombre='Paula', genero='Masculino', edad=88),
            Personas(id=138975, nombre='Daniel', genero='Masculino', edad=66),
            Personas(id=186243, nombre='Pablo', genero='Femenino', edad=50),
        ]
        edad_a_buscar = 50

        generador = (p for p in lista_personas)
        resultado = personas_mayores(generador, edad_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_personas)

    def test_4(self):
        """
        Personas con el mismo nombre
        """
        lista_personas = [
            Personas(id=926242, nombre='Martina', genero='Femenino', edad=36),
            Personas(id=186243, nombre='Martina', genero='Femenino', edad=50),
            Personas(id=138975, nombre='Daniel', genero='Masculino', edad=66),
            Personas(id=673894, nombre='Felipe', genero='No binario', edad=19),
        ]
        expected_lista_personas = [
            Personas(id=138975, nombre='Daniel', genero='Masculino', edad=66),
            Personas(id=186243, nombre='Martina', genero='Femenino', edad=50),
        ]
        edad_a_buscar = 45

        generador = (p for p in lista_personas)
        resultado = personas_mayores(generador, edad_a_buscar)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_lista_personas)

if __name__ == '__main__':
    unittest.main(verbosity=2)