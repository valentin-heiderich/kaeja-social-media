from functools import partial
from kivy.clock import Clock

import app.classes.server_client_conn.recv as re
import app.classes.logging.log as log
import app.classes.server_client_conn.send as send
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
        self.addr = ('127.0.0.1', 8775)
        self.id = None
        self.connecting = True
        self.cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recv = threading.Thread(target=re.recv, args=(self.cs, self.addr))
        self.FORMAT = "utf-8"
        self.HEADER = 1024

        self.establish_connection()
        self.event = None

    def establish_connection(self):
        """Establish a connection between a Server and the client"""
        while self.connecting:
            try:
                self.cs.connect(self.addr)
                self.connecting = False
            except:
                return False

        msg_len = int(self.cs.recv(self.HEADER).decode(self.FORMAT))
        self.id = pickle.loads(self.cs.recv(msg_len))

        bD.socket = self.cs
        bD.address = self.addr

        self.event = Clock.schedule_interval(partial(self.ask_update), 5)
        self.recv.start()

    def ask_update(self, dt):
        """ask server for newest posts"""
        send.send(self.cs, self.id)
