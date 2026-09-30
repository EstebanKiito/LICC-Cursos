import sys
from threading import Thread
from time import sleep
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MiThread(Thread):
    """
    Esta clase representa un thread personalizado que será utilizado durante
    la ejecución de la GUI.
    """

    def __init__(self, senal_actualizar: pyqtSignal) -> None:
        super().__init__()
        self.senal_actualizar = senal_actualizar

    def run(self) -> None:
        for i in range(10):
            sleep(0.5)
            self.senal_actualizar.emit(str(i))
        self.senal_actualizar.emit("Status: thread terminado")


class MiVentana(QWidget):
    # Creamos una señal para manejar la respuesta del thread
    senal_thread = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.thread = None
        # Conectamos la señal al método que maneja
        self.senal_thread.connect(self.actualizar_label)
        self.init_gui()

    def init_gui(self) -> None:
        # Configuramos los widgets de la interfaz
        self.label = QLabel("Status: esperando thread", self)
        self.boton = QPushButton("Ejecutar Thread", self)
        self.boton.clicked.connect(self.ejecutar_thread)

        self.label.setGeometry(10, 10, 230, 30)
        self.boton.setGeometry(10, 50, 230, 30)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Ejemplo thread")
        self.setGeometry(50, 50, 250, 200)
        self.show()

    def ejecutar_thread(self) -> None:
        """
        Este método crea un thread cada vez que se presiona el botón en la
        interfaz. El thread recibirá como argumento la señal sobre la cual
        debe operar.
        """
        if self.thread is None or not self.thread.is_alive():
            self.thread = MiThread(self.senal_thread)
            self.thread.start()

    def actualizar_label(self, texto: str) -> None:
        """
        Este método actualiza el label según los datos enviados desde el
        thread a través del argumento texto. Para este ejemplo, el método
        recibe un texto, pero podría también no recibir nada.
        """
        self.label.setText(texto)


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
