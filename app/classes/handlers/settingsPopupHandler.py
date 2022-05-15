from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import data.basicData as bD

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/settings.kv")

app_inst = None


class SettingsSelectionSection01(BoxLayout):
    pass


class SettingsPopupContent(BoxLayout):
    def apply_settings(self):
        global app_inst
        bD.background_image = self.children[1].ids.background.text
        app_inst.background = f'data/Design/Backgrounds/0{bD.background_image}.png'


class SettingsPopup(Popup):
    pass


class SettingsPopupHandler:
    def __init__(self, app_instance):
        global app_inst
        app_inst = app_instance
        self.popup = SettingsPopup()
        bD.settingsPopup = self.popup
        self.popup.open()
