import pygame, sys
from pygame.locals import *

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
menu = True

#hier beliebige Schriftart runterladen und in den Ordner packen // eventuell ein Bild als Logo?
# Game Font
font = "Wozcott.otf"

# Textverarbeiter kann man auch im Hauptprog nutzen
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText

# startmenu
def main_menu(surface, width, raeder = ("rennrad", "holland", "mountain")):
    global menu
    selected = "start"
    zeiger = 0
    folge = 0
    selected_rad = raeder[zeiger]

    while menu:

        # Start Menu UI
        if folge == 0:
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
                            if folge == 0:
                                print("Start")
                                folge = 1
                            else:
                                menu = False
                        if selected == "quit":
                            pygame.quit()
                            quit()

            if selected == "start":
                text_start = text_format("START", font, 50, WHITE)
            else:
                text_start = text_format("START", font, 50, BLACK)
            if selected == "quit":
                text_quit = text_format("QUIT", font, 50, WHITE)
            else:
                text_quit = text_format("QUIT", font, 50, BLACK)

            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()

            # Main Menu Text
            surface.fill(GREEN)
            title = text_format("VeloZania", font, 70, BLACK)
            title_rect = title.get_rect()
            surface.blit(title, (width / 2 - (title_rect[2] / 2), 80))
            surface.blit(text_start, (width / 2 - (start_rect[2] / 2), 300))
            surface.blit(text_quit, (width / 2 - (quit_rect[2] / 2), 360))



        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if zeiger <2:
                            selected_rad = raeder[zeiger+1]
                            zeiger = zeiger + 1
                    elif event.key == pygame.K_LEFT:
                        if zeiger >=1:
                            selected_rad = raeder[zeiger - 1]
                            zeiger = zeiger - 1
                    if event.key == pygame.K_RETURN:
                        if selected_rad == "quit":
                            pygame.quit()
                            quit()
                        else:
                            menu = False
                            return selected_rad
                            print(selected_rad)
            # Main Menu UI

            if selected_rad == "rennrad":
                rennrad = text_format("rennrad", font, 30, WHITE)
            else:
                rennrad = text_format("rennrad", font, 30, BLACK)
            if selected_rad == "holland":
                holland = text_format("holland", font, 30, WHITE)
            else:
                holland = text_format("holland", font, 30, BLACK)
            if selected_rad == "mountain":
                mounten = text_format("mountain", font, 30, WHITE)
            else:
                mounten = text_format("mountain", font, 30, BLACK)


            # Main Menu Text
            surface.fill(GREEN)
            title = text_format("VeloZania", font, 70, BLACK)
            title_rect = title.get_rect()
            surface.blit(title, (width / 2 - (title_rect[2] / 2), 80))
            surface.blit(rennrad, (130, 450))
            surface.blit(holland, (330, 450))
            surface.blit(mounten, (530, 450))

        pygame.display.update()
