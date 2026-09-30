import sys
from time import sleep
from PyQt6.QtCore import pyqtSignal, QThread, QMutex
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MiThread(QThread):
    # Se define para la clase MiThread,
    # para que cada instancia tenga una propia
    senal_actualizar = pyqtSignal(int, str)

    def __init__(self, indice: int, tiempo: float, mutex: QMutex) -> None:
        super().__init__()
        self.indice = indice
        self.tiempo = tiempo
        self.mutex = mutex

    def run(self) -> None:
        self.mutex.lock()
        for i in range(10):
            sleep(self.tiempo)
            self.senal_actualizar.emit(self.indice, str(i) + " - crítico")
        self.mutex.unlock()

        for i in range(50):
            sleep(self.tiempo)
            self.senal_actualizar.emit(self.indice, str(i) + " - no crítico")

        sleep(self.tiempo)
        self.senal_actualizar.emit(self.indice, "Status: QThread terminado")


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.threads = []
        self.mutex = QMutex()
        self.init_gui()

    def init_gui(self) -> None:
        # Configuramos los widgets de la interfaz
        # Definimos un montón de labels que corresponderán a un thread cada uno
        self.labels = {
            i: QLabel("Status: esperando QThread", self) for i in range(1, 6)
        }
        self.boton = QPushButton("Ejecutar QThreads", self)
        self.boton.clicked.connect(self.ejecutar_threads)

        for i in range(1, 6):
            self.labels[i].setGeometry(10, (i - 1) * 30, 230, 30)

        self.boton.setGeometry(10, 150, 230, 30)
        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Ejemplo QMutex")
        self.setGeometry(50, 50, 250, 200)
        self.show()

    def ejecutar_threads(self) -> None:
        """
        Este método crea cinco threads cada vez que se presiona el botón en la
        interfaz. Los threads recibirán como argumento el índice del label
        que les corresponde y el tiempo que toman entre cada iteración.
        """
        for thread in self.threads:
            if thread.isRunning():
                return

        self.threads = []
        for i in range(1, 6):
            thread = MiThread(i, i / 20, self.mutex)
            # Se conecta la señal emitida por el thread a un método
            # de la ventana
            thread.senal_actualizar.connect(self.actualizar_labels)
            self.threads.append(thread)
            thread.start()

    def actualizar_labels(self, indice: int, texto: str) -> None:
        """
        Este método actualiza el label correspondiente según los datos
        enviados desde un thread a través del índice y aplica el texto.
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
