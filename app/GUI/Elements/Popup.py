from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.core.window import Window

import pyautogui


class PopupWindow:
    def __init__(self, title, content, size, image):
        self.popup = None
        self.title = title
        self.content = content
        self.size_hint = (None, None)
        self.size = size
        self.auto_dismiss = True
        self.background = None
        self.background_color = None
        self.background_normal = None
        self.pos = pyautogui.position()
        self.Image = image
        self.image = None

        self.is_image()
        self.create_popup()
        self.open_popup()

    def is_image(self):
        if self.Image:
            self.create_image()

    def create_image(self):
        self.image = Image(texture=self.content, size_hint=(None, None), size=(self.size[0]-80, self.size[1]-80))

    def create_popup(self):
        self.popup = Popup(title=self.title, content=self.image, auto_dismiss=self.auto_dismiss, size_hint=self.size_hint, size=(self.size[0]-20, self.size[1]-20))

    def open_popup(self):
        self.popup.open()

    def close_popup(self):
        self.popup.dismiss()
