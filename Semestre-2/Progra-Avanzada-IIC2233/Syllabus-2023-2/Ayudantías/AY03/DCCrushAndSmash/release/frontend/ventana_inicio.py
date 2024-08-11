import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt6.QtGui import QPixmap
import parametros as p


# COMPLETAR
class VentanaInicio():

    # COMPLETAR
    # Añadir una señal para enviar el login, utilizada en enviar_login()

    # COMPLETAR
    def __init__(self):

        # Establecer las características base de la ventana
        # e inicializar sus elementos
        pass

    # COMPLETAR
    def crear_elementos(self):

        # Crear un label para el logo, usando la ruta definida en parametros.py

        # Crear layouts para campos de texto y sus labels correspondientes
        # a nombre de usuario y contraseña

        # Crear labels y campos de texto para usuario y contraseña

        # Agregar los elementos correspondientes a los layouts

        # Crear un boton de login, y conectarlo al método enviar login

        # Agregar un layout general para la ventana,
        # y settarlo como el layout principal

        pass

    def enviar_login(self):

        # Emitir la señal que creaste, usando los datos del
        # campo de nombre y contraseña
        pass

    def recibir_validacion(self, valid, errores):

        # Este método es invocado por la lógica de la ventana
        # Recibe un bool valid, que indica si los datos ingresados son válidos o no
        # Así como una lista errores, que contiene los strings "Usuario", "Contraseña"
        # o ambos, en los casos correspondientes

        # De estar todo en órden, se deberá esconder la ventana
        # De lo contrario, se le deberá indicar el error correspondiente al usuario
        # mediante los campos de texto correspondientes

        # Cualquiera sea el caso, los campos deben vaciarse

        pass


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.crear_elementos()
    ventana.show()
    sys.exit(app.exec_())
