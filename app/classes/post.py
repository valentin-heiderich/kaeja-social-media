import time
import uuid
import app.data.basicData as bD


class post:
    def __init__(self, image, content, bvr):
        self.header = bD.user_name
        self.image = image
        self.content = content
        self.created = time.time()
        self.id = uuid.uuid4()
        self.bvr = bvr
