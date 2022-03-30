import pickle
import app.data.basicData as bD


class send:
    def __init__(self, socket, data):
        self.data = data
        self.socket = socket
        self.FORMAT = "utf-8"
        self.HEADER = 1024

        self.load_socket()
        self.send()

    def load_socket(self):
        if self.socket is None:
            if bD.socket is None: raise Exception("Socket is None")
            self.socket = bD.socket

    def send(self):
        data_len = str(len(pickle.dumps(self.data))).encode(self.FORMAT)
        if len(data_len) > self.HEADER: return False
        data_len += b' ' * (self.HEADER - len(data_len))
        self.socket.send(data_len)
        self.socket.send(pickle.dumps(self.data))
        return True
