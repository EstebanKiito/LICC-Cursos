import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Así podemos obtener el hostname de la máquina actual
host = socket.gethostname()
port = 9000

try:
    sock.connect((host,port))
    sock.sendall('GET / HTTP/1.1\n\n\n'.encode('utf-8')) ## Este mensaje es ignorado por el servidor
    data = sock.recv(4096)
    print(data.decode('utf-8'))
except ConnectionError as e:
    # ConnectionError es la clase base BrokenPipeError,ConnectionAbortedError,
    # ConnectionRefusedError y ConnectionResetError.
    print("Ocurrió un error.")
finally:
    # ¡No olvidemos cerrar la conexión!
    sock.close()