import os
import pickle

# posts
current_rendered_posts = pickle.dumps([])
recv_posts = pickle.dumps([])

# server data
server_address = ('127.0.0.1', 8775)
socket = None
address = None
connected = False
client_id = None  # session id

# Popups
createPostPopup = None
settingsPopup = None
filechooserPopup = None

# Popup Elements
path_selection_field_ref = None

# post types
USE_DEFAULT_IMAGE = False
BLUR_IMAGE = False
POST_TYPE_IMAGE = 'image'
POST_TYPE_TEXT = 'text'
POST_TYPE_VIDEO = 'video'
POST_TYPE_AUDIO = 'audio'
POST_TYPE_FILE = 'file'
POST_TYPE_LINK = 'link'
POST_TYPE_SPOILER_NSFW = 'spoiler_nsfw'

# server,client communication msg types
MESSAGE_TYPE_UPDATE_FEED = '00001'
MESSAGE_TYPE_POST = '00010'
MESSAGE_TYPE_CRYPTOGRAPHY = '00011'
MESSAGE_TYPE_ACCOUNT_CREATION = '00100'
MESSAGE_TYPE_ACCOUNT_LOGIN = '00101'

# account data
logged_in = False
user_name = str(os.getlogin())
user_id = None

# SAFETY
pr_key = None
pub_key = None

# Design data
sizer_color = (1, 0.8, 0.2, 0.7)
post_background_color = (0.2, 0.2, 0.2, 0.5)
background_image = 5
BLUR_AMOUNT = 0.5
