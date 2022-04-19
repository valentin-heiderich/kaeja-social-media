from functools import partial
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from app.GUI.updateFeed import update_feed
import app.classes.logging.log as log
from app.classes.handlers.postCreationHandler import postCreationHandler

import threading
import os

Window.size = (1280, 720)
Window.minimum_width, Window.minimum_height = Window.size
Window.pos = (0, 0)
Window.maximize()


class CreatePostWindow(BoxLayout):
    def share(self):
        """Share post"""
        handler = postCreationHandler(self)

    def add_server(self):
        """Add server"""
        pass


class KaejaServers(BoxLayout):

    def add_server(self):
        print("add server button pressed")


class Posts(GridLayout):
    """Here the Feed widget will be Displayed, created and updated"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update()

    def update(self):
        update_feed(self)
        event = Clock.schedule_interval(partial(update_feed, self), 3)


class KaejaApp(App):
    """This is the main GUI application"""
    log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")
