# Escribe tu código aquí
from dccompletada import *

tipo = input()
preciomax = 0
localmax = ''
preciomin =100000000000000
localmin = ''
N= obtener_total_locales()
for i in range(N):
    nombre = obtener_local(i)
    precio = obtener_precio(tipo,nombre)
    if precio > preciomax:
        preciomax = precio
        localmax = nombre
    if precio < preciomin:
        preciomin = precio
        localmin = nombre
print(localmax,preciomax)
print(localmin,preciomin)

