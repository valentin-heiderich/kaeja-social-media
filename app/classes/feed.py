class feed:
    """create feed for the first time"""

    def __init__(self, posts):
        self.feed = posts

    def sort(self):
        pass

    def update(self, posts):
        self.feed = posts
