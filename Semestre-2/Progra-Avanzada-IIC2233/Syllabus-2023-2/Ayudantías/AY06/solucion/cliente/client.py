import socket
import threading
import json
import random
import string
from PyQt6.QtCore import pyqtSignal, QObject


class Cliente(QObject):

    update_lobby_chat = pyqtSignal(str)
    send_username = pyqtSignal(str)
    wait_window = pyqtSignal()
    show_main_window = pyqtSignal()
    hide_main_window = pyqtSignal()
    show_wait_window = pyqtSignal()
    hide_wait_window = pyqtSignal()

    def __init__(self, port, host):
        super().__init__()
        print('Creando cliente')
        self.port = port
        self.host = host
        self.isTalking = False
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.señales_conectadas = threading.Event()
        self.username = 'User' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        try:
            self.connect_to_server()
            self.isConnected = True
            thread = threading.Thread(target=self.buscar_pareja, daemon=True)
            thread.start()
        except ConnectionError:
            print('Conexion terminada')
            self.socket_cliente.close()
            self.isConnected = False
            exit()

    def buscar_pareja(self):
        self.señales_conectadas.wait()
        self.show_wait_window.emit()
        while True:
            data = self.socket_cliente.recv(2**16)
            decoded_data = data.decode()
            decoded_data = decoded_data.replace('\'', '\"')
            mensaje = json.loads(decoded_data)
            if mensaje['type'] == 'connection':
                self.isTalking = True
                self.initBackend()
                self.listen()
                break

    def connect_to_server(self):
        self.socket_cliente.connect((self.host, self.port))
        print('Cliente conectado a servidor')

    def listen(self):
        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def next(self):
        self.isTalking = False

    def listen_thread(self):
        while self.isConnected:
            data = self.socket_cliente.recv(2**16)
            decoded_data = data.decode()
            decoded_data = decoded_data.replace('\'', '\"')  # Esto lo hacemos porque json solo acepta el "", no el ''
            data = json.loads(decoded_data)
            if data["type"] == "wait":
                continue
            if data["type"] == "next":
                if self.isTalking:
                    self.isTalking = False
                    data = {
                        "type": "nexted",
                        "username": self.username,
                        "data": ""
                    }
                    self.send(data)
                thread = threading.Thread(target=self.buscar_pareja, daemon=True)
                thread.start()
                self.hide_main_window.emit()
                break
            self.decode_msg_from_server(data)
            pass

    def send(self, msg):
        json_msg = json.dumps(msg)
        msg_to_send = json_msg.encode()
        largo = len(msg_to_send)
        self.socket_cliente.sendall(largo.to_bytes(4, byteorder='big') + msg_to_send)

    def initBackend(self):
        self.hide_wait_window.emit()
        self.show_main_window.emit()
        self.isTalking = True
        self.chat = ''
        self.update_lobby_chat.emit(self.chat)

    def send_init_info_to_chat(self):
        self.send_username.emit(self.username)

    def recive_msg_from_lobby(self, event):
        self.send(event)

    def decode_msg_from_server(self, msg):
        string_to_add = f'{msg["username"]}: {msg["data"]}\n'
        self.chat += string_to_add
        self.update_lobby_chat.emit(self.chat)


if __name__ == '__main__':
    port = 3245
    host = 'localhost'
    client = Cliente(port, host)
