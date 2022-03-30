import app.redirects.toClasses as toClasses
import app.redirects.toGUI as toGUI
import app.redirects.toData as toData
import app.classes.server_client_conn.updateFeed as uF
from app.classes.tts.handleTts import TtSHandler
import time
import threading
import app.classes.logging.log as log
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

"""create test posts"""


def test():
    for i in range(0, 100):
        log.log(os.path.basename(__file__), log.pc, f"Creating post class for post: {str(i)} {time.asctime()}")
        post = toClasses.create_post(image='data/test/img/Ag02.png', content="testi", bvr=0)
        posts.append(post)
        toData.new_post(post)


"""start .py scripts"""
s_conn.start()
TtS.start()
GUI.run()
