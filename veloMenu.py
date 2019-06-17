import pygame, sys
from pygame.locals import *

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = "Wozcott.otf"
menu = True

def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# startmenu
# Game Fonts


def main_menu(surface, width):
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
        surface.fill(GREEN)
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
        surface.blit(title, (width / 2 - (title_rect[2] / 2), 80))
        surface.blit(text_start, (width / 2 - (start_rect[2] / 2), 300))
        surface.blit(text_quit, (width / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
