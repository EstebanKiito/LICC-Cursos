import datetime
import json
import socket
from threading import Thread
from constantes import HOST_DEFECTO, PORT_DEFECTO, SIZE_BUFFER


class Servidor:
    def __init__(self, host: int, port: int) -> None:
        self.clientes = []

        # Creamos el socket, hacemos bind y listen
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen()

    def escuchar_conexiones(self) -> None:
        print("Empezando a escuchar clientes....")
        while True:
            try:
                # Aceptamos a un cliente
                socket_cliente, info_dir = self.sock.accept()
                print("Conexión aceptada desde", info_dir)

                # Guardamos el socket de este cliente en una lista
                self.clientes.append(socket_cliente)

                # Creamos un thread encargado de escuchar a ese cliente
                thread = Thread(
                    target=self.escuchar_cliente,
                    args=(socket_cliente, info_dir),
                    daemon=True,
                )
                thread.start()

            except ConnectionError:
                print("Ocurrió un error con la conexión. Se cerrará toda conexión")
                return

    # método encargado de escuchar a 1 cliente
    def escuchar_cliente(self, socket_cliente: socket.socket, info_dir: tuple) -> None:
        while True:
            print(f"[{info_dir}] Esperando mensaje")
            try:
                mensaje_codificado = socket_cliente.recv(SIZE_BUFFER)
                mensaje = json.loads(mensaje_codificado.decode("utf-8"))

                print(f"[{info_dir}] mandó un mensaje.... {mensaje}")
                if mensaje["key"] == "cambio":
                    # Si me llega el comando "cambio". Se manda lo que
                    # contenga mensaje["arg"], lo que será "adelantar"
                    # "retrasar". Este comando se manda a cada cliente.

                    respuesta_codificada = mensaje["arg"].encode("utf-8")
                    for socket_c in self.clientes:
                        socket_c.send(respuesta_codificada)

                # En otro caso, mando la hora del país solicitado al socket
                # en particular.
                else:  # mensaje["key"] == "hora":
                    utc_ahora = datetime.datetime.now(datetime.UTC)
                    if mensaje["arg"] == "chile":
                        # Chile está en UTC-3
                        diferencia_horaria = datetime.timedelta(hours=-3)
                    else:  # mensaje["arg"] == "japón"
                        # Japón está en UTC+9
                        diferencia_horaria = datetime.timedelta(hours=9)

                    hora_solicitada = utc_ahora + diferencia_horaria
                    hora_str = str(int(hora_solicitada.timestamp()))

                    socket_cliente.send(hora_str.encode("utf-8"))

            except Exception:
                # Ante cualquier error, se acaba la conexión con este cliente
                # En este caso, se termina el thread que mantenía la conexión
                # con el socket de un cliente.
                # Y debemos eliminar el socket de nuestra lista.
                print(f"[{info_dir}] cerrando conexión")
                self.clientes.remove(socket_cliente)
                return

    def cerrar(self) -> None:
        print("Cerrando socket.")
        self.sock.close()


if __name__ == "__main__":

    servidor = Servidor(HOST_DEFECTO, PORT_DEFECTO)
    try:
        servidor.escuchar_conexiones()
    except KeyboardInterrupt:
        print("Se hizo CTLR+C ... finalizando el programa.")

    servidor.cerrar()
