import pickle


class send:
    def __init__(self, socket, data):
        self.data = data
        self.socket = socket
        self.FORMAT = "utf-8"
        self.HEADER = 1024

        self.send(self.data)

    def send(self, data):
        data_len = str(len(pickle.dumps(data))).encode(self.FORMAT)
        if len(data_len) > self.HEADER: return False
        data_len += b' ' * (self.HEADER - len(data_len))
        self.socket.send(data_len)
        self.socket.send(pickle.dumps(data))
        return True
