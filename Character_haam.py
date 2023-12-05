import numpy as np
from PIL import Image

class Character_haam:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+30, position[1]+30))
        self.shape = Image.open("character_haam.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.life = 5
        self.attack = np.array([position[0] + 30, position[1] + 30, position[0] + 70, position[1] + 70])
        self.position = position
        self.center = np.array([position[0]+15, position[1]+15])
        

    def collision_check(self, character, enemys):
        for enemy in enemys:
            collision = self.overlap(character.attack, enemy.attack)
            if collision:
                if enemy.state == 'live':
                    enemy.state == 'dead'
                    character.state = 'eat'

    def overlap(self, enemys_position, my_position):
        return my_position[2] >= enemys_position[0] >= my_position[0] and my_position[2] >= enemys_position[2] >= my_position[0]