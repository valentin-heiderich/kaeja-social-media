from kivy.uix.button import Button


class Server(Button):
    def __init__(self, **kwargs):
        super(Server, self).__init__(**kwargs)
        self.text = kwargs.get('text')
        self.bind(on_press=self.connect)
        self.background_color = [0.2, 0.2, 0.2, 0.8]
        self.size_hint = (1, None)
        self.height = self.texture_size[1] + 100

    def connect(self, *args):
        pass


class ServerWidget:
    def __init__(self, window, server):
        self.window = window
        self.server = server
        self.widget = None

        self.build()

    def build(self):
        print("Building Server Widget")
        self.widget = Server(text=self.server.name)
        #  self.widget.bind(texture_size=self.widget.setter('size'))
        self.window.add_widget(self.widget)
