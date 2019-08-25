import socket
import json
import threading
import time


class DiscoveryMessage:
    def __init__(self, master, data, addr):
        self.master = master
        self.addr = addr
        self.raw = data
        self.proto = data["proto"]
        self.request = data["request"]
        self.scheme = data["scheme"]
        self.host_raw = data["host"]
        self.host_ip = data["host"]["ip"]
        self.host_port = data["host"]["port"]
        self.host_mask = data["host"]["mask"]
        self.host_mac = data["host"]["mac"]
        self.host_name = data["host"]["hostname"]

        self.data = data["data"]

    def reply(self, msg):
        self.master.sock.sendto(msg.encode("UTF-8"), self.addr)

    def __repr__(self):
        return str(self.raw)


class DiscoveryRequestMessage(DiscoveryMessage):
    def __init__(self, master, data, addr):
        super().__init__(master, data, addr)

    def reply(self, value=True, data=None):
        if data is None:
            data = {}
        msg = self.form_msg(data)
        super().reply(msg)

    def form_msg(self, data):
        return json.dumps({
            "proto": "_cosmo.discovery",
            "request": "discovery.reply",
            "scheme": self.scheme,
            "host": {"ip": get_local_ip(), "port": self.master.port, "mask": self.master.host, "mac": get_mac_addr(),
                     "hostname": socket.gethostname()},
            "data": data
        })


class DiscoveryReplyMessage(DiscoveryMessage):
    def __init__(self, master, data, addr):
        super().__init__(master, data, addr)
