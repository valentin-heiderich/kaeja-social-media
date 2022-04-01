import app.data.basicData as bD

import socket


class socketChanger:
    def __init__(self):
        self.currentSocket = bD.socket
        self.newSocket = None

    def change_socket(self):
        self.currentSocket.close()
        self.newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.newSocket.connect(bD.address)
        except:
            raise Exception("Could not connect to server")
        self.currentSocket = self.newSocket
        bD.socket = self.currentSocket
        return
