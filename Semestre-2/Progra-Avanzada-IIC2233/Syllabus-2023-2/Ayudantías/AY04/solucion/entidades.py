from abc import ABC, abstractmethod
from random import randint
from threading import Thread, Lock, Event, Timer
from time import sleep


class Persona(ABC, Thread):

    lock_bodega = Lock()
    lock_cola_pedidos = Lock()
    lock_cola_pedidos_listos = Lock()

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
        self.evento_plato_asignado = Event()

    def run(self):
        """
        Se queda esperando que la cocina le asigne un plato (evento),
        y luego lo cocina.
        """

        while self.trabajando:
            self.evento_plato_asignado.wait()
            tiempo_cocinar = randint(1, 3)
            sleep(tiempo_cocinar)
            self.cocinar()

    def cocinar(self):
        self.disponible = False
        plato = self.sacar_plato()

        print(f"Cocinero {self.nombre} cocinando {plato[1]}...")
        self.buscar_ingredientes(plato,
                                 self.lugar_trabajo.bodega,
                                 self.lugar_trabajo.recetas)
        sleep(randint(1, 3))
        self.agregar_plato(plato)

        self.evento_plato_asignado.clear()
        self.disponible = True

    def sacar_plato(self):
        with self.lock_cola_pedidos:
            plato = self.lugar_trabajo.cola_pedidos.pop(0)
            return plato

    def buscar_ingredientes(self, plato, bodega, recetas):
        """
        De debe acceder a la bodega con un lock y, en base a los ingredientes
        de un plato, disminuir la cantidad de ingredientes disponible.
        """
        # bodega = {
        #     "alimento_1": int cantidad_alimento_1,
        #     "alimento_2": int cantidad_alimento_2,
        # }

        # recetas = {
        #     "nombre_plato_1": [("ingrediente_1", cantidad_ingrediente_1),
        #                        ("ingrediente_2", cantidad_ingrediente_2)],
        #     "nombre_plato_2": [("ingrediente_1", cantidad_ingrediente_1), 
        #                        ("ingrediente_2", cantidad_ingrediente_2)]
        # }

        print(f"Cocinero {self.nombre} buscando los ingredientes en la bodega....")
        with self.lock_bodega:
            ingredientes = recetas[plato[1]]
            for ingrediente in ingredientes:
                nombre_ingrediente = ingrediente[0]
                cantidad_ingrediente = int(ingrediente[1])
                bodega[nombre_ingrediente] -= cantidad_ingrediente
                print(f"Cocinero {self.nombre} sacando {cantidad_ingrediente}")
                print(f'ahora existen {nombre_ingrediente}: {bodega[nombre_ingrediente]} ingredientes en la bodega')

    def agregar_plato(self, plato):
        with self.lock_cola_pedidos_listos:
            self.lugar_trabajo.cola_pedidos_listos.append(plato)


class Mesero(Persona):


    def __init__(self, nombre):
        super().__init__(nombre)
        self.evento_manejar_pedido = Event()

    def run(self):
        """        
        Mientras esté trabajando,
        - Si está disponible y hay pedidos por entregar: entregar_pedido
        - Si no hay pedidos por entregar puede tomar un nuevo pedido.
        La prioridad es entregar los pedidos antes que tomar uno nuevo.
        """
        while self.trabajando:
            if self.disponible:
                self.evento_manejar_pedido.set()

    def agregar_pedido(self, pedido, cocina):
        """
        pedidos = (str plato1, str plato2, str plato3, ...)
        Con lock agregar pedidos a la cola de la cocina
        """
        self.evento_manejar_pedido.clear()
        sleep(randint(1, 2))
        with self.lock_cola_pedidos:
            cocina.cola_pedidos.append(pedido)
        self.evento_manejar_pedido.set()

    def entregar_pedido(self, cocina):
        """
        Simular que el mesero lleva un pedido a la mesa.
        Debe reflejarse que el mesero está ocupado haciendo esto
        y que se demora cierto tiempo en hacerlo (sleep, timer, etc.)
        """
        self.evento_manejar_pedido.clear()
        tiempo_entrega = randint(1, 3)
        with self.lock_cola_pedidos_listos:
            pedido = cocina.cola_pedidos_listos.pop(0)
            timer_entrega = Timer(tiempo_entrega,
                                  self.pedido_entregado,
                                  args=(pedido,))
            timer_entrega.start()
            print(f"Mesero {self.nombre} entregando pedido a la mesa {pedido[0]}...")

    def pedido_entregado(self, pedido):
        print(f"El plato {pedido[1]} de la mesa {pedido[0]} fue entregado")
        self.evento_manejar_pedido.set()
