from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.label import Label

import app.classes.converters.images as imageConverter

import cv2


# noinspection PyArgumentList
class Post:
    """Add widgets to Grid Layout"""
    def __init__(self, widget, post):
        self.image_array = post.image
        self.image_array = cv2.cvtColor(self.image_array, cv2.COLOR_BGR2RGB)
        self.image_array = cv2.flip(self.image_array, 0)
        self.image = imageConverter.array2image(self.image_array)
        self.texture = Texture.create(size=(self.image.width, self.image.height))

        self.texture.blit_buffer(self.image.tobytes(), colorfmt='rgb', bufferfmt='ubyte')

        content = Label(text=str(post.content), size_hint=(1, None))
        content.bind(texture_size=content.setter('size'))

        widget.add_widget(Label(text=str(post.header), size_hint=(1, None), size=(0, 50)))
        widget.add_widget(Image(texture=self.texture, size_hint=(1, None), size=(0, 300)))
        widget.add_widget(content)
        widget.add_widget(Label(text="-----------------------------------------------------", size_hint=(1, None), size=(0, 50)))


class PostWidget(BoxLayout):
    """Create Box Layout Widget which contains the elements of Post"""
    def __init__(self, post, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text=str(post.header), size_hint=(1, None), size=(0, 50)))
        self.add_widget(Image(source="data/test/img/Ag02.png"))
        self.add_widget(Label(text=str(post.content), size_hint=(1, None), size=(0, 50)))
