from PIL import Image
import numpy as np
import time
from colorsys import hsv_to_rgb
from Character_1 import Character_1
from Character_2 import Character_2
from Character_3 import Character_3
from Character_4 import Character_4
from Character_Left_1 import Character_Left_1
from Character_Left_2 import Character_Left_2
from Character_Left_3 import Character_Left_3
from Character_Left_4 import Character_Left_4
from Character_plant_1 import Character_plant_1
from Character_plant_2 import Character_plant_2
from Character_plant_3 import Character_plant_3
from Character_plant_4 import Character_plant_4
from Character_plant_Left_1 import Character_plant_Left_1
from Character_plant_Left_2 import Character_plant_Left_2
from Character_plant_Left_3 import Character_plant_Left_3
from Character_plant_Left_4 import Character_plant_Left_4
from Character_haam import Character_haam
from Character_haam_plant import Character_haam_plant
from Character_haam_left import Character_haam_left
from Character_haam_plant_left import Character_haam_plant_left
from Character_down import Character_down
from Character_down_left import Character_down_left
from Character_flower import Character_flower
from Character_hurt import Character_hurt
from Enemy_1 import Enemy_1
from Enemy_2 import Enemy_2
from Enemy_box import Enemy_box
from Enemy_flower import Enemy_flower
from Enemy_boss import Enemy_boss
from Bullet import Bullet
from Bullet_2 import Bullet_2
from Bullet_3 import Bullet_3
from Bullet_4 import Bullet_4
from Bullet_5 import Bullet_5
from Joystick import Joystick
from BackGround import BackGround

