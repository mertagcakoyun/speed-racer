                    ##  CHAPTER

import pygame
import sys
import math
import random
from  threading import Timer
from TargetOne import *
from Car import Car
from pTimer import  pTimer
class ChapterOne():
    def __init__(self,screen):
        self.name="Let's Start"
        self.car= Car(screen)
        self.targets=[]
        self.backGroundImage=pygame.transform.scale(pygame.image.load("images/png/background-1.png"),(screen.get_width(), screen.get_height()))
        self.backGroundImageY=0
        self.backGroundImageX = 0
        self.screen= screen
        self.speed=1

        #2 saniyede bir hedef üretilmeli
        #bunun için kendi yazdığımız timer sınıfını kulllıyoruz
        #bu işlem için uygun olan threadlerdir ancak bu konuya sonra geleceğiz
        self.pgenerateTargetTimer=pTimer(2,self.generateTarget,screen)

        self.finishEvent=pygame.event.Event(pygame.USEREVENT, attr1='finishEvent')

    def start(self,screen):

        self.pgenerateTargetTimer.start()
    def finish(self,screen):
        self.pgenerateTargetTimer.stop()
        pygame.event.post(self.finishEvent)
    

    def generateTarget(self,arguments):
        targetChoice= random.randint(0,5)
        print(str(targetChoice))
        newTarget = None

        if targetChoice == 0:
            newTarget= TargetOne(arguments[0])
        elif targetChoice == 1 :
            newTarget = PoliceTarget(TargetOne(arguments[0]))
        elif targetChoice ==2 :
            newTarget = GreenTarget(TargetOne(arguments[0]))
        else:
            newTarget = FuelTarget(TargetOne(arguments[0]))


        self.targets.append(newTarget)


    def drawBackGround(self, screen):
        screen.blit(self.backGroundImage,(0,self.backGroundImageY))
        self.backGroundImageY=self.backGroundImageY+self.speed
        screen.blit(self.backGroundImage,(0,self.backGroundImageY-screen.get_height()))
        #resim dönüşünde x değerini sıfırlıyorus
        if screen.get_height() == self.backGroundImageY:
           self.backGroundImageY=0





    def drawCar(self,screen):
        self.car.draw(screen)
    
    def drawTargets(self,screen):
        for target in self.targets:
            exposed=target.draw(screen)
            if exposed:
                self.targets.remove(target)
                if self.car.exposed:
                    pygame.event.post(self.car.exposedEvent)
                    self.finish(screen)
                    
            else:
                if target.rectangle.colliderect(self.car.rectangle):
                    if not target.exposed:
                        target.expose()
                        print("cakıştı")
                        self.car.expose()
                    

            

            
    def draw(self,screen):
        self.drawBackGround(screen)
        self.drawCar(screen)

        self.drawTargets(screen)