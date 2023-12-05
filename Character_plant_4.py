from PIL import Image

class Character_plant_4:
    def __init__(self, position, background):
        background = background.shape.crop((position[0], position[1], position[0]+30, position[1]+30))
        self.shape = Image.open("character_plant_4.png").convert('RGBA')
        self.shape = Image.alpha_composite(background, self.shape)
        self.position = position