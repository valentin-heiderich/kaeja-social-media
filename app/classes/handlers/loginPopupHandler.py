from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import data.basicData as bD

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/loginPopup.kv")


class LoginPopupContent(BoxLayout):
    pass


class LoginPopup(Popup):
    pass


class loginPopupHandler:
    def __init__(self):
        self.popup = LoginPopup()
        bD.loginPopup = self.popup
        self.popup.open()
