import os.path

import data.basicData as bD
import classes.post as post
import classes.server_client_conn.send as send
import classes.converters.images as imageConverter

import cv2
import random


class postCreationHandler:
    def __init__(self, parent):
        self.parent = parent

        self.user = bD.user_name

        self.use_default_image = bD.USE_DEFAULT_IMAGE
        self.default_image_path = f"data/Design/d_images/d_image{random.randint(1, 20)}.png"
        self.image_path = ""
        self.image = None
        self.image_array = None

        self.content = ""

        self.valid_input = True
        self.not_valid_msg = "Please enter some content or choose an image"

        self.post_types = []

        self.post = None

        self.read()
        self.check_input()
        self.create_post()
        # self.write()
        self.send()
        self.finish()

    def read(self):
        print(self.parent.children)
        self.image_path = str(self.parent.ids.image_path.text).replace('"', '')
        self.content = self.parent.children[1].ids.post_content.text

    def check_input(self):
        if (self.content == "" and self.image_path == "") or self.content == self.not_valid_msg:
            self.valid_input = False
            self.parent.children[1].ids.post_content.text = self.not_valid_msg

    def create_post(self):
        if not self.valid_input: return  # if the input is not valid, do not create a post

        def get_image():
            self.image = cv2.imread(self.image_path)  # read the image
            self.post_types.append(bD.POST_TYPE_IMAGE)  # add the post type to the post types list
            self.image_array = imageConverter.image2array(self.image)  # convert the image to an array

        def get_default_image():
            self.image = cv2.imread(self.default_image_path)  # read the default image
            self.post_types.append(bD.POST_TYPE_IMAGE)  # add the post type to the post types list
            self.image_array = imageConverter.image2array(self.image)  # convert the image to an array

        def try_image():
            try:
                if os.path.isfile(self.image_path):
                    get_image()
                else:
                    if self.use_default_image:
                        get_default_image()
                    else:
                        self.image_array = None
            except:
                if self.use_default_image:
                    get_default_image()
                else:
                    self.image_array = None

        try_image()  # try to get the image

        if not self.content == "" or self.content == self.not_valid_msg:
            self.post_types.append(bD.POST_TYPE_TEXT)  # add the post type to the post types list

        if bD.BLUR_IMAGE:
            self.post_types.append(bD.POST_TYPE_SPOILER_NSFW)  # add the post type to the post types list

        self.post = post.post(image=self.image_array, content=self.content, bvr=0, post_type=self.post_types)  # creates the post

    def write(self):
        # bD.new_posts.append(self.post)
        pass

    def send(self):
        if not self.valid_input: return  # if the input is not valid, do not send a post
        try:
            send.send(None, self.post, bD.MESSAGE_TYPE_POST)  # sends the post to the server
        except:
            self.parent.children[1].ids.post_content.text = "Can't connect to the server"
            self.valid_input = False

    def finish(self):
        if not self.valid_input: return  # if the input is not valid, do not finish the post creation
        self.parent.ids.image_path.text = ""
        self.parent.children[1].ids.post_content.text = ""
        bD.createPostPopup.dismiss()
