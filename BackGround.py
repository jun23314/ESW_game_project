import numpy as np
from PIL import Image

class BackGround:
    def __init__(self):
        self.shape = Image.open("background.png").convert('RGBA')
        self.position = (0, 355)
        
    def move(self, command = None):
        self.list = list(self.position)
        if command['move'] == True:
            if command['left']:
                if(self.list[0]>0):
                    self.list[0] -= 5
                else:
                    self.list[0] = self.list[0]
                
            if command['right']:
                if(self.list[0]<359):
                    self.list[0] += 5
                else:
                    self.list[0] = self.list[0]
        self.position = tuple(self.list)
    
    def jump(self):
        self.list = list(self.position)
        self.list[1] -= 1
        self.position = tuple(self.list)
        
    def jump_down(self):
        self.list = list(self.position)
        self.list[1] += 1
        self.position = tuple(self.list)