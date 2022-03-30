import app.classes.post as post
import app.classes.feed as feed


def create_post(image, content, bvr):
    return post.post(image, content, bvr)


def feed_class(posts):
    return feed.feed(posts)