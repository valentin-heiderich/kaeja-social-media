import socket
import threading
import os

import Server.handleClientConnection as hCC
import Server.data.basicData as bD
# import app.redirects.toClasses as toClasses
import Server.logging.log as log


log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = bD.server_address
server_socket.bind(server_addr)
server_socket.listen(5)

log.log(os.path.basename(__file__), log.SERVER, f"Server running on {str(server_addr)}")


def main_loop():
    while True:
        (cs, addr) = server_socket.accept()
        log.log(os.path.basename(__file__), log.SERVER, f"Client {addr} has connected to the Server")
        client_handler = threading.Thread(target=hCC.clientHandler, args=(cs, addr))
        client_handler.start()


# def test():
#     for i in range(0, 100):
#         log.log(os.path.basename(__file__), log.pc, f"creating post class for post {str(i)} {time.asctime()}")
#         post = toClasses.create_post(image='data/test/img/Ag02.png', content="server testi", bvr=0)
#         bD.posts.append(post)


main_loop()
