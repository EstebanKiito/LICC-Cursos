import datetime
import json
import socket
import threading
import time
from constantes import SIZE_BUFFER
from PyQt6.QtCore import QObject, pyqtSignal


# Definiremos un Thread que simula nuestro Reloj, quien actualizará
# el frontend cada 1 segundo
class Reloj(threading.Thread):
    def __init__(self, senal_actualizar_etiqueta: pyqtSignal) -> None:
        super().__init__()
        self._hora_actual = 0
        self.senal_actualizar_etiqueta = senal_actualizar_etiqueta
        self.lock = threading.Lock()
        self.daemon = True

    @property
    def hora_actual(self) -> int:
        return self._hora_actual

    @hora_actual.setter
    def hora_actual(self, nueva_hora: int) -> None:
        # Para asegurarnos que solo un thread edite la hora a la vez
        # usamos un lock
        with self.lock:
            self._hora_actual = nueva_hora

    def run(self) -> None:
        while True:
            # Transformo la hora en str y emito la señal
            timestamp = datetime.datetime.fromtimestamp(self.hora_actual)
            hora_str = timestamp.strftime("%Y-%m-%d %H:%M:%S %p")
            self.senal_actualizar_etiqueta.emit(hora_str)

            # Sumar 1 segundo (1000ms) y luego dormir 1 segundo antes de
            # actualizar nuevamente la hora
            self.hora_actual += 1
            time.sleep(1)


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
        self.reloj = Reloj(self.senal_actualizar_etiqueta)
        self.senal_mensaje_del_servidor.connect(self.procesar_mensaje)

        print("Inicializando cliente...")
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

        try:
            self.conectar_a_servidor()
            self.pedir_hora("chile")
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
    def procesar_mensaje(self, mensaje: str) -> None:
        if mensaje == "adelantar":
            # Adelantamos 3600 segundos (1 hora)
            self.reloj.hora_actual += 3600
        elif mensaje == "retrasar":
            # Retrasamos 3600 segundos (1 hora)
            self.reloj.hora_actual -= 3600
        else:
            # En este caso, mensaje no es "adelantar" o "retrasar"
            # Entonces es un número (la hora de un país)
            self.reloj.hora_actual = int(mensaje)

        # Si el reloj no ha empezado a ejecutarse, se le hace start()
        if not self.reloj.is_alive():
            self.reloj.start()

    def mandar_comando(self, comando: str) -> None:
        # Si pedimos adelantar o retrasar la hora, mandamos la key "cambio"
        # y en "arg" mandamos el comando: "adelantar" o "retrasar".
        mensaje_json = json.dumps({"key": "cambio", "arg": comando})
        mensaje_codificado = mensaje_json.encode("utf-8")
        self.socket_cliente.send(mensaje_codificado)

    def pedir_hora(self, pais: str) -> None:
        # Si pedimos la hora de un país en específico, mandamos la key "hora"
        # Y en "arg" ponemos el nombre del país.
        mensaje_json = json.dumps({"key": "hora", "arg": pais})
        mensaje_codificado = mensaje_json.encode("utf-8")
        self.socket_cliente.send(mensaje_codificado)
