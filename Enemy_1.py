from PIL import Image
import numpy as np

class Enemy_1:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+70, position[1]+70))
        self.shape = Image.open("plant.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([position[0]+20, position[1]+20, position[0] + 50, position[1] + 50])
        self.touch = 1
        self.state = 'live'
        self.life = 15
        self.position = position

    def death(self, background):
        self.state = 'death'
        self.shape_ = background.crop((self.position[0], self.position[1], self.position[0]+24, self.position[1]+24))
