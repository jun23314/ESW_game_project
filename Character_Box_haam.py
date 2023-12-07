import numpy as np
from PIL import Image

class Character_Box_haam:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+30, position[1]+30))
        self.shape = Image.open("character_box_haam.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.life = 5
        self.attack = np.array([position[0], position[1] + 30, position[0] + 70, position[1] + 30])
        self.position = position
        self.center = np.array([position[0]+15, position[1]+15])
        

    def collision_check(self, character, enemy):
        collision = self.overlap(character.attack, enemy.attack)
        if collision:
            if enemy.state == 'live':
                enemy.state = 'dead'
                    
    def overlap(self, ego_position, other_position):
        
        return (ego_position[2] >= other_position[0] >= ego_position[0] or ego_position[2]>=other_position[2] >= ego_position[0])