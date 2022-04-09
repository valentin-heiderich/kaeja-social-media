import os

# runtime data
feed = []
new_posts = []
recv_posts = []
post_widgets = []

socket = None
address = None
connected = False
client_id = None

# predefined data
user_name = str(os.getlogin())
server_address = ('127.0.0.1', 8775)
