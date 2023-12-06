import numpy as np
from PIL import Image

class Bullet_2:
    def __init__(self,background, character):
        background = background.crop((66, 170, 71, 175))
        self.shape = Image.open('bullet.png').convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array(63, 170, 69, 175)
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
                    print("hurt..2")
                    break

    def overlap(self, ego_position, other_position):
        return (ego_position[2] >= other_position[0] >= ego_position[0] or ego_position[2]>=other_position[2] >= ego_position[0]) and (ego_position[1] <= other_position[1] <= ego_position[3] or ego_position[1] <= other_position[3] <= ego_position[3])
                
                
                
                