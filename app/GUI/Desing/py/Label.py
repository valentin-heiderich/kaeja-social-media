colored_label = '''
<ColoredLabel>:
    size: self.texture_size
    pos: (0,0)
    background_color: (0.2,0.2,0.2, 1)
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size
    '''