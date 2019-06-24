# import and Initialization
import pygame, sys
from pygame.locals import *
from random import randint




# der Radler
class Cycler(pygame.sprite.Sprite):
    # Startkoordinaten
    x_cord = 40
    y_cord = 350
    width = 70
    height = 50

    def __init__(self, bild):
        self.bild = bild
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.bild)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.rect.left = self.x_cord
        self.rect.top = self.y_cord

    def update(self):
        self.rect = (self.x_cord, self.y_cord)

class Auto(pygame.sprite.Sprite):
    # Startkoordinaten
    x_cord = randint(900, 3000)
    y_cord = randint(200, 400)

    def __init__(self, bild, width, height, speed, angel):
        self.pic = bild
        self.width = width
        self.height = height
        self.speed = speed
        self.angel = angel

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.pic)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.flip(self.image, self.angel, 0)
        self.rect = self.image.get_rect()

        self.rect.left = self.x_cord
        self.rect.top = self.y_cord


    def bewegen(self, cycler_speed):
        if self.x_cord > -300:
            self.x_cord -= (self.speed + cycler_speed) # geschwindigkeit des Autos / für Test eignet sich 30

    def update(self):
        self.rect = (self.x_cord, self.y_cord)


class BackgroundElemente(pygame.sprite.Sprite):
    x_cord = 700
    y_cord = 100
    angel = 90

    def __init__(self, bild, height, width, isRand):
        self.bild = bild
        self.width = width
        self.height = height
        #Ist objekt ein Bildelement für den Rand
        self.isRand = isRand

        if (self.isRand):
           self.y_cord = randint(450, 500)
           self.x_cord = randint(0, 800)
           self.angel = 360

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.bild)
        self.image = pygame.transform.scale(self.image, (self.height, self.width))
        self.image = pygame.transform.rotate(self.image, self.angel)
        self.rect = self.image.get_rect()

        self.rect.left = self.x_cord
        self.rect.top = self.y_cord


    def bewegen(self, cycler_speed):
        if self.x_cord > -200:
            self.x_cord -= (2+cycler_speed)

    def update(self):
        self.rect = (self.x_cord, self.y_cord)
