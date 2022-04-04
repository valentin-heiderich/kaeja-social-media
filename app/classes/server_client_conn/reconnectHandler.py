import app.data.basicData as bD
import app.classes.logging.log as logger
from app.classes.server_client_conn.changeSocket import socketChanger

import time
import os
import threading


class reconnectHandler:
    def __init__(self):
        logger.log(os.path.basename(__file__), logger.threading, f"Running on thread: {threading.current_thread()}")
        self.server = bD.address
        self.socket = bD.socket

        self.loop()

    def loop(self):
        while True:
            self.reconnect()
            time.sleep(5)

    def reconnect(self):
        if bD.connected: return
        try:
            socketChanger()
        except:
            logger.log(os.path.basename(__file__), logger.csh, f"Failed to connect to server")
