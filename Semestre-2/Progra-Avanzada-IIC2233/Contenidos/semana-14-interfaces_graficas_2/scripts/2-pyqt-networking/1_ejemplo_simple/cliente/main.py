import sys
from PyQt6.QtWidgets import QApplication
from constantes import PORT_DEFECTO, HOST_DEFECTO
from frontend import ventana
from backend.backend_qthread import Logica
# Cambiar línea 5 por la línea 8 si se quiere usar el
# backend creado con thread
# from backend.backend_thread import Logica

if __name__ == "__main__":
    # Hook para imprimir errores
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication(sys.argv)
    # Instanciamos nuestro backend y frontend
    back = Logica(HOST_DEFECTO, PORT_DEFECTO)
    frontend = ventana.MainWindow()

    # Conectamos señales
    back.senal_actualizar_etiqueta.connect(frontend.actualizar_etiqueta)
    frontend.senal_mandar_comando.connect(back.mandar_comando)

    # Mostramos la ventana y ejecutamos pyqt
    frontend.show()
    sys.exit(app.exec())
