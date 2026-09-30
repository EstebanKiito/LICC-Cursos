from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
from PyQt6.QtCore import pyqtSignal


# Nótese que la ventana del frontend no presenta nada nuevo de esta semana.
# Esto es ya que debido a la separación frontend-backend, el frontend no incluye
# nada de lógica del programa, lo que también incluye comunicación.
class MainWindow(QMainWindow):
    senal_mandar_comando = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Conversa con el servidor")
        self.setGeometry(100, 100, 400, 200)

        self.etiqueta = QLabel(self)
        self.etiqueta.setGeometry(50, 50, 200, 100)

        self.button = QPushButton("Saludame", self)
        self.button.setGeometry(20, 160, 150, 30)
        self.button.clicked.connect(self.pedir_palabra)

        self.button2 = QPushButton("Dame un color", self)
        self.button2.setGeometry(180, 160, 150, 30)
        self.button2.clicked.connect(self.pedir_color)

    def pedir_palabra(self) -> None:
        self.senal_mandar_comando.emit("palabra")

    def pedir_color(self) -> None:
        self.senal_mandar_comando.emit("color")

    def actualizar_etiqueta(self, text: str) -> None:
        self.etiqueta.setText(text)
        self.etiqueta.resize(self.etiqueta.sizeHint())


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
