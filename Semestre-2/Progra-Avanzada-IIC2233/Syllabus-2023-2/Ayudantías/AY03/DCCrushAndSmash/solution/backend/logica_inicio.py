from PyQt6.QtCore import QObject, pyqtSignal
import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, list)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, tupla_respuesta):
        errores = []
        valid = True
        usuario, contrasena = tupla_respuesta[0], tupla_respuesta[1]
        if not usuario.isalnum() or len(usuario) > p.MAX_CARACTERES:
            valid = False
            errores.append('Usuario')
        if contrasena != p.PASSWORD:
            valid = False
            errores.append('Contraseña')
        if valid:
            self.senal_abrir_juego.emit(usuario)
        self.senal_respuesta_validacion.emit(valid, errores)
