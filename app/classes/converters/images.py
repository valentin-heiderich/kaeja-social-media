import numpy as np
from PIL import Image


def image2array(image):
    """
    Convert image to array
    """
    return np.array(image)


def array2image(array):
    """
    Convert array to image
    """
    return Image.fromarray(array)
