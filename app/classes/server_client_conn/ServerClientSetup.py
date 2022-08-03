import classes.server_client_conn.ClientServerHandler as ClientServerHandler
import classes.cryptography.setup_keys as sec_set
import classes.logging.log as log
import data.basicData as bD

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
        sec_set.setup_pycryptodome_keys()
        while self.connecting:
            try:
                self.cs.connect(self.server_addr)
                self.connecting = False
                log.log(os.path.basename(__file__), log.csh, f"Connected to Server: {self.server_addr}")
            except:
                log.log(os.path.basename(__file__), log.csh, f"Failed to reach Server: {self.server_addr}")

        msg_len = int(self.cs.recv(self.HEADER).decode(self.FORMAT))
        self.id = pickle.loads(self.cs.recv(msg_len))

        log.log(os.path.basename(__file__), log.csh, f"Client ID: {self.id}")

        bD.socket = self.cs
        bD.address = self.server_addr
        bD.connected = True
        bD.client_id = self.id

        self.connectionHandler.start()

        return
