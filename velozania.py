# import and Initialization
import pygame, sys
from pygame.locals import *
from random import randint
from veloMenu import *

pygame.init()

# Display
SIZE_WIDTH = 800
SIZE_HEIGHT = 600
SIZE = (SIZE_WIDTH, SIZE_HEIGHT)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
STREET = (150, 150, 150)

screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE)

pygame.display.set_caption('VeloZania')


# Entities
# Text Renderer


# der Radler
class Cycler(pygame.sprite.Sprite):
    # Startkoordinaten
    x_cord = 40
    y_cord = 350
    width = 100
    height = 70

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/Cycler.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.rect.left = self.x_cord
        self.rect.top = self.y_cord

    def update(self):
        self.rect = (self.x_cord, self.y_cord)


class Auto(pygame.sprite.Sprite):
    # Startkoordinaten
    x_cord = 900
    y_cord = randint(100, 400)  # Zufallposi für Position auf der rechten Spur

    def __init__(self, bild, width, height, speed):
        self.pic = bild
        self.width = width
        self.height = height
        self.speed = speed

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.pic)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.flip(self.image, 90, 0)
        self.rect = self.image.get_rect()

        self.rect.left = self.x_cord
        self.rect.top = self.y_cord

    def bewegung(self):
        if self.x_cord > -300:
            self.x_cord -= self.speed  # geschwindigkeit des Autos / für Test eignet sich 30

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
        # Ist objekt ein Bildelement für den Rand
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

    def bewegung(self):
        if self.x_cord > -200:
            self.x_cord -= 2

    def update(self):
        self.rect = (self.x_cord, self.y_cord)


# Hintergrund
class Background(pygame.sprite.Sprite):
    def __init__(self):
        self.bg_weiss = pygame.draw.rect(screen, WHITE, (0, 0, 800, 600))
        self.bg_gruen = pygame.draw.rect(screen, GREEN, (0, 50, 800, 500))
        self.bg_grau = pygame.draw.rect(screen, STREET, (0, 150, 800, 300))


# Funktion zum loopen der AutoObjekte
def loopenAuto(objTupel):
    index = randint(0, (len(objTupel) - 1))
    if objTupel[index].x_cord <= -100:
        objTupel[index].y_cord = randint(250, 400)
        objTupel[index].x_cord = randint(800, 1200)


# Funktion zum loopen der HintergrundElemente
def loopenBackgroundElemente(objTupel):
    index = randint(0, (len(objTupel) - 1))
    if objTupel[index].x_cord <= -200:
        updown = randint(0, 1)
        if updown == 0:
            objTupel[index].y_cord = randint(0, 50)
        elif updown == 1:
            objTupel[index].y_cord = randint(450, 500)
        objTupel[index].x_cord = randint(800, 1000)


# Init des Radlers und Autos

# Grundeinheiten des AutoElements, darauf beziehen sich alle anderen AutoElemente
AUTO_WIDTH = 100
AUTO_HEIGHT = 70

car = Auto('images/redcar.png', AUTO_WIDTH, AUTO_HEIGHT, 7)
lkw = Auto('images/truck.png', AUTO_WIDTH, AUTO_HEIGHT, 6)
bus = Auto('images/english-bus.png', (AUTO_WIDTH * 2), AUTO_HEIGHT, 5)

cycler = Cycler()
bridge = BackgroundElemente('images/bruecke.png', 400, 100, False)
house_1 = BackgroundElemente('images/cartoon-houses-clipart-631895.png', 100, 100, True)
baum_1 = BackgroundElemente('images/cottonwood.png', 100, 100, True)
house_2 = BackgroundElemente('images/building-houses.png', 150, 100, True)

sprite_group = pygame.sprite.Group()
sprite_group.add(car)
sprite_group.add(cycler)
sprite_group.add(lkw)
sprite_group.add(bus)
sprite_group.add(bridge)
sprite_group.add(house_1)
sprite_group.add(baum_1)
sprite_group.add(house_2)

# Action --> Alter

# Assign Variables

# noch ungenutzt
pygame.time.set_timer(USEREVENT, 200)
keepGoing = True
# Leben
lifePoints = 3

# Loop
while keepGoing:

    # Timer
    FPS = 30
    fpsClock = pygame.time.Clock()
    time = pygame.time.get_ticks()
    fpsClock.tick(FPS)

    # Event Handling
    ## Startmenü (kleiner Bug -> zum Anfang alle Gebäude auf einem Haufen // werde noch fixen
    main_menu(screen, SIZE_WIDTH)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Tupel an AutoObjekten:
        autoObj = (car, lkw, bus)
        if ((time % 8) == 0):
            loopenAuto(autoObj)

        # Tupel für BackgroundElemente
        backgroundObj = (house_1, baum_1, house_2)
        if ((time % 12) == 0):
            loopenBackgroundElemente(backgroundObj)

    car.bewegung()
    lkw.bewegung()
    bus.bewegung()
    bridge.bewegung()
    house_1.bewegung()
    baum_1.bewegung()
    house_2.bewegung()
    # refresh des Hintergrunds
    bg = Background()

    # Bewegen des Radlers
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if Cycler.y_cord >= 100:
            Cycler.y_cord -= 3
    elif keys[pygame.K_DOWN]:
        if Cycler.y_cord <= 380:
            Cycler.y_cord += 3

    # Kollision mit Radler
    # Bildrand wegschneiden
    PIC_FRAME = 20
    # carRectVolumen = (car.width, car.height)
    # print (car.rect)
    # Rect für Auto Objecte
    rectCarCollision = pygame.Rect(car.x_cord, (car.y_cord), car.width, (car.height))
    rectBusCollision = pygame.Rect(bus.x_cord, (bus.y_cord), bus.width, (bus.height))
    rectLKWCollision = pygame.Rect(lkw.x_cord, (lkw.y_cord), lkw.width, (lkw.height))

    # Rect Tupel für Auto Objects
    rectAutoCollision = (rectBusCollision, rectLKWCollision, rectCarCollision)

    # Rect für Cycler
    rectCyclerCollison = pygame.Rect(cycler.x_cord, (cycler.y_cord - PIC_FRAME), cycler.width,
                                     (cycler.height - PIC_FRAME))

    for i in rectAutoCollision:
        if rectCyclerCollison.colliderect(i):
            print('collision')

    # Zählt Anzahl um zuverhinder, dass in der AutoObjekt sich selbst als kollidierend ansieht
    count = -1
    for j in rectAutoCollision:
        # tempDeleteAutoCollision =
        count += 1
        autoIndex = j.collidelist(rectAutoCollision)
        if (count != autoIndex):
            if (count == 0):
                bus.y_cord += 10
                break
            elif (count == 1):
                lkw.y_cord += 10
                break
            elif (count == 2):
                car.y_cord -= 10
                break

    sprite_group.update()
    sprite_group.draw(screen)

    # Redisplay
    pygame.display.update()
