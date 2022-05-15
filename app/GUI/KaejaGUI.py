from functools import partial
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


from GUI.updateFeed import update_feed
import classes.logging.log as log
from classes.handlers.postCreationPopupHandler import CreatePostPopupHandler as CPPH
from classes.handlers.settingsPopupHandler import SettingsPopupHandler as SPH
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
        pass

    def show_post_creation(self):
        """Shows the post creation window"""
        log.log(os.path.basename(__file__), log.ui, f"{self}.post_creation")
        CPPH()


class Posts(GridLayout):
    """Here the Feed widget will be Displayed, created and updated"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update()

    def update(self):
        """Updates the feed"""
        update_feed(self)
        event = Clock.schedule_interval(partial(update_feed, self), 3)


class KaejaApp(App):
    """This is the main GUI application"""
    def __init__(self):
        super().__init__()
        log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")
        self.title = 'Kaeja'
        self.icon = 'data/Design/d_images/d_image7.png'
    background = StringProperty(f'data/Design/Backgrounds/0{bD.background_image}.png')
    name = StringProperty(bD.user_name)


def main():
    global app_instance
    app_instance = KaejaApp()
    app_instance.run()
