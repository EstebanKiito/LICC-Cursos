import socket
from random import choice
from threading import Thread
from constantes import HOST_DEFECTO, PORT_DEFECTO, SIZE_BUFFER, SALUDOS, COLORES


# Función encargada de escuchar a 1 cliente
def escuchar_cliente(socket_cliente: socket.socket) -> None:
    while True:
        try:
            mensaje = socket_cliente.recv(SIZE_BUFFER).decode("utf-8")
            if mensaje == "palabra":
                respuesta = choice(SALUDOS)
            else:  # mensaje == "color"
                respuesta = choice(COLORES)
            socket_cliente.send(respuesta.encode("utf-8"))

        except Exception:
            # Ante cualquier error, se acaba la conexión
            # En este caso, se termina el thread que mantenía la conexión
            # con el socket de un cliente
            return


if __name__ == "__main__":
    # Creamos el socket, hacemos bind y listen
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST_DEFECTO, PORT_DEFECTO))
    sock.listen()

    counter = 0
    while counter < 5:
        try:
            print("Esperando que alguien se quiera conectar...")
            # Aceptamos a un cliente
            socket_cliente, address = sock.accept()
            print("Conexión aceptada desde", address)

            # Creamos un thread encargado de escuchar a ese cliente
            thread = Thread(
                target=escuchar_cliente, args=(socket_cliente,), daemon=True
            )
            thread.start()
            counter += 1
        except ConnectionError:
            print("Ocurrió un error con la conexión. Se dejará de escuchar.")
            break

        except KeyboardInterrupt:
            print("Se hizo CTLR+C ... finalizando el programa.")
            break

    print("Cerrando socket.")
    sock.close()
