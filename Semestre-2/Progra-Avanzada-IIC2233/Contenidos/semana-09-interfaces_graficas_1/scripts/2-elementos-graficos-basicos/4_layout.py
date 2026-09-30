import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout)


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, *kwargs)
        self.init_gui()
        self.show()

    def init_gui(self) -> None:
        """
        Este método configura todos los widgets de la ventana.
        """
        self.setGeometry(100, 100, 300, 300)
        self.label1 = QLabel('Texto:', self)
        self.edit1 = QLineEdit('', self)
        self.edit1.resize(100, 20)
        self.boton1 = QPushButton('&Calcular', self)
        self.boton1.resize(self.boton1.sizeHint())

        """
        Creamos el layout horizontal y agregamos los widgets mediante el
        método addWidget(). El método addStretch() nos permite incluir
        opcionalmente espaciadores.
        """
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label1)
        hbox.addWidget(self.edit1)
        hbox.addWidget(self.boton1)
        hbox.addStretch(1)

        """
        Creamos el layout vertical y le agregamos el layout horizontal.
        Opcionalmente agregamos espaciadores para distribuir los widgets.
        Notar el juego entre el valor recibido por los espaciadores.
        """
        vbox = QVBoxLayout()
        vbox.addStretch(5)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
