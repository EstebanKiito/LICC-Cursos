import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QApplication, QWidget, QLabel


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # Configuramos los widgets de la interfaz
        self.label_w = QLabel("Presiona la tecla W", self)
        self.label_w_contador = QLabel("Presionada 0 veces", self)
        self.contador_w = 0

        self.label_a = QLabel("Presiona la tecla A", self)
        self.label_a_contador = QLabel("Presionada 0 veces", self)
        self.contador_a = 0

        self.label_w.setGeometry(10, 10, 230, 30)
        self.label_w_contador.setGeometry(10, 40, 230, 30)
        self.label_a.setGeometry(10, 100, 230, 30)
        self.label_a_contador.setGeometry(10, 130, 230, 30)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Ejemplo isAutoRepeat")
        self.setGeometry(50, 50, 250, 200)
        self.show()

    def keyPressEvent(self, evento: QKeyEvent) -> None:
        if evento.key() == Qt.Key.Key_W:
            self.contador_w += 1
            self.label_w_contador.setText(f"Presionada {self.contador_w} veces")

        if evento.key() == Qt.Key.Key_A and not evento.isAutoRepeat():
            self.contador_a += 1
            self.label_a_contador.setText(f"Presionada {self.contador_a} veces")


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
