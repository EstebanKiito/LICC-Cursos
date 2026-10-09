# Escribe tu código aquí

from dccompletada import *


def cuantos(local):
    i = 0
    seguir = True
    while seguir:
        tipo = obtener_tipo_completo(i)
        if tipo == 'No existe':
            seguir = False
        else:
            i+=1
    return i

def completo_de_oro(local):
    pmax = 0
    tmax = ''
    M = cuantos(local)
    for i in range(M):
        tipo = obtener_tipo_completo(i)
        precio = obtener_precio(tipo,local)
        if precio>pmax:
            pmax=precio
            tmax=tipo
    return tmax
