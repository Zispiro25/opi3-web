from wakeonlan  import send_magic_packet

def prender_server():
    send_magic_packet('00:e0:0b:58:41:08','192.168.100.13')