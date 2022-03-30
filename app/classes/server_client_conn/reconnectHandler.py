import app.data.basicData as bD
import app.classes.logging.log as logger

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
            if not bD.connected:
                self.connect()
            time.sleep(5)

    def connect(self):
        try:
            self.socket.connect(self.server)
        except:
            pass
