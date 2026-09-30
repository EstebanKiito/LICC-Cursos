import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        """
        Este método inicializa la ventana.
        """
        super().__init__(*args, **kwargs)

        # Llamamos a un método propio que
        # inicializa los elementos de la ventana.
        self.init_gui()

    def init_gui(self) -> None:
        """
        Este método configura la interfaz y todos sus widgets,
        posterior a __init__().
        """
        # Ajustamos la geometría de la ventana y su título.
        self.setGeometry(200, 100, 200, 300)
        self.setWindowTitle('Ventana con label y cuadro de texto')

        # Agregamos etiquetas usando el widget QLabel(texto_inicial, padre).
        # Posteriormente, las ubicamos en la ventana.
        self.label1 = QLabel('Texto:', self)
        self.label1.move(10, 15)

        self.label2 = QLabel('Esta etiqueta es variable', self)
        self.label2.move(10, 50)

        # Agregamos cuadros de texto mediante QLineEdit(texto_inicial, padre).
        # Posteriormente, definimos su posición y porte en la ventana.
        self.edit = QLineEdit('', self)
        self.edit.setGeometry(45, 15, 100, 20)

        # Una vez que fueron agregados todos los elementos a la ventana,
        # la desplegamos en pantalla.
        self.show()


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    """
    Recordar que en el programa principal debe existir una instancia de
    QApplication ANTES de crear los demás widgets, incluida la ventana
    principal.
    Si la aplicación no recibe parámetros desde la línea de comandos,
    QApplication recibe una lista vacía como input.
    """

    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
