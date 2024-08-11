from PyQt6.QtWidgets import QApplication
from frontend.ventana import VentanaSimulacion
from backend.logica import ControladorLogico
import sys
import parametros_general as p


class Simulacion:
    def __init__(self):
        self.frontend_juego = VentanaSimulacion(p.TAMAÑO_SIMULACION, p.TAMAÑO_ICONOS)
        self.backend = ControladorLogico(p.TAMAÑO_SIMULACION, p.TAMAÑO_ICONOS)

    def conectar(self):
        # Frontend_juego notifica al backend cuando se hace click en pantalla
        self.frontend_juego.senal_empezar.connect(self.backend.empezar)

        # TODO: completar con las demás señales

    def iniciar(self):
        # Llenar con datos aleatorios
        self.backend.poblar_random()
        # Mostrar ventana de frontend
        self.frontend_juego.show()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    game = Simulacion()
    game.conectar()
    game.iniciar()

    sys.exit(app.exec())
