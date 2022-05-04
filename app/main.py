import redirects.toClasses as toClasses
import redirects.toGUI as toGUI
import classes.server_client_conn.ServerClientSetup as uF
from classes.tts.handleTts import TtSHandler
import threading
import classes.logging.log as log
import os

"""log"""
log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")

"""declare .py scripts"""
GUI = toGUI.create_gui()
s_conn = threading.Thread(target=uF.updateFeed)
TtS = threading.Thread(target=TtSHandler)

"""feed"""
posts = []
feed = toClasses.feed_class(posts)

"""start .py scripts"""
s_conn.start()
TtS.start()
GUI.run()
