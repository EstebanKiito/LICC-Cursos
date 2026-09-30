import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton)


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self) -> None:
        """
        Este método inicializa la interfaz y todos sus widgets.
        """

        # Ajustamos la geometría de la ventana
        self.setGeometry(200, 100, 200, 300)
        self.setWindowTitle('Ventana con botón')

        # Podemos agrupar conjuntos de widgets en alguna estructura
        self.labels = {}
        self.labels['label1'] = QLabel('Texto:', self)
        self.labels['label1'].move(10, 15)
        self.labels['label2'] = QLabel('Aquí se escribe la respuesta', self)
        self.labels['label2'].move(10, 50)

        self.edit1 = QLineEdit('', self)
        self.edit1.setGeometry(45, 15, 100, 20)

        """
        El uso del carácter '&' al inicio del texto de algún botón o menú
        permite que la primera letra del mensaje mostrado esté destacada,
        la visualización depende de la plataforma utilizada.
        El método sizeHint provee un tamaño sugerido para el botón.
        """
        self.boton1 = QPushButton('&Procesar', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(5, 70)

        # Una vez que fueron agregados todos los elementos a la ventana,
        # la desplegamos en pantalla.
        self.show()


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
