from entidades import Cocinero, Mesero
from time import sleep
from random import randint


class Cocina:

    def __init__(self, bodega, recetas):
        super().__init__()
        self.cola_pedidos = list()
        self.cola_pedidos_listos = list()
        self.cocineros = []
        self.meseros = []
        self.bodega = bodega
        self.recetas = recetas
        self.abierta = True

    def iniciar_threads(self):
        # Completar
        pass

    def asignar_cocinero(self):
        # Completar
        pass

    def asignar_mesero(self):
        # Completar
        pass

    def finalizar_jornada_laboral(self):
        for mesero in self.meseros:
            mesero.trabajando = False

        for cocinero in self.cocineros:
            cocinero.trabajando = False
