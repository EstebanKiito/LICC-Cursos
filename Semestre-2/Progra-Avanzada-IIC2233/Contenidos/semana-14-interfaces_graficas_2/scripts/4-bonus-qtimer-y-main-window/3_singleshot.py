from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QFont
import sys
import datetime


class RelojDigital(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Crear label encargado de mostrar la hora
        self.label_timer = QLabel()
        self.label_timer.setFont(QFont("Times", 50))

        # Crear layout vertical para nuestro label
        layout = QVBoxLayout()
        layout.addWidget(self.label_timer)
        self.setLayout(layout)

        # Crear nuestro QTimer encargado de actualizar el tiempo cada 1 segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mostrar_hora)
        self.timer.setInterval(1000)
        self.timer.start()

        # Definir título y tamaño ventana
        self.setWindowTitle("Reloj Digital con QTimer")
        self.setGeometry(100, 100, 250, 100)

        # Ejecutar el método para mostrar hora por primera vez
        self.mostrar_hora()

        # Mostrar ventana
        self.show()

        # Creamos un QTimer que despues de 3 segundos va a esconder la ventana
        self.timer_singleshot_hide = QTimer(self)
        # self.timer_singleshot_hide.setSingleShot(True)
        self.timer_singleshot_hide.timeout.connect(self.hide)
        self.timer_singleshot_hide.setInterval(3000)
        self.timer_singleshot_hide.start()

        # Creamos otro QTimer que despues de 5 segundos va a mostrar la ventana
        self.timer_singleshot_show = QTimer(self)
        # self.timer_singleshot_show.setSingleShot(True)
        self.timer_singleshot_show.timeout.connect(self.show)
        self.timer_singleshot_show.setInterval(5000)
        self.timer_singleshot_show.start()

    def mostrar_hora(self) -> None:
        # Obtener hora actual
        hora_actual = datetime.datetime.now().time()
        # Actualizar texto del label
        self.label_timer.setText(hora_actual.strftime("%H:%M:%S %p"))


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    reloj = RelojDigital()
    sys.exit(app.exec())
