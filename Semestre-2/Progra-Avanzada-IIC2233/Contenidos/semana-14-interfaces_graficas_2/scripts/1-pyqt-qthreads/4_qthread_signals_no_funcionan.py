from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication
import sys
import time


class Thread1(QThread):
    signal_t1 = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.t2 = None

    def run(self):
        print("[Thread 1] Crear Thread 2")
        self.t2 = Thread2(self.signal_t1)

        print("[Thread 1] Conectar Thread 2 (signal_t2) con print de T2")
        self.t2.signal_t2.connect(self.t2.print)

        print("[Thread 1] Ejecutar Thread 2")
        self.t2.start()

        print("[Thread 1] Emitir 2 señales: t1.signal_1 y t2.signal_2")
        self.signal_t1.emit("signal_t1 emitida desde Thread1")
        self.t2.signal_t2.emit("signal_t2 emitida desde Thread1")

        # Espero medio segundo y cierro el programa
        time.sleep(0.5)
        sys.exit(1)

    def print(self, s):
        print("\t[Print de T1] -> ", s)


class Thread2(QThread):
    signal_t2 = pyqtSignal(str)

    def __init__(self, signal_padre: pyqtSignal) -> None:
        super().__init__()
        self.signal_t1 = signal_padre

    def run(self):
        print("[Thread 2] Emitir 2 señales: t1.signal_1 y t2.signal_2")
        self.signal_t1.emit("signal_t1 emitida desde Thread2")
        self.signal_t2.emit("signal_t2 emitida desde Thread2")

    def print(self, s):
        print("\t[Print de T2] -> ", s)


if __name__ == "__main__":
    app = QApplication([])
    print("[MAIN] Crear Thread 1")
    hilo = Thread1()
    print("[MAIN] Conectar Thread 1 (signal_t1) con print de T1")
    hilo.signal_t1.connect(hilo.print)
    print("[MAIN] Ejecutar T1")
    hilo.start()
    sys.exit(app.exec())
