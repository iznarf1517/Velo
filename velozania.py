# import and Initialization
import pygame, sys
from pygame.locals import *
from random import randint
from gameobjekte import *
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
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# startmenu
# Game Fonts
font = "Wozcott.otf"



def main_menu():
    global menu
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"


                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        print("Start")
                        menu = False
                    if selected == "quit":
                        pygame.quit()
                        quit()


        # Main Menu UI
        screen.fill(GREEN)
        title = text_format("VeloZania", font, 70, BLACK)
        if selected == "start":
            text_start = text_format("START", font, 50, WHITE)
        else:
            text_start = text_format("START", font, 50, BLACK)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 50, WHITE)
        else:
            text_quit = text_format("QUIT", font, 50, BLACK)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (800 / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (SIZE_WIDTH / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_quit, (800 / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
        fpsClock.tick(FPS)
        pygame.display.set_caption("VeloZonia")


def cycler_menu():
    global cycler_menu_is
    global cycler_speed
    global cycler
    selected = "dreirad"

    while cycler_menu_is:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected = "dreirad"
                elif event.key == pygame.K_2:
                    selected = "normrad"
                elif event.key == pygame.K_3:
                    selected = "rennrad"


                if event.key == pygame.K_RETURN:
                    if selected == "dreirad":
                        cycler_speed = 1
                        cycler_menu_is = False
                        cycler = Cycler('images/dreirad.png')
                    if selected == "normrad":
                        cycler_speed = 3
                        cycler_menu_is = False
                        cycler = Cycler('images/normrad.png')
                    if selected == "rennrad":
                        cycler_speed = 5
                        cycler_menu_is = False
                        cycler = Cycler('images/rennrad.png')


        # Main Menu UI
        screen.fill(GREEN)
        title = text_format("VeloZania", font, 70, BLACK)
        if selected == "dreirad":
            text_dreirad = text_format("WAEHLE 1 FUER DREIRAD", font, 50, WHITE)
        else:
            text_dreirad = text_format("WAEHLE 1 FUER DREIRAD", font, 50, BLACK)
        if selected == "normrad":
            text_normrad = text_format("WAEHLE 2 FUER STADTRAD", font, 50, WHITE)
        else:
            text_normrad = text_format("WAEHLE 2 FUER STADTRAD", font, 50, BLACK)
        if selected == "rennrad":
            text_rennrad = text_format("WAEHLE 3 FUER RENNRAD", font, 50, WHITE)
        else:
            text_rennrad= text_format("WAEHLE 3 FUER RENNRAD", font, 50, BLACK)


        title_rect = title.get_rect()
        dreirad_rect = text_dreirad.get_rect()
        normrad_rect = text_normrad.get_rect()
        rennrad_rect = text_rennrad.get_rect()

        # Main Menu Text
        screen.blit(title, (800 / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_dreirad, (SIZE_WIDTH / 2 - (dreirad_rect[2] / 2), 300))
        screen.blit(text_normrad, (800 / 2 - (normrad_rect[2] / 2), 360))
        screen.blit(text_rennrad, (800 / 2 - (rennrad_rect[2] / 2), 420))
        pygame.display.update()
        fpsClock.tick(FPS)
        pygame.display.set_caption("VeloZonia")




def gameover_menu(score):
    global gameover
    global menu
    selected = "start"

    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        print("Start")
                        gameover = False
                        menu = True
                        main_menu()
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Collison Menu UI
        screen.fill(GREEN)

        title = text_format("GAME OVER!", font, 70, BLACK)
        score_text = text_format('DEIN SCORE '+str(score), font, 50, BLACK)
        if selected == "start":
            text_start = text_format("ZURUECK ZUM START", font, 50, WHITE)
        else:
            text_start = text_format("ZURUECK ZUM START", font, 50, BLACK)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 50, WHITE)
        else:
            text_quit = text_format("QUIT", font, 50, BLACK)

        title_rect = title.get_rect()
        score_rect = score_text.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (800 / 2 - (title_rect[2] / 2), 80))
        screen.blit(score_text, (SIZE_WIDTH / 2 - (score_rect[2] / 2), 180))
        screen.blit(text_start, (800 / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_quit, (800 / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
        fpsClock.tick(FPS)
        pygame.display.set_caption("VeloZonia")


# Hintergrund
class Background(pygame.sprite.Sprite):
    def __init__(self):

        self.bg_weiss = pygame.draw.rect(screen, WHITE, (0, 0, 800, 600))
        self.bg_gruen = pygame.draw.rect(screen, GREEN, (0, 100, 800, 400))
        self.bg_grau = pygame.draw.rect(screen, STREET, (0, 150, 800, 300))


#Funktion zum loopen der AutoObjekte
def loopenAuto(objTupel):
    index = randint(0, (len(objTupel)-1))
    if objTupel[index].x_cord <= -100:
        objTupel[index].y_cord = randint(200, 400)
        objTupel[index].x_cord = randint(800, 1200)

#Funktion zum loopen der HintergrundElemente
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
    leben = 'leben '+str(lifePoints)
    title = text_format(leben, font, 20, BLACK)
    title_rect = title.get_rect()
    screen.blit(title, (700 - (title_rect[2] / 2), 50))

def showScore(score):

    score_text = 'score '+ str(score)
    title = text_format(score_text, font, 20, BLACK)
    title_rect = title.get_rect()
    screen.blit(title, (700 - (title_rect[2] / 2), 25))


FPS = 30
fpsClock = pygame.time.Clock()
time = pygame.time.get_ticks()
fpsClock.tick(FPS)

menu = True
cycler_menu_is = True
cycler_speed = 1
main_menu()
cycler_menu()


# Init des Radlers und Autos

# Grundeinheiten des AutoElements, darauf beziehen sich alle anderen AutoElemente
AUTO_WIDTH = 100
AUTO_HEIGHT = 70

car = Auto('images/redcar.png', AUTO_WIDTH, AUTO_HEIGHT, 7, 90)
lkw = Auto('images/truck.png', AUTO_WIDTH, AUTO_HEIGHT, 6, 90)
bus = Auto('images/english-bus.png', (AUTO_WIDTH*2), AUTO_HEIGHT, 5, 90)
police = Auto('images/blue-police-car.png', AUTO_WIDTH, AUTO_HEIGHT, 9, 0)

#cycler = Cycler('images/Cycler.png')
#cycler_speed = 3
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
pygame.time.set_timer(USEREVENT+1, 200)

collision = False
gameover = False
keepGoing = True
lifePoints = 3
#cycler_speed = 1


# Loop
while keepGoing:

    # Timer
    FPS = 30
    fpsClock = pygame.time.Clock()
    time = pygame.time.get_ticks()
    fpsClock.tick(FPS)
    #main_menu()
    #cycler_menu()
    score = int((time / 100) * cycler_speed)



    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Tupel an AutoObjekten:
        autoObj = (car, lkw, bus, police)
        if ((time%8) == 0):
            loopenAuto(autoObj)

        #Tupel für BackgroundElemente
        backgroundObj = (house_1, baum_1, house_2, cow)
        if((time%12)==0):
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
    #print (car.rect)
    #Rect für Auto Objecte
    rectCarCollision = pygame.Rect(car.x_cord, (car.y_cord), car.width, (car.height))
    rectBusCollision = pygame.Rect(bus.x_cord, (bus.y_cord), bus.width, (bus.height))
    rectLKWCollision = pygame.Rect(lkw.x_cord, (lkw.y_cord), lkw.width, (lkw.height))
    rectPoliceCollison = pygame.Rect(police.x_cord, police.y_cord, police.width, police.height)

    #Rect Tupel für Auto Objects
    rectAutoCollision = (rectBusCollision, rectLKWCollision, rectCarCollision, rectPoliceCollison)

    #Rect für Cycler
    rectCyclerCollison = pygame.Rect(cycler.x_cord - PIC_FRAME, (cycler.y_cord + PIC_FRAME), cycler.width -PIC_FRAME, (cycler.height - PIC_FRAME*2))

    for i in rectAutoCollision:
        if rectCyclerCollison.colliderect(i):
         print('collision')
         #Cycler.y_cord += 50
         lifePoints -= 1
         for j in autoObj:
             j.x_cord += 600
         aktionenBeiKollision()
         if(lifePoints == 0):
            lifePoints = 3
            gameover=True
            gameover_menu(score)


    #Zählt Anzahl um zuverhinder, dass in der AutoObjekt sich selbst als kollidierend ansieht
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
                police.y_cord -=10
                break

    showLeben(lifePoints)
    showScore(score)
    sprite_group.update()
    sprite_group.draw(screen)

    # Redisplay
    pygame.display.update()
