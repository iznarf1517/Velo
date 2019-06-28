import pygame, sys
from pygame.locals import *

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
menu = True
music = "off"
sounds = "off"
raeder=("dreirad", "stadtrad", "rennrad")
zeiger = 0
selected_rad = raeder[zeiger]


# hier beliebige Schriftart runterladen und in den Ordner packen // eventuell ein Bild als Logo?
# Game Font
font = "Wozcott.otf"


# Textverarbeiter kann man auch im Hauptprog nutzen
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText

# startmenu
def main_menu(surface, width):
    global menu
    selected = "start"
    folge = 0
    global selected_rad
    global music
    global sounds
    global zeiger

    while menu:

        # Start Menu UI
        if folge == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and selected == "sounds":
                        selected = "music"
                    elif event.key == pygame.K_UP and selected == "quit" or event.key == pygame.K_LEFT:
                        selected = "start"

                    elif event.key == pygame.K_RIGHT:
                        selected = "music"
                    elif event.key == pygame.K_DOWN and selected == "music":
                        selected = "sounds"
                    elif event.key == pygame.K_DOWN and selected == "start":
                        selected = "quit"
                    if event.key == pygame.K_RETURN:
                        if selected == "start":
                            if folge == 0:
                                folge = 1
                            else:
                                menu = False
                        if selected == "quit":
                            pygame.quit()
                            quit()
                        if selected == "music":
                            if music == "off":
                                music = "on"
                            else:
                                music = "off"
                        if selected == "sounds":
                            if sounds == "off":
                                sounds = "on"
                            else:
                                sounds = "off"

            if selected == "start":
                text_start = text_format("START", font, 50, WHITE)
            else:
                text_start = text_format("START", font, 50, BLACK)
            if selected == "quit":
                text_quit = text_format("QUIT", font, 50, WHITE)
            else:
                text_quit = text_format("QUIT", font, 50, BLACK)
            if music == "on" and selected == "music":
                text_music = text_format("MUSIC ON", font, 25, (255, 0, 0))
            elif selected == "music":
                text_music = text_format("MUSIC OFF", font, 25, WHITE)
            elif music == "on":
                text_music = text_format("MUSIC ON", font, 25, (155,0,0))
            else:
                text_music = text_format("MUSIC OFF", font, 25, BLACK)
            if sounds == "on" and selected == "sounds":
                text_sounds = text_format("SOUNDS ON", font, 25, (255, 0, 0))
            elif selected == "sounds":
                text_sounds = text_format("SOUNDS OFF", font, 25, WHITE)
            elif sounds == "on":
                text_sounds = text_format("SOUNDS ON", font, 25, (155,0,0))
            else:
                text_sounds = text_format("SOUNDS OFF", font, 25, BLACK)

            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()

            # Main Menu Text
            surface.fill(GREEN)
            title = text_format("VeloZania", font, 70, BLACK)
            title_rect = title.get_rect()
            surface.blit(title, (width / 2 - (title_rect[2] / 2), 80))
            surface.blit(text_start, (width / 2 - (start_rect[2] / 2), 300))
            surface.blit(text_quit, (width / 2 - (quit_rect[2] / 2), 360))

            surface.blit(text_music, (600, 340))
            surface.blit(text_sounds, (600, 370))

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if zeiger < 2:
                            selected_rad = raeder[zeiger + 1]
                            zeiger = zeiger + 1
                    elif event.key == pygame.K_LEFT:
                        if zeiger >= 1:
                            selected_rad = raeder[zeiger - 1]
                            zeiger = zeiger - 1
                    if event.key == pygame.K_RETURN:
                        if selected_rad == "quit":
                            pygame.quit()
                            quit()
                        else:
                            menu = False
                            return selected_rad
            # Main Menu UI

            if selected_rad == "dreirad":
                dreirad = text_format("dreirad", font, 30, WHITE)
            else:
                dreirad = text_format("dreirad", font, 30, BLACK)
            if selected_rad == "stadtrad":
                stadtrad = text_format("stadtrad", font, 30, WHITE)
            else:
                stadtrad = text_format("stadtrad", font, 30, BLACK)
            if selected_rad == "rennrad":
                rennrad = text_format("rennrad", font, 30, WHITE)
            else:
                rennrad = text_format("rennrad", font, 30, BLACK)

            # Main Menu Text
            surface.fill(GREEN)
            title = text_format("VeloZania", font, 70, BLACK)
            title_rect = title.get_rect()
            surface.blit(title, (width / 2 - (title_rect[2] / 2), 80))
            surface.blit(dreirad, (130, 450))
            surface.blit(stadtrad, (330, 450))
            surface.blit(rennrad, (530, 450))

        pygame.display.update()


def gameover_menu(score, surface, gameover):
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
                        gameover = False
                        menu = True

                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Collison Menu UI
        surface.fill(GREEN)

        title = text_format("GAME OVER!", font, 70, BLACK)
        score_text = text_format('DEIN SCORE ' + str(score), font, 50, BLACK)
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
        surface.blit(title, (800 / 2 - (title_rect[2] / 2), 80))
        surface.blit(score_text, (800 / 2 - (score_rect[2] / 2), 180))
        surface.blit(text_start, (800 / 2 - (start_rect[2] / 2), 300))
        surface.blit(text_quit, (800 / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
        pygame.display.set_caption("VeloZonia")

def is_music ():
    if music == 'on':
        return True
    else:
        return False

def is_sound():
    if sounds == 'on':
        return True
    else:
        return False

def get_Radtyp():
    return selected_rad


