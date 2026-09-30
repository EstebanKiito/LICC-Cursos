import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QHBoxLayout, QVBoxLayout, QLineEdit)


class CampoFormulario(QHBoxLayout):
    # Heredamos de Layout Horizontal para colocar cada campo.
    def __init__(self, texto: str, *args, **kwargs) -> None:
        # Llama al constructor de la clase madre.
        super().__init__(*args, **kwargs)

        # Crea la etiqueta y cuadro correspondientes.
        label = QLabel(f"{texto}: ")
        campo = QLineEdit("")

        # Los coloca dentro del Layout.
        self.addStretch(1)
        self.addWidget(label)
        self.addWidget(campo)
        self.addStretch(1)

class Formulario(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Fija datos de ventana.
        self.setWindowTitle("Formulario")
        self.setGeometry(200, 200, 400, 400)

        # Crea contenedor vertical para colocar los campos.
        contenedor = QVBoxLayout()

        # Coloca cada campo que creamos.
        contenedor.addLayout(CampoFormulario("Nombre"))
        contenedor.addLayout(CampoFormulario("Apellido"))
        contenedor.addLayout(CampoFormulario("Dirección"))
        contenedor.addLayout(CampoFormulario("Correo"))
        contenedor.addLayout(CampoFormulario("Usuario"))
        contenedor.addLayout(CampoFormulario("Contraseña"))

        # Fijamos el Layout completo.
        self.setLayout(contenedor)

        self.show()


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    formulario = Formulario()
    sys.exit(app.exec())
