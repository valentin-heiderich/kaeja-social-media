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
        self.B_HEADER = 5

        send.send(self.cs, self.uuid)

        self.loop()

    def loop(self):
        while self.connection:
            a_header = int(self.cs.recv(self.HEADER).decode(self.FORMAT))
            b_header = str(self.cs.recv(self.B_HEADER).decode(self.FORMAT))
            msg = pickle.loads(self.cs.recv(a_header))

            logger.log(os.path.basename(__file__), logger.csh, f"Received message: {str(msg)}")

            if b_header == "00001":
                respond = self.g100p()
                send.send(self.cs, respond)
            elif b_header == "00010":
                bD.posts.append(msg)
            elif b_header == "00011":
                pass
            elif b_header == "00100":
                account_id = uuid.uuid4()
                bD.accounts.update({account_id: msg})

    def g100p(self):
        self.new_posts = bD.posts[-100:]
        return self.new_posts
