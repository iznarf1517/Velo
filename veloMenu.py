import pygame, sys
from pygame.locals import *
from ranking import *

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
menu = True
music = "off"
sounds = "off"
raeder = ("dreirad", "stadtrad", "rennrad")
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
                    elif event.key == pygame.K_UP and selected == "ranking" or event.key == pygame.K_LEFT:
                        selected = "start"
                    elif event.key == pygame.K_UP and selected == "quit":
                        selected = "ranking"
                    elif event.key == pygame.K_RIGHT:
                        selected = "music"
                    elif event.key == pygame.K_DOWN and selected == "music":
                        selected = "sounds"
                    elif event.key == pygame.K_DOWN and selected == "start":
                        selected = "ranking"
                    elif event.key == pygame.K_DOWN and selected == "ranking":
                        selected = "quit"
                    if event.key == pygame.K_RETURN:
                        if selected == "start":
                            if folge == 0:
                                folge = 1
                            else:
                                menu = False
                        if selected == "ranking":
                            if folge == 0:
                                # sortiert die Rankingliste vor dem Anzeigen ranking.py
                                sorter_extra()
                                folge = 2
                            else:
                                menu = False
                        if selected == "quit":
                            pygame.quit()
                            quit()
                        if selected == "music":
                            # music_on_off()
                            print("music_on_off")
                            if music == "off":
                                music = "on"
                            else:
                                music = "off"
                        if selected == "sounds":
                            # music_on_off()
                            print("sounds_on_off")
                            if sounds == "off":
                                sounds = "on"
                            else:
                                sounds = "off"

            if selected == "start":
                text_start = text_format("START", font, 50, WHITE)
            else:
                text_start = text_format("START", font, 50, BLACK)
            if selected == "ranking":
                text_ranking = text_format("RANKING", font, 50, WHITE)
            else:
                text_ranking = text_format("RANKING", font, 50, BLACK)
            if selected == "quit":
                text_quit = text_format("QUIT", font, 50, WHITE)
            else:
                text_quit = text_format("QUIT", font, 50, BLACK)
            if music == "on" and selected == "music":
                text_music = text_format("MUSIC ON", font, 25, (255, 0, 0))
            elif selected == "music":
                text_music = text_format("MUSIC OFF", font, 25, WHITE)
            elif music == "on":
                text_music = text_format("MUSIC ON", font, 25, (155, 0, 0))
            else:
                text_music = text_format("MUSIC OFF", font, 25, BLACK)
            if sounds == "on" and selected == "sounds":
                text_sounds = text_format("SOUNDS ON", font, 25, (255, 0, 0))
            elif selected == "sounds":
                text_sounds = text_format("SOUNDS OFF", font, 25, WHITE)
            elif sounds == "on":
                text_sounds = text_format("SOUNDS ON", font, 25, (155, 0, 0))
            else:
                text_sounds = text_format("SOUNDS OFF", font, 25, BLACK)

            # Main Menu Text
            surface.fill(GREEN)
            title = text_format("VeloZania", font, 70, BLACK)
            title_rect = title.get_rect()
            surface.blit(title, (width / 2 - (title_rect[2] / 2), 80))
            surface.blit(text_start, (300, 300))
            surface.blit(text_ranking, (300, 360))
            surface.blit(text_quit, (300, 420))

            surface.blit(text_music, (600, 305))
            surface.blit(text_sounds, (600, 340))


        # Radwahlmenu
        elif folge == 1:
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
                            print(selected_rad)

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
            dreirad_pic = pygame.image.load('images/dreirad.png')
            dreirad_pic = pygame.transform.scale(dreirad_pic, (120, 150))
            surface.blit(dreirad_pic, (130, 250))
            surface.blit(dreirad, (130, 450))
            stadtrad_pic = pygame.image.load('images/normrad.png')
            stadtrad_pic = pygame.transform.scale(stadtrad_pic, (120, 150))
            surface.blit(stadtrad_pic, (330, 250))
            surface.blit(stadtrad, (330, 450))
            rennrad_pic = pygame.image.load('images/rennrad.png')
            rennrad_pic = pygame.transform.scale(rennrad_pic, (120, 150))
            surface.blit(rennrad_pic, (530, 250))
            surface.blit(rennrad, (530, 450))

        elif folge == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        folge = 0

            rankinglist = []
            back = text_format("back", font, 30, WHITE)
            i = 1
            for eintrag in auslesen_eintrag():
                rankinglist.append(text_format(str(i) + ". " + str(eintrag), font, 30, BLACK))
                i += 1

            # Main Menu Text
            surface.fill(GREEN)
            title = text_format("VeloZania", font, 70, BLACK)
            title_rect = title.get_rect()
            surface.blit(title, (width / 2 - (title_rect[2] / 2), 80))
            surface.blit(back, (350, 550))

            hoehe = 200
            for eintrag in rankinglist:
                surface.blit(eintrag, (300, hoehe))
                hoehe += 40

        pygame.display.update()


