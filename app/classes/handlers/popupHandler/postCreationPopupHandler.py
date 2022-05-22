from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import data.basicData as bD
from classes.handlers.postCreationHandler import postCreationHandler

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/postPopup.kv")


class AdvancedOptionsPostPopup(GridLayout):
    def default_image(self, instance, value):
        bD.USE_DEFAULT_IMAGE = value

    def blur(self, instance, value):
        bD.BLUR_IMAGE = value


class CreatePostPopupContent(BoxLayout):
    def share_post(self):
        postCreationHandler(self)


class CreatePostPopup(Popup):
    pass


class CreatePostPopupHandler:
    def __init__(self):
        self.popup = CreatePostPopup()
        bD.createPostPopup = self.popup
        self.popup.open()
