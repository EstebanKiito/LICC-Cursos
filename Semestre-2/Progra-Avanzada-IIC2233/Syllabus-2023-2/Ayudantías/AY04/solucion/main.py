from lectura_archivo import cargar_ingredientes, cargar_pedidos, generar_bodega
from entidades import Cocinero, Mesero
from cocina import Cocina
from time import sleep
from threading import Thread
from os import path
print("*** Bienvenido a Restaurant DCChef ***")

dict_ingredientes = cargar_ingredientes(path.join("data", "ingredientes.csv"))
bodega = generar_bodega(dict_ingredientes)
dccRestaurant = Cocina(bodega, recetas=dict_ingredientes)
cocineros = [Cocinero(x, dccRestaurant) for x in ('Cleme', 'Carlanga',
                                                  'Pipe', 'Cata', "Pato")]
meseros = [Mesero(x) for x in (f'Mesero {i}' for i in range(1, 10))]

dccRestaurant.meseros = meseros
dccRestaurant.cocineros = cocineros

dccRestaurant.iniciar_threads()
thread_cocineros = Thread(target=dccRestaurant.asignar_cocinero)
thread_meseros = Thread(target=dccRestaurant.asignar_mesero)
thread_cocineros.start()
thread_meseros.start()

for pedido in cargar_pedidos(path.join("data","pedidos.csv")):
    print('un nuevo pedido de la mesa {} acaba de llegar'.format(pedido[0]))
    items = pedido[1::][0]

    'Modificar Abajo de esa Linea'
    sleep(1)
    print('buscando Mesero')
    mesero_encontrado = False
    while not mesero_encontrado:
        for mesero in dccRestaurant.meseros:
            
            if mesero.evento_manejar_pedido.is_set() and not mesero_encontrado:
                print('Encontramos un mesero, {}'.format(mesero.nombre))
                mesa_id = pedido[0]
                mesero_encontrado = True
                for item in items:
                    mesero.agregar_pedido((mesa_id, item,), dccRestaurant)

    'Modificar Arriba de esa Linea'
dccRestaurant.abierta = False
