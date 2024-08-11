from os.path import join
from entities import Item

def cargar_items() -> list:
    items = []

    with open(join("utils", "items.dcc")) as archivo:
        for linea in archivo.readlines():
            nombre, precio, puntos = linea.strip().split(",")
            items.append(Item(nombre, int(precio), int(puntos)))
            
    return items