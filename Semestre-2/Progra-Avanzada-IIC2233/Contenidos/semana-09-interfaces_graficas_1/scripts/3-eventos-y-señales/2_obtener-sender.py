import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QHBoxLayout, QVBoxLayout)
from PyQt6.QtCore import QCoreApplication


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self) -> None:
        self.label_estado = QLabel('Estado: -', self)

        """
        El evento de cada botón es conectado con su slot, en este caso,
        el método boton_clickeado(). Importante notar, que al hacer referencia
        al método no se agregar los paréntesis finales.
        """
        self.boton1 = QPushButton('Botón 1', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.clicked.connect(self.boton_clickeado)

        self.boton2 = QPushButton('Botón 2', self)
        self.boton2.resize(self.boton2.sizeHint())
        self.boton2.clicked.connect(self.boton_clickeado)

        self.boton3 = QPushButton('Salir', self)
        self.boton3.resize(self.boton3.sizeHint())
        self.boton3.clicked.connect(QCoreApplication.instance().quit)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.boton1)
        hbox.addWidget(self.boton2)
        hbox.addWidget(self.boton3)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.label_estado)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)

        self.setGeometry(200, 100, 300, 200)
        self.setWindowTitle('Sender')

    def boton_clickeado(self) -> None:
        # Esta función registra el objeto que envía la señal del evento
        # y lo refleja mediante el método sender() en label de estado.
        sender = self.sender()
        self.label_estado.setText(f'Estado: Presionado botón "{sender.text()}"')
        self.label_estado.resize(self.label_estado.sizeHint())


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
