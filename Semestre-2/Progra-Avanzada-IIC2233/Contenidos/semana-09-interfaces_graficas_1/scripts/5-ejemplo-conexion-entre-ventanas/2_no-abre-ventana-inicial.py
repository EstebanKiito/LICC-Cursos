import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Ventana(QWidget):
    def __init__(self, titulo: str, x: int, y: int, otra_ventana: QWidget | None = None) -> None:
        super().__init__()
        self.otra_ventana = otra_ventana
        self.setWindowTitle(titulo)
        self.setGeometry(x, y, 200, 50)
        self.boton = QPushButton("Abrir otra ventana", self)
        self.boton.clicked.connect(self.abrir_otra_ventana)

    def abrir_otra_ventana(self) -> None:
        if self.otra_ventana is not None:
            self.hide()  # Esconder la ventana actual
            self.otra_ventana.show()  # Mostrar otra ventana


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    # Segunda ventana se crea antes de forma independiente
    otra_ventana = Ventana("Otra ventana", 300, 100)
    # Ventana inicial recibe como argumento a otra_ventana
    ventana = Ventana("Inicial", 100, 100, otra_ventana)
    ventana.show()
    sys.exit(app.exec())
