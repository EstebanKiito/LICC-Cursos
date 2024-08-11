import os
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QProgressBar


class VentanaPantalla(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self) -> None:
        self.posicion = (100, 100)
        self.porte = (640, 360)
        self.setGeometry(*self.posicion, *self.porte)
        self.setWindowTitle('Pantalla')

        self.generar_widgets()
        self.agregar_estilo()

    def generar_widgets(self) -> None:
        # Generamos y posicionamos los distintos widgets
        self.imagen = QLabel('', self)
        self.imagen.setGeometry(0, 0, *self.porte)

        self.canal = QLabel('Canal: #0', self)
        self.canal.move(20, 20)

        self.volumen = QLabel('Volumen: 0', self)
        self.volumen.move(20, self.porte[1] - 30)

        self.volumen_barra = QProgressBar(self, textVisible=False)
        self.volumen_barra.resize(100, 15)
        self.volumen_barra.move(120, self.porte[1] - 30)

    def agregar_estilo(self) -> None:
        # Agregamos un poco de estilo a los labels
        self.canal.setStyleSheet('''
            color: white;
            background: black;
        ''')
        self.volumen.setStyleSheet('''
            color: white;
            background: black;
        ''')

    def actualizar_volumen(self, nuevo_volumen: int) -> None:
        # Cambiamos el texto
        # TODO: COMPLETAR

        # Actualizamos la barra
        self.volumen_barra.setValue(nuevo_volumen)

    def actualizar_canal(self, nuevo_canal: int) -> None:
        # Actualizamos el texto
        # TODO: COMPLETAR

        # Cargamos, rescalamos y cambiamos la imagen
        # TODO: COMPLETAR
        pass

    def prender_apagar(self, encendido: bool) -> None:
        if encendido:
            self.show()
        else:
            self.hide()


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPantalla()
    ventana.show()
    sys.exit(app.exec())
