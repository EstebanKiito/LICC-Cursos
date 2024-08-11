
import collections
import datetime
import functools
import itertools
import math
import utilidades

from typing import Generator


def peliculas_genero(generador_peliculas: Generator, genero: str):
    # Completar
    pass

def personas_mayores(generador_personas: Generator, edad: int):
    # Completar
    pass

def funciones_fecha(generador_funciones: Generator, fecha: str):
    # Completar
    pass

def titulo_mas_largo(generador_peliculas: Generator) -> str:
    # Completar
    pass

def normalizar_fechas(generador_funciones: Generator):
    # Completar
    pass

def personas_reservas(generador_reservas: Generator):
    # Completar
    pass

def peliculas_en_base_al_rating(generador_peliculas: Generator, genero: str, rating_min: int, rating_max: int):
    # Completar
    pass

def mejores_peliculas(generador_peliculas: Generator):
    # Completar
    pass

def pelicula_genero_mayor_rating(generador_peliculas: Generator, genero: str) -> str:
    # Completar
    pass

def fechas_funciones_pelicula(generador_peliculas: Generator, generador_funciones: Generator, titulo: str):
    # Completar
    pass

def genero_mas_transmitido(generador_peliculas: Generator, generador_funciones: Generator, fecha: str) -> str:
    # Completar
    pass

def id_funciones_genero(generador_peliculas: Generator, generador_funciones: Generator, genero: str):
    # Completar
    pass

def butacas_por_funcion(generador_reservas: Generator, generador_funciones: Generator, id_funcion: int) -> int:
    # Completar
    pass

def salas_de_pelicula(generador_peliculas: Generator, generador_funciones: Generator, nombre_pelicula: str):
    # Completar
    pass

def nombres_butacas_altas(generador_personas: Generator, generador_peliculas: Generator, generador_reservas: Generator,
                          generador_funciones: Generator, titulo: str, horario: int):
    # Completar
    pass

def nombres_persona_genero_mayores(generador_personas: Generator, generador_peliculas: Generator,
                                   generador_reservas: Generator, generador_funciones: Generator, nombre_pelicula: str,
                                   genero: str, edad: int):
    # Completar
    pass

def genero_comun(generador_personas: Generator, generador_peliculas: Generator, generador_reservas: Generator,
                 generador_funciones: Generator, id_funcion: int) -> str:
    # Completar
    pass

def edad_promedio(generador_personas: Generator, generador_peliculas: Generator, generador_reservas: Generator,
                  generador_funciones: Generator, id_funcion: int) -> str:
    # Completar
    pass

def obtener_horarios_disponibles(generador_peliculas: Generator, generador_reservas: Generator,
                                 generador_funciones: Generator, fecha_funcion: str, reservas_maximas: int):
    # Completar
    pass

def personas_no_asisten(generador_personas: Generator, generador_reservas: Generator,
                        generador_funciones: Generator, fecha_inicio: str, fecha_termino: str):
    # Completar
    pass
