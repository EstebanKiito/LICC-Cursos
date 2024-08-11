from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
import PyQt6.QtCore as core
import sys


class MainWindow(QWidget):

    send_msg_signal = core.pyqtSignal(dict)
    next_signal = core.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DCCitas a ciegas <3")
        self.displayWidget = QTextEdit(self)
        self.userInputWidget = QTextEdit(self)
        self.sendButton = QPushButton("Enviar", self)
        self.nextButton = QPushButton("Next!", self)
        self.init_gui()

    def init_gui(self):
        self.setGeometry(100, 100, 400, 300)
        self.displayWidget.setMinimumSize(400, 200)
        self.displayWidget.setReadOnly(True)
        self.userInputWidget.setMinimumSize(250, 20)
        self.userInputWidget.setMaximumHeight(20)
        self.sendButton.setMinimumSize(50, 20)
        self.nextButton.setMinimumSize(50, 20)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.displayWidget)
        hbox = QHBoxLayout()
        hbox.addWidget(self.userInputWidget)
        hbox.addWidget(self.sendButton)
        hbox.addWidget(self.nextButton)
        self.vbox.addLayout(hbox)
        self.setLayout(self.vbox)
        self.sendButton.clicked.connect(self.send_msg_to_client)
        self.nextButton.clicked.connect(self.next)

    def closeEvent(self, event):
        sys.exit()

    def next(self):
        data = {
            "type": "next",
            "username": self.username,
            "data": ""
                }
        self.send_msg_signal.emit(data)
        self.next_signal.emit()

    def send_msg_to_client(self):
        print(self.userInputWidget.toPlainText())
        data = {
            "type": "chat",
            "username": self.username,
            "data": self.userInputWidget.toPlainText()
                }
        self.send_msg_signal.emit(data)
        self.userInputWidget.setPlainText('')

    def get_username(self, event):
        self.username = event
        print('Username set')

    def update_chat(self, event):
        self.displayWidget.setPlainText(event)


class WaitWindow(QWidget):

    close_signal = core.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DCCitas a ciegas <3")
        self.setGeometry(100, 100, 300, 50)
        self.label = QLabel("Esperando a que se conecte alguien...", self)
        self.label.setGeometry(10, 10, 300, 20)

    def closeEvent(self, event):
        sys.exit()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
