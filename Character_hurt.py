import numpy as np
from PIL import Image

class Character_hurt:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+30, position[1]+30))
        self.shape = Image.open("character_hurt.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.life = 5
        self.position = position