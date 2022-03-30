from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class inputField:
    def __init__(self, widget, text):
        widget.add_widget(Label(text=text))
        widget.cmd = TextInput(multiline=False)
        widget.add_widget(widget.cmd)
