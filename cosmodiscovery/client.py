import socket
import json
import threading
import time

from .utils import *
from .message import *

class DiscoveryClient:
    def __init__(self, host="255.255.255.255", port=12892, buffer_size=1024, scheme="_discovery.default",
                 device_name=None):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.scheme = scheme
        self.device_name = device_name
        if device_name is None:
            self.device_name = socket.gethostname()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.running = False

        self.results = []

    def form_msg(self, data):
        return json.dumps({
            "proto": "_cosmo.discovery",
            "request": "discovery.find",
            "scheme": self.scheme,
            "host": {"ip": get_local_ip(), "port": self.port, "mask": self.host, "mac": get_mac_addr(),
                     "hostname": socket.gethostname()},
            "data": data
        })

    def push(self, data=None):
        if data is None:
            data = {}
        self.sock.sendto(self.form_msg(data).encode("UTF-8"), (self.host, self.port))

    def listen(self):
        while self.running:
            msg, addr = self.sock.recvfrom(self.buffer_size)
            self._handle_msg(msg, addr)

    def discovery(self, timeout=5, data=None):
        self.running = True
        thd = threading.Thread(target=self.listen,daemon=True)
        thd.start()
        self.push(data)
        time.sleep(timeout)
        self.running = False

        res = self.results.copy()
        self.results = []
        return res

    def _handle_msg(self, msg, addr):
        try:
            data = json.loads(msg.decode("UTF-8"))
        except json.JSONDecodeError:
            return None

        if not data["proto"] == "_cosmo.discovery":  # Check Proto Var
            return None

        if not data["scheme"] == self.scheme:  # Check Scheme Name
            return None

        if data["request"] == "discovery.reply":
            cls = DiscoveryReplyMessage(self, data, addr)
            self.results.append(DiscoveryResult(cls))
            return cls
