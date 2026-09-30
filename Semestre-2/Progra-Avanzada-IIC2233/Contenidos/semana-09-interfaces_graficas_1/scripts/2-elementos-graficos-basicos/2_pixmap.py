import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class MiVentana(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self) -> None:
        """
        Este método inicializa la interfaz y todos sus widgets.
        """

        # Ajustamos la geometría de la ventana y su título.
        self.setGeometry(200, 100, 200, 200)
        self.setWindowTitle('Ventana con imagen')

        # Creamos el QLabel que contendrá la imagen y definimos su tamaño.
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 100, 100)

        # Escribimos la ruta al archivo que contiene la imagen.
        ruta_imagen = os.path.join('img', 'python.jpg')

        # Cargamos la imagen como pixeles.
        pixeles = QPixmap(ruta_imagen)

        # Agregamos los pixeles al elemento QLabel.
        self.label.setPixmap(pixeles)

        # Finalmente, ajustamos el tamaño del contenido al
        # tamaño del elemento (100 x 100).
        self.label.setScaledContents(True)

        # Una vez que fueron agregados todos los elementos a la ventana la
        # desplegamos en pantalla.
        self.show()


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
