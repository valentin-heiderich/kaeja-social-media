import app.data.basicData as bD
import app.classes.logging.log as logger

import time
import os
import socket
import threading


class reconnectHandler:
    def __init__(self):
        logger.log(os.path.basename(__file__), logger.threading, f"Running on thread: {threading.current_thread()}")
        self.server = bD.address
        self.socket = bD.socket

        self.loop()

    def loop(self):
        while True:
            if not bD.connected:
                logger.log(os.path.basename(__file__), logger.csh, f"Trying to reconnect to server {bD.connected}")
                self.connect()
            time.sleep(5)

    def connect(self):
        self.socket.close()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bD.socket = self.socket
        try:
            self.socket.connect(self.server)
            bD.connected = True
            logger.log(os.path.basename(__file__), logger.csh, f"Reconnected to server")
        except: pass
