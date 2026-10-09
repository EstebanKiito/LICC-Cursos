# Escribe tu código aquí
from pizza import *
dia = input()
for i in range(10):
    nombrepizza = input()
    ingrediente1 = ingrediente_principal(nombrepizza)
    ingrediente2 = ingrediente_secundario(nombrepizza)
    precio = precio_ingrediente(ingrediente1,dia)+precio_ingrediente(ingrediente2,dia)
    if precio<=9990:
        print(f'{nombrepizza} {precio}')
