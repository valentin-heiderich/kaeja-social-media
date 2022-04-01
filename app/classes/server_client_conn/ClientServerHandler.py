from kivy.clock import Clock
from functools import partial

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
        self.client_id = bD.client_id

        self.recv = None
        self.reconnectHandler = None

        self.declare_threads()
        self.handle_runtime()

        self.update = self.event = Clock.schedule_interval(partial(self.ask_for_update), 5)

    def declare_threads(self):
        self.recv = threading.Thread(target=re.recv, args=(self.client_socket, self.server_address))
        self.reconnectHandler = threading.Thread(target=reconnectHandler.reconnectHandler)
        self.start_threads()

    def start_threads(self):
        self.recv.start()
        self.reconnectHandler.start()

    def handle_runtime(self):
        pass

    def ask_for_update(self, dt):
        send.send(None, self.client_id)

