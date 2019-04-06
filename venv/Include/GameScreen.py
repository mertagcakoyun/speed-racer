
import pygame
import sys
import math
import random
pygame.init()

gameDisplay_width=1000
gameDisplay_height=800
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Speed Racer')

crashed = False

clock = pygame.time.Clock()
backGroundImage=pygame.image.load("images/png/road.png")
backGroundImage= pygame.transform.scale(backGroundImage, (gameDisplay.get_width(), gameDisplay.get_height()))


pygame.quit()
quit()

