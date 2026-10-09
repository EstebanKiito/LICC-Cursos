# Escribe tu código aquí
from diccionario import *
def corregir(palabra, pos):
    for letra in 'aeiou':
        nueva_palabra = palabra[:pos]+letra+palabra[pos+1:]
        if valida(nueva_palabra):
            return nueva_palabra
    return palabra
