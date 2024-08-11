
from collections import namedtuple

# ----------------------------------------------------------------------------
# NO MODIFICAR
# ----------------------------------------------------------------------------

Personas = namedtuple('Personas', 'id, nombre, genero, edad')
Peliculas = namedtuple('Peliculas', 'id, titulo, genero, rating')
Funciones = namedtuple('Funciones', 'id, numero_sala, id_pelicula, horario, fecha')
Reservas = namedtuple('Reservas', 'id_persona, id_funcion, numero_butaca')