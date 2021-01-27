import pygame
import time

from pygame.locals import *

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)
pink = (250, 100, 200)

color_light = (170, 170, 170)
color_dark = (100, 100, 100)

width = 400
height = 400

display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tictactoe')


pygame.init()


def outline():

    x = 50
    y = 350
    z = 120
    display_surface.fill(white)
    pygame.draw.line(display_surface, green,
                     (x+100, z), (x+100, y), 2)
    pygame.draw.line(display_surface, green,
                     (x+200, z), (x+200, y), 2)

    pygame.draw.line(display_surface, green,
                     (x, z+73), (y, z+73), 2)
    pygame.draw.line(display_surface, green,
                     (x, z+153), (y, z+153), 2)

    pygame.draw.line(display_surface, red,
                     (x, y), (y, y), 3)
    pygame.draw.line(display_surface, red,
                     (x, z), (y, z), 3)

    pygame.draw.line(display_surface, red,
                     (x, z), (x, y), 3)
    pygame.draw.line(display_surface, red,
                     (y, z), (y, y), 3)


outline()

c = [(100, 158), (200, 158), (300, 158),
     (100, 235), (200, 235), (300, 235),
     (100, 312), (200, 312), (300, 312)]


for i in range(0, 0):
    pygame.draw.circle(display_surface,
                       blue, c[i], 25, 3)

e = [(80, 180), (120, 130),
     (180, 180), (220, 130),
     (280, 180), (320, 130),

     (80, 260), (120, 210),
     (180, 260), (220, 210),
     (280, 260), (320, 210),

     (80, 340), (120, 290),
     (180, 340), (220, 290),
     (280, 340), (320, 290)]

ee = [(120, 180), (80, 130),
      (220, 180), (180, 130),
      (320, 180), (280, 130),

      (120, 260), (80, 210),
      (220, 260), (180, 210),
      (320, 260), (280, 210),

      (120, 340), (80, 290),
      (220, 340), (180, 290),
      (320, 340), (280, 290)]

j = -1

while j >= 0:
    pygame.draw.line(display_surface, red,
                     e[j], e[j+1], 3)

    pygame.draw.line(display_surface, red,
                     ee[j], ee[j+1], 3)

    j = j-2

# pygame.draw.line(display_surface, red,
#                 (30, 10), (10, 30), 3)


font = pygame.font.Font('freesansbold.ttf', 17)
font1 = pygame.font.Font('freesansbold.ttf', 18)
smallfont = pygame.font.SysFont('Corbel', 17)
smallfont1 = pygame.font.SysFont('Corbel', 13)
bigfont = pygame.font.SysFont('Bauhuas 93', 60)

f = 140

turn = 0
score2 = score1 = 0
arr = [None, None, None,
       None, None, None,
       None, None, None]
player1 = "Player 1"
wplayer = ""
player2 = "Player 2"
ti = None
copmuter = 0
start_on = gameOn = True
sound = True
dif = 0
ti = 40
ttt = 0

pygame.mixer.init()
pygame.mixer.music.load("Surf_David_Renda.mp3")
pygame.mixer.music.play(-1, 0.0)


