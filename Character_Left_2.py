import numpy as np
from PIL import Image

class Character_Left_2:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+30, position[1]+30))
        self.shape = Image.open("character_left_2.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.life = 5
        self.safe = np.array([position[0] , position[1] , position[0] + 30, position[1] + 30])
        self.level = 1
        self.position = position
        self.center = np.array([position[0]+35, position[1]+35])