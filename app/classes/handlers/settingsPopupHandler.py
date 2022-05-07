from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import data.basicData as bD

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/settings.kv")


class SettingsSelectionSection01(BoxLayout):
    pass


class SettingsPopupContent(BoxLayout):
    pass


class SettingsPopup(Popup):
    pass


class SettingsPopupHandler:
    def __init__(self):
        self.popup = SettingsPopup()
        bD.settingsPopup = self.popup
        self.popup.open()
