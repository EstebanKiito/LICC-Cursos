from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPixmap, QColor, QMouseEvent
from PyQt6.QtCore import pyqtSignal, Qt
import frontend.parametros_frontend as p


# Creamos una clase que hereda de QLabel
# Esta clase detecta cuando le hacemos click en ella y emite una señal
class IconoClickeable(QLabel):
    # Señal que avisa que el QLabel fue seleccionado por el click
    # derecho del mouse. Envía el ID del QLabel
    senal_click = pyqtSignal(int)

    def __init__(self, parent: QWidget, id: int) -> None:
        super().__init__(parent=parent)
        self.id = id

    # Hacemos overriding de mousePressEvent para detectar cuando
    # presionamos este QLabel
    def mousePressEvent(self, evento: QMouseEvent) -> None:
        # Si el click es el mouse derecho, emito la señal
        if evento.button() == Qt.MouseButton.LeftButton:
            self.senal_click.emit(self.id)


class Ventana(QWidget):
    # Señal para avisar al backend que debe detener el movimiento de un rectangulo
    senal_parar_icono = pyqtSignal(int)

    def __init__(self, tamaño_ventana: list) -> None:
        super().__init__()

        self.ancho = tamaño_ventana[0]
        self.largo = tamaño_ventana[1]

        # Definimos tamaño y título de la ventana
        self.setGeometry(100, 100, self.ancho, self.largo)
        self.setWindowTitle("Ejemplo Aplicado")

        # Definimos QLabel para el fondo de la ventana
        self.background = QLabel(self)
        self.background.setStyleSheet(f"background: {p.COLOR_FONDO};")
        self.background.setGeometry(0, 0, self.ancho, self.largo)

        # Diccionario para guardar cada labels
        self.labels = {}

    # Método encargado de hacer "show" del label y la ventana
    def empezar(self) -> None:
        self.background.show()
        self.show()

    # Método encargado de crear un QLabel
    def aparecer_icono(self, id_icono: int, x: int, y: int, tamaño: int) -> None:
        # Creamos nuestro label (IconoClickeable) y definimos su posición y tamaño
        label = IconoClickeable(self, id_icono)
        label.setGeometry(x, y, tamaño, tamaño)
        # Luego guardamos el label en nuestro diccionario
        self.labels[id_icono] = label

        # Conectamos su señal con nuestro método "parar_icono"
        label.senal_click.connect(self.parar_icono)

        # Creamos un QPimaxo
        pixmap = QPixmap(tamaño, tamaño)
        # Pintamos el QPixmap
        pixmap.fill(QColor(255, 0, 0))
        # Le damos el QPixmap al label
        label.setPixmap(pixmap)

        # Mostramos el label
        label.show()

    # Método encargado de mover un QLabel
    def mover_icono(self, id_icono: int, x: int, y: int) -> None:
        # Buscamos el label a mover
        label = self.labels[id_icono]

        # Movemos el label
        label.move(x, y)

    # Método encargado de parar un QLabel
    def parar_icono(self, id_icono: int) -> None:
        # Buscamos el label a detener
        label = self.labels[id_icono]

        # Tomamos el QPixmap de dicho label
        pixmap = label.pixmap()
        # Le cambiamos el color
        pixmap.fill(QColor(0, 255, 0))
        # se lo devolvemos al QLabel
        label.setPixmap(pixmap)

        # Avisamos al backend que detenga su movimiento
        self.senal_parar_icono.emit(id_icono)
