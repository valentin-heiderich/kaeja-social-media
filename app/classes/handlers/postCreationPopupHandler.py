from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

import app.data.basicData as bD
from app.classes.handlers.postCreationHandler import postCreationHandler

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/postPopup.kv")


class CreatePostPopupContent(BoxLayout):
    def share_post(self):
        postCreationHandler(self)
        bD.createPostPopup.dismiss()


class CreatePostPopup(Popup):
    pass


class CreatePostPopupHandler:
    def __init__(self):
        self.popup = CreatePostPopup()
        bD.createPostPopup = self.popup
        self.popup.open()
