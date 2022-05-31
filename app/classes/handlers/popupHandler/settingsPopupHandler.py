from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import data.basicData as bD

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/settings.kv")

app_inst = None


class SettingsSelectionSection01(GridLayout):
    pass


class SettingsPopupContent(BoxLayout):
    def apply_settings(self):
        """Applies the settings to the application."""
        global app_inst
        """getting the values from the settings"""
        bD.background_image = self.children[1].ids.background.text
        print(self.children[1].ids)
        bD.BLUR_AMOUNT = round(self.children[1].ids.blur_amount.value, 2)
        """Updating the application"""
        app_inst.background = f'data/Design/Backgrounds/0{bD.background_image}.png'
        app_inst.background_image_id = f'{bD.background_image}'
        app_inst.blur_amount = bD.BLUR_AMOUNT
        """Closing the popup"""
        bD.settingsPopup.dismiss()


class SettingsPopup(Popup):
    pass


class SettingsPopupHandler:
    def __init__(self, app_instance):
        global app_inst

        app_inst = app_instance

        self.popup = None

        self.open_settings_popup()

    def open_settings_popup(self):
        self.popup = SettingsPopup()
        bD.settingsPopup = self.popup
        self.popup.open()
