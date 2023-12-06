import numpy as np
from PIL import Image

class Character_down:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+30, position[1]+30))
        self.shape = Image.open("character_down.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.life = 5
        self.safe = np.array([position[0] , position[1] , position[0] + 30, position[1] + 30])
        self.attack = np.array([position[0], position[1] + 30, position[0] + 50, position[1] + 30])
        self.state = None
        self.direction = 'right'
        self.position = position
        self.center = np.array([position[0]+15, position[1]+15])

    def collision_check(self, character, enemys, character_):
        for enemy in enemys[::-1]:
            
            collision = self.overlap(character.safe, enemy.attack)

            if collision:
                if enemy.state == 'live':
                    character_.life -= enemy.touch
                    break

    def overlap(self, enemys_position, my_position):
        return (my_position[2] >enemys_position[0] > my_position[0] or my_position[2] >= enemys_position[2] >= my_position[0]) and (my_position[1] <= enemys_position[1] <= my_position[3] or my_position[1] <= enemys_position[3] <= my_position[3])