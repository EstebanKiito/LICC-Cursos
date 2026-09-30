import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit)


class VentanaPresionable(QWidget):
    """
    Creamos las señales como atributos de clase.
    """
    senal_simple = pyqtSignal()                 # Señal simple.
    senal_texto = pyqtSignal(str)               # Señal que permite enviar texto.
    senal_coordenadas = pyqtSignal(int, int)    # Señal que permite enviar dos ints.

    def __init__(self) -> None:
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self) -> None:
        self.label = QLabel('Presiona esta ventana', self)
        self.label.move(20, 10)
        self.label.resize(self.label.sizeHint())

        self.etiqueta = QLineEdit(self)
        self.etiqueta.move(20, 60)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emite señal')
        self.setMouseTracking(True)
        self.show()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Se emite la señal simple, sin argumento.
        """
        self.senal_simple.emit()
        """
        Se emite la señal que permite enviar un str. El contenido de la señal,
        será el texto que contenga la etiqueta de la ventana.
        """
        self.senal_texto.emit(self.etiqueta.text())

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Se emite la señal que permite enviar dos ints,
        enviamos la posición del mouse.
        """
        self.senal_coordenadas.emit(event.pos().x(), event.pos().y())


class VentanaQueSeEdita(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self) -> None:
        self.etiqueta_1 = QLabel('', self)
        self.etiqueta_1.move(20, 10)
        self.etiqueta_1.resize(self.etiqueta_1.sizeHint())

        self.etiqueta_2 = QLabel('', self)
        self.etiqueta_2.move(20, 40)
        self.etiqueta_2.resize(self.etiqueta_2.sizeHint())

        self.etiqueta_3 = QLabel('', self)
        self.etiqueta_3.move(20, 70)
        self.etiqueta_3.resize(self.etiqueta_3.sizeHint())

        self.setGeometry(700, 300, 290, 150)
        self.setWindowTitle('Recibe señal')
        self.show()

    def edita_etiqueta_click(self) -> None:
        """
        Este método no tiene argumentos,
        ya que se conectará a una señal simple.
        """
        self.etiqueta_1.setText('¡Oh! Alguien ha presionado el mouse')
        self.etiqueta_1.resize(self.etiqueta_1.sizeHint())

    def edita_etiqueta_texto(self, texto) -> None:
        """
        Este método tiene un argumento,
        el str que se espera del evento conectado.
        """
        self.etiqueta_2.setText(f'Recibí del evento: {texto}')
        self.etiqueta_2.resize(self.etiqueta_2.sizeHint())

    def edita_etiqueta_posicion_mouse(self, x, y) -> None:
        """
        Este método tiene dos argumentos,
        los ints que se espera del evento conectado.
        """
        self.etiqueta_3.setText(f'Recibí posiciones: {x}, {y}')
        self.etiqueta_3.resize(self.etiqueta_3.sizeHint())


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    ventana_click = VentanaPresionable()
    ventana_edit = VentanaQueSeEdita()

    """
    Conectamos la señal con el método que cada una debe activar.
    """
    ventana_click.senal_simple.connect(ventana_edit.edita_etiqueta_click)
    ventana_click.senal_texto.connect(ventana_edit.edita_etiqueta_texto)
    ventana_click.senal_coordenadas.connect(ventana_edit.edita_etiqueta_posicion_mouse)

    sys.exit(app.exec())
