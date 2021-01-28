import pygame
import time as clock

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
player1 = "Player1"
wplayer = ""
player2 = "Player2"
copmuter = 0
start_on = gameOn = True
sound = True
dif = 0
ti = 7
ttt = 1
target = 3
name = ""
dr = 0

pygame.mixer.init()
pygame.mixer.music.load("Surf_David_Renda.mp3")
pygame.mixer.music.play(-1, 0.0)


def getno():
    global player1
    global player2
    global copmuter

    b = [100, 117, 200, 20]
    bb = (200, 127)

    if player1 == "" or player1 == " ":
        player1 = "Player 1"

    name = player1
    pygame.draw.rect(display_surface, white, b)
    text1 = font1.render(name + " ", True, black, white)
    textRect1 = text1.get_rect()
    textRect1.center = bb
    display_surface.blit(text1, textRect1)
    pygame.display.update()

    b = [100, 200, 200, 20]
    bb = (200, 210)

    name = "Player 2"

    if player2 == "" or player2 == " ":
        if copmuter == 0:
            player2 = "Player 2"
        else:
            name = "Computer"
    else:
        if copmuter == 0:
            name = player2
        else:
            name = "Computer"

    pygame.draw.rect(display_surface, white, b)
    text1 = font1.render(name + " ", True, black, white)
    textRect1 = text1.get_rect()
    textRect1.center = bb
    display_surface.blit(text1, textRect1)
    pygame.display.update()

    return


def getn(p1):
    name = ""
    global copmuter
    f = True
    temp = ""
    namet = ""
    b = bb = None

    if p1 == 1:
        namet = "Player 1"
        b = [100, 117, 200, 20]
        bb = (200, 127)
    else:
        namet = "Player 2"
        b = [100, 200, 200, 20]
        bb = (200, 210)

    while f:
        pygame.draw.rect(display_surface, color_light, b)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))

                if pygame.key.name(event.key) == "backspace":
                    print("get out")
                    name = name[:-1]
                elif pygame.key.name(event.key) == "return" or pygame.key.name(event.key) == "escape":
                    f = False
                    if p1 == 2:
                        if copmuter == 1:
                            if name == "" or name == " ":
                                namet = "Computer"
                            else:
                                copmuter = 0

                    elif name == "" or name == " ":
                        name = namet
                    pygame.draw.rect(display_surface, white, b)
                    text1 = font1.render(name + " ", True, black, white)
                    textRect1 = text1.get_rect()
                    textRect1.center = bb
                    display_surface.blit(text1, textRect1)
                    pygame.display.update()
                    return name
                else:
                    name = name + str(event.unicode)
                print(event.unicode)
                print(name)
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 100 <= mouse[0] <= 120+200 and 120 <= mouse[1] <= 120 + 28:
                    pass
                else:
                    f = False
                    if p1 == 2:
                        if copmuter == 1:
                            if name == "" or name == " ":
                                namet = "Computer"
                            else:
                                copmuter = 0

                    elif name == "" or name == " ":
                        name = namet

                    pygame.draw.rect(display_surface, white, b)
                    text1 = font1.render(namet + " ", True, black, white)
                    textRect1 = text1.get_rect()
                    textRect1.center = bb
                    display_surface.blit(text1, textRect1)
                    pygame.display.update()
                    return name

        text1 = font1.render(name + "|", True, black, color_light)
        textRect1 = text1.get_rect()
        textRect1.center = bb
        display_surface.blit(text1, textRect1)
        pygame.display.update()


