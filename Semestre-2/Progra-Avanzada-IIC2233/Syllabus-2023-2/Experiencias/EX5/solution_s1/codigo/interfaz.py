import os
import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon,QAction
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt6.QtWidgets import QPushButton,QLabel,QLineEdit


class miVentana(QWidget):
    def __init__(self,status_bar_signal):
        super().__init__()
        self.status_bar_signal = status_bar_signal
        self.init_gui()

    def init_gui(self):
        "Este método inicializa,el main widget y sus elementos."
        self.label_text = QLabel("Texto",self)
        self.print_label = QLabel("Print,texto:",self)
        self.line_edit = QLineEdit("",self)

        self.boton = QPushButton("&Procesar",self)
        self.boton.resize(self.boton.sizeHint())
        self.boton.clicked.connect(self.boton_callback)

        self.label_text.move(20,15)
        self.line_edit.setGeometry(55,15,100,20)
        self.print_label.move(20,50)
        self.boton.move(20,80)

    def boton_callback(self):
        """
        Este método es el encargado ejecutar una acción cada vez que el botón
        es presionado. En esta caso,realiza el cambio en print_label y el status bar
        mediate la emisión de una señal en la cual se envía el texto correspondiente.
        """
        self.print_label.setText(f"Print texto: {self.line_edit.text()}")
        self.print_label.resize(self.print_label.sizeHint())
        self.status_bar_signal.emit(f"QEdit: {self.line_edit.text()}")


class mainWindow(QMainWindow):
    # Esta señal permite comunicar la barra de estados con el resto de los widgets
    # en el formulario,incluidos el central widget.
    onchange_status_bar = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        """Configuramos la geometría de la ventana."""
        self.setWindowTitle("Ventana con Boton")
        self.setGeometry(200,100,300,250)

        """Configuramos las acciones."""
        ver_status = QAction(QIcon(None),"&Cambiar Status",self)
        ver_status.setStatusTip("Este es un ítem de prueba")
        ver_status.triggered.connect(self.cambiar_status_bar)

        limpiar_status = QAction(QIcon(None),"&Limpiar Status",self)
        limpiar_status.setStatusTip("Esta acción limpia la barra de estado")
        limpiar_status.triggered.connect(self.limpiar_status_bar)

        buscar = QAction(QIcon(os.path.join("img","search_icon.png")),"&Search",self)
        buscar.setStatusTip("Un ícono de búsqueda")

        salir = QAction(QIcon(None),"&Exit",self)
        salir.setShortcut("Ctrl+Q")
        salir.setStatusTip("Salir de la aplicación")
        salir.triggered.connect(QApplication.quit)

        """Creamos la barra de menú."""
        menubar = self.menuBar()
        archivo_menu = menubar.addMenu("Archivo")  # primer menú
        archivo_menu.addAction(ver_status)
        archivo_menu.addAction(salir)

        otro_menu = menubar.addMenu("Otro Menú")  # segundo menú
        otro_menu.addAction(limpiar_status)

        """Creamos la barra de herramientas."""
        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(buscar)
        toolbar.addAction(salir)

        """Incluimos la barra de estado."""
        self.statusBar().showMessage("Listo")
        self.onchange_status_bar.connect(self.actualizar_status_bar)

        """
        Configuramos el widget central con una instancia de la clase
        MiVentana(). Además cargamos la señal en el central widget para
        que este pueda interactuar con la barra de estados de la ventana
        principal.
        """
        self.form = MiVentana(self.onchange_status_bar)
        self.setCentralWidget(self.form)

    def cambiar_status_bar(self):
        self.statusBar().showMessage("Cambié el Status")

    def limpiar_status_bar(self):
        self.statusBar().showMessage("Status limpio.")

    def actualizar_status_bar(self,msg):
        self.statusBar().showMessage(f"Actualizado. {msg}")


if __name__ == "__main__":

    def hook(type,value,traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec())
