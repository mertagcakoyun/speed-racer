                    ##  CHAPTER

import pygame
import sys
import math
import random
from  threading import Timer
from TargetOne import *
from Car import Car
from pTimer import  pTimer

pygame.font.init()
font = pygame.font.Font(None, 38)
green=(16, 137, 2)
orange=(255, 179, 15)
red=(255, 10, 10)
gray=(181, 183, 188)
black=(0,0,0)
colors=[green,orange,red]
score_font = pygame.font.Font(None, 28)

class ChapterOne():
    def __init__(self,screen):
        self.name="Let's Start"
        self.car= Car(screen)
        self.target=TargetOne(screen)
        self.targets=[]
        self.backGroundImage=pygame.transform.scale(pygame.image.load("images/png/background-1.png"),(screen.get_width(), screen.get_height()))
        self.backGroundImageY=0
        self.backGroundImageX = 0
        self.screen= screen
        self.speed=1
        self.endFlag=False

        #2 saniyede bir hedef üretilmeli

        self.pgenerateTargetTimer=pTimer(2.5,self.generateTarget,screen)
        self.finishEvent=pygame.event.Event(pygame.USEREVENT, attr1='finishEvent')
        self.complatedEvent=pygame.event.Event(pygame.USEREVENT, attr1='GameComplated')
        self.gasUseTimer = pTimer(1, self.car.useGas, screen)
    def start(self,screen):
        self.gasUseTimer.start()
        self.pgenerateTargetTimer.start()

    def finish(self,screen):
        self.pgenerateTargetTimer.stop()
        self.gasUseTimer.stop()
        pygame.event.post(self.finishEvent)
        print("CIKILDI")
    def complated(self,screen):
        self.pgenerateTargetTimer.stop()
        self.gasUseTimer.stop()
        pygame.event.post(self.complatedEvent)

    def generateTarget(self,arguments):
        targetChoice= random.randint(0,8)
        print(str(targetChoice))
        newTarget = None

        if targetChoice == 0 or targetChoice == 4 or targetChoice == 7:
            newTarget= TargetOne(arguments[0])
        elif targetChoice == 1 or targetChoice == 5 or targetChoice == 8:
            newTarget = PoliceTarget(TargetOne(arguments[0]))
        elif targetChoice ==2 or targetChoice == 6 :
            newTarget = GreenTarget(TargetOne(arguments[0]))
        elif targetChoice==3:
            newTarget = FuelTarget(TargetOne(arguments[0]))


        self.targets.append(newTarget)



    def drawGas(self,screen,gasValue):
        color=None
        if gasValue>60:
           color=green
        elif gasValue<35 :
            color=red
        elif gasValue<=60 and gasValue>=35:
            color=orange
        else:
            return False
        pygame.draw.rect(screen, gray,
        pygame.Rect(screen.get_width() - 20, screen.get_height() - 300 + 10, 10,
                                     300))
        pygame.draw.rect(screen, color, pygame.Rect(screen.get_width()-20, screen.get_height()-(gasValue*3)+10, 10, gasValue*3))
        gasText = score_font.render("GAS", 1, black)
        screen.blit(gasText, (757, 290))
        return True

    def drawBackGround(self, screen):
        screen.blit(self.backGroundImage,(0,self.backGroundImageY))
        self.backGroundImageY=self.backGroundImageY+4 #self.speed
        screen.blit(self.backGroundImage,(0,self.backGroundImageY-screen.get_height()))
        #resim dönüşünde x değerini sıfırlıyorus
        if screen.get_height() == self.backGroundImageY:
           self.backGroundImageY=0



    def drawCar(self,screen):
        self.car.draw(screen)
    
    def drawTargets(self,screen):
        for target in self.targets:
            if type(target) != FuelTarget:
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
            else:
                exposed = target.draw(screen)
                # target.draw(screen)
                if not self.car.exposed:


                    if target.rectangle.colliderect(self.car.rectangle):
                        if not target.exposed:
                            self.targets.remove(target)
                            if self.car.gasValue<75:
                                self.car.gasValue+= 25
                            else:
                                self.car.gasValue=100
                            target.expose()

    def draw(self,screen):
        self.drawBackGround(screen)
        self.drawCar(screen)
        self.drawGas(screen, self.car.gasValue)
        self.drawTargets(screen)

    def drawGameTime(self,gameTime,screen):
        color=black
        game_time = font.render("Time:", 1, pygame.Color("black"))
        if gameTime/1000>50:
            color=red

        game_time_counter = score_font.render(str(gameTime / 1000), 1, color)
        screen.blit(game_time, (10, 10))
        screen.blit(game_time_counter, (82, 14))

        self.drawScore(gameTime,screen)
        if gameTime/1000>60:
            self.finish(screen)
        else:
            if self.updateScore()>130:
                self.complated(screen)

    def drawScore(self,gameTime,screen):

        score=font.render("Score:", 1,black)
        score_counter=score_font.render(str(self.updateScore()), 1, red)
        screen.blit(score, (685, 10))
        screen.blit(score_counter, (765, 14))


    def updateScore(self):
        score=0
        for target in self.targets:
            if target.rectangle[1]>600:
                score+=1
        return score*10
    def carInRoad(self,screen):

        if self.car.rectangle[0] > 140 and self.car.rectangle[0] < 640:# sinir kontrolu
            return True
        else:
            self.finish(screen)
    def isGasExist(self,screen):
        if self.car.gasValue < 0:
            self.finish(screen)

