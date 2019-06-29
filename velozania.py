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
SKYBLUE = (168, 255, 255)
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
        self.bg_weiss = pygame.draw.rect(screen, SKYBLUE, (0, 0, 800, 600))
        self.bg_gruen = pygame.draw.rect(screen, GREEN, (0, 80, 800, 520))
        self.bg_grau = pygame.draw.rect(screen, STREET, (0, 150, 800, 300))




# Funktion zum loopen der AutoObjekte
def loopen_Auto(objTupel):
    index = randint(0, (len(objTupel) - 1))
    if objTupel[index].x_cord <= -100:
        objTupel[index].y_cord = randint(200, 400)
        objTupel[index].x_cord = randint(800, 1200)


# Funktion zum loopen der HintergrundElemente
def loopen_BackgroundElemente(objTupel):
    index = randint(0, (len(objTupel) - 1))
    if objTupel[index].x_cord <= -200:
        updown = randint(0, 1)
        if updown == 0:
            objTupel[index].y_cord = randint(0, 50)
        elif updown == 1:
            objTupel[index].y_cord = randint(450, 500)
        objTupel[index].x_cord = randint(800, 1000)

def loopen_Energie(objTupel):
    index = randint(0, (len(objTupel) - 1))
    if objTupel[index].x_cord <= -100:
        objTupel[index].y_cord = randint(200, 400)
        objTupel[index].x_cord = randint(800, 1200)


def aktionen_Bei_Kollision():
    title = text_format("- 1 Leben", font, 70, BLACK)
    title_rect = title.get_rect()
    screen.blit(title, (800 / 2 - (title_rect[2] / 2), 80))

def aktion_bei_Energie():
    title = text_format("+ 10 Punkte", font, 70, BLACK)
    title_rect = title.get_rect()
    screen.blit(title, (800 / 2 - (title_rect[2] / 2), 80))


def show_Leben(lifePoints):
    leben = 'leben ' + str(lifePoints)
    title = text_format(leben, font, 20, BLACK)
    title_rect = title.get_rect()
    screen.blit(title, (700 - (title_rect[2] / 2), 50))


def show_Score(score):
    score_text = 'score ' + str(score)
    title = text_format(score_text, font, 20, BLACK)
    title_rect = title.get_rect()
    screen.blit(title, (700 - (title_rect[2] / 2), 25))


def show_Level(level):
    score_text = 'level ' + str(level)
    title = text_format(score_text, font, 20, BLACK)
    title_rect = title.get_rect()
    screen.blit(title, (100 , 25))


FPS = 30
fpsClock = pygame.time.Clock()
time = pygame.time.get_ticks()
fpsClock.tick(FPS)

tempscore = 1
temptime = 0
anzeigedauer = 0
auto_kollision = False
collision = False
gameover = False
keepGoing = True
lifePoints = 3
count = 1
energie_kollision = False
weitere_Runde = False
level = 1


main_menu(screen, SIZE_WIDTH)

cycler = Cycler(get_Radtyp())


# Grundeinheiten des AutoElements, darauf beziehen sich alle anderen AutoElemente
AUTO_WIDTH = 100
AUTO_HEIGHT = 70

# Autoobjektte intialisieren
car = Auto('images/redcar.png', AUTO_WIDTH, AUTO_HEIGHT, 7, 90)
lkw = Auto('images/truck.png', AUTO_WIDTH, AUTO_HEIGHT, 6, 90)
bus = Auto('images/english-bus.png', (AUTO_WIDTH * 2), AUTO_HEIGHT, 5, 90)
police = Auto('images/blue-police-car.png', AUTO_WIDTH, AUTO_HEIGHT, 9, 0)

# Hintergrundelemente initialisieren
bridge = BackgroundElemente('images/bruecke.png', 400, 100, False)
house_1 = BackgroundElemente('images/cartoon-houses-clipart-631895.png', 100, 100, True)
baum_1 = BackgroundElemente('images/cottonwood.png', 100, 100, True)
house_2 = BackgroundElemente('images/building-houses.png', 150, 100, True)
cow = BackgroundElemente('images/cow.png', 70, 50, True)
baum_2 = BackgroundElemente('images/forest.png', 150, 150, True)

# Energieelemente intialisieren
banane = Energie('images/banana.png', 30, 30, 2000)
wasser = Energie('images/bottle.png', 30, 30, 3000)

sprite_group = pygame.sprite.Group()
sprite_group.add(banane)
sprite_group.add(wasser)
sprite_group.add(car)
sprite_group.add(cycler)
sprite_group.add(lkw)
sprite_group.add(bus)
sprite_group.add(police)
sprite_group.add(cow)
sprite_group.add(bridge)
sprite_group.add(house_1)
sprite_group.add(baum_1)
sprite_group.add(house_2)
sprite_group.add(baum_2)

# noch ungenutzt
pygame.time.set_timer(USEREVENT + 1, 200)

# Soundelemte
crash_sound = pygame.mixer.Sound("sounds/car-crash.wav")
energie_sound = pygame.mixer.Sound("sounds/energie.wav")

# Musik
musik = pygame.mixer.music
#musik an und aus
if (is_music()):

    musik.load('sounds/GameMusik.mp3')
    musik.play(-1)

