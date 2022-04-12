import os.path

import app.data.basicData as bD
from app.redirects.toClasses import create_post
import app.classes.server_client_conn.send as send
import app.classes.converters.images as imageConverter

import cv2


class postCreationHandler:
    def __init__(self, parent):
        self.parent = parent

        self.user = bD.user_name
        self.default_image_path = "data/test/img/Ag02.png"
        self.image_path = "data/test/img/Ag02.png"
        self.image = None
        self.image_array = None
        self.content = ""
        self.valid_input = True

        self.post = None

        self.read()
        self.check_input()
        self.create_post()
        # self.write()
        self.send()
        self.finish()

    def read(self):
        self.image_path = self.parent.children[1].ids.header_input.text  # gives the ability of a custom header
        self.content = self.parent.children[1].ids.content_input.text

    def check_input(self):
        if self.image_path == "":
            pass
        if self.content == "" or self.content == "Please enter some content":
            self.valid_input = False
            self.parent.children[1].ids.content_input.text = "Please enter some content"

    def create_post(self):
        if not self.valid_input: return  # if the input is not valid, do not create a post
        # Image(source=self.image_path, size_hint=(1, None), size=(0, 300))
        try:
            if os.path.isfile(self.image_path): self.image = cv2.imread(self.image_path)  # read image
            else: self.image = cv2.imread(self.default_image_path)  # default image
        except:
            self.image = cv2.imread(self.default_image_path)  # default image

        self.image_array = imageConverter.image2array(self.image)  # converts the image to a numpy array

        self.post = create_post(image=self.image_array, content=self.content, bvr=0)  # creates the post

    def write(self):
        # bD.new_posts.append(self.post)
        pass

    def send(self):
        if not self.valid_input: return  # if the input is not valid, do not send a post
        send.send(None, self.post)  # sends the post to the server

    def finish(self):
        if not self.valid_input: return  # if the input is not valid, do not finish the post creation
        self.parent.children[1].ids.header_input.text = ""
        self.parent.children[1].ids.content_input.text = ""
