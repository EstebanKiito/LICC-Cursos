import funciones
import inspect
import re
import unittest

from itertools import product
from os import remove
from typing import Generator
from utilidades import Pelicula, Genero


class ComandoProhibidoError(BaseException):
    def __init__(self, comandos: list, prohibido: bool = True, *args: object) -> None:
        if prohibido:
            mensaje = 'Se utiliza alguno de estos elementos en la función: '
        else:
            mensaje = 'No se utiliza alguno de estos elementos esperado en la función: '
        mensaje += ', '.join(comandos)
        super().__init__(mensaje, *args[2:])


def usa_comando_prohibido(func, comandos):
    '''
    Comprueba el uso de un comando prohibido en el código.
    En caso de encontrarlo, levanta una excepción.
    '''

    codigo_fuente = inspect.getsource(func).replace('\\', ' ')
    codigo = codigo_fuente.strip()
    for comando in comandos:
        expresion = rf'{comando}([^\n]\s+)'
        if re.search(expresion, codigo):
            raise ComandoProhibidoError(comandos)


def usa_metodo_prohibido(func, comandos):
    '''
    Comprueba el uso de un método prohibido en el código.
    En caso de encontrarlo, levanta una excepción.
    '''

    codigo_fuente = inspect.getsource(func).replace('\\', ' ')
    codigo = codigo_fuente.strip()
    for comando in comandos:
        expresion = rf'{comando}\s*\('
        if re.search(expresion, codigo):
            raise ComandoProhibidoError(comandos)


