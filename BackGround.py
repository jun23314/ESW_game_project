import numpy as np
from PIL import Image

class BackGround:
    def __init__(self):
        self.shape = Image.open("background.png").convert('RGBA')
        self.position = (119, 259)
        
    def move(self, command = None):
        self.list = list(self.position)
        if command['move'] == True:
            if command['up']:
                self.list[1] += 20
            
            if command['left']:
                if(self.list[0]>0):
                    self.list[0] -= 5
                else:
                    self.list[0] = self.list[0]
                
            if command['right']:
                if(self.list[0]<259):
                    self.list[0] += 5
                else:
                    self.list[0] = self.list[0]
        self.position = tuple(self.list)
    
    def jump(self, flag = 0):
        self.list = list(self.position)
        if flag == 0:
                self.list[1] += 1
        elif flag == 15:
            self.list[1] -= 1