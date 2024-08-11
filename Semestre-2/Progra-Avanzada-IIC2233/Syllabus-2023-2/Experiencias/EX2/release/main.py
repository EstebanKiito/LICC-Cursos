import sys
from PyQt6.QtWidgets import QApplication

from backend.logica import ControladorLogico
from frontend.control_remoto import VentanaControlRemoto
from frontend.pantalla import VentanaPantalla


if __name__ == '__main__':
    app = QApplication([])

    # Instanciamos las clases
    controlador_logico = ControladorLogico()
    control_remoto = VentanaControlRemoto()
    pantalla = VentanaPantalla()

    # Conectamos las señales
    # TODO: COMPLETAR

    # Empezamos la ejecución del programa
    controlador_logico.empezar()

    sys.exit(app.exec())
