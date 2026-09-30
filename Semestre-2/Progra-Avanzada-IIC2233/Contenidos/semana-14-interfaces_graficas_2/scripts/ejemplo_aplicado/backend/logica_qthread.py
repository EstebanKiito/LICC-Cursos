from PyQt6.QtCore import QObject, QThread, pyqtSignal
import backend.parametros_backend as p
import time


class Icono(QThread):
    # Atributo de clase para tener un ID distinto por ícono
    identificador = 0

    def __init__(self, x: int, y: int, ancho_ventana: int, tamaño: int,
                 velocidad: int, senal_mover: pyqtSignal) -> None:

        super().__init__()
        # Guardamos su ID y sumamos 1 al atributo de clase
        self.id = Icono.identificador
        Icono.identificador += 1

        # Guardamos los atributos
        self.ancho_ventana = ancho_ventana
        self.velocidad = velocidad
        self.tamaño = tamaño
        self.x = x
        self.y = y
        self.senal_mover = senal_mover

        # Definimos que inicialmente nos movemos a la derecha (1)
        self.direccion = 1
        self.correr = True

    # Método encargado de mover al cuadrado en cada "tick"
    def mover(self) -> None:
        # Aumento mi posición en el eje X según la velocidad que tenga
        self.x += self.direccion * self.velocidad

        # Si llegué al tope derecho de la ventana, ahora mi dirección
        # es a la izquierda (-1)
        if self.x + self.tamaño >= self.ancho_ventana:
            self.direccion = -1

        # Si llegué al tope izquierdo de la ventana, ahora mi dirección
        # es a la derecha (1)
        elif self.x <= 0:
            self.direccion = 1

        # Emito la señal para mover mi cuadrado
        self.senal_mover.emit(self.id, self.x, self.y)

    def run(self) -> None:
        # Mientras pueda correr
        while self.correr:
            # Me muevo y luego espero un poco de tiempo.
            self.mover()

            # Descanso los MS indicados. sleep recibe la cantidad en segundos
            # por lo tanto, debemos dividir por 1000 para transformar p.TIEMPO_MOVIMIENTO
            # en segundos
            time.sleep(p.TIEMPO_MOVIMIENTO / 1000)


class Juego(QObject):
    # Definimos 3 señales.
    # Esta avisa cuando empieza todo
    senal_empezar = pyqtSignal()
    # Esta avisa cuando un ícono se debe mover. Envía: ID, X, Y
    senal_mover_icono = pyqtSignal(int, int, int)
    # Esta avisa cuando un ícono debe aparecer en el frontend. Envía: ID, X, Y, Tamaño
    senal_aparecer_icono = pyqtSignal(int, int, int, int)

    def __init__(self, tamaño_ventana: list) -> None:
        super().__init__()
        # Guadamos los atributos
        self.ancho = tamaño_ventana[0]
        self.todos = {}

    # Empieza el backend a funcionar
    def empezar(self) -> None:
        # Creamos los íconos
        self.crear_iconos()
        # Avisamos al frontend que empiece su ejecución
        self.senal_empezar.emit()
        # A cada ícono creado, hacemos que empiece
        for icono in self.todos.values():
            icono.start()

    # Método encargado de crear cada cuadrado
    def crear_iconos(self) -> None:
        for cuadrado in p.CUADRADOS:
            x = 0
            y = cuadrado["y"]
            tamaño = cuadrado["tamaño"]
            velocidad = cuadrado["vel"]

            # A cada cuadrado (Icono) le digo
            # que su posición inicial en "x" es 0,
            # le doy los demás atributos y le paso la
            # señal "senal_mover_icono" para que pueda avisar
            # al frontend cada vez que se mueva
            icono = Icono(
                0,
                y,
                self.ancho,
                tamaño,
                velocidad,
                self.senal_mover_icono,
            )
            # Guardo el ícono en mi diccionario de todos
            self.todos[icono.id] = icono
            # Aviso al frontend que debe crear visualmente este cuadrado
            self.senal_aparecer_icono.emit(icono.id, x, y, tamaño)

    # Método encargado de detener al ícono
    def parar_icono(self, id_icono: int) -> None:
        icono = self.todos[id_icono]
        icono.correr = False
