from PIL import Image

class Tree_Disappear_1:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+70, position[1]+70))
        self.shape = Image.open("tree_disappear_1.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.position = position