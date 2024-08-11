from PyQt6.QtWidgets import QApplication
import sys
from client import Cliente
from lobby import MainWindow, WaitWindow

app = QApplication([])

PORT = 3245
HOST = 'localhost'

wait_window = WaitWindow()
main_window = MainWindow()
cliente = Cliente(PORT, HOST)
cliente.send_username.connect(main_window.get_username)
cliente.update_lobby_chat.connect(main_window.update_chat)
cliente.send_init_info_to_chat()
cliente.hide_main_window.connect(main_window.hide)
cliente.show_main_window.connect(main_window.show)
cliente.hide_wait_window.connect(wait_window.hide)
cliente.show_wait_window.connect(wait_window.show)
main_window.send_msg_signal.connect(cliente.recive_msg_from_lobby)
main_window.next_signal.connect(cliente.next)
cliente.señales_conectadas.set()

sys.exit(app.exec())
