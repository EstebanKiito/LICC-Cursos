import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Así podemos obtener el hostname de la máquina actual
host = 'localhost'
port = 8998

try:
    sock.connect((host, port))
    data = sock.recv(4096)
    print(data.decode('utf-8'))
except ConnectionError as e:
    # ConnectionError es la clase base BrokenPipeError, ConnectionAbortedError,
    # ConnectionRefusedError y ConnectionResetError.
    print("[Cliente] Ocurrió un error.")
finally:
    # ¡No olvidemos cerrar la conexión!
    sock.close()
