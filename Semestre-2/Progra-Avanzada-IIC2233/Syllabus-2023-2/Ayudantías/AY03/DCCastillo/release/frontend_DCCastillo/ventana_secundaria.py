import sys
import os
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtGui import QPixmap, QPalette, QBrush, QPainter
from PyQt6.QtCore import Qt,pyqtSignal

class Secundaria(QWidget):
    
    senal_abrir_castillo = pyqtSignal()
    senal_dormir = pyqtSignal(str)
    
    def __init__(self,tipo,hora):
        
        super().__init__()
        self.tipo = tipo
        self.hora = hora
        
        if self.tipo == "Dormitorio":
            self.setWindowTitle("¡ Dormitorio !")
            # https://co.pinterest.com/pin/427279083400366800/ 
            imagen_ruta = os.path.join("imagenes_DCCastillo", "dormitorio_DCCastillo.jpg")
            
        elif self.tipo == "Baño":
            self.setWindowTitle("¡ Baño !")
            # https://www.freepik.es/fotos-premium/bano-inspirado-castillo-medieval_50628276.htm 
            imagen_ruta = os.path.join("imagenes_DCCastillo", "bano_DCCastillo.jpg")
            
        self.setGeometry(0, 0, 500, 500)
            
        layout_vertical = QVBoxLayout()
        
        imagen = QPixmap(os.path.join(imagen_ruta))
        label_imagen = QLabel()
        label_imagen.setPixmap(imagen)
        
        boton_ir_castillo = QPushButton("Volver al Castillo", self)
        boton_ir_castillo.clicked.connect(self.volver)
        
        layout_vertical.addWidget(label_imagen)
        layout_vertical.addWidget(boton_ir_castillo)
        
        if self.tipo == "Dormitorio":
            boton_dormir = QPushButton("Dormir", self)
            boton_dormir.clicked.connect(self.dormir)
            layout_vertical.addWidget(boton_dormir)
            
        self.setLayout(layout_vertical)
    
    #En el caso que se clickee el boton volver al castillo, para reabrir la ventana principal y cerrar la secundaria
    def volver(self):
        
        self.senal_abrir_castillo.emit()
        self.hide()
            
    #Para abrir la ventana en caso que el tipo sea igual al string que llego
    def abrir_ventana(self,string):
        
        if string == self.tipo:
            self.show()
    
    #En el caso que se seleccione dormir, se envia la hora al backend para comprobar las condiciones
    def dormir(self):
        
        self.senal_dormir.emit(self.hora)
        
    #En el caso que efectivamente se vaya a dormir, se cierra la ventana
    def fue_dormir(self):
        
        self.close()