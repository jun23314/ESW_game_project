import numpy as np
from PIL import Image

class Bullet:
    def __init__(self,background, character):
        background = background.crop((81, 152, 86, 157))
        self.shape = Image.open('bullet.png').convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([81, 152, 86, 157])
        self.touch = 3
        self.position = character.position
        self.shot = False

    def collision_check_long(self, enemys):
        for enemy in enemys:
            collision = self.overlap(self.attack, enemy.attack)

            if collision:
                if enemy.state == 'live':
                    self.shot = True
                    enemy.life -= self.touch
                    print("hurt..1")
                    break

    def overlap(self, ego_position, other_position):
        return (ego_position[2] >= other_position[0] >= ego_position[0] or ego_position[2]>=other_position[2] >= ego_position[0]) and (ego_position[1] <= other_position[1] <= ego_position[3] or ego_position[1] <= other_position[3] <= ego_position[3])
                
                
                
                