def room():
    global start_on
    global player2
    global ti
    global copmuter
    global dif
    global ti
    global ttt

    display_surface.fill(white)

    while start_on:

        pygame.draw.rect(display_surface, color_dark,
                         [0, 33, 400, 28])
        text1 = font1.render("Game Option", True, white, color_dark)
        textRect1 = text1.get_rect()
        textRect1.center = (200, 47)
        display_surface.blit(text1, textRect1)

        text1 = font1.render("Player 1 :", True, black, white)
        textRect1 = text1.get_rect()
        textRect1.center = (140, 97)
        display_surface.blit(text1, textRect1)

        pygame.draw.rect(display_surface, color_light,
                         [100, 120, 200, 28])

        text1 = font1.render("Player 2 :", True, black, white)
        textRect1 = text1.get_rect()
        textRect1.center = (140, 177)
        display_surface.blit(text1, textRect1)

        # pygame.draw.rect(display_surface, blue, [210, 165, 33, 24])
        user = None
        kk = -80
        if copmuter == 1:
            user = "Computer"
        else:
            user = "User"

        pygame.draw.rect(display_surface, color_dark, [195, 165, 96, 24])
        text1 = font1.render(user, True, white, color_dark)
        textRect1 = text1.get_rect()
        textRect1.center = (243, 177)
        display_surface.blit(text1, textRect1)

        pygame.draw.rect(display_surface, color_light,
                         [100, 200, 200, 28])

        text1 = font1.render("Difficulty", True, black, white)
        textRect1 = text1.get_rect()
        textRect1.center = (200+kk, 250)
        display_surface.blit(text1, textRect1)

        if dif == 0:
            pygame.draw.rect(display_surface, color_light,
                             [162+kk, 270, 80, 40])
            text1 = font1.render("Normal", True, white, color_light)
            textRect1 = text1.get_rect()
            textRect1.center = (202+kk, 290)
            display_surface.blit(text1, textRect1)

        elif dif == 1:
            pygame.draw.rect(display_surface, color_dark,
                             [162+kk, 270, 80, 40])
            text1 = font1.render("Medium", True, white, color_dark)
            textRect1 = text1.get_rect()
            textRect1.center = (202+kk, 290)
            display_surface.blit(text1, textRect1)
        elif dif == 2:
            pygame.draw.rect(display_surface, black,
                             [162+kk, 270, 80, 40])
            text1 = font1.render("Hard", True, white, black)
            textRect1 = text1.get_rect()
            textRect1.center = (202+kk, 290)
            display_surface.blit(text1, textRect1)

        pygame.draw.rect(display_surface, color_dark,
                         [140+kk, 280, 20, 20])
        pygame.draw.rect(display_surface, color_dark,
                         [244+kk, 280, 20, 20])

        pygame.draw.rect(display_surface, color_light,
                         [294, 340, 64, 30])
        text1 = font1.render("Start", True, white, color_light)
        textRect1 = text1.get_rect()
        textRect1.center = (326, 354)
        display_surface.blit(text1, textRect1)

        pygame.draw.rect(display_surface, color_light,
                         [45, 340, 64, 30])
        text1 = font1.render("Back", True, white, color_light)
        textRect1 = text1.get_rect()
        textRect1.center = (75, 354)
        display_surface.blit(text1, textRect1)

        # pygame.draw.rect(display_surface, color_light,
        #                 [160, 343, 33, 24])
        pygame.draw.rect(display_surface, color_light,
                         [242, 270, 80, 40])

        if ttt == 0:
            tt = "Stopwatch"
        else:
            tt = "Counter"

        pygame.draw.rect(display_surface, color_dark,
                         [230, 237, 100, 26])
        text1 = font1.render(tt, True, white, color_dark)
        textRect1 = text1.get_rect()
        textRect1.center = (280, 250)
        display_surface.blit(text1, textRect1)

        text1 = font1.render(str(ti)+"s", True, white, color_light)
        textRect1 = text1.get_rect()
        textRect1.center = (280, 290)
        display_surface.blit(text1, textRect1)

        pygame.draw.rect(display_surface, color_dark,
                         [220, 280, 20, 20])
        pygame.draw.rect(display_surface, color_dark,
                         [324, 280, 20, 20])

        pygame.draw.line(display_surface, color_light,
                         (202, 255), (202, 325), 3)

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == KEYDOWN:

                if event.key == K_BACKSPACE:
                    pygame.quit()

            elif event.type == QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if 195 <= mouse[0] <= 195+96 and 165 <= mouse[1] <= 165 + 24:
                    # start_on = False [195, 165, 96, 24]
                    copmuter = not copmuter

                elif 244+kk <= mouse[0] <= 244+kk+20 and 280 <= mouse[1] <= 280 + 20:
                    # [252, 280, 20, 20])
                    if dif >= 0 and dif < 2:
                        dif = dif+1
                elif 140+kk <= mouse[0] <= 140+kk+20 and 280 <= mouse[1] <= 280 + 20:
                    # [252, 280, 20, 20])
                    if dif > 0 and dif <= 2:
                        dif = dif-1

                elif 220 <= mouse[0] <= 220+20 and 280 <= mouse[1] <= 280 + 20:
                    # [252, 280, 20, 20])
                    ti = ti-5
                elif 324 <= mouse[0] <= 324+20 and 280 <= mouse[1] <= 280 + 20:
                    # [252, 280, 20, 20])
                    ti = ti+5

                elif 230 <= mouse[0] <= 230+100 and 237 <= mouse[1] <= 237 + 26:
                    ttt = not ttt
                    pass
                elif 156 <= mouse[0] <= 156+87 and 310 <= mouse[1] <= 310 + 35:
                    pygame.quit()

                elif 40 <= mouse[0] <= 40+14 and 370 <= mouse[1] <= 370 + 14:
                    pass

        pygame.display.update()


