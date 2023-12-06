import numpy as np
from PIL import Image

class Character_flower:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+30, position[1]+30))
        self.shape = Image.open("character_flower.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.life = 5
        self.attack = np.array([position[0], position[1] + 30, position[0] + 50, position[1] + 30])
        self.position = position
        self.center = np.array([position[0]+15, position[1]+15])