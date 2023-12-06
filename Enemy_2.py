from PIL import Image
import numpy as np

class Enemy_2:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+70, position[1]+70))
        self.shape = Image.open("tree.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([position[0]+10, position[1], position[0] + 60, position[1] + 70])
        self.touch = 5
        self.state = 'live'
        self.life = 12
        self.position = position

    def death(self, background):
        self.state = 'death'
        self.shape_ = background.crop((self.position[0], self.position[1], self.position[0]+70, self.position[1] + 70))
