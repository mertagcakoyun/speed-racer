import pygame
import sys
import math
import random


class TargetOne():
    ExposedEvent = pygame.event.Event(pygame.USEREVENT, attr1='TargetOneExposed')

    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.mx = 0  # x haraket yönü
        self.my = 1  # y haraket yönü
        self.life = 100
        self.scrn =screen
        width = self.scrn.get_width()
        height = self.scrn.get_height()
        randx = [155,290,410,550]
        self.x = randx[random.randint(0,3)]
        self.rectangle = pygame.rect.Rect(self.x, self.y + int(height / 10) / 2, 65,
                                          111)

        self.flyImageOrder = 0
        self.flyImages =[]
        self.flyImages.append(pygame.transform.scale(pygame.image.load("images/png/Car/car(0).png"),
                                       (self.rectangle[2], self.rectangle[3])))



        self.explosionImageOrder = -1
        self.explosionImages = []
        for i in range(1, 10):
            self.explosionImages.append(
                pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_1_Expo (" + str(i) + ").png"),
                                       (self.rectangle[2] * 4, self.rectangle[2] * 4)))
        self.exposed = False

    def draw(self, screen):
        if self.explosionImageOrder == -1:
            self.flyImageOrder =0
            #self.rectangle[0] = self.rectangle[0] - self.mx * 2
            self.rectangle[1]=self.rectangle[1]+self.my*2
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            print(" target :  ",self.rectangle[0],self.rectangle[1])
            screen.blit(self.flyImages[self.flyImageOrder],
                        [self.x,
                         self.rectangle[1] - int(self.flyImages[self.flyImageOrder].get_height() / 2)])
        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx = self.rectangle.centerx - self.mx * 2
            if self.explosionImageOrder == 8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.rectangle[0] - int(self.explosionImages[self.explosionImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
            if self.explosionImageOrder == 8:
                self.explosionImageOrder = -1

        return False

    def expose(self):
        self.life = 0
        self.exposed = True
        if self.explosionImageOrder < 0:
            self.explosionImageOrder = 0





class PoliceTarget(TargetOne):
    def __init__(self,TargetOne):
        super().__init__(TargetOne.scrn)
        self.rectangle =TargetOne.rectangle
        self.flyImageOrder = 0
        self.flyImages = []

        self.flyImages.append(pygame.image.load("images/png/Car/car(2).png"))
        self.explosionImages = TargetOne.explosionImages


    def draw(self, screen):
        if self.explosionImageOrder == -1:
            self.flyImageOrder = 0
            # self.rectangle[0] = self.rectangle[0] - self.mx * 2
            self.rectangle[1] = self.rectangle[1] + self.my * 2
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            print(" target :  ", self.rectangle[0], self.rectangle[1])
            screen.blit(self.flyImages[self.flyImageOrder],
                        [self.x,
                         self.rectangle[1] - int(self.flyImages[self.flyImageOrder].get_height() / 2)])
        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx = self.rectangle.centerx - self.mx * 2
            if self.explosionImageOrder == 8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.rectangle[0] - int(self.explosionImages[self.explosionImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
            if self.explosionImageOrder == 8:
                self.explosionImageOrder = -1

        return False


# class OrangeTarget(TargetOne):
#     def __init__(self, TargetOne):
#         super().__init__(TargetOne.scrn)
#
#         self.flyImageOrder = 0
#         self.flyImages = []
#
#         self.flyImages.append(pygame.image.load("images/png/Car/car(0).png"))
#         self.explosionImages = []
#
#     def draw(self, screen):
#         self.rectangle[1] = self.rectangle[1] + self.my * 2
#         screen.blit(self.flyImages[self.flyImageOrder],
#                         [self.x,
#                          self.rectangle[1] - int(self.flyImages[self.flyImageOrder].get_height() / 2)])

class GreenTarget(TargetOne):
    def __init__(self, TargetOne):
        super().__init__(TargetOne.scrn)

        self.flyImageOrder = 0
        self.flyImages = []

        self.flyImages.append(pygame.image.load("images/png/Car/car(1).png"))
        self.explosionImages = []

        self.explosionImages = TargetOne.explosionImages

    def draw(self, screen):
        if self.explosionImageOrder == -1:
            self.flyImageOrder = 0
            # self.rectangle[0] = self.rectangle[0] - self.mx * 2
            self.rectangle[1] = self.rectangle[1] + self.my * 2
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            print(" target :  ", self.rectangle[0], self.rectangle[1])
            screen.blit(self.flyImages[self.flyImageOrder],
                        [self.x,
                         self.rectangle[1] - int(self.flyImages[self.flyImageOrder].get_height() / 2)])
        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx = self.rectangle.centerx - self.mx * 2
            if self.explosionImageOrder == 8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.rectangle[0] - int(self.explosionImages[self.explosionImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
            if self.explosionImageOrder == 8:
                self.explosionImageOrder = -1

        return False

class FuelTarget(TargetOne):
    def __init__(self, TargetOne):
        super().__init__(TargetOne.scrn)

        self.flyImageOrder = 0
        self.flyImages = []

        self.flyImages.append(pygame.image.load("images/png/Car/car(3).png"))
        self.explosionImages = []

        self.explosionImages = TargetOne.explosionImages

    def draw(self, screen):
        if self.explosionImageOrder == -1:
            self.flyImageOrder = 0
            # self.rectangle[0] = self.rectangle[0] - self.mx * 2
            self.rectangle[1] = self.rectangle[1] + self.my * 2
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            print(" target :  ", self.rectangle[0], self.rectangle[1])
            screen.blit(self.flyImages[self.flyImageOrder],
                        [self.x,
                         self.rectangle[1] - int(self.flyImages[self.flyImageOrder].get_height() / 2)])
        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx = self.rectangle.centerx - self.mx * 2
            if self.explosionImageOrder == 8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.rectangle[0] - int(self.explosionImages[self.explosionImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
            if self.explosionImageOrder == 8:
                self.explosionImageOrder = -1

        return False