def start_screen():

    global start_on
    global sound

    display_surface.fill(white)

    pygame.draw.rect(display_surface, black,
                     [0, 42, 400, 70])

    pygame.draw.rect(display_surface, color_light,
                     [157, 160, 87, 35])

    pygame.draw.rect(display_surface, color_light,
                     [157, 210, 87, 35])

    pygame.draw.rect(display_surface, color_light,
                     [157, 260, 87, 35])

    pygame.draw.rect(display_surface, color_light,
                     [157, 310, 87, 35])

    pygame.draw.rect(display_surface, color_light,
                     [40, 370, 14, 14])
    pygame.draw.rect(display_surface, color_dark,
                     [44, 374, 6, 6])

    while start_on:

        text1 = bigfont.render("TicTacToe", True, white, black)
        textRect1 = text1.get_rect()
        textRect1.center = (200, 77)
        display_surface.blit(text1, textRect1)

        text1 = font1.render("Start", True, white, color_light)
        textRect1 = text1.get_rect()
        textRect1.center = (200, 177)
        display_surface.blit(text1, textRect1)

        text1 = font1.render("Quick", True, white, color_light)
        textRect1 = text1.get_rect()
        textRect1.center = (200, 228)
        display_surface.blit(text1, textRect1)

        text1 = font1.render("Credits", True, white, color_light)
        textRect1 = text1.get_rect()
        textRect1.center = (200, 277)
        display_surface.blit(text1, textRect1)

        text1 = font1.render("Exit", True, white, color_light)
        textRect1 = text1.get_rect()
        textRect1.center = (200, 327)
        display_surface.blit(text1, textRect1)

        text1 = smallfont1.render("Jesvi Jonathan", True, black, white)
        textRect1 = text1.get_rect()
        textRect1.center = (348, 390)
        display_surface.blit(text1, textRect1)

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == KEYDOWN:

                if event.key == K_BACKSPACE:
                    pygame.quit()

            elif event.type == QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if 156 <= mouse[0] <= 156+87 and 160 <= mouse[1] <= 160 + 35:
                    # start_on = False
                    room()

                elif 156 <= mouse[0] <= 156+87 and 210 <= mouse[1] <= 210 + 35:
                    start_on = False
                    reset_ne()
                    outline()

                elif 156 <= mouse[0] <= 156+87 and 260 <= mouse[1] <= 260 + 35:
                    pass
                elif 156 <= mouse[0] <= 156+87 and 310 <= mouse[1] <= 310 + 35:
                    pygame.quit()

                elif 40 <= mouse[0] <= 40+14 and 370 <= mouse[1] <= 370 + 14:

                    if sound == True:
                        pygame.mixer.music.set_volume(0)
                        sound = False
                        pygame.draw.rect(display_surface, color_light,
                                         [40, 370, 14, 14])
                    elif sound == False:
                        pygame.mixer.music.set_volume(100)
                        sound = True
                        pygame.draw.rect(display_surface, color_light,
                                         [40, 370, 14, 14])
                        pygame.draw.rect(display_surface, color_dark,
                                         [44, 374, 6, 6])

                else:
                    pass

        pygame.display.update()


