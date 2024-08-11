from PyQt6.QtCore import QObject,pyqtSignal


class Logica(QObject):
    
    
    #Señal que provoca que la ventana del dormitorio se cierre en cierto caso
    
    senal_ver_dormir = pyqtSignal()
    
    def __init__(self):
        
        super().__init__()
        
    def ver_dormir(self,hora):
        
        #Debera emitir la señal dependiendo de lo solicitiado
        
        #COMPLETAR
