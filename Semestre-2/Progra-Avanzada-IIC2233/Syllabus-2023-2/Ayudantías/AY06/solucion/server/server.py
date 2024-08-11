import socket
import threading
import json
import time
import random


class Servidor:

    sockets_lock = threading.Lock()

    def __init__(self, port, host):
        self.max_recv = 2**16
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockets = {}
        self.bind_listen()
        self.accept_connections()

    def bind_listen(self):
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(250)
        print(f'Servidor escuchando en {self.host} : {self.port}')

    def accept_connections(self):
        thread = threading.Thread(
            target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self):
        while True:
            client_socket, address = self.socket_server.accept()
            self.sockets[client_socket] = False
            matching_client_thread = threading.Thread(
                target=self.match_client_thread,
                args=(client_socket, ),
                daemon=True)
            matching_client_thread.start()

    def match_client_thread(self, client_socket):
        switch = True
        while switch:
            time.sleep(5)
            try:
                self.sockets_lock.acquire()
                msg = {"type": "wait", "username": "", "data": ""}
                self.send(msg, client_socket)
            except ConnectionError:
                if client_socket in self.sockets.keys():
                    print("Usuario eliminado")
                    del self.sockets[client_socket]
                break
            finally:
                self.sockets_lock.release()
            try:
                time.sleep(0.1)
                self.sockets_lock.acquire()
                if self.sockets[client_socket]:
                    break
                sockets_list = list(self.sockets.keys())
                random.shuffle(sockets_list)
                for socket_ in sockets_list:
                    if not self.sockets[socket_] and socket_ != client_socket:
                        print("Matched")
                        self.sockets[client_socket] = True
                        self.sockets[socket_] = True
                        thread1 = threading.Thread(
                            target=self.listen_client_thread,
                            args=(client_socket, socket_),
                            daemon=True)
                        thread2 = threading.Thread(
                            target=self.listen_client_thread,
                            args=(socket_, client_socket),
                            daemon=True)
                        thread1.start()
                        thread2.start()
                        msg = {"type": "connection", "username": "", "data": ""}
                        self.send(msg, client_socket)
                        self.send(msg, socket_)
                        switch = False
                        break
                if switch:
                    msg = {"type": "wait", "username": "", "data": ""}
                    self.send(msg, client_socket)
            except ConnectionError:
                if client_socket in self.sockets.keys():
                    print("Usuario eliminado")
                    del self.sockets[client_socket]
                switch = False
            except KeyError:
                switch = False
            finally:
                self.sockets_lock.release()

    def listen_client_thread(self, client1_socket, client2_socket):
        while True:
            try:
                largo_archivo = int.from_bytes(
                    client1_socket.recv(4), byteorder='big')
                if largo_archivo > self.max_recv:
                    largo_archivo = self.max_recv
                bytes_leidos = bytearray()
                while len(bytes_leidos) < largo_archivo:
                    # El último recv será probablemente más chico que 4096
                    bytes_leer = min(4096, largo_archivo - len(bytes_leidos))
                    respuesta = client1_socket.recv(bytes_leer)
                    bytes_leidos += respuesta
                    mensaje_entero = json.loads(bytes_leidos)
                if mensaje_entero["type"] == "next":
                    msg = {"type": "next", "username": "", "data": ""}
                    self.send(msg, client1_socket)
                    self.send(msg, client2_socket)
                    self.sockets[client1_socket] = False
                    self.sockets[client2_socket] = False
                    matching_client1_thread = threading.Thread(
                        target=self.match_client_thread,
                        args=(client1_socket, ),
                        daemon=True)
                    matching_client2_thread = threading.Thread(
                        target=self.match_client_thread,
                        args=(client2_socket, ),
                        daemon=True)
                    matching_client1_thread.start()
                    matching_client2_thread.start()
                    break
                if mensaje_entero["type"] == "nexted":
                    break
                self.send(mensaje_entero, client1_socket)
                self.send(mensaje_entero, client2_socket)
            except ConnectionError:
                print('Usuario eliminado')
                msg = {"type": "next", "username": "", "data": ""}
                self.send(msg, client2_socket)
                self.sockets[client2_socket] = False
                matching_client2_thread = threading.Thread(
                    target=self.match_client_thread,
                    args=(client2_socket, ),
                    daemon=True)
                matching_client2_thread.start()
                with self.sockets_lock:
                    if client1_socket in self.sockets.keys():
                        del self.sockets[client1_socket]
                break

    def send(self, value, sock):
        str_value = json.dumps(value)
        msg_bytes = str_value.encode()
        sock.sendall(msg_bytes)


if __name__ == '__main__':
    port = 3245
    host = 'localhost'
    server = Servidor(port, host)
