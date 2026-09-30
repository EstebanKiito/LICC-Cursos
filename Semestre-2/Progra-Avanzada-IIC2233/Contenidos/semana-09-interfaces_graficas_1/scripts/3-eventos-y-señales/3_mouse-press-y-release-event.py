import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QMouseEvent


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(100, 100, 110, 400)
        self.label = QLabel("Haz click en mí", self)
        self.label.setGeometry(10, 10, 90, 100)
        self.label.setStyleSheet("background-color: lightblue;")
        self.click_dentro_del_label = False

    def mousePressEvent(self, event: QMouseEvent) -> None:
        x = event.position().x()
        y = event.position().y()
        print(f"El mouse fue presionado en {x},{y}")
        self.click_dentro_del_label = self.label.underMouse()
        if self.click_dentro_del_label:
            print("\tFue presionado dentro del QLabel")
        else:
            print("\tFue presionado fuera del QLabel")

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        x = event.position().x()
        y = event.position().y()
        print(f"El mouse fue liberado en {x},{y}")

        if self.click_dentro_del_label:
            print("\tAntes se había presionado dentro del QLabel")
        else:
            print("\tAntes habías presionado fuera del QLabel")

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        x = event.position().x()
        y = event.position().y()
        print(f"El mouse se mueve... está en {x},{y}")


if __name__ == "__main__":
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
