class DiscoveryServer:
    def __init__(self, host="", port=12892, buffer_size=1024, scheme="_discovery._cosmo.default"):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.scheme = scheme

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.running = False

        self.discovery_callback_func = default_discovery_callback

    def listen(self, threaded=False):
        if threaded:
            thd = threading.Thread(target=self._run,daemon=True)
            thd.start()
        else:
            self._run()

    def _run(self):
        self.sock.bind((self.host, self.port))
        self.running = True
        self._handle()

    def discovery_callback(self, func):
        self.discovery_callback_func = func

    def _handle(self):
        while self.running:
            msg, addr = self.sock.recvfrom(self.buffer_size)

            self._handle_msg(msg, addr)

    def _handle_msg(self, msg, addr):
        try:
            data = json.loads(msg.decode("UTF-8"))
        except json.JSONDecodeError:
            return None

        if not data["proto"] == "_cosmo.discovery":  # Check Proto Var
            return None

        if not data["scheme"] == self.scheme:  # Check Scheme Name
            return None

        if data["request"] == "discovery.find":
            cls = DiscoveryRequestMessage(self, data, addr)
            self.discovery_callback_func(cls)
            return cls

    def close(self):
        self.running = False
