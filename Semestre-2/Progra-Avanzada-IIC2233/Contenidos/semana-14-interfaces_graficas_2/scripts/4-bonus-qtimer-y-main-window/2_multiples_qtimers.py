import sys
from PyQt6.QtCore import pyqtSignal, QObject, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MiTimer(QObject):
    senal_actualizar = pyqtSignal(int, str)

    def __init__(self, indice: int, tiempo: float) -> None:
        super().__init__()
        self.indice = indice
        self.tiempo = tiempo
        self.indice_actual = 0
        self.timer = QTimer(self)

        # Acá se asigna el tiempo de duración del periodo entre ejecuciones
        self.timer.setInterval(int(tiempo * 1000))
        # Acá se conecta la subrutina que se ejecutará
        self.timer.timeout.connect(self.enviar_dato)

    def enviar_dato(self) -> None:
        if self.indice_actual <= 9:
            self.senal_actualizar.emit(self.indice, str(self.indice_actual))
            self.indice_actual += 1
        else:
            self.senal_actualizar.emit(self.indice, "Status: Qtimer terminado")
            self.timer.stop()

    def comenzar(self) -> None:
        self.timer.start()

    def sigue_andando(self) -> bool:
        return self.timer.isActive()


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.timers = []
        self.init_gui()

    def init_gui(self) -> None:
        # Configuramos los widgets de la interfaz
        # Definimos un montón de labels que corresponderán a un Qtimer cada uno
        self.labels = {i: QLabel("Status: esperando Qtimer", self) for i in range(1, 6)}
        self.boton = QPushButton("Ejecutar Qtimers", self)
        self.boton.clicked.connect(self.ejecutar_timers)

        for i in range(1, 6):
            self.labels[i].setGeometry(10, (i - 1) * 30, 230, 30)

        self.boton.setGeometry(10, 150, 230, 30)
        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Ejemplo Qtimers")
        self.setGeometry(50, 50, 250, 200)
        self.show()

    def ejecutar_timers(self) -> None:
        """
        Este método crea cinco timers cada vez que se presiona el botón en la
        interfaz. Los timers recibirán como argumento el índice del label
        que les corresponde y el tiempo que toman entre cada iteración.
        """
        for timer in self.timers:
            if timer.sigue_andando():
                return

        self.timers = []
        for i in range(1, 6):
            timer = MiTimer(i, i / 10)
            # Se conecta la señal emitida por el timer a un método
            # de la ventana
            timer.senal_actualizar.connect(self.actualizar_labels)
            self.timers.append(timer)
            timer.comenzar()

    def actualizar_labels(self, indice: int, texto: str) -> None:
        """
        Este método actualiza el label correspondiente según los datos
        enviados desde un timer a través del índice y aplica el texto.
        """
        self.labels[indice].setText(texto)


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
