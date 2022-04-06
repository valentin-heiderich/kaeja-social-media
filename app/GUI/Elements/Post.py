from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.lang import Builder

import app.classes.converters.images as imageConverter

import cv2

kv = '''
<ColoredLabel>:
    size: (1,1)
    pos: (0,0)
    background_color: (0.2,0.2,0.2, 1)
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size
    '''

Builder.load_string(kv)


class ColoredLabel(Label):
    pass


class Post:
    """Add widgets to Grid Layout"""
    def __init__(self, widget, post):
        self.image_array = post.image
        self.image_array = cv2.cvtColor(self.image_array, cv2.COLOR_BGR2RGB)
        self.image_array = cv2.flip(self.image_array, 0)
        self.image = imageConverter.array2image(self.image_array)

        self.texture = Texture.create(size=(self.image.width, self.image.height))
        self.texture.blit_buffer(self.image.tobytes(), colorfmt='rgb', bufferfmt='ubyte')

        content = ColoredLabel(text=str(post.content), size_hint=(1, None))
        content.bind(texture_size=content.setter('size'))

        header = ColoredLabel(text=str(post.header), size_hint=(1, None))
        header.bind(texture_size=content.setter('size'))

        widget.add_widget(header)
        widget.add_widget(Image(texture=self.texture, size_hint=(1, None), size=(0, 400)))
        widget.add_widget(content)