def room():
    start_onn = True
    global start_on
    global player2
    global player1
    global ti
    global copmuter
    global dif
    global t
    global time
    global time1
    global time2
    global roundd
    global ttt
    global target
    global dr

    display_surface.fill(white)

    while start_onn:

        pygame.draw.rect(display_surface, color_dark,
                         [0, 33, 400, 28])
        text1 = font1.render("Game Option", True, white, color_dark)
        textRect1 = text1.get_rect()
        textRect1.center = (200, 47)
        display_surface.blit(text1, textRect1)

        if dr == 1:
            pygame.draw.rect(display_surface, color_light,
                             [380, 35, 5, 25])

        text1 = font1.render("Player 1 :", True, black, white)
        textRect1 = text1.get_rect()
        textRect1.center = (140, 97)
        display_surface.blit(text1, textRect1)

        # pygame.draw.rect(display_surface, color_light,
        #  [100, 120, 200, 28])
        pygame.draw.rect(display_surface, color_dark,
                         [100, 137, 200, 3])

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

        pygame.draw.rect(display_surface, color_dark,
                         [100, 220, 200, 3])

        text1 = font1.render(user, True, white, color_dark)
        textRect1 = text1.get_rect()
        textRect1.center = (243, 177)
        display_surface.blit(text1, textRect1)

        # pygame.draw.rect(display_surface, color_light,
        #               [100, 200, 200, 28])
        if copmuter == 1:
            pygame.draw.rect(display_surface, white,
                             [132+kk, 240, 160, 90])
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
        else:
            pygame.draw.rect(display_surface, white,
                             [132+kk, 240, 160, 90])

            text1 = font1.render("Target", True, black, white)
            textRect1 = text1.get_rect()
            textRect1.center = (200+kk, 250)
            display_surface.blit(text1, textRect1)

            pygame.draw.rect(display_surface, color_light,
                             [162+kk, 270, 80, 40])
            text1 = font1.render(str(target), True, white, color_light)
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

        pygame.draw.rect(display_surface, white,
                         [230, 237, 100, 26])
        text1 = font1.render(tt, True, black, white)
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
                    if copmuter == 1:
                        if dif >= 0 and dif < 2:
                            dif = dif+1
                    elif copmuter == 0:
                        target += 1

                elif 140+kk <= mouse[0] <= 140+kk+20 and 280 <= mouse[1] <= 280 + 20:
                    # [252, 280, 20, 20])
                    if copmuter == 1:
                        if dif > 0 and dif <= 2:
                            dif = dif-1
                    elif copmuter == 0:
                        target -= 1
                        if target <= 0:
                            target = 1

                elif 220 <= mouse[0] <= 220+20 and 280 <= mouse[1] <= 280 + 20:
                    # [252, 280, 20, 20])
                    ti = ti-2
                elif 324 <= mouse[0] <= 324+20 and 280 <= mouse[1] <= 280 + 20:
                    # [252, 280, 20, 20])
                    ti = ti+2

##
                elif 350 <= mouse[0] <= 350+50 and 35 <= mouse[1] <= 35 + 25:
                    dr = not dr
                    print(dr)
##

                elif 230 <= mouse[0] <= 230+100 and 237 <= mouse[1] <= 237 + 26:
                    ttt = not ttt
                    if ttt == 0:
                        target = 1
                    pass
                elif 156 <= mouse[0] <= 156+87 and 310 <= mouse[1] <= 310 + 35:
                    pygame.quit()

                elif 100 <= mouse[0] <= 100+200 and 120 <= mouse[1] <= 120 + 28:
                    print("p 1")
                    player1 = getn(1)
                elif 100 <= mouse[0] <= 100+200 and 200 <= mouse[1] <= 200 + 28:
                    print("p 2")
                    player2 = getn(2)
                elif 294 <= mouse[0] <= 294+64 and 340 <= mouse[1] <= 340 + 30:
                    start_on = False
                    reset_ne()
                    time1 = time2 = time = ti*100
                    print(time)
                    outline()
                    roundd = 1
                    return
                elif 45 <= mouse[0] <= 45+64 and 340 <= mouse[1] <= 340 + 30:
                    start_on = True
                    return 3
        getno()
        pygame.display.update()


def dra():
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


def start_screen():

    global start_on
    global sound
    global time
    global time1
    global time2
    global ti
    global ttt
    global target

    dra()

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
                    #start_on = True
                    target = 5
                    ti = 5
                    time1 = time2 = time = ti*100
                    if room() == 3:
                        dra()
                    else:
                        return

                elif 156 <= mouse[0] <= 156+87 and 210 <= mouse[1] <= 210 + 35:
                    start_on = False
                    reset_ne()
                    sreset()
                    ti = 10
                    time1 = time2 = time = ti*100
                    target = 1
                    ttt = 0
                    outline()

                elif 156 <= mouse[0] <= 156+87 and 260 <= mouse[1] <= 260 + 35:
                    Credits()
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


et = 0


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
    clock.sleep(2)


def bannermain(t1="", t2="", t3=2):
    pygame.draw.rect(display_surface, color_light,
                     [103, 170, 200, 100])

    text1 = font.render(t1, True, blue, white)
    textRect1 = text1.get_rect()
    textRect1.center = (200, 200)
    display_surface.blit(text1, textRect1)

    text1 = font.render(t2, True, blue, color_light)
    textRect1 = text1.get_rect()
    textRect1.center = (200, 240)
    display_surface.blit(text1, textRect1)

    pygame.display.flip()
    pygame.display.update()
    clock.sleep(t3)


def banner_draw():
    pygame.draw.rect(display_surface, color_light,
                     [103, 170, 200, 100])
    text1 = font.render("Match Tie !", True, blue, white)
    textRect1 = text1.get_rect()
    textRect1.center = (200, 220)
    display_surface.blit(text1, textRect1)

    pygame.display.flip()
    pygame.display.update()
    clock.sleep(2)


