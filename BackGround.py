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
                if(self.list[1]>-50):
                    for _ in range(0, 15):
                        self.list[1] -= 1
                        self.position = tuple(self.list)
                    for _ in range(0, 15):
                        self.list[1] += 1
                        self.position = tuple(self.list)
                else:
                    self.list[1] = self.list[1]

            if command['left']:
                if(self.list[0]>0):
                    self.list[0] -= 5
                    self.position = tuple(self.list)
                else:
                    self.list[0] = self.list[0]
                    self.position = tuple(self.list)
                
            if command['right']:
                if(self.list[0]<259):
                    self.list[0] += 5
                    self.position = tuple(self.list)
                else:
                    self.list[0] = self.list[0]
                    self.position = tuple(self.list)
        