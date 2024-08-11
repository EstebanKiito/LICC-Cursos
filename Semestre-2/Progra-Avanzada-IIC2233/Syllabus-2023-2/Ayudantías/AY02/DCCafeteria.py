from collections import namedtuple
from functools import reduce
from itertools import tee

Producto = namedtuple('Producto', 'nombre, precio, categoria')

# NO MODIFICAR
def cargar_productos(ruta):
    with open(ruta, 'r') as archivo:
        linea = archivo.readline()
        for linea in archivo:
            nombre, precio, categoria = linea.strip('\n').split(',')
            precio = int(precio)
            yield Producto(nombre, precio, categoria)

'''
Retorna un generador con el nombre de todos los productos.
'''
def obtener_productos(generador_productos):
    # COMPLETAR
    pass


'''
Retorna un generador con todos los nombres de los Productos 
pertenecientes a la categoría indicada.
'''
def filtrar_por_categoria(generador_productos,
                          nombre_categoria):
    # COMPLETAR
    pass


'''
Retorna un generador con el nombres del Producto más económico,
en caso de haber más de uno, debe retornarlos todos.
'''
def buscar_mas_barato(generador_productos):
    # NO MODIFICAR
    # Esta función duplica el generador
    generador_copia_1, generador_copia_2 = tee(generador_productos, 2)
    
    # COMPLETAR
    pass


generador_productos = cargar_productos('dcccafe.txt')
print(list(obtener_productos(generador_productos)))

generador_productos = cargar_productos('dcccafe.txt')
print(list(filtrar_por_categoria(generador_productos, 'cafe_frio')))

generador_productos = cargar_productos('dcccafe.txt')
print(list(buscar_mas_barato(generador_productos)))