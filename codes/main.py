from PIL import Image
import time
import numpy as np
from colorsys import hsv_to_rgb
from Character_1 import Character_1
from Joystick import Joystick
from BackGround import BackGround

def main():
    joystick = Joystick()
    background = BackGround()
    start = Image.open('~\ESW_game_project\images\start.png')
    
    character_ = Character_1((background.position[0]+90, background.position[1]+130), background)
    my_image_ = background.shape.crop((background.position[0],background.position[1], background.position[0]+240, background.position[1]+240))
    my_image_.paste(character_.shape, (90, 130))
    
    joystick.disp.image(start)

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
            
        
    joystick.disp.image(my_image_)
        
        

if __name__ == '__main__':
    main()
