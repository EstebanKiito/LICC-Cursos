import sys
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QGridLayout,
)


class VentanaControlRemoto(QWidget):

    senal_volumen = pyqtSignal(str)
    senal_canal = pyqtSignal(str)
    senal_encendido = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self) -> None:
        self.generar_botones()
        # self.generar_layout()
        # self.conectar_botones()
        # self.agregar_estilo()

        self.setWindowTitle('Control remoto')
        self.move(800, 100)

    def generar_botones(self) -> None:
        # Botón encendido/apagado
        self.on_off = None  # TODO: COMPLETAR

        # Botones de volumen
        self.volumen = [
            QPushButton('+', self),
            QPushButton('-', self)
        ]

        # Botones de canales
        self.canales = [
            QPushButton('+', self),
            QPushButton('-', self),
        ]

        # Botones de números
        self.numeros = []
        # TODO: COMPLETAR

    def generar_layout(self) -> None:
        # Generamos el layout principal
        vbox = QVBoxLayout()

        # Generamos un layout para los botones centrales
        hbox = QHBoxLayout()
        # TODO: COMPLETAR
        # self.generar_layout_subir_bajar(self.volumen, 'Vol')
        # self.generar_layout_subir_bajar(self.canales, 'Canal')

        # Agregamos los botones al layout principal
        vbox.addWidget(self.on_off)
        vbox.addStretch()
        vbox.addLayout(hbox)
        vbox.addStretch()
        vbox.addLayout(self.generar_layout_numeros())
        vbox.addStretch()

        # Setteamos el layout
        self.setLayout(vbox)

    def generar_layout_subir_bajar(self, botones: list, texto: str) -> None:
        texto = QLabel(texto, self)
        texto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(botones[0])
        vbox.addWidget(texto)
        vbox.addWidget(botones[1])
        return vbox

    def generar_layout_numeros(self) -> None:
        # Creamos la grilla de los números
        grilla_numeros = QGridLayout()

        # Agregamos los botones a la grilla
        for pos, boton in enumerate(self.numeros):
            pos_x = pos // 3
            pos_y = pos % 3
            grilla_numeros.addWidget(boton, pos_x, pos_y)

        # Retornamos la grilla
        return grilla_numeros

    def agregar_estilo(self) -> None:
        # Aplicamos estilo a los elementos
        self.setStyleSheet('''
            background: #2e2d2b;
            color:white;
        ''')
        self.on_off.setStyleSheet('''
            background: red;
        ''')

        # Ajustamos el tamaño de los botones
        for boton in (*self.volumen, *self.canales, *self.numeros):
            boton.setMinimumWidth(boton.sizeHint().height())
        self.on_off.setFixedSize(50, 50)

        # Ajustamos el tamaño del control
        self.resize(50, 360)

    def conectar_botones(self) -> None:
        # Botones de volumen
        for boton in self.volumen:
            boton.clicked.connect(self.actualizar_volumen)

        # Botones de canales
        for boton in [*self.canales, *self.numeros]:
            boton.clicked.connect(self.actualizar_canal)

        # Botón apagado
        self.on_off.clicked.connect(self.senal_encendido.emit)

    def actualizar_canal(self) -> None:
        # TODO: COMPLETAR
        pass

    def actualizar_volumen(self) -> None:
        # TODO: COMPLETAR
        pass


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaControlRemoto()
    ventana.show()
    sys.exit(app.exec())
