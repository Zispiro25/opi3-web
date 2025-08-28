from wakeonlan  import send_magic_packet
from socket import socket, AF_INET, SOCK_STREAM
from time import sleep
def prender_server():
    send_magic_packet('00-e0-0b-58-41-08')
def apagar_server():
    sock = socket(AF_INET, SOCK_STREAM)
    connect = ""
    for i in range(5):
        try:
            sock.connect("192.168.100.13", 5001)
            connect = sock.recv(1024)
            if connect.decode("ascii") == "conectado":
                break
        except ConnectionRefusedError:
            sleep(5)
    orden = "sudo shudown now"
    mensaje = orden.encode("ascii")
    sock.sendall(mensaje)
