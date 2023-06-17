import sys
import pygame
import random
import math
import time

pygame.init() 
from pygame.locals import * 
screen = pygame.display.set_mode((302,419))
pygame.display.set_caption("My Game")

def gameloop():
    
    #score
    score_value = 0
    speed_value = 1
    font1= pygame.font.Font("freesansbold.ttf",10)
    def show_score(x,y):
        score = font1.render(" "+ str(score_value), True, (0,0,0))
        screen.blit(score, (x,y))
    
    #highscore 
    with open ("highscore.txt","r") as f:
            highscore = f.read()
    def show_highscore(x,y):
        Hiscore_text = font1.render(' ' + str(highscore),True,(0,0,0))
        screen.blit (Hiscore_text,(x,y))
        pygame.display.update()
    def show_speed(x,y):
        speed_text = font1.render(' ' + str(speed_value),True,(0,0,0))
        screen.blit (speed_text,(x,y))
        pygame.display.update()


    #players car
    maincar = pygame.image.load('maincar.png')
    maincarX = 42
    maincarY = 340
    maincarX_change = 0
    maincarY_change = 0
    #other cars
    car1 = pygame.image.load('maincar.png')
    car1X = random.choice([42,107])
    car1Y = -80
    car1Ychange = 0
    car2 = pygame.image.load('maincar.png')
    car2X = random.choice([42,107])
    car2Y = -240
    car2Ychange = 0
    car3 = pygame.image.load('maincar.png')
    car3X = random.choice([42,107])
    car3Y = -400
    car3Ychange = 0
    car4 = pygame.image.load('maincar.png')
    car4X = random.choice([42,107])
    car4Y = -560
    car4Ychange = 0
    car5 = pygame.image.load('maincar.png')
    car5X = random.choice([42,107])
    car5Y = -720
    car5Ychange = 0
    car6 = pygame.image.load('maincar.png')
    car6X = random.choice([42,107])
    car6Y = -880
    car6Ychange = 0
    
    theirspeed = 2
    
    #left blocks
    block1 = pygame.image.load('block.png')
    block1X = 0
    block1Y = -40
    block1Ychange = 0
    block2 = pygame.image.load('block.png')
    block2X = 0
    block2Y = -120
    block2Ychange = 0
    block3 = pygame.image.load('block.png')
    block3X = 0
    block3Y = -200
    block3Ychange = 0
    block4 = pygame.image.load('block.png')
    block4X = 0
    block4Y = -280
    block4Ychange = 0
    block5 = pygame.image.load('block.png')
    block5X = 0
    block5Y = -360
    block5Ychange = 0
    block6 = pygame.image.load('block.png')
    block6X = 0
    block6Y = -440
    block6Ychange = 0
    block7 = pygame.image.load('block.png')
    block7X = 0
    block7Y = -520
    block7Ychange = 0
    block8 = pygame.image.load('block.png')
    block8X = 0
    block8Y = -600
    block8Ychange = 0
    block9 = pygame.image.load('block.png')
    block9X = 0
    block9Y = -680
    block9Ychange = 0
    block10 = pygame.image.load('block.png')
    block10X = 0
    block10Y = -760
    block10Ychange = 0
    block11 = pygame.image.load('block.png')
    block11X = 0
    block11Y = -840
    block11Ychange = 0
    block12 = pygame.image.load('block.png')
    block12X = 0
    block12Y = -920
    block12Ychange = 0
    #right blocks 
    block13 = pygame.image.load('block.png')
    block13X = 190
    block13Y = -40
    block13Ychange = 0
    block14 = pygame.image.load('block.png')
    block14X = 190
    block14Y = -120
    block14Ychange = 0
    block15 = pygame.image.load('block.png')
    block15X = 190
    block15Y = -200
    block15Ychange = 0
    block16 = pygame.image.load('block.png')
    block16X = 190
    block16Y = -280
    block16Ychange = 0
    block17 = pygame.image.load('block.png')
    block17X = 190
    block17Y = -360
    block17Ychange = 0
    block18 = pygame.image.load('block.png')
    block18X = 190
    block18Y = -440
    block18Ychange = 0
    block19 = pygame.image.load('block.png')
    block19X = 190
    block19Y = -520
    block19Ychange = 0
    block20 = pygame.image.load('block.png')
    block20X = 190
    block20Y = -600
    block20Ychange = 0
    block21 = pygame.image.load('block.png')
    block21X = 190
    block21Y = -680
    block21Ychange = 0
    block22 = pygame.image.load('block.png')
    block22X = 190
    block22Y = -760
    block22Ychange = 0
    block23 = pygame.image.load('block.png')
    block23X = 190
    block23Y = -840
    block23Ychange = 0
    block24 = pygame.image.load('block.png')
    block24X = 190
    block24Y = -920
    block24Ychange = 0   

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_RIGHT:
                    maincarX += (13*5)
                if event.key == K_LEFT:
                    maincarX -= (13*5)
                       
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_RIGHT:
                    maincarX_change = 0            
                if event.key == pygame.K_LEFT:
                    maincarX_change = 0                
                
        #boundary for main car
        if maincarX < 42:
            maincarX = 42
        if maincarX > 107:
            maincarX = 107 
        if maincarY < 0:
            maincarY = 0
        if maincarY > 340:
            maincarY = 340

        bg = pygame.image.load('bg5.png')
        screen.blit(bg,(0,0))
        
        screen.blit(maincar,(maincarX,maincarY))
        screen.blit(car1,(car1X,car1Y))
        screen.blit(car2,(car2X,car2Y))
        screen.blit(car3,(car3X,car3Y))
        screen.blit(car4,(car4X,car4Y))
        screen.blit(car5,(car5X,car5Y))
        screen.blit(car6,(car6X,car6Y))
        screen.blit(block1,(block1X,block1Y))
        screen.blit(block2,(block2X,block2Y))
        screen.blit(block3,(block3X,block3Y))
        screen.blit(block4,(block4X,block4Y))
        screen.blit(block5,(block5X,block5Y))
        screen.blit(block6,(block6X,block6Y))
        screen.blit(block7,(block7X,block7Y))
        screen.blit(block8,(block8X,block8Y))
        screen.blit(block9,(block9X,block9Y))
        screen.blit(block10,(block10X,block10Y))
        screen.blit(block11,(block11X,block11Y))
        screen.blit(block12,(block12X,block12Y))
        screen.blit(block13,(block13X,block13Y))
        screen.blit(block14,(block14X,block14Y))
        screen.blit(block15,(block15X,block15Y))
        screen.blit(block16,(block16X,block16Y))
        screen.blit(block17,(block17X,block17Y))
        screen.blit(block18,(block18X,block18Y))
        screen.blit(block19,(block19X,block19Y))
        screen.blit(block20,(block20X,block20Y))
        screen.blit(block21,(block21X,block21Y))
        screen.blit(block22,(block22X,block22Y))
        screen.blit(block23,(block23X,block23Y))
        screen.blit(block24,(block24X,block24Y))

        #colling functions
        show_score(240,20)
        show_highscore(240,53)
        show_speed(240,90)

        maincarX += maincarX_change
        maincarY +=maincarY_change

        car1Y += theirspeed
        car2Y += theirspeed
        car3Y += theirspeed
        car4Y += theirspeed
        car5Y += theirspeed
        car6Y += theirspeed
        block1Y += theirspeed
        block2Y += theirspeed
        block3Y += theirspeed
        block4Y += theirspeed
        block5Y += theirspeed
        block6Y += theirspeed
        block7Y += theirspeed
        block8Y += theirspeed
        block9Y += theirspeed
        block10Y += theirspeed
        block11Y += theirspeed
        block12Y += theirspeed
        block13Y += theirspeed
        block14Y += theirspeed
        block15Y += theirspeed
        block16Y += theirspeed
        block17Y += theirspeed
        block18Y += theirspeed
        block19Y += theirspeed
        block20Y += theirspeed
        block21Y += theirspeed
        block22Y += theirspeed
        block23Y += theirspeed
        block24Y += theirspeed

        if car1Y > 500:
            car1X = random.choice([42,107])
            car1Y = -480
            score_value += 100
            speed_value += 1
        if car2Y > 500:
            car2X = random.choice([42,107])
            car2Y = -480
            score_value += 100
            speed_value += 1
        if car3Y > 500:
            car3X = random.choice([42,107])
            car3Y = -480
            score_value += 100
            speed_value += 1
        if car4Y > 500:
            car4X = random.choice([42,107])
            car4Y = -480
            score_value += 100
            speed_value += 1
        if car5Y > 500:
            car5X = random.choice([42,107])
            car5Y = -480
            score_value += 100
            speed_value += 1
        if car6Y > 500:
            car6X = random.choice([42,107])
            car6Y = -480
            score_value += 100
            speed_value += 1
        if block1Y > 430:
            block1X = 0
            block1Y = -520
        if block2Y > 430:
            block2X = 0
            block2Y = -520
        if block3Y > 430:
            block3X = 0
            block3Y = -520
        if block4Y > 430:
            block4X = 0
            block4Y = -520
        if block5Y > 430:
            block5X = 0
            block5Y = -520
        if block6Y > 430:
            block6X = 0
            block6Y = -520
        if block7Y > 430:
            block7X = 0
            block7Y = -520
        if block8Y > 430:
            block8X = 0
            block8Y = -520
        if block9Y > 430:
            block9X = 0
            block9Y = -520
        if block10Y > 430:
            block10X = 0
            block10Y = -520
        if block11Y > 430:
            block11X = 0
            block11Y = -520
        if block12Y > 430:
            block12X = 0
            block12Y = -520
        
        if block13Y > 430:
            block13X = 190
            block13Y = -520
        if block14Y > 430:
            block14X = 190
            block14Y = -520
        if block15Y > 430:
            block15X = 190
            block15Y = -520
        if block16Y > 430:
            block16X = 190
            block16Y = -520
        if block17Y > 430:
            block17X = 190
            block17Y = -520
        if block18Y > 430:
            block18X = 190
            block18Y = -520
        if block19Y > 430:
            block19X = 190
            block19Y = -520
        if block20Y > 430:
            block20X = 190
            block20Y = -520
        if block21Y > 430:
            block21X = 190
            block21Y = -520
        if block22Y > 430:
            block22X = 190
            block22Y = -520
        if block23Y > 430:
            block23X = 190
            block23Y = -520
        if block24Y > 430:
            block24X = 190
            block24Y = -520
           
        if score_value > int(highscore):
            highscore = score_value
        
        if score_value > 100:
            car1Y += 2
            car2Y += 2
            car3Y += 2
            car4Y += 2
            car5Y += 2
            car6Y += 2

        
        def iscollision(carX,carY,mycarX,mycarY):
            distance = math.sqrt(math.pow(carX-mycarX,2) + math.pow(carY - mycarY,2)) 
            if distance < 40: 
                return True
            else:
                return False

        coll1 = iscollision(car1X,car1Y,maincarX,maincarY)
        coll2 = iscollision(car2X,car2Y,maincarX,maincarY) 
        coll3 = iscollision(car3X,car3Y,maincarX,maincarY) 
        coll4 = iscollision(car4X,car4Y,maincarX,maincarY) 
        coll5 = iscollision(car5X,car5Y,maincarX,maincarY) 
        coll6 = iscollision(car6X,car6Y,maincarX,maincarY) 
        
        if coll1 or coll2 or coll3 or coll4 or coll5 or coll6:  
            go = pygame.image.load('go.png')
            screen.blit(go,(0,0))
            score_value = 0
            speed_value = 1
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car4Ychange = 0
            car5Ychange = 0
            car6Ychange = 0
            block1Ychange = 0
            block2Ychange = 0
            block3Ychange = 0
            block4Ychange = 0
            block5Ychange = 0
            block6Ychange = 0
            block7Ychange = 0
            block8Ychange = 0
            block9Ychange = 0
            block10Ychange = 0
            block11Ychange = 0
            block12Ychange = 0
            block13Ychange = 0
            block14Ychange = 0
            block15Ychange = 0
            block16Ychange = 0
            block17Ychange = 0
            block18Ychange = 0
            block19Ychange = 0
            block20Ychange = 0
            block21Ychange = 0
            block22Ychange = 0
            block23Ychange = 0
            block24Ychange = 0
        
            maincarX_change = 0
            maincarY_change = 0
            
        with open ("highscore.txt","w") as f:
            f.write(str(highscore))

        pygame.display.update()
        
gameloop()