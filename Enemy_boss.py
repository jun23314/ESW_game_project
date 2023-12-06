from PIL import Image
import numpy as np

class Enemy_boss:
    def __init__(self, position, background):
        background = background.crop((position[0], position[1], position[0]+150, position[1]+150))
        self.shape = Image.open("enemy_boss.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([position[0]+10, position[1], position[0] + 120, position[1] + 150])
        self.touch = 5
        self.state = 'live'
        self.life = 15
        self.position = position

    def death(self, background):
        self.state = 'death'
        self.shape_ = background.crop((self.position[0], self.position[1], self.position[0]+150, self.position[1] + 150))
