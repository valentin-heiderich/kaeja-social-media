import uuid
import pickle
import os

import Server.data.basicData as bD
import Server.requests.send as send
import Server.logging.log as logger


class clientHandler:
    def __init__(self, cs, addr):
        self.cs = cs
        self.c_addr = addr
        self.connection = True
        self.uuid = uuid.uuid4()
        self.new_posts = []
        self.FORMAT = "utf-8"
        self.HEADER = 1024

        send.send(self.cs, self.uuid)

        self.loop()

    def loop(self):
        while self.connection:
            msg_len = int(self.cs.recv(self.HEADER).decode(self.FORMAT))
            msg = pickle.loads(self.cs.recv(msg_len))

            logger.log(os.path.basename(__file__), logger.csh, f"Received message: {str(msg)}")

            if msg == self.uuid:
                msg = self.g100p()
                send.send(self.cs, msg)
            else:
                bD.posts.append(msg)

    def g100p(self):
        self.new_posts = bD.posts[-100:]
        return self.new_posts
