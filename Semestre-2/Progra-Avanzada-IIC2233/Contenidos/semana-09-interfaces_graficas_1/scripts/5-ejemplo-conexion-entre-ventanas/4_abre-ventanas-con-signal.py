import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import pyqtSignal


class Ventana(QWidget):
    # Otra señal para avisar a una segunda ventana.
    senal_abrir_otra_ventana = pyqtSignal()

    def __init__(self, titulo: str, x: int, y: int) -> None:
        super().__init__()
        # Definimos lo básico de la ventana.
        self.setWindowTitle(titulo)
        self.setGeometry(x, y, 200, 50)

        # Creamos botón que se conecta a método self.abrir_otra_ventana.
        self.boton = QPushButton("Abrir otra ventana", self)
        self.boton.clicked.connect(self.abrir_otra_ventana)

    def abrir_otra_ventana(self) -> None:
        self.hide()
        self.senal_abrir_otra_ventana.emit()


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])

    # Instanciamos dos ventanas distintas. Cada una comienza con una señal
    # propia que le permite ser abierta por otra.
    ventana_1 = Ventana("Inicial", 100, 100)
    ventana_2 = Ventana("Alternativa", 500, 100)

    ventana_1.senal_abrir_otra_ventana.connect(ventana_2.show)
    ventana_2.senal_abrir_otra_ventana.connect(ventana_1.show)

    ventana_1.show()
    sys.exit(app.exec())
