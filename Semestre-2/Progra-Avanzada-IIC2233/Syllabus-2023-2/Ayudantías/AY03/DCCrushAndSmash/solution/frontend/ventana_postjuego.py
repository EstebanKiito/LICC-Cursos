from PyQt6.QtCore import pyqtSignal
from PyQt6 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_POSTJUEGO)


class VentanaPostjuego(window_name, base_class):

    senal_abrir_inicio = pyqtSignal()
    senal_cerrar_juego = pyqtSignal()

    def __init__(self):
        # Geometría
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana PostJuego")
        self.button_salir.clicked.connect(self.salir)
        self.button_volver.clicked.connect(self.volver_inicio)

    def volver_inicio(self):
        self.senal_abrir_inicio.emit()
        self.hide()

    def abrir(self, puntaje):
        self.show()
        self.puntaje = puntaje
        self.puntaje_label_2.setText(puntaje)
        self.puntaje_label_2.repaint()

    def salir(self):
        self.hide()
        self.senal_cerrar_juego.emit()


if __name__ == '__main__':
    pass
