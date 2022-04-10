import app.data.basicData as bD
from app.GUI.Elements.Post import Post
import app.classes.logging.log as log
import os
import pickle


def update_feed(widget, *args):
    log.log(os.path.basename(__file__), log.ui, f"Updating Feed Widget")
    widget.clear_widgets()
    new_posts = bD.recv_posts
    feed = pickle.loads(new_posts)
    if len(feed) > 100:
        while len(feed) > 100:
            popped_post = feed.pop(0)
    for i in range(len(feed)):
        post = feed[-1]
        post_widget = Post(widget, post)
        feed.remove(post)
    log.log(os.path.basename(__file__), log.ui, f"Finished updating Feed Widget")
