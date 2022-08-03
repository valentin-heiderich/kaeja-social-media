import threading

from Server.sockets.ServerSocket import ServerSocket
from Server.console.console import console
import Server.classes.posts as posts


class Server:
    def __init__(self):
        self.socket = None
        self.console = None

        self.start()

    def start(self):
        self.socket = threading.Thread(target=ServerSocket).start()
        # self.console = threading.Thread(target=console).start()

        posts.load_posts()


if __name__ == '__main__':
    Server()
