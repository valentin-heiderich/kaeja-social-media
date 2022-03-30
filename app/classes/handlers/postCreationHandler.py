import app.data.basicData as bD
from app.redirects.toClasses import create_post
import app.classes.server_client_conn.send as send
import app.classes.converters.images as imageConverter

import cv2


class postCreationHandler:
    def __init__(self, parent):
        self.parent = parent

        self.user = bD.user_name
        self.image_path = "data/test/img/Ag02.png"
        self.image = None
        self.content = ""

        self.post = None

        self.read()
        self.create_post()
        self.write()
        self.send()
        self.finish()

    def read(self):
        self.image_path = self.parent.children[1].ids.header_input.text  # gives the ability of a custom header
        self.content = self.parent.children[1].ids.content_input.text

    def create_post(self):
        # Image(source=self.image_path, size_hint=(1, None), size=(0, 300))
        self.image = imageConverter.image2array(cv2.imread(self.image_path))
        self.post = create_post(image=self.image, content=self.content, bvr=0)

    def write(self):
        bD.new_posts.append(self.post)

    def send(self):
        send.send(None, self.post)

    def finish(self):
        self.parent.children[1].ids.header_input.text = ""
        self.parent.children[1].ids.content_input.text = ""