def gameover_menu(score, surface, gameover):
    global menu

    selected = "char1"
    folge = 0
    zeiger_char = 0

    chars = ("char1", "char2", "char3")
    zeiger = 0

    cs = [0, 0, 0]

    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and folge == 1:
                    if selected == "start":
                        print("Start")
                        gameover = False
                        menu = True

                    if selected == "quit":
                        pygame.quit()
                        quit()
                if event.key == pygame.K_RIGHT and selected == chars[zeiger_char] and folge == 0:
                    if zeiger_char < 2:
                        selected = chars[zeiger_char + 1]
                        zeiger_char += 1
                elif event.key == pygame.K_LEFT and selected == chars[zeiger_char] and folge == 0:
                    if zeiger_char > 1:
                        selected = chars[zeiger_char - 1]
                        zeiger_char -= 1

                if event.key == pygame.K_RETURN and folge == 0:
                    # print("Start")
                    folge = 1
                    selected = "start"
                    name = char_eintrag(cs[0]) + char_eintrag(cs[1]) + char_eintrag(cs[2])
                    neuer_eintrag(str(name), str(score))
                if event.key == pygame.K_UP and folge == 1:
                    selected = "start"
                elif event.key == pygame.K_DOWN and folge == 1:
                    selected = "quit"

                if event.key == pygame.K_UP and selected == chars[zeiger_char] and folge == 0:
                    if cs[zeiger_char] < 25:
                        cs[zeiger_char] += 1
                    else:
                        cs[zeiger_char] = 0
                if event.key == pygame.K_DOWN and selected == chars[zeiger_char] and folge == 0:
                    if cs[zeiger_char] > 0:
                        cs[zeiger_char] -= 1
                    else:
                        cs[zeiger_char] = 25

        # Collison Menu UI
        surface.fill(GREEN)

        title = text_format("GAME OVER!", font, 70, BLACK)
        if selected == "char1":
            ranking_name1 = text_format(char_eintrag(cs[0]), font, 50, WHITE)
        else:
            ranking_name1 = text_format(char_eintrag(cs[0]), font, 50, BLACK)
        if selected == "char2":
            ranking_name2 = text_format(char_eintrag(cs[1]), font, 50, WHITE)
        else:
            ranking_name2 = text_format(char_eintrag(cs[1]), font, 50, BLACK)
        if selected == "char3":
            ranking_name3 = text_format(char_eintrag(cs[2]), font, 50, WHITE)
        else:
            ranking_name3 = text_format(char_eintrag(cs[2]), font, 50, BLACK)

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
        surface.blit(ranking_name1, (320, 280))
        surface.blit(ranking_name2, (380, 280))
        surface.blit(ranking_name3, (440, 280))
        surface.blit(score_text, (800 / 2 - (score_rect[2] / 2), 180))
        surface.blit(text_start, (800 / 2 - (start_rect[2] / 2), 400))
        surface.blit(text_quit, (800 / 2 - (quit_rect[2] / 2), 460))
        pygame.display.update()
        pygame.display.set_caption("VeloZonia")


def is_music():
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
