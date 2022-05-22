from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import data.basicData as bD
from classes.handlers.registrationHandler import registrationHandler

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/registrationPopup.kv")  # Load the KV file


class RegistrationPopupContent(BoxLayout):
    def register(self):
        registrationHandler()


class RegistrationPopup(Popup):
    pass


class registrationPopupHandler:
    def __init__(self):
        self.popup = RegistrationPopup()
        bD.registrationPopup = self.popup
        self.popup.open()
