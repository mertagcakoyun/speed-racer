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
        width=screen.get_width()
        height=screen.get_height()
        self.rectangle=pygame.rect.Rect(10,int(height/2)-int(height/5/2),67,111)
        self.flyImageOrder=0
        self.flyImage=pygame.image.load("images/png/Car/car_red.png")
        self.shootImageOrder=0

        self.exposed=False
        self.exposedEvent=pygame.event.Event(pygame.USEREVENT, attr1='carExposedEvent')


    def draw(self,screen):

        screen.blit(self.flyImage, self.rectangle)
        self.rectangle[0]=self.rectangle[0]+self.mx*4
        self.rectangle[1] = self.rectangle[1] + self.my * 4
        print("car : ",self.rectangle[0],self.rectangle[1])
        self.rectangle.clamp_ip(screen.get_rect())# car objesini ekran karesi içinde tutar



    def expose(self):
        self.exposed=True
