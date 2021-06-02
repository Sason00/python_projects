import socket
from threading import Thread

class proxy2server(Thread):
    def __init__(self, host, port):
        super(proxy2server, self).__init__()
        self.game = None
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((self.host, self.port))
    def run(self):
        while True:
            data = self.server.recv(4096)
            if data:
                self.game.sendall(data)
            print("hi")

class game2proxt(Thread):
    def __init__(self, host, port):
        super(game2proxt, self)
        self.server = None
        self.host = host
        self.port = port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))
        sock.listen(1)
        self.game, addr = socket.accept()
    def run(self):
        while True:
            self.game.recv(4096)
            if data:
                self.server.sendall(data)

class Proxy(Thread):
    def __innit__(self, from_host, to_host, port):
        super(Proxy, self).__init__()
        self.from_host = from_host
        self.to_host = to_host
        self.port = port
    def run(self):
        while True:
            print(r"proxy{self.port} getting ready")
            self.g2p = game2proxt(self.from_host, self.port)
            self.p2s = proxy2server(self.to_host, self.port)
            print(r"proxy{self.port} is ready")
            self.g2p.server = self.p2s.server
            self.p2s.game = self.g2p.game
            self.g2p.start()
            self.p2s.start()


m_s = Proxy("0.0.0.0", "104.22.77.208", 3333)

for i in range(3000, 3006):
    _game_server = Proxy("0.0.0.0", "104.22.77.208", 3333)
    _game_server.start()