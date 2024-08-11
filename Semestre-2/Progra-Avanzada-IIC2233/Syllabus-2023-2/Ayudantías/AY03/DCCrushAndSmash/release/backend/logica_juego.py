import sys

from PyQt6.QtCore import QObject, pyqtSignal, QTimer, QRect
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel
from random import randint

import parametros as p


class Topo(QObject):
    def __init__(self, pos_topo, dir):
        super().__init__()

        self.pos_topo_out = (pos_topo.x(), pos_topo.y())
        self.pos_topo_in = p.POS_TOPO_HIDE
        self.pos_topo = pos_topo
        self.topo_label = QLabel('')
        self.pixeles_topo = QPixmap(p.RUTA_TOPO)
        self.topo_label.setPixmap(self.pixeles_topo)
        self.topo_label.setScaledContents(True)
        self.topo_label.resize(p.WIDTH_TOPO, p.HEIGHT_TOPO)
        self.pos_topo.moveTo(*self.pos_topo_in)
        self.topo_label.move(self.pos_topo.x(), self.pos_topo.y())

        self.dir = dir
        self.is_out = False
        self.cooldown = p.TOPO_COOLDOWN
        self.in_cooldown = False
        self.tiempo_salir = randint(*p.RANGO_APARICION_TOPO)
        self.tiempo_afuera = randint(*p.RANGO_AFUERA_TOPO)
        self.instanciar_timer()

    def instanciar_timer(self):
        self.timer_salir = QTimer()
        self.timer_salir.setInterval(self.tiempo_salir)
        self.timer_salir.setSingleShot(True)
        self.timer_salir.timeout.connect(self.toggle_hide)

        self.timer_afuera = QTimer()
        self.timer_afuera.setInterval(self.tiempo_afuera)
        self.timer_afuera.setSingleShot(True)
        self.timer_afuera.timeout.connect(self.toggle_hide)

    def start_timer(self):
        self.timer_salir.start()

    def check_hit(self):
        self.toggle_hide()

    def toggle_hide(self):
        if self.is_out:
            self.is_out = False
            self.pos_topo.moveTo(*self.pos_topo_in)
            self.timer_salir.start(randint(*p.RANGO_APARICION_TOPO))
        else:
            self.is_out = True
            self.pos_topo.moveTo(*self.pos_topo_out)
            self.timer_afuera.start(randint(*p.RANGO_AFUERA_TOPO))


class Martillo(QObject):

    def __init__(self, pos_martillo=QRect(*p.POS_INICIO_MARTILLO)):
        super().__init__()

        self.pos_martillo = pos_martillo
        self.martillo_label = QLabel('')
        self.pixeles_martillo = QPixmap(p.RUTA_MARTILLO)
        self.martillo_label.setPixmap(self.pixeles_martillo)
        self.martillo_label.setScaledContents(True)
        self.martillo_label.resize(p.WIDTH_MARTILLO, p.HEIGHT_MARTILLO)
        self.martillo_label.move(self.pos_martillo.x(), self.pos_martillo.y())

    def mover(self, dir):
        if dir == 'L':
            self.pos_martillo.moveTo(p.MARTILLO_L_X, p.MARTILLO_L_Y)
        elif dir == 'R':
            self.pos_martillo.moveTo(p.MARTILLO_R_X, p.MARTILLO_R_Y)
        elif dir == 'U':
            self.pos_martillo.moveTo(p.MARTILLO_U_X, p.MARTILLO_U_Y)
        elif dir == 'D':
            self.pos_martillo.moveTo(p.MARTILLO_D_X, p.MARTILLO_D_Y)

    def reset(self):
        self.pos_martillo.moveTo(p.POS_INICIO_MARTILLO[0],
                                 p.POS_INICIO_MARTILLO[1])