class TestCargarDatos(unittest.TestCase):
    '''
    Test orientado a comprobar las funciones:
    - cargar_peliculas
    - cargar_generos
    '''

    data_peliculas = [
        # peliculas_1.csv
        'id,titulo,director,año_estreno,rating_promedio\n'
        '20,The Social Network,David Fincher,2010,7.7',
        # peliculas_2.csv
        'id,titulo,director,año_estreno,rating_promedio\n'
        '14,The Lion King,Roger Allers,1994,8.5\n'
        '15,The Avengers,Joss Whedon,2012,8.0\n'
        '16,Interstellar,Christopher Nolan,2014,8.6\n'
        '17,Gone with the Wind,Victor Fleming,1939,8.1\n'
        '18,Casablanca,Michael Curtiz,1942,8.5\n'
        '19,The Great Gatsby,Baz Luhrmann,2013,7.2',
        # peliculas_3.csv
        'id,titulo,director,año_estreno,rating_promedio\n'
        '7,The Matrix,Lana Wachowski,1999,8.7\n'
        '8,Goodfellas,Martin Scorsese,1990,8.7\n'
        '9,Schindler\'s List,Steven Spielberg,1993,8.9',
        # peliculas_4.csv
        'id,titulo,director,año_estreno,rating_promedio\n'
        '1,The Shawshank Redemption,Frank Darabont,1994,9.3\n'
        '2,The Godfather,Francis Ford Coppola,1972,9.2\n'
        '3,Pulp Fiction,Quentin Tarantino,1994,8.9\n'
        '4,The Dark Knight,Christopher Nolan,2008,9.0\n'
        '5,Fight Club,David Fincher,1999,8.8\n'
        '6,Inception,Christopher Nolan,2010,8.8\n'
        '10,Forrest Gump,Robert Zemeckis,1994,8.8\n'
        '11,The Silence of the Lambs,Jonathan Demme,1991,8.6\n'
        '12,The Lord of the Rings: The Fellowship of the Ring,Peter Jackson,2001,8.8\n'
        '13,The Departed,Martin Scorsese,2006,8.5'
    ]
    data_generos = [
        # generos_1.csv
        'genero,id_pelicula\n'
        'Drama,20',
        # generos_2.csv
        'genero,id_pelicula\n'
        'Animation,14\n'
        'Action,15\n'
        'Adventure,16\n'
        'Drama,17\n'
        'War,18\n'
        'Romance,19',
        # generos_3.csv
        'genero,id_pelicula\n'
        'Action,7\nSci-Fi,7\n'
        'Biography,8\nCrime,8\nDrama,8\n'
        'Biography,9\nDrama,9\nHistory,9',
        # generos_4.csv
        'genero,id_pelicula\n'
        'Drama,1\nCrime,1\n'
        'Drama,2\nCrime,2\n'
        'Drama,3\nCrime,3\n'
        'Action,4\nDrama,4\nCrime,4\n'
        'Drama,5\n'
        'Action,6\nDrama,6\n'
        'Action,7\nSci-Fi,7\n'
        'Biography,8\nCrime,8\nDrama,8\n'
        'Biography,9\nDrama,9\nHistory,9\n'
        'Drama,10\nRomance,10\n'
        'Drama,11\n'
        'Crime,12\nAdventure,12\nDrama,12\n'
        'Crime,13\nDrama,13'
    ]

    @classmethod
    def setUpClass(cls):
        '''
        Al inicio de la ejecución de los tests se crean los archivos
        necesarios para comprobar las función que cargan datos.
        '''

        for i in range(len(cls.data_peliculas)):
            with open(f'peliculas_{i + 1}.csv', 'w') as file:
                file.write(cls.data_peliculas[i])

            with open(f'generos_{i + 1}.csv', 'w') as file:
                file.write(cls.data_generos[i])

    @classmethod
    def tearDownClass(cls):
        '''
        Al finalizar la ejecución de los tests se eliminan
        los archivos creados anteriormente.
        '''

        for i in range(len(cls.data_peliculas)):
            remove(f'peliculas_{i + 1}.csv')
            remove(f'generos_{i + 1}.csv')

    def test_cargar_peliculas_1(self):
        '''
        Se comprueba que la función "cargar_peliculas" cargue correctamente
        las peliculas del archivo "peliculas_1.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_peliculas".
        '''

        datos = funciones.cargar_peliculas('peliculas_1.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        pelicula = Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7)
        self.assertSequenceEqual(lista_datos[0], pelicula)
        self.assertSequenceEqual(lista_datos[-1], pelicula)

    def test_cargar_peliculas_2(self):
        '''
        Se comprueba que la función "cargar_peliculas" cargue correctamente
        las peliculas del archivo "peliculas_2.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_peliculas".
        '''

        datos = funciones.cargar_peliculas('peliculas_2.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        pelicula_1 = Pelicula(14, 'The Lion King', 'Roger Allers', 1994, 8.5)
        pelicula_2 = Pelicula(15, 'The Avengers', 'Joss Whedon', 2012, 8.0)
        pelicula_3 = Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6)
        pelicula_4 = Pelicula(17, 'Gone with the Wind', 'Victor Fleming', 1939, 8.1)
        pelicula_5 = Pelicula(18, 'Casablanca', 'Michael Curtiz', 1942, 8.5)
        pelicula_6 = Pelicula(19, 'The Great Gatsby', 'Baz Luhrmann', 2013, 7.2)
        self.assertSequenceEqual(lista_datos[0], pelicula_1)
        self.assertSequenceEqual(lista_datos[1], pelicula_2)
        self.assertSequenceEqual(lista_datos[2], pelicula_3)
        self.assertSequenceEqual(lista_datos[3], pelicula_4)
        self.assertSequenceEqual(lista_datos[4], pelicula_5)
        self.assertSequenceEqual(lista_datos[5], pelicula_6)

    def test_cargar_peliculas_3(self):
        '''
        Se comprueba que la función "cargar_peliculas" cargue correctamente
        las peliculas del archivo "peliculas_3.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_peliculas".
        '''

        datos = funciones.cargar_peliculas('peliculas_3.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        pelicula_1 = Pelicula(7, 'The Matrix', 'Lana Wachowski', 1999, 8.7)
        pelicula_2 = Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.7)
        pelicula_3 = Pelicula(9, 'Schindler\'s List', 'Steven Spielberg', 1993, 8.9)
        self.assertSequenceEqual(lista_datos[0], pelicula_1)
        self.assertSequenceEqual(lista_datos[1], pelicula_2)
        self.assertSequenceEqual(lista_datos[2], pelicula_3)

    def test_cargar_peliculas_4(self):
        '''
        Se comprueba que la función "cargar_peliculas" cargue correctamente
        las peliculas del archivo "peliculas_4.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_peliculas".
        '''

        datos = funciones.cargar_peliculas('peliculas_4.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        pelicula_2 = Pelicula(2, 'The Godfather', 'Francis Ford Coppola', 1972, 9.2)
        pelicula_13 = Pelicula(13, 'The Departed', 'Martin Scorsese', 2006, 8.5)
        self.assertSequenceEqual(lista_datos[1], pelicula_2)
        self.assertSequenceEqual(lista_datos[-1], pelicula_13)

    def test_cargar_generos_1(self):
        '''
        Se comprueba que la función "cargar_generos" cargue correctamente
        las peliculas del archivo "generos_1.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_generos".
        '''

        datos = funciones.cargar_generos('generos_1.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        categoria = Genero('Drama', 20)
        self.assertSequenceEqual(lista_datos[0], categoria)
        self.assertSequenceEqual(lista_datos[-1], categoria)

    def test_cargar_generos_2(self):
        '''
        Se comprueba que la función "cargar_generos" cargue correctamente
        las peliculas del archivo "generos_2.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_generos".
        '''

        datos = funciones.cargar_generos('generos_2.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        genero_1 = Genero('Animation', 14)
        genero_2 = Genero('Action', 15)
        genero_3 = Genero('Adventure', 16)
        genero_4 = Genero('Drama', 17)
        genero_5 = Genero('War', 18)
        genero_6 = Genero('Romance', 19)

        self.assertSequenceEqual(lista_datos[0], genero_1)
        self.assertSequenceEqual(lista_datos[1], genero_2)
        self.assertSequenceEqual(lista_datos[2], genero_3)
        self.assertSequenceEqual(lista_datos[3], genero_4)
        self.assertSequenceEqual(lista_datos[4], genero_5)
        self.assertSequenceEqual(lista_datos[5], genero_6)
        self.assertSequenceEqual(lista_datos[-1], genero_6)

    def test_cargar_generos_3(self):
        '''
        Se comprueba que la función "cargar_generos" cargue correctamente
        las peliculas del archivo "generos_3.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_generos".
        '''

        datos = funciones.cargar_generos('generos_3.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        genero_1 = Genero('Action', 7)
        genero_2 = Genero('Sci-Fi', 7)
        genero_6 = Genero('Biography', 9)
        genero_7 = Genero('Drama', 9)
        genero_8 = Genero('History', 9)
        self.assertSequenceEqual(lista_datos[0], genero_1)
        self.assertSequenceEqual(lista_datos[1], genero_2)
        self.assertSequenceEqual(lista_datos[5], genero_6)
        self.assertSequenceEqual(lista_datos[6], genero_7)
        self.assertSequenceEqual(lista_datos[7], genero_8)
        self.assertSequenceEqual(lista_datos[-1], genero_8)

    def test_cargar_generos_4(self):
        '''
        Se comprueba que la función "cargar_generos" cargue correctamente
        las peliculas del archivo "generos_4.csv". Se puede revisar el contenido
        del archivo en el atributo de clase "data_generos".
        '''

        datos = funciones.cargar_generos('generos_4.csv')

        # Verificar tipo de dato pedido
        self.assertIsInstance(datos, Generator)
        lista_datos = list(datos)

        # Verificar resultados
        genero_1 = Genero('Drama', 1)
        genero_n = Genero('Drama', 13)
        self.assertSequenceEqual(lista_datos[0], genero_1)
        self.assertSequenceEqual(lista_datos[27], genero_n)
        self.assertSequenceEqual(lista_datos[-1], genero_n)


class TestConsultas(unittest.TestCase):
    '''
    Test orientado a comprobar las funciones:
    - obtener_directores
    - obtener_str_titulos
    '''

    def generador_peliculas(self, variacion):
        '''
        Función generadora que retorna distintas instancias de película.
        '''

        if variacion == 1:
            yield Pelicula(19, 'The Great Gatsby', 'Baz Luhrmann', 2013, 7.2)
        elif variacion == 2:
            yield Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8)
            yield Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7)
        elif variacion == 3:
            yield Pelicula(17, 'Gone with the Wind', 'Victor Fleming', 1939, 8.1)
            yield Pelicula(18, 'Casablanca', 'Michael Curtiz', 1942, 8.5)
            yield Pelicula(19, 'The Great Gatsby', 'Baz Luhrmann', 2013, 7.2)
        elif variacion == 4:
            yield Pelicula(4, 'The Dark Knight', 'Christopher Nolan', 2008, 9.0)
            yield Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8)
            yield Pelicula(6, 'Inception', 'Christopher Nolan', 2010, 8.8)
            yield Pelicula(7, 'The Matrix', 'Lana Wachowski', 1999, 8.7)
            yield Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.7)
            yield Pelicula(13, 'The Departed', 'Martin Scorsese', 2006, 8.5)
            yield Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6)

    def test_obtener_directores_1(self):
        '''
        Se comprueba que la función "obtener_directores" obtenga correctamente un set
        con el nombre de los directores de las películas de la variación 1 (generador_peliculas).
        '''

        datos = funciones.obtener_directores(self.generador_peliculas(1))
        self.assertIsInstance(datos, set)
        self.assertSequenceEqual(datos, {'Baz Luhrmann'})

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_directores, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_directores, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_directores_2(self):
        '''
        Se comprueba que la función "obtener_directores" obtenga correctamente un set
        con el nombre de los directores de las películas de la variación 2 (generador_peliculas).
        '''

        datos = funciones.obtener_directores(self.generador_peliculas(2))
        self.assertIsInstance(datos, set)
        self.assertSequenceEqual(datos, {'David Fincher'})

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_directores, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_directores, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_directores_3(self):
        '''
        Se comprueba que la función "obtener_directores" obtenga correctamente un set
        con el nombre de los directores de las películas de la variación 3 (generador_peliculas).
        '''

        datos = funciones.obtener_directores(self.generador_peliculas(3))
        self.assertIsInstance(datos, set)
        self.assertSequenceEqual(datos, {'Victor Fleming', 'Michael Curtiz', 'Baz Luhrmann'})

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_directores, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_directores, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_directores_4(self):
        '''
        Se comprueba que la función "obtener_directores" obtenga correctamente un set
        con el nombre de los directores de las películas de la variación 4 (generador_peliculas).
        '''

        datos = funciones.obtener_directores(self.generador_peliculas(4))
        self.assertIsInstance(datos, set)
        self.assertSequenceEqual(datos, {'Christopher Nolan', 'David Fincher', 'Lana Wachowski', 'Martin Scorsese'})

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_directores, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_directores, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_directores_vacio(self):
        '''
        Se comprueba que la función "obtener_directores" cree correctamente un set vacío
        cuando no se le pasan películas.
        '''

        datos = funciones.obtener_directores(self.generador_peliculas(5))
        self.assertIsInstance(datos, set)
        self.assertSequenceEqual(datos, set())

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_directores, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_directores, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_str_titulos_1(self):
        '''
        Se comprueba que la función "obtener_str_titulos" obtenga correctamente un string
        que contenga los títulos concatenados de las películas de la variación 1 (generador_peliculas).
        '''

        titulos = funciones.obtener_str_titulos(self.generador_peliculas(1))
        titulos_esperado = 'The Great Gatsby'
        self.assertIsInstance(titulos, str)
        self.assertEqual(titulos, titulos_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_str_titulos, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_str_titulos, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_str_titulos_2(self):
        '''
        Se comprueba que la función "obtener_str_titulos" obtenga correctamente un string
        que contenga los títulos concatenados de las películas de la variación 2 (generador_peliculas).
        '''

        titulos = funciones.obtener_str_titulos(self.generador_peliculas(2))
        titulos_esperado = 'Fight Club, The Social Network'
        self.assertIsInstance(titulos, str)
        self.assertEqual(titulos, titulos_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_str_titulos, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_str_titulos, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_str_titulos_3(self):
        '''
        Se comprueba que la función "obtener_str_titulos" obtenga correctamente un string
        que contenga los títulos concatenados de las películas de la variación 3 (generador_peliculas).
        '''

        titulos = funciones.obtener_str_titulos(self.generador_peliculas(3))
        titulos_esperado = 'Gone with the Wind, Casablanca, The Great Gatsby'
        self.assertIsInstance(titulos, str)
        self.assertEqual(titulos, titulos_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_str_titulos, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_str_titulos, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_str_titulos_4(self):
        '''
        Se comprueba que la función "obtener_str_titulos" obtenga correctamente un string
        que contenga los títulos concatenados de las películas de la variación 4 (generador_peliculas).
        '''

        titulos = funciones.obtener_str_titulos(self.generador_peliculas(4))
        titulos_esperado = 'The Dark Knight, Fight Club, Inception, The Matrix, Goodfellas, The Departed, Interstellar'
        self.assertIsInstance(titulos, str)
        self.assertEqual(titulos, titulos_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_str_titulos, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_str_titulos, ['list', 'dict', 'set', 'tuple'])

    def test_obtener_str_titulos_vacio(self):
        '''
        Se comprueba que la función "obtener_str_titulos" obtenga correctamente un string vacío
        cuando no se le pasan películas.
        '''

        titulos = funciones.obtener_str_titulos(self.generador_peliculas(5))
        titulos_esperado = ''
        self.assertIsInstance(titulos, str)
        self.assertEqual(titulos, titulos_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.obtener_str_titulos, ['for', 'while'])
        usa_metodo_prohibido(funciones.obtener_str_titulos, ['list', 'dict', 'set', 'tuple'])


class TestFiltros(unittest.TestCase):
    '''
    Test orientado a comprobar las funciones:
    - filtrar_peliculas
    - filtrar_peliculas_por_genero
    '''

    def generador_peliculas(self, variacion):
        '''
        Función generadora que retorna distintas instancias de película.
        '''

        if variacion == 1:
            yield Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8)
            yield Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7)
        elif variacion == 2:
            yield Pelicula(4, 'The Dark Knight', 'Christopher Nolan', 2008, 9.0)
            yield Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8)
            yield Pelicula(6, 'Inception', 'Christopher Nolan', 2010, 8.8)
            yield Pelicula(7, 'The Matrix', 'Lana Wachowski', 1999, 8.7)
            yield Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.7)
            yield Pelicula(13, 'The Departed', 'Martin Scorsese', 2006, 8.5)
            yield Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6)
            yield Pelicula(21, 'The Wolf of Wall Street', 'Martin Scorsese', 2013, 8.2)
        elif variacion == 3:
            yield Pelicula(13, 'The Departed', 'Martin Scorsese', 2006, 8.5)
            yield Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6)
            yield Pelicula(21, 'The Wolf of Wall Street', 'Martin Scorsese', 2013, 8.2)

    def generador_generos(self, variacion):
        '''
        Función generadora que retorna distintas instancias de genero.
        '''

        if variacion == 1:
            yield Genero('Drama', 5)
            yield Genero('Drama', 20)
        elif variacion == 2:
            yield Genero('Action', 4)
            yield Genero('Drama', 4)
            yield Genero('Crime', 4)
            yield Genero('Drama', 5)
            yield Genero('Action', 6)
            yield Genero('Drama', 6)
            yield Genero('Action', 7)
            yield Genero('Sci-Fi', 7)
            yield Genero('Biography', 8)
            yield Genero('Crime', 8)
            yield Genero('Drama', 8)
            yield Genero('Crime', 13)
            yield Genero('Drama', 13)
            yield Genero('Adventure', 16)
            yield Genero('Drama', 16)
            yield Genero('Sci-Fi', 16)
            yield Genero('Comedy', 21)
            yield Genero('Crime', 21)
            yield Genero('Drama', 21)
        elif variacion == 3:
            yield Genero('Action', 4)
            yield Genero('Drama', 5)
            yield Genero('Sci-Fi', 7)
            yield Genero('Biography', 8)

    def test_filtrar_peliculas_por_director(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        cuando solo se le entrega el nombre de un director. Se utilizan las películas
        de la variación 2 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(2), director='Christopher Nolan')
        peliculas = [
            Pelicula(4, 'The Dark Knight', 'Christopher Nolan', 2008, 9.0),
            Pelicula(6, 'Inception', 'Christopher Nolan', 2010, 8.8),
            Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6)
        ]
        self.assertIsInstance(datos, filter)
        self.assertSequenceEqual(list(datos), peliculas)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.filtrar_peliculas, ['for', 'while'])
        usa_metodo_prohibido(funciones.filtrar_peliculas, ['list', 'dict', 'set', 'tuple'])

    def test_filtrar_peliculas_por_rating_min(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        cuando solo se le entrega un rating mínimo. Se utilizan las películas
        de la variación 1 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(1), rating_min=8)
        peliculas = [
            Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8)
        ]
        self.assertIsInstance(datos, filter)
        self.assertSequenceEqual(list(datos), peliculas)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.filtrar_peliculas, ['for', 'while'])
        usa_metodo_prohibido(funciones.filtrar_peliculas, ['list', 'dict', 'set', 'tuple'])

    def test_filtrar_peliculas_por_rating_max(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        cuando solo se le entrega un rating máximo. Se utilizan las películas
        de la variación 1 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(1), rating_max=7.7)
        peliculas = [
            Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7)
        ]
        self.assertIsInstance(datos, filter)
        self.assertSequenceEqual(list(datos), peliculas)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.filtrar_peliculas, ['for', 'while'])
        usa_metodo_prohibido(funciones.filtrar_peliculas, ['list', 'dict', 'set', 'tuple'])

    def test_filtrar_peliculas_todo(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        cuando solo se le entrega el nombre de un director, un rating mínimo y un rating máximo.
        Se utilizan las películas de la variación 2 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(2), director='Martin Scorsese', rating_min=8.5, rating_max=9)
        peliculas = [
            Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.7),
            Pelicula(13, 'The Departed', 'Martin Scorsese', 2006, 8.5)
        ]
        self.assertIsInstance(datos, filter)
        self.assertSequenceEqual(list(datos), peliculas)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.filtrar_peliculas, ['for', 'while'])
        usa_metodo_prohibido(funciones.filtrar_peliculas, ['list', 'dict', 'set', 'tuple'])

    def test_filtrar_peliculas_vacio(self):
        '''
        Se comprueba que la función "filtrar_peliculas" se aplique correctamente
        y retorne vacío cuando corresponde. Se utilizan las películas de la
        variación 1 (generador_peliculas).
        '''

        datos = funciones.filtrar_peliculas(self.generador_peliculas(1), director='Lana Wachowski', rating_min=8.5, rating_max=9)
        self.assertIsInstance(datos, filter)
        self.assertSequenceEqual(list(datos), [])

        # No usa for, while o loop
        usa_comando_prohibido(funciones.filtrar_peliculas, ['for', 'while'])
        usa_metodo_prohibido(funciones.filtrar_peliculas, ['list', 'dict', 'set', 'tuple'])

    def test_filtrar_por_genero_1(self):
        '''
        Se comprueba que la función "filtrar_peliculas_por_genero" obtiene y filtrar
        los pares película-genero, cuando se le entrega un genero de película.
        Se utilizan las películas de la variación 1 (generador_peliculas) y los generos
        de la variación 1 (generador_generos).
        '''

        datos = funciones.filtrar_peliculas_por_genero(self.generador_peliculas(1), self.generador_generos(1), 'Drama')
        resultado_esperado = [
            (Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8), Genero('Drama', 5)),
            (Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7), Genero('Drama', 20))
        ]
        self.assertSequenceEqual(list(datos), resultado_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.filtrar_peliculas_por_genero, ['for', 'while'])
        usa_metodo_prohibido(funciones.filtrar_peliculas_por_genero, ['list', 'dict', 'set', 'tuple'])

    def test_filtrar_por_genero_2(self):
        '''
        Se comprueba que la función "filtrar_peliculas_por_genero" obtiene y filtrar
        los pares película-genero, cuando se le entrega un genero de película.
        Se utilizan las películas de la variación 2 (generador_peliculas) y los generos
        de la variación 2 (generador_generos).
        '''

        datos = funciones.filtrar_peliculas_por_genero(self.generador_peliculas(2), self.generador_generos(2), 'Comedy')
        resultado_esperado = [
            (Pelicula(21, 'The Wolf of Wall Street', 'Martin Scorsese', 2013, 8.2), Genero('Comedy', 21))
        ]
        self.assertSequenceEqual(list(datos), resultado_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.filtrar_peliculas_por_genero, ['for', 'while'])
        usa_metodo_prohibido(funciones.filtrar_peliculas_por_genero, ['list', 'dict', 'set', 'tuple'])

    def test_filtrar_por_genero_none(self):
        '''
        Se comprueba que la función "filtrar_peliculas_por_genero" obtiene y filtrar
        los pares película-genero, cuando no se entrega un genero de película.
        Se utilizan las películas de la variación 2 (generador_peliculas) y los generos
        de la variación 3 (generador_generos).
        '''

        datos = funciones.filtrar_peliculas_por_genero(self.generador_peliculas(2), self.generador_generos(3))
        resultado_esperado = [
            (Pelicula(4, 'The Dark Knight', 'Christopher Nolan', 2008, 9.0), Genero('Action', 4)),
            (Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8), Genero('Drama', 5)),
            (Pelicula(7, 'The Matrix', 'Lana Wachowski', 1999, 8.7), Genero('Sci-Fi', 7)),
            (Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.7), Genero('Biography', 8))
        ]
        self.assertSequenceEqual(list(datos), resultado_esperado)

        # No usa for, while o loop
        usa_comando_prohibido(funciones.filtrar_peliculas_por_genero, ['for', 'while'])
        usa_metodo_prohibido(funciones.filtrar_peliculas_por_genero, ['list', 'dict', 'set', 'tuple'])

    def test_filtrar_por_genero_vacio_1(self):
        '''
        Se comprueba que la función "filtrar_peliculas_por_genero" retorna vacío,
        cuando no hay películas del genero indicado.
        Se utilizan las películas de la variación 1 (generador_peliculas) y los generos
        de la variación 1 (generador_generos).
        '''

        datos = funciones.filtrar_peliculas_por_genero(self.generador_peliculas(1), self.generador_generos(1), 'Comedy')
        self.assertSequenceEqual(list(datos), [])

        # No usa for, while o loop
        usa_comando_prohibido(funciones.filtrar_peliculas_por_genero, ['for', 'while'])
        usa_metodo_prohibido(funciones.filtrar_peliculas_por_genero, ['list', 'dict', 'set', 'tuple'])

    def test_filtrar_por_genero_vacio_2(self):
        '''
        Se comprueba que la función "filtrar_peliculas_por_genero" retorna vacío,
        cuando los generadores de películas y generos no tiene pares con el mismo id.
        Se utilizan las películas de la variación 1 (generador_peliculas) y los generos
        de la variación 1 (generador_generos).
        '''

        datos = funciones.filtrar_peliculas_por_genero(self.generador_peliculas(3), self.generador_generos(3))
        self.assertSequenceEqual(list(datos), [])

        # No usa for, while o loop
        usa_comando_prohibido(funciones.filtrar_peliculas_por_genero, ['for', 'while'])
        usa_metodo_prohibido(funciones.filtrar_peliculas_por_genero, ['list', 'dict', 'set', 'tuple'])


