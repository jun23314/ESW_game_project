import numpy as np
from PIL import Image

class Character_Box_Left_3:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+30, position[1]+30))
        self.shape = Image.open("character_box_left_3.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.safe = np.array([position[0] , position[1] , position[0] + 30, position[1] + 30])
        self.position = position