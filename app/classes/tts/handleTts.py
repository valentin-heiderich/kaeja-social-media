import os
import threading
import app.classes.logging.log as log
import app.classes.tts.female01 as female_voice


class TtSHandler:
    def __init__(self):
        log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")
        self.voice = female_voice
        self.welcome()

    def welcome(self):
        self.say("Welcome in Kaeja")

    def say(self, text):
        self.voice.say(text)