# Loop
while keepGoing:

    # Prüft ob weitere Runde stattfindet um Änderungen des Nutzer in der Radtyp Einstellung in musik on/off zu übernehmen
    if weitere_Runde:
        sprite_group.remove(cycler)
        cycler = Cycler(get_Radtyp())
        sprite_group.add(cycler)
        if (is_music()):
            musik = pygame.mixer.music
            musik.load('sounds/GameMusik.mp3')
            musik.play(-1)
        else:
            musik.pause()
        weitere_Runde = False

    #Score
    if temptime < time:
        temptime = time
        tempscore += 1 * cycler_speed / 10

    # Timer
    FPS = 30
    fpsClock = pygame.time.Clock()
    time = pygame.time.get_ticks()
    fpsClock.tick(FPS)

    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Tupel an AutoObjekten:
        autoObj = (car, lkw, bus, police)
        if ((time % (9-level)) == 0):
            loopen_Auto(autoObj)

        # Tupel für BackgroundElemente
        backgroundObj = (house_1, baum_1, house_2, cow)
        if ((time % 12) == 0):
            loopen_BackgroundElemente(backgroundObj)

        energieObj = (banane, wasser)
        if ((time % 20) == 0):
            loopen_Energie(energieObj)

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
    banane.bewegen(cycler_speed)
    wasser.bewegen(cycler_speed)
    # refresh des Hintergrunds
    bg = Background()

    # Bewegen des Radlers
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if Cycler.y_cord >= 115:
            Cycler.y_cord -= 3
    elif keys[pygame.K_DOWN]:
        if Cycler.y_cord <= 395:
            Cycler.y_cord += 3

    # Kollision mit Radler
    # Bildrand wegschneiden bei radler
    PIC_FRAME = 20
    # Rect für Auto Objecte
    rectCarCollision = pygame.Rect(car.x_cord, (car.y_cord), car.width, (car.height))
    rectBusCollision = pygame.Rect(bus.x_cord, (bus.y_cord), bus.width, (bus.height))
    rectLKWCollision = pygame.Rect(lkw.x_cord, (lkw.y_cord), lkw.width, (lkw.height))
    rectPoliceCollison = pygame.Rect(police.x_cord, police.y_cord, police.width, police.height)

    # Rect Tupel für Auto Objects
    rectAutoCollision = (rectBusCollision, rectLKWCollision, rectCarCollision, rectPoliceCollison)

    rectBananaCollision = pygame.Rect(banane.x_cord, banane.y_cord, banane.width, banane.height)
    rectWaterCollision = pygame.Rect(wasser.x_cord, wasser.y_cord, wasser.width, wasser.height)

    rectEnergieCollision = (rectBananaCollision, rectWaterCollision)

    # Rect für Cycler
    rectCyclerCollison = pygame.Rect(cycler.x_cord - PIC_FRAME, (cycler.y_cord + PIC_FRAME), cycler.width - PIC_FRAME,
                                     (cycler.height - PIC_FRAME * 2))

    #checkt ob Radler mit Autoobjekt collidiert
    for i in rectAutoCollision:
        if rectCyclerCollison.colliderect(i):
            lifePoints -= 1
            for j in autoObj:
                j.x_cord += 600
                auto_kollision = True
                anzeigedauer = tempscore + 4
                if(is_sound()):
                    crash_sound.play()
            if (lifePoints == 0):
                lifePoints = 3
                gameover = True
                gameover_menu(int(tempscore), screen, gameover)
                tempscore = 0
                weitere_Runde =True
                main_menu(screen, SIZE_WIDTH)
                auto_kollision = False

    # Anzeige bei Lebenverlust
    if auto_kollision == True:
        if tempscore <= anzeigedauer:
            aktionen_Bei_Kollision()
        else:
            auto_kollision = False

    # Zählt Anzahl um zuverhinder, dass in der AutoObjekt sich selbst als kollidierend ansieht
    count = -1
    # Koordiniert das vorbeifahren der Audioobjekte mit anderen Autoobjekten
    for j in rectAutoCollision:
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

    #Einsammeln Banane
    if rectCyclerCollison.colliderect(rectBananaCollision):
            tempscore += 10
            energie_kollision = True
            anzeigedauer = tempscore + 4
            if(is_sound()):
                energie_sound.play()
            banane.x_cord = -100

    #Einsammeln Wasserflasche
    if rectCyclerCollison.colliderect(rectWaterCollision):
            tempscore += 10
            energie_kollision = True
            anzeigedauer = tempscore + 4
            if(is_sound()):
                energie_sound.play()
            wasser.x_cord = -100

    #Anzeige Pluspunkte bei Energie Objekt eingesammlt
    if energie_kollision == True:
        if tempscore <= anzeigedauer:
            aktion_bei_Energie()
        else:
            energie_kollision = False


    # Levelanzeige, weiter ausbaubar auf noch mehr Level, ein höheres Level führ zu mehr Autoobjekten auf der Strasse
    if tempscore<100:
        level = 1
    if tempscore>100:
        level = 2
    if tempscore>300:
        level = 3

    #Anzeigen Aufruf für verschiedene Elemente
    show_Leben(lifePoints)
    show_Score(int(tempscore))
    show_Level(level)
    sprite_group.update()
    sprite_group.draw(screen)

    # Redisplay
    pygame.display.flip()


