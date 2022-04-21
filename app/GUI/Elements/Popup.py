from kivy.uix.popup import Popup
from kivy.uix.label import Label

import pyautogui


class PopupWindow:
    def __init__(self):
        self.popup = None
        self.title = "Add Server"
        self.content = Label(text='Hello world')
        self.size_hint = (None, None)
        self.size = (400, 400)
        self.auto_dismiss = True
        self.background = None
        self.background_color = None
        self.background_normal = None
        self.pos = pyautogui.position()

        self.create_popup()
        self.open_popup()

    def create_popup(self):
        self.popup = Popup(title=self.title, content=self.content, auto_dismiss=self.auto_dismiss, size_hint=self.size_hint, size=self.size)

    def open_popup(self):
        self.popup.open()

    def close_popup(self):
        self.popup.dismiss()
