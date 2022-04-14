from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.lang import Builder

import app.classes.converters.images as imageConverter
from app.GUI.Desing.py.Label import colored_label
import app.data.basicData as bD

import cv2

Builder.load_string(colored_label)


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

        content = ColoredLabel(text=str(post.content), size_hint=(1, None), background_color=bD.post_background_color)
        content.bind(texture_size=content.setter('size'))

        header = ColoredLabel(text=str(post.header), size_hint=(1, None), background_color=bD.post_background_color)
        header.bind(texture_size=header.setter('size'))

        sizer = ColoredLabel(text=" ", size_hint=(1, None), size=(0, 1), background_color=bD.sizer_color)

        widget.add_widget(header)
        widget.add_widget(Image(texture=self.texture, size_hint=(1, None), size=(0, 300)))
        widget.add_widget(content)
        widget.add_widget(sizer)
