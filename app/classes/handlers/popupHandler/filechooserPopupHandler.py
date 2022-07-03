from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import data.basicData as bD

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/FileChooserIconView.kv")


class FilechooserPopup(Popup):
    def load(self, path, file):
        bD.path_selection_field_ref.text = str(file).replace("\\", "/").replace("[", "").replace("]", "").replace("'", "")
        self.dismiss()


class filechooserPopupHandler:
    def __init__(self):
        self.popup = None
        self.open_filechooser_popup()

    def open_filechooser_popup(self):
        self.popup = FilechooserPopup()
        bD.filechooserPopup = self.popup
        self.popup.open()
