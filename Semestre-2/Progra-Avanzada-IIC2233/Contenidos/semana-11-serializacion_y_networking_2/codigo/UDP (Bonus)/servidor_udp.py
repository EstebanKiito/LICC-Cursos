import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Con un string vacío como argumento del bind, indicamos que el socket es
# alcanzable desde cualquier dirección que pueda tener el servidor.
sock.bind(("", 15000))

while True:
    data, (host_cliente, puerto_cliente) = sock.recvfrom(4096)
    print(data.decode('utf-8'))
    respuesta = f"Aquí va mi respuesta para {host_cliente}."
    sock.sendto(respuesta.encode('utf-8'), (host_cliente, puerto_cliente))
