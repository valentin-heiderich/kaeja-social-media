import app.data.basicData as bD
import app.classes.logging.log as logger

import time
import os
import threading
import pickle
import socket


class reconnectHandler:
    def __init__(self):
        logger.log(os.path.basename(__file__), logger.threading, f"Running on thread: {threading.current_thread()}")
        self.server = bD.address
        self.socket = bD.socket
        self.addr = bD.address
        self.id = bD.client_id
        self.HEADER = 1024
        self.FORMAT = 'utf-8'

        self.loop()

    def loop(self):
        while True:
            self.reconnect()
            time.sleep(5)

    def reconnect(self):
        if bD.connected: return
        try:
            self.change_socket()
        except:
            logger.log(os.path.basename(__file__), logger.csh, f"Failed to connect to server")

    def change_socket(self):
        bD.socket.close()
        bD.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket = bD.socket

        self.establish_connection()

    def establish_connection(self):
        """Establish a connection between a Server and the client"""
        try:
            bD.socket.connect(self.addr)
        except:
            return

        msg_len = int(bD.socket.recv(self.HEADER).decode(self.FORMAT))
        self.id = pickle.loads(bD.socket.recv(msg_len))

        bD.connected = True
        bD.client_id = self.id
        return

