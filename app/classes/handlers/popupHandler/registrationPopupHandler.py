from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

import data.basicData as bD
from classes.handlers.registrationHandler import registrationHandler

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/registrationPopup.kv")  # Load the KV file


class RegistrationPopupContent(BoxLayout):
    def register(self):
        username = self.ids["username"].text
        email = self.ids["email"].text
        password = self.ids["password"].text
        confirm_password = self.ids["confirm_password"].text

        # Check if the passwords match
        if password != confirm_password:
            error_popup = Popup(title="Error", content=GridLayout(cols=1, size_hint=(1, 1)), size_hint=(None, None), size=(400, 200))
            error_popup.content.add_widget(Label(text="Passwords do not match"))
            error_popup.open()
            return

        registrationHandler(username, email, password)


class RegistrationPopup(Popup):
    pass


class registrationPopupHandler:
    def __init__(self):
        self.popup = RegistrationPopup()
        bD.registrationPopup = self.popup
        self.popup.open()