def main():
    joystick = Joystick()
    background = BackGround()
    newBackground = BackGround()
    start_ = Image.open('start.png')
    isJump = False
    flag = True # if true : up, false : down
    i = 0
    
    box = Enemy_box((100, 523), background.shape)
    background.shape.paste(box.shape, box.position)
    plant = Enemy_1((200, 533), background.shape)
    background.shape.paste(plant.shape, plant.position)
    tree = Enemy_2((250, 493), background.shape)
    background.shape.paste(tree.shape, tree.position)
    flower = Enemy_flower((150, 533), background.shape)
    background.shape.paste(flower.shape, flower.position)
    boss = Enemy_boss((300, 403), background.shape)
    background.shape.paste(boss.shape, boss.position)

    character_ = Character_1((background.position[0]+50, background.position[1]+167), background)
    my_image_ = background.shape.crop((background.position[0],background.position[1], background.position[0]+240, background.position[1]+240))
    my_image_.paste(character_.shape, (50, 167))
    
    enemys = [box, plant, flower, tree, boss]
    
    joystick.disp.image(start_)

    while True:               
        command = {'move': False, 'up': False , 'down': False, 'left': False, 'right': False, 'attack': False, 'haam': False}
        
        # move
        if not joystick.button_Left.value: 
            command['left'] = True
            command['move'] = True
            character_.direction = 'left'

        if not joystick.button_Right.value: 
            command['right'] = True
            command['move'] = True
            character_.direction = 'right'
            
        if not joystick.button_Five.value: 
            command['up'] = True
            command['move'] = True
            
        if not joystick.button_Six.value:
            bullet = Bullet_5(my_image_, character_)
            before = bullet.shot
            my_image_.paste(bullet.shape, (93, 167))
            joystick.disp.image(my_image_)
            bullet.collision_check_long(enemys)
            after = bullet.shot
            if before != after:
                bullet.shot = False
                continue            
            
        # spit it out    
        if not joystick.button_Down.value:
            if character_.state == None:
                continue
            else:
                character_.state = None
                if character_.direction == 'right':
                    my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                    character = Character_down((background.position[0]+50, background.position[1]+167), background)
                    my_image_.paste(character.shape, (50, 167))
                    joystick.disp.image(my_image_)
                    my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                    character = Character_1((background.position[0]+50, background.position[1]+167), background)
                    my_image_.paste(character.shape, (50, 167))
                    joystick.disp.image(my_image_)
                elif character_.direction == 'right':
                    my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                    character = Character_down_left((background.position[0]+50, background.position[1]+167), background)
                    my_image_.paste(character.shape, (50, 167))
                    joystick.disp.image(my_image_)
                    my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                    character = Character_Left_1((background.position[0]+50, background.position[1]+167), background)
                    my_image_.paste(character.shape, (50, 167))
                    joystick.disp.image(my_image_)
            
        # eat    
        if not joystick.button_Up.value:
            if character_.state == 'flower':
                continue
            elif character_.state == 'plant':
                if character_.direction == 'left':
                    character = Character_haam_plant_left((background.position[0]+50, background.position[1]+167), background)
                elif character_.direction == 'right':
                    character = Character_haam_plant((background.position[0]+50, background.position[1]+167), background)
            else:
                if character_.direction == 'left':
                    character = Character_haam_left((background.position[0]+50, background.position[1]+167), background)
                elif character_.direction == 'right':
                    character = Character_haam((background.position[0]+50, background.position[1]+167), background)
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            my_image_.paste(character.shape, (50, 167))
            joystick.disp.image(my_image_)
            
            for enemy in enemys:
                collision = character.overlap(character.attack, enemy.attack)
                if collision:
                    if enemy.state == 'live':
                        enemy.state = 'dead'
                        if enemy == flower:
                            character_.state = 'flower'
                        elif enemy == plant:
                            character_.state = 'plant'
                        elif enemy == box:
                            character_.state = 'plant'
                
            time.sleep(1)
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            if character_.state == 'plant':
                character = Character_plant_1((background.position[0]+50, background.position[1]+167), background)
            elif character_.state == 'flower':
                character = Character_flower((background.position[0]+50, background.position[1]+167), background)
            elif character_.state == None:
                character = Character_1((background.position[0]+50, background.position[1]+167), background)
            my_image_.paste(character.shape, (50, 167))
            joystick.disp.image(my_image_)
        
        
        
        
        for enemy in enemys:
            if enemy.state == 'dead':
                enemy.death(newBackground.shape)
                background.shape.paste(enemy.shape_, (enemy.position[0], enemy.position[1]))
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))                    
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                    
        background.move(command) 
        
        if command['up'] == True and command['move'] == True:
            if isJump == True:
                continue
            isJump = True
            background.jump()
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            character = Character_1((background.position[0]+50, background.position[1]+167), background)
            my_image_.paste(character.shape, (50, 167))
            joystick.disp.image(my_image_)
            i = 1      
               
        if command['move']==True and command['right']==True:
            if character_.state == 'flower':
                continue
            elif character_.state == 'plant':
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_plant_2((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_plant_3((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_plant_4((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_plant_1((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                before = character_.life
                character_.collision_check(character, enemys, character_)
                after = character_.life
                if before != after:
                    for _ in range(0, (5 - character_.life)):
                        my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                        character = Character_hurt((background.position[0]+50, background.position[1]+167), background)
                        my_image_.paste(character.shape, (50, 167))
                        joystick.disp.image(my_image_)
                        my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                        character = Character_plant_1((background.position[0]+50, background.position[1]+167), background)
                        my_image_.paste(character.shape, (50, 167))
                        joystick.disp.image(my_image_)
            else:
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_2((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_3((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_4((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_1((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                before = character_.life
                character_.collision_check(character, enemys, character_)
                after = character_.life
                if before != after:
                    for _ in range(0, (5 - character_.life)):
                        my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                        character = Character_hurt((background.position[0]+50, background.position[1]+167), background)
                        my_image_.paste(character.shape, (50, 167))
                        joystick.disp.image(my_image_)
                        my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                        character = Character_1((background.position[0]+50, background.position[1]+167), background)
                        my_image_.paste(character.shape, (50, 167))
                        joystick.disp.image(my_image_)
            
            if character_.life <= 0:
                my_image_ = Image.open('gameover.png')
                joystick.disp.image(my_image_)
                exit(0)
                
            
        if command['move']==True and command['left']==True:
            if character_.state == 'flower':
                continue
            elif character_.state == 'plant':
                    my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                    character = Character_plant_Left_2((background.position[0]+50, background.position[1]+167), background)
                    my_image_.paste(character.shape, (50, 167))
                    joystick.disp.image(my_image_)
                    my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                    character = Character_plant_Left_3((background.position[0]+50, background.position[1]+167), background)
                    my_image_.paste(character.shape, (50, 167))
                    joystick.disp.image(my_image_)
                    my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                    character = Character_plant_Left_4((background.position[0]+50, background.position[1]+167), background)
                    my_image_.paste(character.shape, (50, 167))
                    joystick.disp.image(my_image_)
                    my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                    character = Character_plant_Left_1((background.position[0]+50, background.position[1]+167), background)
                    my_image_.paste(character.shape, (50, 167))
                    joystick.disp.image(my_image_)
                    before = character_.life
                    character_.collision_check(character, enemys, character_)
                    after = character_.life
                    if before != after:
                        for _ in range(0, (5 - character_.life)):
                            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                            character = Character_hurt((background.position[0]+50, background.position[1]+167), background)
                            my_image_.paste(character.shape, (50, 167))
                            joystick.disp.image(my_image_)
                            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                            character = Character_plant_Left_1((background.position[0]+50, background.position[1]+167), background)
                            my_image_.paste(character.shape, (50, 167))
                            joystick.disp.image(my_image_)
            else:
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_Left_2((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_Left_3((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_Left_4((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_Left_1((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                before = character_.life
                character_.collision_check(character, enemys, character_)
                after = character_.life
                if before != after:
                    for _ in range(0, (5 - character_.life)):
                        my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                        character = Character_hurt((background.position[0]+50, background.position[1]+167), background)
                        my_image_.paste(character.shape, (50, 167))
                        joystick.disp.image(my_image_)
                        my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                        character = Character_Left_1((background.position[0]+50, background.position[1]+167), background)
                        my_image_.paste(character.shape, (50, 167))
                        joystick.disp.image(my_image_)
        
        if isJump == True and i == 0:
            background.jump_down()
            my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
            character = Character_1((background.position[0]+50, background.position[1]+167), background)
            my_image_.paste(character.shape, (50, 167))
            joystick.disp.image(my_image_)
            isJump = False
            flag = True
        
        if isJump == True and i == 30:
            flag = False
            
        if isJump == True:
            if flag == True:
                print("up")
                background.jump()
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_1((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                i += 1
            elif flag == False:
                print("down")
                background.jump_down()
                my_image_ = background.shape.crop((background.position[0], background.position[1], background.position[0]+240, background.position[1]+240))
                character = Character_1((background.position[0]+50, background.position[1]+167), background)
                my_image_.paste(character.shape, (50, 167))
                joystick.disp.image(my_image_)
                i -= 1
        
        check = 0        
        for enemy in enemys:
            print(enemy.state)
            if enemy.state == 'death':
                check += 1
                
        if check == 4:
            my_image_ = Image.open('clear.png')
            joystick.disp.image(my_image_)
            exit(0)
                
    joystick.disp.image(my_image_)
        
        

if __name__ == '__main__':
    main()
