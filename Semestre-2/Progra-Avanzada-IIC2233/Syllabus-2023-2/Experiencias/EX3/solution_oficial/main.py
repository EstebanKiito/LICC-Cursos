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
        self.frontend_juego.senal_click_pantalla.connect(self.backend.click_pantalla)
        self.frontend_juego.senal_empezar.connect(self.backend.empezar)

        # Backend notifica al frontend_juego cuando aparece, se mueve
        # y desaparece el meteorito
        self.backend.senal_aparecer_icono.connect(self.frontend_juego.aparecer_icono)
        self.backend.senal_mover_icono.connect(self.frontend_juego.mover_icono)
        self.backend.senal_actualizar_icono.connect(
            self.frontend_juego.actualizar_icono
        )

        # Backend notifica al frontend_juego cuando pasa 1 segundo
        self.backend.senal_actualizar_tiempo.connect(
            self.frontend_juego.actualizar_tiempo
        )

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
