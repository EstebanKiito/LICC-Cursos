import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QGridLayout, QVBoxLayout)

class MiVentana(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self) -> None:
        # Agregamos un label para indicar el último botón seleccionado.
        self.label1 = QLabel('Último botón seleccionado:', self)
        self.label2 = QLabel('', self)
        self.grilla = QGridLayout()

        valores = ['1', '2', '3',
                   '4', '5', '6',
                   '7', '8', '9',
                   '*', '0', '#']

        posiciones = [(i, j) for i in range(4) for j in range(3)]

        for i in range(len(valores)):
            posicion = posiciones[i]
            valor = valores[i]
            boton = QPushButton(valor, self)
            """
            Aquí conectamos el evento clicked() de cada botón con el slot
            correspondiente. En este ejemplo, todos los botones usan el
            mismo slot (self.boton_clickeado).
            """
            boton.clicked.connect(self.boton_clickeado)
            self.grilla.addWidget(boton, *posicion)

        # Posicionamos tanto el label como la grilla en un layout vertical.
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addStretch(1)
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)

        self.setGeometry(300, 150, 200, 200)
        self.setWindowTitle('Celular')

    def boton_clickeado(self) -> None:
        """
        Esta función se ejecuta cada vez que uno de los botones de la grilla
        es presionado. Cada vez que el botón genera el evento, la función
        inspecciona cuál botón fue presionado y recupera la posición en que
        utiliza en la grilla.
        """

        # Sender retorna el objeto que fue clickeado.
        # Ahora, la variable boton referencia una instancia de QPushButton
        boton = self.sender()

        # Podemos obtener el texto del boton
        label_boton = boton.text()

        # Obtenemos el identificador del elemento en la grilla.
        idx = self.grilla.indexOf(boton)

        # Con el identificador obtenemos la posición del ítem en la grilla.
        posicion = self.grilla.getItemPosition(idx)

        # Actualizamos el texto del label2.
        self.label2.setText(f'Botón {idx} con label {label_boton}, en fila/columna: {posicion[:2]}.')


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
