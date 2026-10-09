from pizza import *
# Escribe tu código aquí
def mejor_dia(i1,i2):
    menor = precio_ingrediente(i1,'lunes')+precio_ingrediente(i2,'lunes')
    menordia = 'lunes'
    for i in range(2,8):
        dia = nombre_dia(i)
        precio = precio_ingrediente(i1,dia)+precio_ingrediente(i2,dia)
        if precio<menor:
            menor = precio
            menordia = dia
    return menordia
