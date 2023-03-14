import data.basicData as bD
from GUI.Elements.Post import Post
import classes.logging.log as log
import os
import pickle
import copy

def add_new_posts():
    recv_posts = pickle.loads(bD.recv_posts)
    cur_rend_posts =  pickle.loads(bD.current_rendered_posts)
    new_content_c = 0
    new_content = []
    for p in recv_posts:
        sid = p.id
        ids = [c.id for c in cur_rend_posts]
        if not sid in ids:
            print(cur_rend_posts, p)
            cur_rend_posts.insert(0, p)
            new_content.insert(0, p)
            new_content_c += 1
    bD.current_rendered_posts = pickle.dumps(cur_rend_posts)
    return [new_content_c, cur_rend_posts, new_content]

def update_feed(widget, *args):
    x = add_new_posts()
    if x[0]<=0:return
    log.log(os.path.basename(__file__), log.ui, f"Refreshing UI...")
    widget.clear_widgets()
    feed = x[1][:100]
    for i in range(len(feed)):
        post = feed[-1]
        post_widget = Post(widget, post)
        feed.remove(post)
