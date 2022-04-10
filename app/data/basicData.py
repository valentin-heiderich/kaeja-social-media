import os
import pickle

# runtime data
recv_posts = pickle.dumps([])

socket = None
address = None
connected = False
client_id = None

# predefined data
user_name = str(os.getlogin())
server_address = ('127.0.0.1', 8775)
