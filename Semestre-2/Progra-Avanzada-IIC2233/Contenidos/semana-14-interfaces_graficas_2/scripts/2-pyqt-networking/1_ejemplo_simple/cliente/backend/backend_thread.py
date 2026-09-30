import socket
import threading
from constantes import SIZE_BUFFER
from PyQt6.QtCore import QObject, pyqtSignal


# Definimos un Thread personalizado, que recibirá un socket
# Y se dedicará a escuchar cualquier mensaje de este y enviarlo al componente
class EscucharThread(threading.Thread):
    def __init__(self, socket: socket.socket, senal_mensaje: pyqtSignal) -> None:
        super().__init__()
        self.socket = socket
        self.senal_mensaje_del_servidor = senal_mensaje
        self.daemon = True

    def run(self) -> None:
        print("Levantando el thread que escucha al servidor...")
        while True:
            data = self.socket.recv(SIZE_BUFFER).decode("utf-8")
            if len(data) == 0:
                print("Me llegó un mensaje vacío, dejaré de escuchar")
                break

            # Emitimos la señal con el mensaje decodificado
            self.senal_mensaje_del_servidor.emit(data)


# En este componente lógico instanciamos el socket para
# la comunicación, y las funciones de recepción y envío de mensajes.
# Esta hará uso de nuestro Thread para escuchar mensajes.
class Logica(QObject):

    senal_actualizar_etiqueta = pyqtSignal(str)
    senal_mensaje_del_servidor = pyqtSignal(str)

    def __init__(self, host: str, port: int) -> None:
        super().__init__()
        self.thread = None
        self.senal_mensaje_del_servidor.connect(self.procesar_mensaje)

        print("Inicializando cliente...")
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

        try:
            self.conectar_a_servidor()
            self.escuchar()
        except ConnectionError:
            print("Conexión terminada.")
            self.socket_cliente.close()
            exit()

    def conectar_a_servidor(self) -> None:
        self.socket_cliente.connect((self.host, self.port))
        print("Cliente conectado exitosamente al servidor.")

    def escuchar(self) -> None:
        # Revisamos si hay un thread que escucha activo o no,
        # y creamos uno en caso contrario
        if self.thread is None or not self.thread.is_alive():
            self.thread = EscucharThread(
                self.socket_cliente, self.senal_mensaje_del_servidor
            )

            # Empezamos el thread
            self.thread.start()

    # Aquí procesamos el contenido del mensaje
    # Para este ejemplo, solo lo mandamos al frontend
    def procesar_mensaje(self, mensaje: str) -> None:
        self.senal_actualizar_etiqueta.emit(mensaje)

    def mandar_comando(self, comando: str) -> None:
        self.socket_cliente.send(comando.encode("utf-8"))
