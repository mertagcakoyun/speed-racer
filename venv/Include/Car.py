                ## DERS PLANE
import pygame
import sys
import math
import random

class Car():
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.mx=0 #x haraket yönü
        self.my=0 #x haraket yönü
        self.screen=screen
        width=screen.get_width()
        height=screen.get_height()
        self.rectangle=pygame.rect.Rect(int(width/2)-30,height-200,67,111)
        self.carImageOrder=0
        self.carImage=pygame.image.load("images/png/Car/car_red.png")
        self.shootImageOrder=0
        self.gasValue = 100
        self.exposed=False
        self.exposedEvent=pygame.event.Event(pygame.USEREVENT, attr1='carExposedEvent')


    def draw(self,screen):

        screen.blit(self.carImage, self.rectangle)
        self.rectangle[0]=self.rectangle[0]+self.mx*4
        self.rectangle[1] = self.rectangle[1] + self.my * 4
        #print("car : ",self.rectangle[0],self.rectangle[1])
        self.rectangle.clamp_ip(screen.get_rect())# car objesini ekran karesi içinde tutar



    def expose(self):

        self.exposed=True

    def useGas(self,screen):

        self.gasValue-=2
        return self.gasValue

    def isRoad(self):

        if  self.rectangle[0]>140 and self.rectangle[0]<640:
            return True
        else:
            return False

