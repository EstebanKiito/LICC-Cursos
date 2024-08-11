from PyQt6.QtCore import Qt, pyqtSignal, QUrl
from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QIcon, QAction, QMouseEvent
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from os.path import join
import frontend.parametros_frontend as p
import sys


class IconoClickeable(QLabel):
    senal_click = pyqtSignal(str)

    def __init__(self, tipo: str, parent):
        super().__init__(parent=parent)
        self.tipo = tipo

    # TODO: QLabel especial que avisará cuando hagamos click en él
    def mousePressEvent(self, evento: QMouseEvent):
        # Cada vez que me hagan click, emitiré una señal con el tipo de icono
        # que soy: anticucho, choripan o empanaa
        self.senal_click.emit(self.tipo)


class FondoClickeable(QLabel):
    senal_click = pyqtSignal(int, int)

    def __init__(self, parent):
        super().__init__(parent=parent)

    # TODO: QLabel especial que avisará la posición del click que hagan sobre él
    def mousePressEvent(self, evento: QMouseEvent):
        x = evento.pos().x()
        y = evento.pos().y()
        if evento.button() == Qt.MouseButton.LeftButton:
            self.senal_click.emit(x, y)


class VentanaSimulacion(QMainWindow):
    senal_click_pantalla = pyqtSignal(int, int, str)
    senal_empezar = pyqtSignal()

    def __init__(self, tamaño_simulacion: list, tamaño_icono: int):
        super().__init__()
        self.ancho_simulacion = tamaño_simulacion[0]
        self.largo_simulacion = tamaño_simulacion[1]
        self.tamaño_icono = tamaño_icono

        ancho_ventana = self.ancho_simulacion + p.PADDING + p.ANCHO_ZONA_BOTONES
        self.setWindowTitle("Choripan --> Anticucho --> Empanada --> Choripan")
        self.setGeometry(300, 100, ancho_ventana, self.largo_simulacion + p.PADDING)

        # QLabel para el Background. No editar
        self.background = FondoClickeable(self)
        self.background.setStyleSheet(f"background: {p.COLOR_FONDO};")
        self.background.setGeometry(0, 0, self.ancho_simulacion, self.largo_simulacion)
        self.background.senal_click.connect(self.agregar_icono)

        self.labels = {}  # id: label
        self.pixmaps = {
            "anticucho": QPixmap(join("frontend", "sprites", "anticucho.png")),
            "empanada": QPixmap(join("frontend", "sprites", "empanada.png")),
            "choripan": QPixmap(join("frontend", "sprites", "choripan.png")),
            "comida4": QPixmap(join("frontend", "sprites", "comida4.png")),
        }

        for index, tipo in enumerate(["anticucho", "empanada", "choripan", "comida4"]):
            icono = IconoClickeable(tipo, self)
            icono.setPixmap(self.pixmaps[tipo])
            icono.setScaledContents(True)
            icono.setGeometry(
                self.ancho_simulacion + p.PADDING,  # x
                p.PADDING + index * self.tamaño_icono,  # y
                self.tamaño_icono - 10,  # ancho un poquito más pequeño que el original
                self.tamaño_icono - 10,  # largo un poquito más pequeño que el original
            )
            icono.senal_click.connect(self.seleccionar)

        self.ultimo_seleccionado = None

        # TODO: Agregar una opción a la barra del menú e incluir la acción.
        # esta acción llama al método juego
        empezar = QAction(QIcon(None), "Empezar", self)
        menu = self.menuBar().addMenu("OWOWOWO")
        menu.addAction(empezar)
        empezar.triggered.connect(self.empezar_simulacion)

        # Vamos a crear una segunda acción para detener la música
        parar_musica = QAction(QIcon(None), "STOP", self)
        menu.addAction(parar_musica)
        parar_musica.triggered.connect(self.detener_musica)

        # TODO: Crear reproductor de música
        file_url = QUrl.fromLocalFile(join("frontend", "sprites", "sountrack.mp3"))
        self.media_player = QMediaPlayer(self)
        self.media_player.setAudioOutput(QAudioOutput(self))
        self.media_player.setSource(file_url)

    def detener_musica(self):
        self.media_player.stop()

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key.Key_Space:
            self.empezar_simulacion()

        elif event.key() == Qt.Key.Key_Q:
            # Alternativa funcional pero mala practica
            sys.exit()
            # Lo Optimo y CORRECTO es
            # 1. Mandar señal al backend de fin de la simluación
            # 2. Cerrar ventana
            # 3. Que backend detenga cada Thread

    def empezar_simulacion(self):
        self.senal_empezar.emit()
        # TODO: Comenzar a reproducir música
        self.media_player.play()

    def agregar_icono(self, x: int, y: int):
        if self.ultimo_seleccionado is not None:
            self.senal_click_pantalla.emit(x, y, self.ultimo_seleccionado)

    def seleccionar(self, tipo: str):
        self.ultimo_seleccionado = tipo

    def actualizar_tiempo(self, segundos: int):
        texto = f"Han pasado {segundos} segundos"
        self.statusBar().showMessage(texto)

    def aparecer_icono(self, id_icono: int, x: int, y: int, tipo: str):
        label = QLabel(self.background)
        label.setStyleSheet("background: transparent;")
        label.setPixmap(self.pixmaps[tipo])
        label.setScaledContents(True)
        label.setGeometry(x, y, self.tamaño_icono, self.tamaño_icono)

        self.labels[id_icono] = label
        label.show()

    def actualizar_icono(self, id_icono: int, nuevo_tipo: str):
        label: QLabel = self.labels[id_icono]
        label.setPixmap(self.pixmaps[nuevo_tipo])
        label.setScaledContents(True)
        label.show()

    def mover_icono(self, id_icono: int, x: int, y: int):
        label: QLabel = self.labels[id_icono]
        label.move(x, y)