class LogicaJuego(QObject):

    # Señal para abrir ventana puntaje
    senal_termino_juego = pyqtSignal(str)
    senal_actualizar = pyqtSignal(str, str)
    senal_tiempo = pyqtSignal(str)
    senal_topos = pyqtSignal(list)
    senal_martillo = pyqtSignal(Martillo)
    senal_cerrar_ventana_juego = pyqtSignal()

    def __init__(self, martillo):
        super().__init__()
        self._puntaje = 0
        self.topos = []
        self.timers = []
        self.martillo = martillo
        self.instanciar_timer()

    @property
    def puntaje(self):
        return self._puntaje

    @puntaje.setter
    def puntaje(self, valor):
        if valor <= 0:
            self._puntaje = 0
        else:
            self._puntaje = valor

    def instanciar_timer(self):
        self.timer_juego = QTimer()
        self.timer_juego.setSingleShot(True)
        self.timer_juego.setInterval(p.TIEMPO_JUEGO)
        self.timer_juego.timeout.connect(self.terminar_juego)
        self.timers.append(self.timer_juego)

        self.timer_actualizar_juego = QTimer()
        self.timer_actualizar_juego.setInterval(p.ACTUALIZAR_JUEGO)
        self.timer_actualizar_juego.timeout.connect(self.actualizar_juego)
        self.timers.append(self.timer_actualizar_juego)

        self.timer_martillo = QTimer()
        self.timer_martillo.setInterval(p.RESET_MARTILLO)
        self.timer_martillo.timeout.connect(self.reset_martillo)
        self.timers.append(self.timer_martillo)

    def iniciar_juego(self):
        self.puntaje = 0
        self.generar_topos()
        for topo in self.topos:
            topo.start_timer()
        for timer in self.timers:
            timer.start()

    def generar_topos(self):
        pos_topo_l = QRect(p.TOPO_L_X, p.TOPO_L_Y, p.WIDTH_TOPO, p.HEIGHT_TOPO)
        pos_topo_r = QRect(p.TOPO_R_X, p.TOPO_R_Y, p.WIDTH_TOPO, p.HEIGHT_TOPO)
        pos_topo_u = QRect(p.TOPO_U_X, p.TOPO_U_Y, p.WIDTH_TOPO, p.HEIGHT_TOPO)
        pos_topo_d = QRect(p.TOPO_D_X, p.TOPO_D_Y, p.WIDTH_TOPO, p.HEIGHT_TOPO)
        topo_l = Topo(pos_topo_l, dir='L')
        topo_r = Topo(pos_topo_r, dir='R')
        topo_u = Topo(pos_topo_u, dir='U')
        topo_d = Topo(pos_topo_d, dir='D')
        self.topos.append(topo_l)
        self.topos.append(topo_r)
        self.topos.append(topo_u)
        self.topos.append(topo_d)

    def mover_martillo(self, dir):
        self.martillo.mover(dir)
        self.senal_martillo.emit(self.martillo)
        self.timer_martillo.start()
        hit = False
        for topo in self.topos:
            if self.martillo.pos_martillo.intersects(topo.pos_topo):
                topo.check_hit()
                self.puntaje += p.PUNTAJE_HIT
                hit = True
                break
        if not hit:
            self.puntaje -= p.PUNTAJE_MISS
        self.senal_topos.emit(self.topos)

    def reset_martillo(self):
        self.martillo.reset()
        self.senal_martillo.emit(self.martillo)

    def actualizar_juego(self):
        tiempo_juego = self.timer_juego.remainingTime() // 1000
        self.senal_actualizar.emit(str(round(tiempo_juego)), str(self.puntaje))
        self.senal_topos.emit(self.topos)

    def terminar_juego(self):
        self.senal_termino_juego.emit(str(self.puntaje))
        self.senal_cerrar_ventana_juego.emit()
        for topo in self.topos:
            topo.topo_label.close()
        self.topos.clear()


if __name__ == '__main__':
    log = LogicaJuego()
    log.generar_topos()

    app = QApplication([])
    sys.exit(app.exec_())
