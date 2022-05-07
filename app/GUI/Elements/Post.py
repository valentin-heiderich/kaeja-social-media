from kivy.uix.image import Image as KvImage
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window

import classes.converters.images as imageConverter
from GUI.Design.py.Label import colored_label
from GUI.Elements.Popup import PopupWindow
import data.basicData as bD

import cv2

Builder.load_string(colored_label)


class ColoredLabel(Label):
    pass


class Image(KvImage):
    def __init__(self, normal_texture, **kwargs):
        super(Image, self).__init__(**kwargs)
        self.normal_texture = normal_texture

    def maximize(self):
        PopupWindow("Image", self.normal_texture, Window.size, image=True)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.maximize()


class Post:
    """Add widgets to Grid Layout"""
    def __init__(self, widget, post):
        """Create a post with the given data"""

        '''header'''
        header = ColoredLabel(text=str(post.header), size_hint=(0.5, None), background_color=(0.1, 0.1, 0.1, 0.7))
        header.bind(texture_size=header.setter('size'))
        widget.add_widget(header)

        '''image'''
        if bD.POST_TYPE_IMAGE in post.post_type:
            self.image_array = post.image
            self.image_array = cv2.cvtColor(self.image_array, cv2.COLOR_BGR2RGB)
            self.image_array = cv2.flip(self.image_array, 0)
            self.image_array_duplicate = self.image_array.copy()

            if bD.POST_TYPE_SPOILER_NSFW in post.post_type:
                self.image_array_preview = cv2.blur(self.image_array_duplicate, (50, 50))
            else: self.image_array_preview = self.image_array

            self.image = imageConverter.array2image(self.image_array)
            self.image_preview = imageConverter.array2image(self.image_array_preview)

            self.texture = Texture.create(size=(self.image.width, self.image.height))
            self.texture_preview = Texture.create(size=(self.image_preview.width, self.image_preview.height))

            self.texture.blit_buffer(self.image.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
            self.texture_preview.blit_buffer(self.image_preview.tobytes(), colorfmt='rgb', bufferfmt='ubyte')

            widget.add_widget(Image(texture=self.texture_preview, size_hint=(1, None), size=(0, 300), normal_texture=self.texture))

        '''text'''
        if bD.POST_TYPE_TEXT in post.post_type:
            text = ColoredLabel(text=str(post.content), size_hint=(0.5, None),  background_color=bD.post_background_color)
            text.bind(texture_size=text.setter('size'))
            widget.add_widget(text)

        # '''sizer'''
        # sizer = ColoredLabel(text=" ", size_hint=(1, None), size=(0, 1), background_color=bD.sizer_color)
        # widget.add_widget(sizer)
