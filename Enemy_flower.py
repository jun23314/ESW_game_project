from PIL import Image
import numpy as np

class Enemy_flower:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+30, position[1]+30))
        self.shape = Image.open("flower.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([position[0]+10, position[1], position[0] + 20, position[1] + 30])
        self.state = 'live'
        self.touch = 0
        self.life = 1
        self.position = position

    def death(self, background):
        self.state = 'death'
        self.shape_ = background.crop((self.position[0], self.position[1], self.position[0]+30, self.position[1]+30))
