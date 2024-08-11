import socket
import threading
import pickle
import sys
import os


class Mensaje:
    def __init__(self, operacion=None, data=None, estado=None):
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

    def bind_listen(self):
        # TODO: Debe enlazar el puerto y el host, y escuchar conexiones
        pass

    def accept_connections(self):
        # TODO: Debe inicializar el thread encargado de aceptar nuevas
        # conexiones
        pass

    def accept_connections_thread(self):
        # TODO: El servidor debe estar constantemente aceptando nuevas conexiones
        # A cada nueva conexión, le debe inicializar un hilo para escuchar a dicho
        # cliente.
        pass

    def listen_client_thread(self, socket_cliente: socket):
        # TODO: Recibe los mensajes del socket, carga el mensaje y llama al método
        # manejar mensaje.
        pass

    def recibir_bytes(self, socket_cliente: socket, cantidad: int):
        # TODO: Debe recibir <cantidad> bytes desde el <socket_cliente>
        pass

    def enviar_mensaje(self, mensaje: Mensaje, socket_cliente: socket):
        # TODO: Debe enviar el mensaje cumpliendo con las reglas antes mencionadas:
        # Primero enviar 4 bytes con el largo del mensaje, y luego el mensaje
        pass

    def manejar_mensaje(self, mensaje: Mensaje, socket_cliente: socket):
        # TODO: Si la operacion del mensaje es listar, debe enviar
        # la lista de archivos. Si la operacion es descargar, debe
        # verificar que el archivo exista, y si existe entonces debe
        # enviarlo utilizando el método enviar_archivo
        pass

    def enviar_archivo(self, archivo: str, socket_cliente: socket):
        # TODO: Debe enviar el archivo al socket
        pass

    def listar_archivos(self):
        return os.listdir("archivos")


if __name__ == "__main__":
    # TODO: El puerto y el host deben poder pasarse por consola,
    # y en caso de que no se reciban, tener por defecto un valor.
    PORT = None
    HOST = None
    server = Servidor(PORT, HOST)
