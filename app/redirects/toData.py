import app.data.basicData as bD


def store_feed(feed):
    bD.feed = feed


def new_post(post):
    bD.new_posts.append(post)


def new_post_widget(post):
    bD.post_widgets.append(post)
