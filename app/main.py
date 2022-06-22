import redirects.toClasses as toClasses
from GUI.KaejaGUI import main as KaejaGUI
import classes.server_client_conn.ServerClientSetup as uF
from classes.tts.handleTts import TtSHandler
import classes.logging.log as log

import threading
import os


class app:
    def __init__(self):
        """log"""
        log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")
        self.gui = None
        self.s_conn = None
        self.TtS = None

        self.posts = []
        self.feed = []

        self.declare_py_scripts()
        self.initialize_feed()
        self.start_py_scripts()

    def declare_py_scripts(self):
        """declare .py scripts"""
        self.gui = KaejaGUI
        self.s_conn = threading.Thread(target=uF.updateFeed)
        self.TtS = threading.Thread(target=TtSHandler)

    def initialize_feed(self):
        """feed"""
        self.feed = toClasses.feed_class(self.posts)

    def start_py_scripts(self):
        """start .py scripts"""
        self.s_conn.start()
        self.TtS.start()
        self.gui()


if __name__ == "__main__":
    app = app()
