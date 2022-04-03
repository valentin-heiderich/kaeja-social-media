import app.data.basicData as bD

import socket


class socketChanger:
    def __init__(self):
        self.currentSocket = bD.socket
        self.newSocket = None

        self.change_socket()

    def change_socket(self):
        self.currentSocket.close()
        self.newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.newSocket.connect(bD.address)
            self.currentSocket = self.newSocket
            bD.socket = self.currentSocket
            bD.connected = True
        except:
            return
        return
