import sys
from time import sleep
from PyQt6.QtCore import pyqtSignal, QThread
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MiThread(QThread):
    """
    Esta clase representa un thread personalizado que será utilizado durante
    la ejecución de la GUI.
    """

    # Creamos una señal para manejar la respuesta del thread
    senal_thread = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        for i in range(10):
            sleep(0.5)
            self.senal_thread.emit(str(i))

        sleep(0.5)
        self.senal_thread.emit("Status: QThread terminado")


class MiVentana(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.thread = None
        self.init_gui()

    def init_gui(self) -> None:
        # Configuramos los widgets de la interfaz
        self.label = QLabel("Status: esperando QThread", self)
        self.boton = QPushButton("Ejecutar QThread", self)
        self.boton.clicked.connect(self.ejecutar_thread)

        self.label.setGeometry(10, 10, 230, 30)
        self.boton.setGeometry(10, 50, 230, 30)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Ejemplo QThread")
        self.setGeometry(50, 50, 250, 200)
        self.show()

    def ejecutar_thread(self) -> None:
        """
        Este método crea un thread cada vez que se presiona el botón en la
        interfaz. El thread recibirá como argumento la señal sobre la cual
        debe operar.
        """
        # Aquí debemos ocupar isRunning en lugar de is_alive
        if self.thread is None or not self.thread.isRunning():
            self.thread = MiThread()
            # Conectamos la señal del thread al método que maneja
            self.thread.senal_thread.connect(self.actualizar_label)
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
