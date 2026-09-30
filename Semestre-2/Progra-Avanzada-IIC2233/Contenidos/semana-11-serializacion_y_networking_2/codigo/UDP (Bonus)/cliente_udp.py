import socket

server_host = socket.gethostname()
server_port = 15000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mensaje = "Hola, simplemente te estoy enviando un mensaje.".encode('utf-8')
sock.sendto(mensaje, (server_host, server_port))

data, (host_origen, puerto_origen) = sock.recvfrom(4096)
print(data.decode('utf-8'))

sock.close()
