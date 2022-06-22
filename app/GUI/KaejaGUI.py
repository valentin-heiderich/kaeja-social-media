from functools import partial
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window, Animation

from GUI.updateFeed import update_feed
import classes.logging.log as log
from classes.handlers.popupHandler.postCreationPopupHandler import CreatePostPopupHandler as CPPH
from classes.handlers.popupHandler.settingsPopupHandler import SettingsPopupHandler as SPH
from classes.handlers.popupHandler.accountPopupHandler import accountPopupHandler as APH
from classes.handlers.popupHandler.registerOrLoginPopupHandler import loginOrRegisterPopupHandler as LORPH
import data.basicData as bD

import threading
import os

app_instance = None

Window.size = (1280, 720)
Window.minimum_width, Window.minimum_height = Window.size
Window.pos = (0, 0)
Window.maximize()


class TopMenuBar(BoxLayout):
    """Here the actions of the top menu bar are defined"""

    name = StringProperty(bD.user_name)

    def show_settings(self):
        """Shows the settings window"""
        log.log(os.path.basename(__file__), log.ui, f"{self}.settings")
        global app_instance
        SPH(app_instance)

    def show_account(self):
        """Shows the account window"""
        log.log(os.path.basename(__file__), log.ui, f"{self}.account management")
        if not bD.logged_in: LORPH()

    def show_post_creation(self):
        """Shows the post creation window"""
        log.log(os.path.basename(__file__), log.ui, f"{self}.post_creation")
        CPPH()


class Feed(BoxLayout):
    def refresh(self):
        log.log(os.path.basename(__file__), log.ui, f"Refreshed UI manually")
        update_feed(self.children[0].children[0])


class Posts(GridLayout):
    """Here the Feed widget will be Displayed, created and updated"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update()

    def update(self):
        """Updates the feed"""
        update_feed(self)
        event = Clock.schedule_interval(partial(update_feed, self), 30)


class KaejaApp(App):
    """This is the main GUI application"""
    def __init__(self):
        super().__init__()
        log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")
        self.title = 'Kaeja'
        self.icon = 'data/Design/d_images/d_image7.png'
    """Declare variables"""
    background = StringProperty(f'data/Design/Backgrounds/0{bD.background_image}.png')
    background_image_id = StringProperty(f'{bD.background_image}')
    name = StringProperty(bD.user_name)
    blur_amount = bD.BLUR_AMOUNT


def main():
    global app_instance
    app_instance = KaejaApp()
    app_instance.run()
