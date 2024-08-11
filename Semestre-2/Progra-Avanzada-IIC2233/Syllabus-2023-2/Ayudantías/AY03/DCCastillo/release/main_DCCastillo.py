import sys
from PyQt6.QtWidgets import QApplication
from frontend_DCCastillo.ventana_principal import Castillo
from frontend_DCCastillo.ventana_secundaria import Secundaria
from backend_DCCastillo.logica import Logica

if __name__ == '__main__':
    
    app = QApplication([])

    logica = Logica()
    ventana_1 = Castillo()
    ventana_2 = Secundaria("Dormitorio","20:57")
    ventana_3 = Secundaria("Baño","20:57")
    ventana_1.show()
    
    # RELLENAR 
    
    sys.exit(app.exec())