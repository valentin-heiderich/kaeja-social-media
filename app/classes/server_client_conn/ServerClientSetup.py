import app.classes.server_client_conn.ClientServerHandler as ClientServerHandler
import app.classes.logging.log as log
import app.data.basicData as bD

import socket
import threading
import time
import os
import pickle


class updateFeed:
    def __init__(self):
        """Create all vars and start functions/files"""
        log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")
        self.start_time = time.time()
        self.server_addr = bD.server_address
        self.id = None
        self.connecting = True

        self.cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.FORMAT = "utf-8"
        self.HEADER = 1024

        self.connectionHandler = threading.Thread(target=ClientServerHandler.ClientServerHandler, args=(self.cs, self.server_addr))

        self.establish_connection()
        self.event = None

        return

    def establish_connection(self):
        """Establish a connection between a Server and the client"""
        while self.connecting:
            try:
                self.cs.connect(self.server_addr)
                self.connecting = False
            except:
                return

        msg_len = int(self.cs.recv(self.HEADER).decode(self.FORMAT))
        self.id = pickle.loads(self.cs.recv(msg_len))

        bD.socket = self.cs
        bD.address = self.server_addr
        bD.connected = True
        bD.client_id = self.id

        self.connectionHandler.start()

        return
