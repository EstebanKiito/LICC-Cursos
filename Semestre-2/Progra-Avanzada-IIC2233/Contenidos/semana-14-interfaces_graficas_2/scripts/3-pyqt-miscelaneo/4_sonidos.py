import sys
import os
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer, QSoundEffect, QAudioOutput
from os.path import join


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Configuramos los widgets de la interfaz
        self.boton_sorpresa = QPushButton("Wooow", self)
        self.boton_empezar = QPushButton("Empezar música de fondo", self)
        self.boton_parar = QPushButton("Parar música de fondo", self)

        self.boton_sorpresa.setGeometry(10, 10, 230, 30)
        self.boton_empezar.setGeometry(10, 50, 230, 30)
        self.boton_parar.setGeometry(10, 90, 230, 30)

        self.boton_sorpresa.clicked.connect(self.empezar_sonido_sorpresa)
        self.boton_empezar.clicked.connect(self.empezar_musica_fondo)
        self.boton_parar.clicked.connect(self.parar_musica_fondo)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle("Ejemplo Sonidos")
        self.setGeometry(50, 50, 250, 200)

        # Opción MP3: QMediaPlayer en PyQt6 tiene pequeñas diferencias
        # 1. Para que QMediaPlayer reproduzca audio, se debe agregar un QAudioOutput
        # 2. Necesitas utilizar el path absoluto. Para lograr generarlo correctamente
        #    usaremos os.path.abspath que transforma el relativo a absoluto según cada PC
        # 3. Se utiliza setSource para indicar el path al audio a escuchar
        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)
        path = os.path.abspath(join("sounds", "waku-waku.mp3"))
        self.player.setSource(QUrl.fromLocalFile(path))

        # Opción Wav: QSoundEffect
        self.media_player_wav = QSoundEffect(self)
        self.media_player_wav.setVolume(0.1)  # Opcional
        file_url = QUrl.fromLocalFile(join("sounds", "see-you-again.wav"))
        self.media_player_wav.setSource(file_url)

        # Mostrar ventana
        self.show()

    def empezar_sonido_sorpresa(self) -> None:
        self.player.play()

    def empezar_musica_fondo(self) -> None:
        if not self.media_player_wav.isPlaying():
            self.media_player_wav.play()

    def parar_musica_fondo(self) -> None:
        if self.media_player_wav.isPlaying():
            self.media_player_wav.stop()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
