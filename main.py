from PIL import Image
import numpy as np
from colorsys import hsv_to_rgb
from Character_1 import Character_1
from Joystick import Joystick
from BackGround import BackGround

def main():
    joystick = Joystick()
    background = BackGround()
    makenew = BackGround()
    gameclearflag = 0
    life_count = 0
    start_ = Image.open('start.png')
    
    character_ = Character_1((background.position[0]+10, background.position[1]+130), background)
    my_image_ = background.shape.crop((background.position[0],background.position[1], background.position[0]+240, background.position[1]+240))
    my_image_.paste(character_.shape, (10, 130))
    
    joystick.disp.image(start_)

    while True:
        command = {'move': False, 'up': False , 'down': False, 'left': False, 'right': False}
        
        # 이동
        if not joystick.button_Five.value:
            command['up'] = True
            command['move'] = True

        if not joystick.button_Down.value:
            command['down'] = True
            command['move'] = True

        if not joystick.button_Left.value: 
            command['left'] = True
            command['move'] = True

        if not joystick.button_Right.value: 
            command['right'] = True
            command['move'] = True
            
        background.move(command)
        if command['move']==True:
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            character = Character_1((background.position[0]+10, background.position[1]+130), background)
            my_image_.paste(character.shape, (10, 130))
            joystick.disp.image(my_image_)

    joystick.disp.image(my_image_)
        
        

if __name__ == '__main__':
    main()
