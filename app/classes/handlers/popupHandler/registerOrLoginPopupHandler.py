from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import data.basicData as bD

from classes.handlers.popupHandler.registrationPopupHandler import registrationPopupHandler as rPH
from classes.handlers.popupHandler.loginPopupHandler import loginPopupHandler as lPH

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/registerORlogin.kv")


class LoginOrRegisterPopupContent(BoxLayout):
    def login(self):
        lPH()

    def register(self):
        rPH()


class LoginOrRegisterPopup(Popup):
    pass


class loginOrRegisterPopupHandler:
    def __init__(self):
        self.popup = LoginOrRegisterPopup()
        bD.registerOrLoginPopup = self.popup
        self.popup.open()
