import numpy as np
from PIL import Image

class Bullet:
    def __init__(self, position, command):
        self.appearance = 'circle'
        self.speed = 10
        self.damage = 3
        self.position = np.array([position[0] -3, position[1] -3, position[0] +3, position[1] +3])
        self.direction = {'left' : False, 'right' : False}
        self.state = None
        self.outline = "#184600" #green
        
        if command['left']:
            self.direction['left'] = True
        if command['right']:
            self.direction['right'] = True
            
    def move(self):
        if self.direction['left']:
            self.position[0] -= self.speed
            self.position[2] -= self.speed
            
        if self.direction['right']:
            self.position[0] += self.speed
            self.position[2] += self.speed
            
    def collision_check(self, enemys):
        for enemy in enemys:
            collision = self.overlap(self.position, enemy.position)
            
            if collision:
                enemy.state = 'die'
                self.state = 'hit'
                
    def overlap(self, ego_position, other_position):
        return ego_position[0] > other_position[0] and ego_position[1] > other_position[1] \
            and ego_position[2] < other_position[2] and ego_position[3] < other_position[3]  
                
                
                
                