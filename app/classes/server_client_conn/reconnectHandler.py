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
        while not bD.connected:
            logger.log(os.path.basename(__file__), logger.csh, f"Trying to reconnect to server {bD.connected}")
            try:
                socketChanger()
                bD.connected = True
            except:
                raise Exception("Could not connect to server")
            time.sleep(5)
