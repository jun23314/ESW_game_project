from PIL import Image
import numpy as np
from colorsys import hsv_to_rgb
from Character_1 import Character_1
from Character_2 import Character_2
from Character_3 import Character_3
from Character_4 import Character_4
from Character_Left_1 import Character_Left_1
from Character_Left_2 import Character_Left_2
from Character_Left_3 import Character_Left_3
from Character_Left_4 import Character_Left_4
from Enemy_1 import Enemy_1
from Enemy_2 import Enemy_2
from Bullet import Bullet
from Joystick import Joystick
from BackGround import BackGround

def main():
    joystick = Joystick()
    background = BackGround()
    makenew = BackGround()
    start_ = Image.open('start.png')
    
    
    plant = Enemy_1((100, 543), background.shape)
    background.shape.paste(plant.shape, plant.position)
    tree = Enemy_2((170, 543), background.shape)
    background.shape.paste(tree.shape, tree.position)
    
    character_ = Character_1((background.position[0]+50, background.position[1]+187), background)
    my_image_ = background.shape.crop((background.position[0],background.position[1], background.position[0]+240, background.position[1]+240))
    my_image_.paste(character_.shape, (50, 187))
    
    enemys = [plant, tree]
    
    joystick.disp.image(start_)

    bullets = []
    while True:
        command = {'move': False, 'up': False , 'down': False, 'left': False, 'right': False, 'attack': False}
        
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
        
         # 공격
        if not joystick.button_Six.value:
            command['attack'] = True
            
            

        background.move(command)
        
        if command['attack'] == True:
            bullet = Bullet(my_image_, character)
            my_image_.paste(bullet.shape, (85, 75))
            joystick.disp.image(my_image_)
            bullet.collision_check_long(character_, enemys)
            bullet.move()
            my_image_.paste(bullet.shape, (85, 75))
            joystick.disp.image(my_image_)
            bullet.collision_check_long(character_, enemys)
            my_image_.paste(bullet.shape, (85, 75))
            joystick.disp.image(my_image_)
            bullet.collision_check_long(character_, enemys)
            my_image_.paste(bullet.shape, (85, 75))
            joystick.disp.image(my_image_)
            bullet.collision_check_long(character_, enemys)
            
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            my_image_.paste(character.shape, (90, 130))
            joystick.disp.image(my_image_)
            
            
        
        if command['move']==True and command['right']==True:
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            character = Character_2((background.position[0]+50, background.position[1]+187), background)
            my_image_.paste(character.shape, (50, 187))
            joystick.disp.image(my_image_)
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            character = Character_3((background.position[0]+50, background.position[1]+187), background)
            my_image_.paste(character.shape, (50, 187))
            joystick.disp.image(my_image_)
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            character = Character_4((background.position[0]+50, background.position[1]+187), background)
            my_image_.paste(character.shape, (50, 187))
            joystick.disp.image(my_image_)
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            character = Character_1((background.position[0]+50, background.position[1]+187), background)
            my_image_.paste(character.shape, (50, 187))
            joystick.disp.image(my_image_)
            
        if command['move']==True and command['left']==True:
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            character = Character_Left_2((background.position[0]+50, background.position[1]+187), background)
            my_image_.paste(character.shape, (50, 187))
            joystick.disp.image(my_image_)
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            character = Character_Left_3((background.position[0]+50, background.position[1]+187), background)
            my_image_.paste(character.shape, (50, 187))
            joystick.disp.image(my_image_)
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            character = Character_Left_4((background.position[0]+50, background.position[1]+187), background)
            my_image_.paste(character.shape, (50, 187))
            joystick.disp.image(my_image_)
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            character = Character_Left_1((background.position[0]+50, background.position[1]+187), background)
            my_image_.paste(character.shape, (50, 187))
            joystick.disp.image(my_image_)
        
        
    joystick.disp.image(my_image_)
        
        

if __name__ == '__main__':
    main()
