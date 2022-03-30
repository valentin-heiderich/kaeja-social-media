import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
engine.setProperty('voice', voices[1].id)


def say(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
