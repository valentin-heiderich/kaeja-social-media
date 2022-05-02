from functools import partial
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from app.GUI.updateFeed import update_feed
import app.classes.logging.log as log
from app.classes.handlers.postCreationPopupHandler import CreatePostPopupHandler as CPPH

import threading
import os

Window.size = (1280, 720)
Window.minimum_width, Window.minimum_height = Window.size
Window.pos = (0, 0)
Window.maximize()


class TopMenuBar(BoxLayout):
    """Here the actions of the top menu bar are defined"""
    def show_settings(self):
        """Shows the settings window"""
        pass

    def show_post_creation(self):
        """Shows the post creation window"""
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
    log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")
