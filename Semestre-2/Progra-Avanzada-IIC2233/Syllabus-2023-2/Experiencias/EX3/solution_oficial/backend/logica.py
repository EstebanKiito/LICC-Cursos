from PyQt6.QtCore import QObject, QTimer, pyqtSignal
import backend.parametros_backend as p
import backend.utils as utils
import random


class Icono(QObject):
    # Señal **interna** del backend para notificar el choque.
    # Manda el id del chocado y el nuevo tipo que debe ser.
    senal_choque = pyqtSignal(int, str)

    identificador = 0

    def __init__(
        self,
        x: int,
        y: int,
        tipo: str,
        ancho_simulacion: int,
        largo_simulacion: int,
        tamaño: int,
        senal_mover: pyqtSignal,
    ):
        super().__init__()
        self.id = Icono.identificador
        Icono.identificador += 1
        self.ancho_simulacion = ancho_simulacion
        self.largo_simulacion = largo_simulacion
        self.tamaño = tamaño
        self.tipo = tipo
        self.senal_mover = senal_mover
        self._x = int(x - tamaño / 2)  # Esquina del icono
        self._y = int(y - tamaño / 2)  # Esquina del icono
        self.otros_enemigos = []

        # TODO: Crear QTimer para mover el ícono cada p.TIEMPO_MOVIMIENTO
        self.timer_movimiento = QTimer(self)
        self.timer_movimiento.setInterval(p.TIEMPO_MOVIMIENTO)
        self.timer_movimiento.timeout.connect(self.mover)

    @property
    def x(self):
        return self._x

    @property
    def centro_x(self):
        return int(self._x + self.tamaño / 2)

    @x.setter
    def x(self, nuevo_x: int):
        x = utils.acotar_numero(nuevo_x, 0, self.ancho_simulacion - self.tamaño)
        self._x = int(x)

    @property
    def y(self):
        return self._y

    @property
    def centro_y(self):
        return int(self._y + self.tamaño / 2)

    @y.setter
    def y(self, nuevo_y):
        y = utils.acotar_numero(nuevo_y, 0, self.largo_simulacion - self.tamaño)
        self._y = int(y)

    def mover(self):
        enemigo_actual = None
        distancia_actual = float("inf")  # Valor muy grande
        # Encontrar al enemigo más cercano
        for enemigo in self.otros_enemigos:
            if enemigo.tipo == self.tipo:
                continue
            nueva_distancia = utils.distancia(self, enemigo)
            if nueva_distancia < distancia_actual:
                enemigo_actual = enemigo
                distancia_actual = max(nueva_distancia, 0.0000001)

        # Si es que hay algún enemigo, veo si acercame o alejarme
        if enemigo_actual is not None:
            dx = self.centro_x - enemigo_actual.centro_x
            dy = self.centro_y - enemigo_actual.centro_y
            if utils.gano_yo(self, enemigo_actual):
                # Me acerco a él
                nuevo_x = self.x - p.DELTA_ACERCARSE * (dx / distancia_actual)
                nuevo_y = self.y - p.DELTA_ACERCARSE * (dy / distancia_actual)
                if distancia_actual < (self.tamaño / 2 + enemigo_actual.tamaño / 2):
                    # Alcancé a mi enemigo
                    self.senal_choque.emit(enemigo_actual.id, self.tipo)
            else:
                # Me alejo a él
                nuevo_x = self.x + p.DELTA_HUIR * (dx / distancia_actual)
                nuevo_y = self.y + p.DELTA_HUIR * (dy / distancia_actual)

            self.x = nuevo_x
            self.y = nuevo_y
            # Aviso mi nueva posición.
            self.senal_mover.emit(self.id, self.x, self.y)


class ControladorLogico(QObject):
    # Señal que manda posición del icono. Manda id, x, y
    senal_mover_icono = pyqtSignal(int, int, int)
    # Señal para actualizar imagen de un icono. Manda id y el tipo
    senal_actualizar_icono = pyqtSignal(int, str)
    # Señal para crear un icono, manda id, x, y, tipo
    senal_aparecer_icono = pyqtSignal(int, int, int, str)
    # Señal para actualizar el tiempo, manda el tiempo como int
    senal_actualizar_tiempo = pyqtSignal(int)

    def __init__(self, tamaño_simulacion: list, tamaño_icono: int):
        super().__init__()
        self.ancho_simulacion = tamaño_simulacion[0]
        self.largo_simulacion = tamaño_simulacion[1]
        self.tamaño_icono = tamaño_icono
        self.segundos = 0
        self.empece = False
        self.iconos = {}

        # TODO: Crear QTimer para actualizar el tiempo cada 1 segundo
        self.timer_simulacion = QTimer(self)
        self.timer_simulacion.setInterval(1000)  # 1 segundo
        self.timer_simulacion.timeout.connect(self.actualizar_tiempo)

    def actualizar_tiempo(self):
        # TODO: Cada vez que se ejecuta este método, pasa 1 segundo y
        # se actualiza el tiempo en frontend
        self.segundos += 1
        self.senal_actualizar_tiempo.emit(self.segundos)

    def empezar(self):
        self.empece = True
        # TODO: Comenzar Qtimer de simulación y que todos los íconos tambien partan
        # con su movimiento
        self.timer_simulacion.start()
        for icono in self.iconos.values():
            icono.otros_enemigos = list(self.iconos.values())
            icono.timer_movimiento.start()

    def click_pantalla(self, x: int, y: int, tipo: str):
        if self.empece:
            return

        # TODO: Completar para crear una instancia de Icono, guardarlo en "todos"
        # y avisar a frontned que aparezca el ícono en pantalla.
        icono = Icono(
            x,
            y,
            tipo,
            self.ancho_simulacion,
            self.largo_simulacion,
            self.tamaño_icono,
            self.senal_mover_icono,
        )
        self.iconos[icono.id] = icono
        icono.senal_choque.connect(self.choque)
        self.senal_aparecer_icono.emit(icono.id, icono.x, icono.y, tipo)

    def choque(self, enemigo_id: int, tipo: str):
        self.iconos[enemigo_id].tipo = tipo
        # TODO: Avisar que se debe actualizar la imagen del icono correspondiente.
        self.senal_actualizar_icono.emit(enemigo_id, tipo)

    def poblar_random(self):
        for _ in range(p.CANTIDAD_RANDOM):
            x = random.randint(0, self.ancho_simulacion - self.tamaño_icono)
            y = random.randint(0, self.largo_simulacion - self.tamaño_icono)
            tipo = random.choice(["anticucho", "empanada", "choripan"])
            self.click_pantalla(x, y, tipo)
