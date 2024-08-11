import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt6.QtGui import QPixmap
import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()

        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    # Esto lo completaran los estudiantes
    def crear_elementos(self):

        self.logo = QLabel("Logo", self)
        pixeles = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)
        self.logo.setMaximumSize(500, 300)

        # Creamos layouts para campos de texto y sus labels
        self.lay_text = QHBoxLayout()
        self.lay_text2 = QHBoxLayout()

        # Creamos campos de texto y labels
        self.usuario = QLineEdit("")
        self.label_usuario = QLabel("Ingresa tu nombre de usuario", self)
        self.contrasena = QLineEdit("")
        self.contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_contrasena = QLabel("Ingresa la contraseña", self)

        # Agregamos a los layouts horizontales
        self.lay_text.addWidget(self.label_usuario)
        self.lay_text.addWidget(self.usuario)
        self.lay_text2.addWidget(self.label_contrasena)
        self.lay_text2.addWidget(self.contrasena)

        # Creamos un botón
        self.button = QPushButton("Empezar juego!")
        self.button.clicked.connect(self.enviar_login)

        # Creamos layout general y lo llenamos
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.logo)
        self.layout.addLayout(self.lay_text)
        self.layout.addLayout(self.lay_text2)
        self.layout.addWidget(self.button)
        self.update()

    def enviar_login(self):
        self.senal_enviar_login.emit(
            (self.usuario.text(), self.contrasena.text()))

    def recibir_validacion(self, valid, errores):
        if valid:
            self.hide()
        else:
            self.contrasena.setPlaceholderText('')
            self.usuario.setPlaceholderText('')
            if 'Usuario' in errores:
                self.usuario.setPlaceholderText('Usuario inválido')
            if 'Contraseña' in errores:
                self.contrasena.setPlaceholderText('Contraseña inválida')
            self.usuario.setText("")
            self.contrasena.setText("")


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.crear_elementos()
    ventana.show()
    sys.exit(app.exec_())
