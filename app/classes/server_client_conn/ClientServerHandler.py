import app.classes.server_client_conn.recv as re
import app.classes.server_client_conn.reconnectHandler as reconnectHandler
import app.classes.logging.log as logger
import app.data.basicData as bD
import app.classes.server_client_conn.send as send

import threading
import os
import time


class ClientServerHandler:
    def __init__(self, client_socket, server_address):
        logger.log(os.path.basename(__file__), logger.csh, f"Running on Thread: {threading.current_thread()}")

        self.client_socket = client_socket
        self.server_address = server_address

        self.recv = None
        self.reconnectHandler = None

        self.declare_threads()
        self.start_threads()
        self.handle_runtime()

    def declare_threads(self):
        self.recv = threading.Thread(target=re.recv, args=(self.client_socket, self.server_address))
        self.reconnectHandler = threading.Thread(target=reconnectHandler.reconnectHandler)

    def start_threads(self):
        self.recv.start()
        self.reconnectHandler.start()

    def handle_runtime(self):
        while bD.connected:
            self.client_socket = bD.socket
            send.send(None, bD.client_id)
            time.sleep(5)


