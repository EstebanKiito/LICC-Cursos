from abc import ABC, abstractmethod
from random import randint
from threading import Thread, Lock, Event, Timer
from time import sleep


class Persona(ABC, Thread):

    # Completar

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.disponible = True
        self.trabajando = True
        self.daemon = True

    @abstractmethod
    def run(self):
        pass


class Cocinero(Persona):

    def __init__(self, nombre, cocina):
        super().__init__(nombre)
        self.lugar_trabajo = cocina
        # Completar

    def run(self):
        # Completar
        pass

    def cocinar(self):
        # Completar
        pass

    def sacar_plato(self):
        # Completar
        pass

    def buscar_ingredientes(self, plato, bodega, recetas):
        # Formato de los dicts entregados:
        # bodega = {
        #     "alimento_1": int cantidad_alimento_1,
        #     "alimento_2": int cantidad_alimento_2,
        # }
        # recetas = {
        #     "nombre_plato_1": [("ingrediente_1", "cantidad_ingrediente_1"),
        #                        ("ingrediente_2", "cantidad_ingrediente_2")],
        #     "nombre_plato_2": [("ingrediente_1", "cantidad_ingrediente_1"), 
        #                        ("ingrediente_2", "cantidad_ingrediente_2")]
        # }

        # Completar
        pass

    def agregar_plato(self, plato):
        # Completar
        pass


class Mesero(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
        # Completar

    def run(self):
        # Completar
        pass

    def agregar_pedido(self, pedido, cocina):
        # Completar
        pass

    def entregar_pedido(self, cocina):
        # Completar
        pass

    def pedido_entregado(self, pedido):
        # Completar
        pass