def reset_ne():

    global f
    global turn
    global arr
    global ti
    global time
    global time1
    global time2
    if ttt != 0:
        time1 = time2 = time = ti*100
    turn = 0
    arr = [None, None, None,
           None, None, None,
           None, None, None]
    outline()
    score1 = score2 = 0
    print("reseted")


def sreset():
    global time
    global time1
    global time2
    global ttt
    global roundd
    global score1
    global score2
    turn = 0
    if ttt != 1:
        score1 = score2 = 0
        #roundd -=1
    else:
        pass

    arr = [None, None, None,
           None, None, None,
           None, None, None]
    t = 0
    outline()


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
        global roundd
        roundd = roundd+1
        return 1


def game_logic(tile):
    global turn
    global arr
    print(arr)
    global roundd
    global dr

    b = None

    if turn == 8:
        pass

    if turn % 2 == 0:
        b = 0
    else:
        b = 1

    if arr[tile-1] == None:
        arr[tile-1] = b

        global et
        et = 1

        strike(tile=tile-1, pl=b)

        turn = turn+1
        if turn == 9:
            roundd = roundd+1
            if check_if_won() == 1:
                pass
            else:
                banner_draw()
                #roundd = roundd+1

                outline()
                reset_ne()
                global score2
                global score1
                if dr == 1:
                    score2 += 1
                    score1 += 1

    else:
        pass

    print(tile, turn, roundd)
    check_if_won()


def end():
    global score1
    global score2
    global roundd
    global player1
    global player2
    global start_on

    bannermain(t1="Match Ended !", t3=1)
    if score1 == score2:
        bannermain(t1="Draw", t2=str(score1)+":"+str(score1) +
                   " in "+str(roundd)+" Rounds", t3=5)
    elif score1 > score2:
        bannermain(t1=player1+" Wins !", t2="By "+str(score1)+":"+str(score2) +
                   " in "+str(roundd)+" Rounds", t3=5)
    else:
        bannermain(t1=player2+" Wins !", t2="By "+str(score2)+":"+str(score1) +
                   " in "+str(roundd)+" Rounds", t3=5)
    start_on = True


def count(sp=0.7):
    global target
    global ti
    st = "Target " + str(target) + " | Time " + str(ti)+"s"
    bannermain(t1="3", t2=st, t3=sp)
    bannermain(t1="2", t2=st, t3=sp)
    bannermain(t1="1", t2=st, t3=sp)
    bannermain(t1="Go !", t3=0.5)


def Credits():
    cred = True

    while cred:
        display_surface.fill(white)

        text1 = font.render("Programed By : ", True, black, white)
        textRect1 = text1.get_rect()
        textRect1.center = (110, 70)
        display_surface.blit(text1, textRect1)

        text1 = font.render("Jesvi Jonathan", True, blue, white)
        textRect1 = text1.get_rect()
        textRect1.center = (260, 70)
        display_surface.blit(text1, textRect1)

        text1 = font.render("Version : ", True, black, white)
        textRect1 = text1.get_rect()
        textRect1.center = (135, 100)
        display_surface.blit(text1, textRect1)

        text1 = font.render("v0.3", True, blue, white)
        textRect1 = text1.get_rect()
        textRect1.center = (215, 100)
        display_surface.blit(text1, textRect1)

        text1 = font.render("Date : ", True, black, white)
        textRect1 = text1.get_rect()
        textRect1.center = (148, 130)
        display_surface.blit(text1, textRect1)

        text1 = font.render("28/1/2021", True, blue, white)
        textRect1 = text1.get_rect()
        textRect1.center = (235, 130)
        display_surface.blit(text1, textRect1)
        k = 30

        pygame.draw.rect(display_surface, (200, 250, 205),
                         [40, 180, 340, 120])

        text1 = font.render(
            "This was intended to be a simple game ", True, pink, (200, 250, 205))
        textRect1 = text1.get_rect()
        textRect1.center = (210, 170+k)
        display_surface.blit(text1, textRect1)

        text1 = font.render(
            "powered by AI/ML to compete with users", True, pink, (200, 250, 205))
        textRect1 = text1.get_rect()
        textRect1.center = (210, 210+k)
        display_surface.blit(text1, textRect1)

        text1 = font.render(
            "All built in native python (1 week)", True, pink, (200, 250, 205))
        textRect1 = text1.get_rect()
        textRect1.center = (210, 250+k)
        display_surface.blit(text1, textRect1)

        pygame.draw.rect(display_surface, color_light,
                         [270, 325, 73, 24])
        pygame.draw.rect(display_surface, color_light,
                         [170, 325, 73, 24])
        pygame.draw.rect(display_surface, color_light,
                         [70, 325, 73, 24])

        bt = smallfont.render('Back', True, white)
        bt1 = smallfont.render('Website', True, white)
        bt2 = smallfont.render('Support', True, white)
        display_surface.blit(bt, (90, 328))
        display_surface.blit(bt1, (180, 328))
        display_surface.blit(bt2, (280, 328))

        clock.sleep(0.01)

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == KEYDOWN:

                if event.key == K_BACKSPACE:
                    gameOn = True
                    display_surface.fill(white)
                    start_on = True
                    dra()
                    return

            elif event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 70 <= mouse[0] <= 70+73 and 325 <= mouse[1] <= 325 + 24:

                    gameOn = True
                    display_surface.fill(white)
                    start_on = True
                    dra()
                    return

        pygame.display.flip()
        pygame.display.update()

    pass


