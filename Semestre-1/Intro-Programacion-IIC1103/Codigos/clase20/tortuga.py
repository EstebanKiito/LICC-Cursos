from turtle import *

def dibujar_arbol(n, longitud):
    #CASO BASE
    if n==0:
        return
    #CASO RECURSIVO
    forward(longitud)
    left(45)
    dibujar_arbol(n-1,longitud*2/3)
    right(90)
    dibujar_arbol(n-1,longitud*2/3)
    left(45)
    back(longitud)

# COD PPAL
dibujar_arbol(8,100)
input()
