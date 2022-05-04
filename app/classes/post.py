import time
import uuid
import data.basicData as bD


class post:
    def __init__(self, image, content, bvr, post_type):
        self.header = bD.user_name
        self.image = image
        self.content = content
        self.created = time.time()
        self.id = uuid.uuid4()
        self.bvr = bvr
        self.post_type = post_type
        self.likes = 0
        self.comments = []
