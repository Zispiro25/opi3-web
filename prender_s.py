from wakeonlan  import send_magic_packet

def prender_server():
    try:
        send_magic_packet('00:e0:0b:58:41:08',ip_address='192.168.100.13')
        return True
    except ValueError as e:
        return False