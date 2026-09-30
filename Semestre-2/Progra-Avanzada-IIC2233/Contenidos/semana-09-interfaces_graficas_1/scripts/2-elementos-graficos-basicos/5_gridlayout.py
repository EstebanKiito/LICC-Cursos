import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.show()

    def init_gui(self) -> None:
        # Creamos la grilla para ubicar los widgets de manera matricial.
        grilla = QGridLayout()

        valores = ['1', '2', '3',
                   '4', '5', '6',
                   '7', '8', '9',
                   '*', '0', '#']

        # Generamos las posiciones de los botones en la grilla y le asociamos
        # el texto que debe desplegar cada botón guardados en la lista valores.
        posiciones = [(i, j) for i in range(4) for j in range(3)]

        for i in range(len(posiciones)):
            posicion = posiciones[i]
            valor = valores[i]
            boton = QPushButton(valor, self)
            grilla.addWidget(boton, *posicion)

        self.setLayout(grilla)

        self.move(300, 150)
        self.setWindowTitle('Celular')


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
