#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
import random
import time
from Chapter import *
from Menu import Menu
from Car import *


pygame.init()

gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Speed Racer')


car=Car(gameDisplay)
crashed=False
clock = pygame.time.Clock()
chapter= ChapterOne(gameDisplay)
chapter.start(gameDisplay)
endEvent=pygame.event.Event(pygame.USEREVENT, attr1='endEvent')
speed=0
menu=Menu(gameDisplay.get_rect())
end=False
startTime = pygame.time.get_ticks()

def text_objects(text,font):    # metinimizin ozellikleri belirlendi ve donduruldu
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message(text):              ## metin fontu ayarlandi ve belirlenen konuma yazma islemi yapildi
    text_message=pygame.font.Font("fonts/ARCADE.TTF",80)
    textsurf,textrect=text_objects(text,text_message)
    textrect.center=((gameDisplay_width/2),(gameDisplay_height/2))
    gameDisplay.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)


def crash(text):    #oyunda cesitli sebeplerden kural ihlali saptanirsa calisir
    message(text)




while not crashed:

    chapter.isGasExist(gameDisplay) #Benzin kontrolu yapildi
    for event in pygame.event.get():
        #chapter.speed=speed

        if event.type == pygame.QUIT:
            #crashed = True
            chapter.finish(gameDisplay)
        elif event.type == pygame.KEYDOWN:

            if event.key==pygame.K_ESCAPE:
                chapter.pgenerateTargetTimer.pause(True)
                crashed=menu.runMenu(gameDisplay)
                chapter.pgenerateTargetTimer.pause(False)

            if event.key == pygame.K_UP:
                #chapter.speed+=1
                chapter.car.my -= 2
                # speed+=1
            if event.key == pygame.K_DOWN:
                #chapter.speed+=1
                #speed-=2
                chapter.car.my += 2
            chapter.carInRoad(gameDisplay)  # sinir kontrolu
            if event.key == pygame.K_LEFT:
                chapter.car.mx-=2
            if event.key == pygame.K_RIGHT:
                chapter.car.mx+=2




        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                #chapter.speed-=1
                chapter.car.my=0
            if event.key == pygame.K_DOWN:
                chapter.car.my=0
            if event.key == pygame.K_LEFT:
                chapter.car.mx=0
            if event.key == pygame.K_RIGHT:
                chapter.car.mx=0

        #event karşılaştırmalarında eşitlik koşulu çalışır
        #eventlar aynı olmalı özellikleriyle birlikte
        elif event== chapter.finishEvent or chapter.endFlag==True :
            crash("GAME OVER...")
            print(event)
            end=True
            crashed=True
        elif event== chapter.complatedEvent:
            crash("COMPLATED...")
            print(event)
            end = True
            crashed = True

        elif event== chapter.car.exposedEvent:
            print(event)

    if not end:
        chapter.draw(gameDisplay)
        gameTime = pygame.time.get_ticks() - startTime
        chapter.drawGameTime(gameTime, gameDisplay)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()


