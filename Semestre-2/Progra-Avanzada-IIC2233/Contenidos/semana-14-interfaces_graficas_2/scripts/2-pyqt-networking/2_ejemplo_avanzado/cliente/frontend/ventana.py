from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
from PyQt6.QtCore import pyqtSignal


class MainWindow(QMainWindow):
    senal_mandar_comando = pyqtSignal(str)
    senal_pedir_hora = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Conversa con el servidor")
        self.setGeometry(100, 100, 400, 300)

        self.etiqueta = QLabel(self)
        self.etiqueta.setGeometry(50, 50, 200, 100)

        self.button = QPushButton("Adelantar 1 hora", self)
        self.button.setGeometry(20, 160, 150, 30)
        self.button.clicked.connect(self.adelantar)

        self.button2 = QPushButton("Atrasar 1 hora", self)
        self.button2.setGeometry(180, 160, 150, 30)
        self.button2.clicked.connect(self.retrasar)

        self.button3 = QPushButton("Hora en Chile", self)
        self.button3.setGeometry(20, 200, 150, 30)
        self.button3.clicked.connect(self.hora_chile)

        self.button4 = QPushButton("Hora en Japón", self)
        self.button4.setGeometry(180, 200, 150, 30)
        self.button4.clicked.connect(self.hora_japon)

    def adelantar(self) -> None:
        self.senal_mandar_comando.emit("adelantar")

    def retrasar(self) -> None:
        self.senal_mandar_comando.emit("retrasar")

    def hora_chile(self) -> None:
        self.senal_pedir_hora.emit("chile")

    def hora_japon(self) -> None:
        self.senal_pedir_hora.emit("japón")

    def actualizar_etiqueta(self, text: str) -> None:
        self.etiqueta.setText(text)
        self.etiqueta.resize(self.etiqueta.sizeHint())


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
