import pygame
import sys
import math
import random
from Chapter import *

class TargetOne():
    ExposedEvent = pygame.event.Event(pygame.USEREVENT, attr1='TargetOneExposed')


    def __init__(self, screen):

        self.x = 0
        self.y = 0
        self.mx = 0  # x haraket yönü
        self.my = 1  # y haraket yönü
        self.speed=2
        self.screen =screen
        width =screen.get_width()
        height =screen.get_height()
        randx = [165,300,430,550]
        self.x = randx[random.randint(0,3)]
        self.rectangle = pygame.rect.Rect(self.x, self.y , 65,111)
        self.carImagesOrder = 0
        self.carImages =[]  #arac goruntulerinin listesi (bir adet aracimiz var araclarda anlik efekt degisimi istenirse kolay ayarlanmasi icin liste olarak tutuldu)
        self.carImages.append(pygame.transform.scale(pygame.image.load("images/png/Car/car(0).png"),(self.rectangle[2], self.rectangle[3])))

        self.explosionImageOrder = -1 #carpisma oldugunda verilecek efekt goruntulerinin index degeri
        self.explosionImages = []   #carpisma oldugunda verilecek efekt goruntulerinin listesi
        for i in range(1, 10):
            self.explosionImages.append(
                pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_1_Expo (" + str(i) + ").png"),
                                       (self.rectangle[2] * 4, self.rectangle[2] * 4)))
        self.exposed = False

    def draw(self, screen):
        if self.explosionImageOrder == -1:
            self.carImagesOrder =0
            self.rectangle[1]=self.rectangle[1]+self.my*2 #y ekseninde asagi dogru hareket saglanir
            print(" target :  ",self.rectangle[0],self.rectangle[1])
            screen.blit(self.carImages[self.carImagesOrder],
                        [self.x,
                         self.rectangle[1] - int(self.carImages[self.carImagesOrder].get_height() / 2)])
        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx = self.rectangle.centerx - self.mx * 4
            if self.explosionImageOrder == 8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.rectangle[0] - int(self.explosionImages[self.explosionImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
            if self.explosionImageOrder == 8:
                self.explosionImageOrder = -1

        return False

    def expose(self):

        self.exposed = True
        if self.explosionImageOrder < 0:
            self.explosionImageOrder = 0





class PoliceTarget(TargetOne):
    def __init__(self,TargetOne):
        super().__init__(TargetOne.screen)
        randx = [165, 300, 430, 550]
        self.x = randx[random.randint(0, 3)]
        self.rectangle = pygame.rect.Rect(self.x, self.y, 65, 111)
        self.carImagesOrder = 0
        self.carImages = []

        self.carImages.append(pygame.image.load("images/png/Car/car(2).png"))
        self.explosionImages = TargetOne.explosionImages


    def draw(self, screen):
        if self.explosionImageOrder == -1:
            self.carImagesOrder = 0
            self.rectangle[1] = self.rectangle[1] + self.my * 3
            print(" target :  ", self.rectangle[0], self.rectangle[1])
            screen.blit(self.carImages[self.carImagesOrder],
                        [self.x,
                         self.rectangle[1] - int(self.carImages[self.carImagesOrder].get_height() / 2)])
            return False
        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx = self.rectangle.centerx - self.mx * self.speed
            if self.explosionImageOrder == 8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.rectangle[0] - int(self.explosionImages[self.explosionImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
            if self.explosionImageOrder == 8:
                self.explosionImageOrder = -1



class GreenTarget(TargetOne):
    def __init__(self, TargetOne):
        super().__init__(TargetOne.screen)

        self.carImagesOrder = 0
        self.carImages = []

        self.carImages.append(pygame.image.load("images/png/Car/car(1).png"))
        self.explosionImages = []

        self.explosionImages = TargetOne.explosionImages

    def draw(self, screen):
        if self.explosionImageOrder == -1:
            self.carImagesOrder = 0
            # self.rectangle[0] = self.rectangle[0] - self.mx * 2
            self.rectangle[1] = self.rectangle[1] + self.my * 3
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            print(" target :  ", self.rectangle[0], self.rectangle[1])
            screen.blit(self.carImages[self.carImagesOrder],
                        [self.x,
                         self.rectangle[1] - int(self.carImages[self.carImagesOrder].get_height() / 2)])
            return False
        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            self.rectangle.centerx = self.rectangle.centerx - self.mx * self.speed
            if self.explosionImageOrder == 8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.rectangle[0] - int(self.explosionImages[self.explosionImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
            if self.explosionImageOrder == 8:
                self.explosionImageOrder = -1



class FuelTarget(TargetOne):

    def __init__(self, TargetOne):
        super().__init__(TargetOne.screen)


        self.carImagesOrder = 0
        self.carImages = []

        self.carImages.append(pygame.image.load("images/png/Car/car_fuel.png"))
        self.explosionImages = []

        self.explosionImages = TargetOne.explosionImages

    def draw(self, screen):


        if self.explosionImageOrder == -1:
            self.carImagesOrder = 0
            # self.rectangle[0] = self.rectangle[0] - self.mx * 2
            self.rectangle[1] = self.rectangle[1] + self.my * 2
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            print(" target :  ", self.rectangle[0], self.rectangle[1])
            screen.blit(self.carImages[self.carImagesOrder],
                        [self.x,
                         self.rectangle[1] - int(self.carImages[self.carImagesOrder].get_height() / 2)])
            return False
        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx = self.rectangle.centerx - self.mx * self.speed
            if self.explosionImageOrder == 8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.rectangle[0] - int(self.explosionImages[self.explosionImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
            if self.explosionImageOrder == 8:
                self.explosionImageOrder = -1




