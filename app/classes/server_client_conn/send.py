import pickle
import os

import data.basicData as bD
import classes.logging.log as log


class send:
    def __init__(self, socket, data, data_type=None):
        self.valid = True

        self.socket = bD.socket
        self.FORMAT = "utf-8"
        self.HEADER = 1024

        self.data = data
        self.data_len = None
        self.data_type = data_type
        self.a_header = ""
        self.b_header = ""

        self.load_socket()
        self.prepare_data()
        self.check_validity()
        self.send()

    def load_socket(self):
        if self.socket is None:
            if bD.socket is None: self.valid = False
            self.socket = bD.socket

    def prepare_data(self):
        self.data_len = str(len(pickle.dumps(self.data))).encode(self.FORMAT)
        self.data_len += b' ' * (self.HEADER - len(self.data_len))

        self.data_type = str(self.data_type).encode(self.FORMAT)

        self.a_header = self.data_len
        self.b_header = self.data_type

    def check_validity(self):
        if len(self.a_header) > self.HEADER: self.valid = False
        if not len(self.b_header) == 5: self.valid = False
        if not bD.connected: self.valid = False
        if self.data_type is None: self.valid = False

        if not self.valid: raise Exception("send: data is not valid")  # raise exception if data is not valid

    def send(self):
        try:
            self.socket.send(self.a_header)
            self.socket.send(self.b_header)
            self.socket.send(pickle.dumps(self.data))
        except:
            log.log(os.path.basename(__file__), log.csh, "Error sending data, server may be down")
            bD.connected = False
        return True
