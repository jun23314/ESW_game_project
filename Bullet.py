import numpy as np
from PIL import Image

class Bullet:
    def __init__(self, background, character, position):
        background = background.shape.crop((position[0], position[1], position[0]+5, position[1]+5))
        self.shape = Image.open("bullet.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([character.center[0] , character.center[1] , character.center[0] + 5, character.center[1] + 5])
        self.damage = 3
        self.position = character.position
        
        
    def move(self):
        self.position[0] += 5

    def overlap(self, ego_position, other_position):
        return (ego_position[2] >= other_position[0] >= ego_position[0] or ego_position[2]>=other_position[2] >= ego_position[0]) and (ego_position[1] <= other_position[1] <= ego_position[3] or ego_position[1] <= other_position[3] <= ego_position[3])
            
    def collision_check(self, enemys):
        for enemy in enemys:
            collision = self.overlap(self.position, enemy.position)
            
            if collision:
                enemy.life -= self.damage
                if enemy.life <= 0:
                    enemy.state = 'dead'
                
                
                
                