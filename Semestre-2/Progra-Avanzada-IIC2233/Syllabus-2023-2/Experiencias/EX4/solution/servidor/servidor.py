import socket
import threading
import pickle
import sys
import os
from typing import List

class Mensaje:
    
    def __init__(self, operacion = None, data = None, estado = None):
        # Guarda el tipo de operación: listar o descargar
        self.operacion = operacion
        # Guarda la información necesaria según la consulta
        self.data = data
        # Guarda el resultado de la consulta "ok" o "error"
        self.estado = estado

class Servidor:
    id_clientes = 0

    def __init__(self, port: int, host: str):
        self.chunk_size = 2**16
        self.host = host
        self.port = port
        self.sockets = {}
        # TODO: Instanciar un socket para que sea servidor y pueda escuchar conexiones
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_listen()
        self.accept_connections()


    def bind_listen(self) -> None:
        # TODO: Hacemos bind al host y puerto indicado, luego
        # habilitamos el socket para escuchar
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(250)
        print(f'Servidor escuchando en {self.host} : {self.port}')

    def accept_connections(self) -> None:
        # TODO: Creamos un thread que estará escuchando a todo 
        # cliente que se quiera conectar
        thread = threading.Thread(
            target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self) -> None:
        # TODO: Eternamente el thread escucha posibles sockets que quieran
        # conectarse, guarda su dirección en un dicionario y crea otro thread
        # encargado de escuchar únicamente a ese nuevo cliente.
        while True:
            socket_cliente, address = self.socket_server.accept()
            self.sockets[socket_cliente] = address
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(socket_cliente, ),
                daemon=True)
            listening_client_thread.start()

    def listen_client_thread(self, socket_cliente: socket) -> None:
        # TODO: Completar para escuchar mensaje del cliente y procesar su solicitud
        while True:
            print(f"[{self.sockets[socket_cliente]}] Recibiendo largo del siguiente mensaje")
            
            largo_mensaje = int.from_bytes(self.recibir_bytes(socket_cliente, 4), 'big')
            print(f"[{self.sockets[socket_cliente]}] Recibiendo mensaje de largo {largo_mensaje}")
            
            bytes_mensaje = self.recibir_bytes(socket_cliente, largo_mensaje)
            print(f"[{self.sockets[socket_cliente]}] Mensaje de largo {largo_mensaje} recibido")
            if largo_mensaje == 0:
                # Mensaje de largo 0, se cerró el cliente de golpe
                print(f"[{self.sockets[socket_cliente]}] Cliente desconectado")
                del self.sockets[socket_cliente]
                break
            try:
                mensaje = pickle.loads(bytes_mensaje)
                self.manejar_mensaje(mensaje, socket_cliente)
            except Exception as e:
                # En este caso, da lo mismo el tipo de error que ocurra, si el mensaje
                # del cliente provoca un error, se elimina su información y se deja de escuchar
                # de este modo el servidor sigue funcionando 
                print(f"[{self.sockets[socket_cliente]}] Cliente desconectado")
                del self.sockets[socket_cliente]
                break

    def recibir_bytes(self, socket_cliente: socket, cantidad: int) -> bytearray:
        # TODO: Completar con protocolo de recibir mensajes de un socket
        # pero de a chunks cuyo tamaño será máximo self.chunk_size
        bytes_leidos = bytearray()
        while len(bytes_leidos) < cantidad:
            cantidad_restante = cantidad - len(bytes_leidos)
            bytes_leer = min(self.chunk_size, cantidad_restante)
            # Importante recv(N) va a leer hasta N bytes que le manden. Si le mandan
            # menos, por ejemplo, K (con K < N) entonces respuesta será de largo K
            respuesta = socket_cliente.recv(bytes_leer)
            if len(respuesta) < bytes_leer: 
                # Si me llega menos de lo esperado, algo pasó con el cliente, 
                # retorno lo que llevo para intentar ver el mensaje
                return bytes_leidos
            bytes_leidos += respuesta
        return bytes_leidos

    def enviar_mensaje(self, mensaje: Mensaje, socket_cliente: socket) -> None:
        # TODO: Completar con protocolo para enviar mensaje
        print(f'[{self.sockets[socket_cliente]}] Enviando {mensaje}')
        bytes_mensaje = pickle.dumps(mensaje)
        socket_cliente.sendall(len(bytes_mensaje).to_bytes(4, 'big'))
        socket_cliente.sendall(bytes_mensaje)
        print(f'[{self.sockets[socket_cliente]}] {mensaje} enviado')

    def manejar_mensaje(self, mensaje: Mensaje, socket_cliente: socket) -> None:
        # TODO: Respuesta del servidor según el comando enviado por el cliente
        if mensaje.operacion == 'listar':
            respuesta = Mensaje(data=self.listar_archivos(), estado = 'ok')
            self.enviar_mensaje(respuesta, socket_cliente)
        elif mensaje.operacion == 'descargar':
            nombre_archivo = mensaje.data
            if nombre_archivo in self.listar_archivos():
                self.enviar_archivo(nombre_archivo, socket_cliente)
            else:
                respuesta = Mensaje(estado = 'error')
                self.enviar_mensaje(respuesta, socket_cliente)

    def enviar_archivo(self, archivo: str, socket_cliente: socket) -> None:
        # TODO: Completar método para enviar un archivo
        with open(os.path.join('archivos', archivo), 'rb') as file:
            bytes_archivo = file.read()
        respuesta = Mensaje(data=bytes_archivo, estado='ok')
        self.enviar_mensaje(respuesta, socket_cliente)

    def listar_archivos(self) -> List[str]:
        return os.listdir('archivos')

if __name__ == '__main__':
    # TODO: Completar con el uso de sys.argv para dar parámetros por consola
    # Por ejemplo: python3 servidor.py 4444 localhost
    PORT = 3247 if len(sys.argv) < 2 else int(sys.argv[1])
    HOST = 'localhost' if len(sys.argv) < 3 else sys.argv[2]
    server = Servidor(PORT, HOST)
