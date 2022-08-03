import socket
import threading
import os

import Server.connectionManagement.handleClientConnection as hCC
import Server.data.basicData as bD
import Server.logging.log as log


class ServerSocket:
    def __init__(self):
        self.addr = bD.server_address
        self.socket = None
        self.clients = []

        self.initialize()
        self.accept_clients()

    def initialize(self):
        log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.addr)
        self.socket.listen(5)

        bD.running = True

        log.log(os.path.basename(__file__), log.SERVER, f"Server running on {str(self.addr)}")

    def accept_clients(self):
        while bD.running:
            (cs, client_addr) = self.socket.accept()
            log.log(os.path.basename(__file__), log.SERVER, f"Client {client_addr} has connected to the Server")
            threading.Thread(target=hCC.clientHandler, args=(cs, client_addr)).start()
