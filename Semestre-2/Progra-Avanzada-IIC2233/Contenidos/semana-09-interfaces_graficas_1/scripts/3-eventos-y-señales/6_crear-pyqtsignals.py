import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QApplication, QWidget, QLabel


class VentanaPresionable(QWidget):
    """
    Creamos una señal como atributo de clase.
    """
    senal_escribir = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self) -> None:
        self.etiqueta = QLabel('Presiona esta ventana', self)
        self.etiqueta.move(20, 10)
        self.etiqueta.resize(self.etiqueta.sizeHint())

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emite señal')
        self.show()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Al ejecutar la siguiente línea, se emite la señal,
        y los métodos conectados se llamarán automáticamente.
        """
        self.senal_escribir.emit()


class VentanaQueSeEdita(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self) -> None:
        self.etiqueta = QLabel('', self)
        self.etiqueta.move(20, 10)
        self.etiqueta.resize(self.etiqueta.sizeHint())

        self.setGeometry(700, 300, 290, 150)
        self.setWindowTitle('Recibe señal')
        self.show()

    # Este es el método que conectaremos a la señal
    def edita_etiqueta(self) -> None:
        self.etiqueta.setText('¡Oh! Alguien ha presionado el mouse')
        self.etiqueta.resize(self.etiqueta.sizeHint())


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    ventana_click = VentanaPresionable()
    ventana_edit = VentanaQueSeEdita()

    """
    Conectamos la señal con el método que debe activar.
    """
    ventana_click.senal_escribir.connect(ventana_edit.edita_etiqueta)

    sys.exit(app.exec())
