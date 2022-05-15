from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import data.basicData as bD

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/accountPopup.kv")


class AccountPopupContent(BoxLayout):
    pass


class accountPopup(Popup):
    pass


class accountPopupHandler:
    def __init__(self):
        self.popup = accountPopup()
        bD.accountPopup = self.popup
        self.popup.open()