def strike(tile, pl):
    if pl == 0:
        pygame.draw.circle(display_surface,
                           blue, c[tile], 25, 3)
    if pl == 1:
        pygame.draw.line(display_surface, red,
                         e[2*tile], e[2*tile+1], 3)

        pygame.draw.line(display_surface, red,
                         ee[2*tile], ee[2*tile+1], 3)


def checker_hover():
    global arr
    global turn

    t = None

    if 50 <= mouse[0] <= 50+100 and 122 <= mouse[1] <= 122 + 70:
        pass
        t = 1

    if 151 <= mouse[0] <= 151+100 and 122 <= mouse[1] <= 122 + 70:
        pass
        t = 2

    if 252 <= mouse[0] <= 252+100 and 122 <= mouse[1] <= 122 + 70:
        pass
        t = 3

# Svssdkhbsdkjcdslvjafglarglagflargaerliy

    if 50 <= mouse[0] <= 50+100 and 194 <= mouse[1] <= 194 + 77:
        pass
        t = 4

    if 151 <= mouse[0] <= 151+100 and 194 <= mouse[1] <= 194 + 77:
        pass
        t = 5

    if 252 <= mouse[0] <= 252+100 and 194 <= mouse[1] <= 194 + 77:
        pass
        t = 6

    # Svssdkhbsdkjcdslvjafglarglagflargaerliy

    if 50 <= mouse[0] <= 50+100 and 274 <= mouse[1] <= 274 + 77:
        pass
        t = 7

    if 151 <= mouse[0] <= 151+100 and 274 <= mouse[1] <= 274 + 77:
        pass
        t = 8

    if 252 <= mouse[0] <= 252+100 and 274 <= mouse[1] <= 274 + 77:
        pass
        t = 9

    if t == None:
        pass
    else:
        game_logic(tile=t)


def banner():
    pygame.draw.rect(display_surface, color_light,
                     [103, 170, 200, 100])

    text1 = font.render(wplayer + " Won !", True, blue, white)
    textRect1 = text1.get_rect()
    textRect1.center = (200, 200)
    display_surface.blit(text1, textRect1)

    text1 = font.render("Score +1", True, blue, color_light)
    textRect1 = text1.get_rect()
    textRect1.center = (200, 240)
    display_surface.blit(text1, textRect1)

    pygame.display.flip()
    pygame.display.update()
    time.sleep(2)


def banner_draw():
    pygame.draw.rect(display_surface, color_light,
                     [103, 170, 200, 100])
    text1 = font.render("Match Tie !", True, blue, white)
    textRect1 = text1.get_rect()
    textRect1.center = (200, 220)
    display_surface.blit(text1, textRect1)

    pygame.display.flip()
    pygame.display.update()
    time.sleep(2)


def reset_ne():

    global f
    global t
    global turn
    global arr
    f = 0
    t = 0
    turn = 0
    arr = [None, None, None,
           None, None, None,
           None, None, None]
    outline()
    print("reseted")


def check_if_won():
    global score1
    global player1
    global player2
    global wplayer
    global score2
    global turn
    win = -1
    global arr

    for p in range(0, 2):
        if arr[0] == p and arr[1] == p and arr[2] == p:
            win = p
        if arr[3] == p and arr[4] == p and arr[5] == p:
            win = p
        if arr[6] == p and arr[7] == p and arr[8] == p:
            win = p

        if arr[0] == p and arr[3] == p and arr[6] == p:
            win = p
        if arr[1] == p and arr[4] == p and arr[7] == p:
            win = p
        if arr[2] == p and arr[5] == p and arr[8] == p:
            win = p

        if arr[0] == p and arr[4] == p and arr[8] == p:
            win = p
        if arr[2] == p and arr[4] == p and arr[6] == p:
            win = p

    if win == 1 or win == 0:
        print(win, "Wins")
        if win == 0:
            score1 = score1+1
            wplayer = player1
        else:
            score2 = score2+1
            wplayer = player2
        banner()
        reset_ne()
        return 1


