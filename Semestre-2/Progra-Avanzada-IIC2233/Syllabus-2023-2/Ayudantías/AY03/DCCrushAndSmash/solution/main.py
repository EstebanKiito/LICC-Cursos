import sys

from PyQt6.QtWidgets import QApplication

from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego, Martillo
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_postjuego import VentanaPostjuego


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # Instanciación de ventanas
    ventana_inicio = VentanaInicio()
    ventana_juego = VentanaJuego()
    ventana_postjuego = VentanaPostjuego()

    # Instanciación de lógica
    martillo = Martillo()
    logica_inicio = LogicaInicio()
    logica_juego = LogicaJuego(martillo)

    # ~~ Conexiones de señales ~~

    # Señales de inicio
    ventana_inicio.senal_enviar_login.connect(logica_inicio.comprobar_usuario)

    logica_inicio.senal_respuesta_validacion.connect(
        ventana_inicio.recibir_validacion)
    logica_inicio.senal_abrir_juego.connect(ventana_juego.mostrar_ventana)

    # Señales de juego
    ventana_juego.senal_iniciar_juego.connect(logica_juego.iniciar_juego)
    ventana_juego.senal_tecla.connect(logica_juego.mover_martillo)

    logica_juego.senal_martillo.connect(ventana_juego.mover_martillo)
    logica_juego.senal_actualizar.connect(ventana_juego.actualizar_datos)
    logica_juego.senal_topos.connect(ventana_juego.actualizar_topos)
    logica_juego.senal_termino_juego.connect(ventana_postjuego.abrir)
    logica_juego.senal_cerrar_ventana_juego.connect(ventana_juego.salir)

    # Señales de postjuego
    ventana_postjuego.senal_abrir_inicio.connect(ventana_inicio.show)
    ventana_postjuego.senal_cerrar_juego.connect(app.exit)

    ventana_inicio.show()
    app.exec()