v = 0
roundd = 1
while gameOn:

    if start_on == True:
        start_screen()
        bannermain(t1="Starting In", t3=1)
        count()
        sreset()

    clock.sleep(0.01)

    if score1 >= target and score2 >= target:
        bannermain(t1="Draw !", t2="Score "+str(score1)+":" +
                   str(score2)+" in "+str(roundd)+" rounds", t3=5)
        start_on = True
    elif score1 >= target:
        bannermain(t1=player1+" Wins !", t2="by "+str(score1)+":" +
                   str(score2)+" in "+str(roundd)+" rounds", t3=5)
        start_on = True
    elif score2 >= target:
        bannermain(t1=player2+" Wins !", t2="by "+str(score2)+":" +
                   str(score1)+" in "+str(roundd)+" rounds", t3=5)
        start_on = True

    g1 = g = " "
    if ttt == 1:
        if turn % 2 == 0:
            g = "*"
            g1 = " "
            if time1 > 0:
                time1 = time1-1
            elif time1 <= 0:
                bannermain(t1="Time Up !", t3=1.3)

                bannermain(t1=player2 + " Wins !", t2="Score +1", t3=2)
                score2 = score2+1
                time2 = time1 = time = ti*100
                count()
                sreset()
                reset_ne()
                roundd = 0
                turn = 0

        else:
            g = " "
            g1 = "*"
            if time2 > 0:
                time2 = time2-1
            elif time2 <= 0:
                bannermain(t1="Time Up !", t3=1.3)
                bannermain(t1=player1 + " Wins !", t2="Score +1", t3=2)
                score1 = score1+1
                time1 = time2 = time = ti*100
                count()
                sreset()
                reset_ne()
                roundd = 0
                turn = 0
    else:
        if turn % 2 == 0:
            g = "*"
            g1 = " "
            if time1 > 0:
                time1 = time1-1
            elif time1 <= 0:
                bannermain(t1="Game Over !", t3=1.3)
                bannermain(t1=player2 + "  Wins !", t2="by " +
                           str(score1)+":"+str(score2)+" in "+str(roundd) + " rounds", t3=6)
                start_on = True

        else:
            g = " "
            g1 = "*"
            if time2 > 0:
                time2 = time2-1
            elif time2 <= 0:
                bannermain(t1="Game Over !", t3=1.3)
                bannermain(t1=player1 + "  Wins !", t2="by " +
                           str(score1)+":"+str(score2)+" in "+str(roundd) + " rounds", t3=6)
                start_on = True

    pygame.draw.rect(display_surface, color_dark,
                     [0, 13, 400, 28])
    text1 = font1.render("Round "+str(roundd), True, white, color_dark)
    textRect1 = text1.get_rect()
    textRect1.center = (200, 27)
    display_surface.blit(text1, textRect1)

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

    text = font.render("  "+str(time1)+"  ", True, black, white)
    textRect = text.get_rect()
    textRect.center = (150, 100)
    display_surface.blit(text, textRect)

    text1 = font.render("Time -", True, black, white)
    textRect1 = text1.get_rect()
    textRect1.center = (264, 100)
    display_surface.blit(text1, textRect1)

    text = font.render("  "+str(time2)+"  ", True, black, white)
    textRect = text.get_rect()
    textRect.center = (315, 100)
    display_surface.blit(text, textRect)

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

                bannermain(t1="Reseted", t3=1)
                time1 = time2 = time = ti*100
                roundd = roundd
                arr = [None, None, None,
                       None, None, None,
                       None, None, None]
                count(0.5)
                sreset()

            if 270 <= mouse[0] <= 270+65 and 365 <= mouse[1] <= 365 + 24:
                # pygame.quit()
                print("end")
                end()

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
    bt2 = smallfont.render('End', True, white)
    display_surface.blit(bt, (83, 368))
    display_surface.blit(bt1, (183, 368))
    display_surface.blit(bt2, (287, 368))

    pygame.display.flip()
    pygame.display.update()

    if et == 1:
        if v == 1:
            clock.sleep(0.3)
            et = 0
            v = 0
        else:
            v = v+1
