import os

feed = []
new_posts = []
recv_posts = []
post_widgets = []

socket = None
address = None
connected = False

user_name = str(os.getlogin())
