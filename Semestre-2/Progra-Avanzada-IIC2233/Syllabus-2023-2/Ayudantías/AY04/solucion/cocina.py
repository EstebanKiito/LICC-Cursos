from collections import deque
from entidades import Cocinero, Mesero
from time import sleep
from random import randint,shuffle

class Cocina():

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
        for mesero in self.meseros:
            mesero.start()

        for cocinero in self.cocineros:
            cocinero.start()

    def asignar_cocinero(self):
        while self.abierta:
            sleep(1)
            if self.cola_pedidos:
                cocinero_asignado = False
                for cocinero in self.cocineros:
                    if cocinero.disponible and not cocinero_asignado:
                        cocinero.evento_plato_asignado.set()
                        cocinero_asignado = True

    def asignar_mesero(self):
        while self.abierta:
            sleep(1)
            if self.cola_pedidos_listos:
                mesero_asignado = False
                shuffle(self.meseros)
                for mesero in self.meseros:
                    if mesero.disponible and not mesero_asignado:
                        mesero.evento_manejar_pedido.set()
                        mesero.entregar_pedido(self)
                        mesero_asignado = True
        self.finalizar_jornada_laboral()

    def finalizar_jornada_laboral(self):

        for mesero in self.meseros:
            mesero.trabajando = False

        for cocinero in self.cocineros:
            cocinero.trabajando = False