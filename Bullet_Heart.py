import numpy as np
from PIL import Image

class Bullet_Heart:
    def __init__(self,background, character):
        background = background.crop((105, 182, 114, 187))
        self.shape = Image.open('heart.png').convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.attack = np.array([character.center[0] , character.center[1] - 2.5 , character.center[0] + 20, character.center[1] + 2.5])
        self.touch = 3
        self.shot = False

    def collision_check_long(self, enemys):
        for enemy in enemys:
            collision = self.overlap(enemy.attack, self.attack)
            print(self.attack)
            print(enemy.attack)

            if collision:
                if enemy.state == 'live':
                    self.shot = True
                    enemy.life -= self.touch
                    print("hurt..5")
                    break

    def overlap(self, ego_position, other_position):
        return (ego_position[2] >= other_position[0] >= ego_position[0] or ego_position[2]>=other_position[2] >= ego_position[0]) 
    
    def death(self, background):
        self.state = 'death'
        self.shape_ = background.crop((90, 182, 98, 187))
                
                
                
                