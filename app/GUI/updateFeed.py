import app.data.basicData as bD
from app.GUI.Elements.Post import Post
import app.classes.logging.log as log
import os


def update_feed(widget, *args):
    log.log(os.path.basename(__file__), log.ui, f"Updating Feed Widget")
    widget.clear_widgets()
    bD.new_posts = bD.recv_posts
    for post in bD.new_posts:
        bD.feed.append(post)
    if len(bD.feed) > 100:
        while len(bD.feed) > 100:
            popped_post = bD.feed.pop(0)
    for post in bD.feed:
        feed_len = len(bD.feed)-1
        post_pos = feed_len - bD.feed.index(post)
        post = bD.feed[post_pos]
        post_widget = Post(widget, post)
        bD.post_widgets.append(post_widget)
    bD.new_posts = []
    bD.feed = []
    log.log(os.path.basename(__file__), log.ui, f"Finished updating Feed Widget")
