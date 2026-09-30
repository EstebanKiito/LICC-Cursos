import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Así podemos obtener el hostname de la máquina actual
host = 'localhost'
port = 8998

sock.bind((host, port))
sock.listen()
print("[Servidor] Aceptando conexiones en el puerto", port)

counter = 0
while counter < 5:
    try:
        socket_cliente, address = sock.accept()
        print("[Servidor] Conexión aceptada desde", address)

        ## Este servidor no lee lo que envía el cliente, sino que responde
        ## lo mismo por cada conexión.
        socket_cliente.sendall("Gracias por conectarte\n".encode("utf-8"))
        socket_cliente.close()
        counter += 1
    except ConnectionError:
        print("[Servidor] Ocurrió un error.")

print("[Servidor] Se han recibido 5 clientes, por lo que se cerrara la conexión")
sock.close()