class TestIterables(unittest.TestCase):

    def lista_peliculas(self, variacion):
        '''
        Función que retorna listas de películas.
        '''

        if variacion == 1:
            return [Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7)]
        elif variacion == 2:
            return [
                Pelicula(10, 'Forrest Gump', 'Robert Zemeckis', 1994, 8.8),
                Pelicula(1, 'The Shawshank Redemption', 'Frank Darabont', 1994, 9.3),
                Pelicula(3, 'Pulp Fiction', 'Quentin Tarantino', 1994, 8.9),
                Pelicula(14, 'The Lion King', 'Roger Allers', 1994, 8.5),
            ]
        elif variacion == 3:
            return [
                Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6),
                Pelicula(17, 'Gone with the Wind', 'Victor Fleming', 1939, 8.1),
                Pelicula(18, 'Casablanca', 'Michael Curtiz', 1942, 8.5),
                Pelicula(19, 'The Great Gatsby', 'Baz Luhrmann', 2013, 7.2),
                Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7),
            ]
        elif variacion == 4:
            return [
                Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8),
                Pelicula(6, 'Inception', 'Christopher Nolan', 2010, 8.8),
                Pelicula(7, 'The Matrix', 'Lana Wachowski', 1999, 8.7),
                Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.9),
            ]

    def lista_peliculas_ordenada(self, variacion):
        '''
        Función que retorna listas de películas ordenadas según los criterios de DCCMax.
        '''

        if variacion == 1:
            return [Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7)]
        elif variacion == 2:
            return [
                Pelicula(1, 'The Shawshank Redemption', 'Frank Darabont', 1994, 9.3),
                Pelicula(3, 'Pulp Fiction', 'Quentin Tarantino', 1994, 8.9),
                Pelicula(10, 'Forrest Gump', 'Robert Zemeckis', 1994, 8.8),
                Pelicula(14, 'The Lion King', 'Roger Allers', 1994, 8.5),
            ]
        elif variacion == 3:
            return [
                Pelicula(17, 'Gone with the Wind', 'Victor Fleming', 1939, 8.1),
                Pelicula(18, 'Casablanca', 'Michael Curtiz', 1942, 8.5),
                Pelicula(20, 'The Social Network', 'David Fincher', 2010, 7.7),
                Pelicula(19, 'The Great Gatsby', 'Baz Luhrmann', 2013, 7.2),
                Pelicula(16, 'Interstellar', 'Christopher Nolan', 2014, 8.6),
            ]
        elif variacion == 4:
            return [
                Pelicula(8, 'Goodfellas', 'Martin Scorsese', 1990, 8.9),
                Pelicula(5, 'Fight Club', 'David Fincher', 1999, 8.8),
                Pelicula(7, 'The Matrix', 'Lana Wachowski', 1999, 8.7),
                Pelicula(6, 'Inception', 'Christopher Nolan', 2010, 8.8),
            ]

    def test_DCCMax_iter(self):
        '''
        Se comprueba que el método "__iter__" de la clase "DCCMax" retorne un iterador
        de la clase "IteradorDCCMax". Se utiliza una lista de películas arbitraria.
        '''

        peliculas = self.lista_peliculas(1)
        iterable = funciones.DCCMax(peliculas)
        iterador = iter(iterable)
        self.assertIsInstance(iterador, funciones.IteradorDCCMax)

        # No usa for ni while
        usa_comando_prohibido(funciones.DCCMax, ['for', 'while'])

    def test_IteradorDCCMax_iter(self):
        '''
        Se comprueba que el método "__iter__" de la clase "IteradorDCCMax" retorne un iterador
        de la clase "IteradorDCCMax". Se utiliza una lista de películas arbitraria.
        '''

        peliculas = self.lista_peliculas(1)
        iterable = funciones.IteradorDCCMax(peliculas)
        iterador = iter(iterable)
        self.assertIsInstance(iterador, funciones.IteradorDCCMax)

        # No usa for ni while
        usa_comando_prohibido(funciones.IteradorDCCMax, ['for', 'while'])

    def test_IteradorDCCMax_StopIteration(self):
        '''
        Se comprueba que al acabarse los elementos del IteradorDCCMax,
        este levante la excepción correspondiente.
        '''

        iterador_dcc_max = funciones.IteradorDCCMax([])
        self.assertRaises(StopIteration, next, iterador_dcc_max)

        # No usa for ni while
        usa_comando_prohibido(funciones.IteradorDCCMax, ['for', 'while'])

    def test_IteradorDCCMax_next_1(self):
        '''
        Se comprueba que el IteradorDCCMax entrega las películas en el orden esperado.
        Una vez se acaban los elemento del iterador, se levanta la excepción correspondiente.
        Se utilizan las películas de la variación 1 (lista_peliculas).
        '''

        lista_peliculas = self.lista_peliculas(1)
        peliculas_ordenadas = self.lista_peliculas_ordenada(1)
        dcc_max = funciones.IteradorDCCMax(lista_peliculas)

        pelicula_next = next(dcc_max)
        self.assertSequenceEqual(pelicula_next, peliculas_ordenadas[0])
        self.assertRaises(StopIteration, next, dcc_max)

        # No usa for ni while
        usa_comando_prohibido(funciones.IteradorDCCMax, ['for', 'while'])

    def test_IteradorDCCMax_next_2(self):
        '''
        Se comprueba que el IteradorDCCMax entrega las películas en el orden esperado.
        Una vez se acaban los elemento del iterador, se levanta la excepción correspondiente.
        Se utilizan las películas de la variación 2 (lista_peliculas).
        '''

        peliculas = self.lista_peliculas(2)
        peliculas_ordenadas = self.lista_peliculas_ordenada(2)
        dcc_max = funciones.IteradorDCCMax(peliculas)

        for pelicula_ordenado in peliculas_ordenadas:
            pelicula_next = next(dcc_max)
            self.assertSequenceEqual(pelicula_next, pelicula_ordenado)

        self.assertRaises(StopIteration, next, dcc_max)

        # No usa for ni while
        usa_comando_prohibido(funciones.IteradorDCCMax, ['for', 'while'])

    def test_IteradorDCCMax_next_3(self):
        '''
        Se comprueba que el IteradorDCCMax entrega las películas en el orden esperado.
        Una vez se acaban los elemento del iterador, se levanta la excepción correspondiente.
        Se utilizan las películas de la variación 3 (lista_peliculas).
        '''

        peliculas = self.lista_peliculas(3)
        peliculas_ordenadas = self.lista_peliculas_ordenada(3)
        dcc_max = funciones.IteradorDCCMax(peliculas)

        for pelicula_ordenado in peliculas_ordenadas:
            pelicula_next = next(dcc_max)
            self.assertSequenceEqual(pelicula_next, pelicula_ordenado)

        self.assertRaises(StopIteration, next, dcc_max)

        # No usa for ni while
        usa_comando_prohibido(funciones.IteradorDCCMax, ['for', 'while'])

    def test_IteradorDCCMax_next_4(self):
        '''
        Se comprueba que el IteradorDCCMax entrega las películas en el orden esperado.
        Una vez se acaban los elemento del iterador, se levanta la excepción correspondiente.
        Se utilizan las películas de la variación 4 (lista_peliculas).
        '''

        peliculas = self.lista_peliculas(4)
        peliculas_ordenadas = self.lista_peliculas_ordenada(4)
        dcc_max = funciones.IteradorDCCMax(peliculas)

        for pelicula_ordenado in peliculas_ordenadas:
            pelicula_next = next(dcc_max)
            self.assertSequenceEqual(pelicula_next, pelicula_ordenado)

        self.assertRaises(StopIteration, next, dcc_max)

        # No usa for ni while
        usa_comando_prohibido(funciones.IteradorDCCMax, ['for', 'while'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
