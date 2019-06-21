# import and Initialization
import pygame, sys
from pygame.locals import *
from random import randint
from gameobjekte import *
from veloMenu import *
from time import *

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

class Cycler(pygame.sprite.Sprite):
    # Startkoordinaten + Groesse
    x_cord = 40
    y_cord = 350

    width = 70
    height = 50

    # Inizialisierung des Radlers
    ## radwahl wird von veloMenu übergeben // bisher ändert sich bloss das Aussehen des Rads
    ### vielleicht sollten wir die Geschwindigkeit hier mitemplementieren
    def __init__(self, radwahl):
        global cycler_speed
        pygame.sprite.Sprite.__init__(self)
        if radwahl == "dreirad":
            self.image = pygame.image.load('images/dreirad.png')
            cycler_speed = 1
        elif radwahl == "stadtrad":
            self.image = pygame.image.load('images/normrad.png')
            cycler_speed = 2
        else:
            self.image = pygame.image.load('images/rennrad.png')
            cycler_speed = 3
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.rect.left = self.x_cord
        self.rect.top = self.y_cord

    def update(self):
        self.rect = (self.x_cord, self.y_cord)


# Hintergrund
class Background(pygame.sprite.Sprite):
    def __init__(self):
        self.bg_weiss = pygame.draw.rect(screen, WHITE, (0, 0, 800, 600))
        self.bg_gruen = pygame.draw.rect(screen, GREEN, (0, 100, 800, 400))
        self.bg_grau = pygame.draw.rect(screen, STREET, (0, 150, 800, 300))


# Funktion zum loopen der AutoObjekte
def loopenAuto(objTupel):
    index = randint(0, (len(objTupel) - 1))
    if objTupel[index].x_cord <= -100:
        objTupel[index].y_cord = randint(200, 400)
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


def aktionenBeiKollision():

    title = text_format("- 1 Leben", font, 70, BLACK)
    title_rect = title.get_rect()
    screen.blit(title, (800 / 2 - (title_rect[2] / 2), 80))


def showLeben(lifePoints):
    print(lifePoints)
    leben = 'leben ' + str(lifePoints)
    title = text_format(leben, font, 20, BLACK)
    title_rect = title.get_rect()
    screen.blit(title, (700 - (title_rect[2] / 2), 50))


def showScore(score):
    score_text = 'score ' + str(score)
    title = text_format(score_text, font, 20, BLACK)
    title_rect = title.get_rect()
    screen.blit(title, (700 - (title_rect[2] / 2), 25))


FPS = 30
fpsClock = pygame.time.Clock()
time = pygame.time.get_ticks()
fpsClock.tick(FPS)


cycler = Cycler(main_menu(screen, SIZE_WIDTH))

# Grundeinheiten des AutoElements, darauf beziehen sich alle anderen AutoElemente
AUTO_WIDTH = 100
AUTO_HEIGHT = 70

car = Auto('images/redcar.png', AUTO_WIDTH, AUTO_HEIGHT, 7, 90)
lkw = Auto('images/truck.png', AUTO_WIDTH, AUTO_HEIGHT, 6, 90)
bus = Auto('images/english-bus.png', (AUTO_WIDTH * 2), AUTO_HEIGHT, 5, 90)
police = Auto('images/blue-police-car.png', AUTO_WIDTH, AUTO_HEIGHT, 9, 0)

# cycler = Cycler('images/Cycler.png')
# cycler_speed = 3
bridge = BackgroundElemente('images/bruecke.png', 400, 100, False)
house_1 = BackgroundElemente('images/cartoon-houses-clipart-631895.png', 100, 100, True)
baum_1 = BackgroundElemente('images/cottonwood.png', 100, 100, True)
house_2 = BackgroundElemente('images/building-houses.png', 150, 100, True)
cow = BackgroundElemente('images/cow.png', 70, 50, True)
baum_2 = BackgroundElemente('images/forest.png', 150, 150, True)

sprite_group = pygame.sprite.Group()
sprite_group.add(car)
sprite_group.add(cycler)
sprite_group.add(lkw)
sprite_group.add(bus)
sprite_group.add(police)
sprite_group.add(bridge)
sprite_group.add(house_1)
sprite_group.add(baum_1)
sprite_group.add(house_2)
sprite_group.add(cow)
sprite_group.add(baum_2)

# Action --> Alter

# Assign Variables

# noch ungenutzt
pygame.time.set_timer(USEREVENT + 1, 200)

collision = False
gameover = False
keepGoing = True
lifePoints = 3

#musik an und aus
if (is_music()):
    musik = pygame.mixer.music
    musik.load('sounds/GameMusik.mp3')
    musik.play()

# game Musik
#pygame.mixer.music.load('Sounds/GameMusik.wav')
#pygame.mixer.music.play()


# Loop
while keepGoing:


    # Timer
    FPS = 30
    fpsClock = pygame.time.Clock()
    time = pygame.time.get_ticks()
    fpsClock.tick(FPS)
    #Repeat musik
    if (is_music() and ((musik.get_busy())==False)):
       musik.play()



    #game_music.
    # main_menu()
    # cycler_menu()

    score = int((time / 100) * cycler_speed)

    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Tupel an AutoObjekten:
        autoObj = (car, lkw, bus, police)
        if ((time % 8) == 0):
            loopenAuto(autoObj)

        # Tupel für BackgroundElemente
        backgroundObj = (house_1, baum_1, house_2, cow)
        if ((time % 12) == 0):
            loopenBackgroundElemente(backgroundObj)

    print(cycler_speed)
    car.bewegen(cycler_speed)
    lkw.bewegen(cycler_speed)
    bus.bewegen(cycler_speed)
    police.bewegen(cycler_speed)
    bridge.bewegen(cycler_speed)
    house_1.bewegen(cycler_speed)
    baum_1.bewegen(cycler_speed)
    house_2.bewegen(cycler_speed)
    cow.bewegen(cycler_speed)
    baum_2.bewegen(cycler_speed)
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
    rectPoliceCollison = pygame.Rect(police.x_cord, police.y_cord, police.width, police.height)

    # Rect Tupel für Auto Objects
    rectAutoCollision = (rectBusCollision, rectLKWCollision, rectCarCollision, rectPoliceCollison)

    # Rect für Cycler
    rectCyclerCollison = pygame.Rect(cycler.x_cord - PIC_FRAME, (cycler.y_cord + PIC_FRAME), cycler.width - PIC_FRAME,
                                     (cycler.height - PIC_FRAME * 2))

    for i in rectAutoCollision:
        if rectCyclerCollison.colliderect(i):
            print('collision')
            # Cycler.y_cord += 50
            lifePoints -= 1
            for j in autoObj:
                j.x_cord += 600
            aktionenBeiKollision()
            if (lifePoints == 0):
                lifePoints = 3
                gameover = True
                gameover_menu(score, screen, gameover)
                main_menu(screen, SIZE_WIDTH)


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
            elif (count == 3):
                police.y_cord -= 10
                break

    showLeben(lifePoints)
    showScore(score)
    sprite_group.update()
    sprite_group.draw(screen)

    # Redisplay
    pygame.display.flip()