def game_logic(tile):
    global turn
    global arr
    print(arr)

    b = None

    if turn == 8:
        pass

    if turn % 2 == 0:
        b = 0
    else:
        b = 1

    if arr[tile-1] == None:
        arr[tile-1] = b

        strike(tile=tile-1, pl=b)

        turn = turn+1
        if turn == 9:
            if check_if_won() == 1:
                pass
            else:
                banner_draw()
                global score2
                global score1
                score2 = score2 + 1
                score1 = score1 + 1
                reset_ne()

    else:
        pass

    print(tile, turn)
    check_if_won()


while gameOn:

    if start_on == True:
        start_screen()

    g1 = g = ""
    if turn % 2 == 0:
        g = "*"
        g1 = ""
    else:
        g = ""
        g1 = "*"
    text1 = font.render(g + player1 + " -", True, blue, white)
    textRect1 = text1.get_rect()
    textRect1.center = (110, 70)
    display_surface.blit(text1, textRect1)

    text = font.render(str(score1), True, blue, white)
    textRect = text.get_rect()
    textRect.center = (160, 70)
    display_surface.blit(text, textRect)

    text2 = font.render(g1 + player2 + " -", True, pink, white)
    textRect2 = text2.get_rect()
    textRect2.center = (275, 70)
    display_surface.blit(text2, textRect2)

    text = font.render(str(score2), True, pink, white)
    textRect = text.get_rect()
    textRect.center = (323, 70)
    display_surface.blit(text, textRect)

    text1 = font.render("Time -", True, black, white)
    textRect1 = text1.get_rect()
    textRect1.center = (100, 100)
    display_surface.blit(text1, textRect1)

    text = font.render(str(f), True, black, white)
    textRect = text.get_rect()
    textRect.center = (145, 100)
    display_surface.blit(text, textRect)

    if f > 0:
        f = f-1

    # time.sleep(0.1)
    eve = None

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_BACKSPACE:
                gameOn = False

        elif event.type == QUIT:
            gameOn = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            eve = event.type
            if 67 <= mouse[0] <= 67+65 and 365 <= mouse[1] <= 365 + 24:
                start_on = True

            if 170 <= mouse[0] <= 170+65 and 365 <= mouse[1] <= 365 + 24:
                f = 600
                turn = 0
                score1 = 0
                arr = [None, None, None,
                       None, None, None,
                       None, None, None]
                t = 0

            if 270 <= mouse[0] <= 270+65 and 365 <= mouse[1] <= 365 + 24:
                pygame.quit()

            checker_hover()

    if 67 <= mouse[0] <= 67+65 and 365 <= mouse[1] <= 365 + 24:
        pygame.draw.rect(display_surface, color_light,
                         [67, 365, 65, 24])

    else:
        pygame.draw.rect(display_surface, color_dark,
                         [67, 365, 65, 24])

    if 170 <= mouse[0] <= 170+65 and 365 <= mouse[1] <= 365 + 24:
        pygame.draw.rect(display_surface, color_light,
                         [170, 365, 65, 24])

    else:
        pygame.draw.rect(display_surface, color_dark,
                         [170, 365, 65, 24])

    if 270 <= mouse[0] <= 270+65 and 365 <= mouse[1] <= 365 + 24:
        pygame.draw.rect(display_surface, color_light,
                         [270, 365, 65, 24])

    else:
        pygame.draw.rect(display_surface, color_dark,
                         [270, 365, 65, 24])

    bt = smallfont.render('Back', True, white)
    bt1 = smallfont.render('Reset', True, white)
    bt2 = smallfont.render('Quit', True, white)
    display_surface.blit(bt, (83, 368))
    display_surface.blit(bt1, (183, 368))
    display_surface.blit(bt2, (287, 368))

    pygame.display.flip()
    pygame.display.update()
