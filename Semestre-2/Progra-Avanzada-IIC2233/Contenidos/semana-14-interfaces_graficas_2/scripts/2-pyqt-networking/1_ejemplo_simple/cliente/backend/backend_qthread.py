import socket
from constantes import SIZE_BUFFER
from PyQt6.QtCore import QObject, QThread, pyqtSignal


# Primero, definiremos un QThread personalizado, que recibirá un socket
# Y se dedicará a escuchar cualquier mensaje de este y enviarlo al componente
class EscucharQThread(QThread):
    # Señal que enviará información del mensaje al componente lógico
    senal_mensaje_del_servidor = pyqtSignal(str)

    def __init__(self, socket: socket.socket) -> None:
        super().__init__()
        self.socket = socket

    def run(self) -> None:
        print("Levantando el thread que escucha al servidor...")
        while True:
            data = self.socket.recv(SIZE_BUFFER).decode("utf-8")

            # Emitimos la señal con el mensaje decodificado
            self.senal_mensaje_del_servidor.emit(data)


# En este componente lógico instanciamos el socket para
# la comunicación, y las funciones de recepción y envío de mensajes.
# Esta hará uso de nuestro QThread para escuchar mensajes.
class Logica(QObject):

    senal_actualizar_etiqueta = pyqtSignal(str)

    def __init__(self, host: str, port: int) -> None:
        super().__init__()
        self.thread = None

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
        if self.thread is None or not self.thread.isRunning():
            self.thread = EscucharQThread(self.socket_cliente)
            # Conectamos la señal a una función que procese mensajes
            self.thread.senal_mensaje_del_servidor.connect(self.procesar_mensaje)
            # Empezamos el thread
            self.thread.start()

    # Aquí procesamos el contenido del mensaje
    # Para este ejemplo, solo lo mandamos al frontend
    def procesar_mensaje(self, mensaje: str) -> None:
        self.senal_actualizar_etiqueta.emit(mensaje)

    def mandar_comando(self, comando: str) -> None:
        self.socket_cliente.send(comando.encode("utf-8"))
