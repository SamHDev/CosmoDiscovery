def get_local_ip():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return host_ip


def get_mac_addr():
    import uuid
    mac = hex(uuid.getnode())[2:]
    mac = f"{mac[0:2]}:{mac[2:4]}:{mac[4:6]}:{mac[6:8]}:{mac[8:10]}:{mac[10:12]}"
    return mac


def emptyCallback(*args, **kwargs):
    pass


def default_discovery_callback(cls):
    cls.reply()
    print(cls)
