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
pygame.display.set_caption('Tictac')
display_surface.fill(white)

pygame.init()


x = 50
y = 350
z = 120


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
smallfont = pygame.font.SysFont('Corbel', 17)

f = 140

gameOn = True


while gameOn:

    text1 = font.render("Score1 -", True, blue, white)
    textRect1 = text1.get_rect()
    textRect1.center = (110, 70)
    display_surface.blit(text1, textRect1)

    text = font.render(str("01"), True, blue, white)
    textRect = text.get_rect()
    textRect.center = (155, 70)
    display_surface.blit(text, textRect)

    text2 = font.render("Score2 -", True, pink, white)
    textRect2 = text2.get_rect()
    textRect2.center = (260, 70)
    display_surface.blit(text2, textRect2)

    text = font.render(str("02"), True, pink, white)
    textRect = text.get_rect()
    textRect.center = (305, 70)
    display_surface.blit(text, textRect)

    text1 = font.render("Time -", True, black, white)
    textRect1 = text1.get_rect()
    textRect1.center = (105, 100)
    display_surface.blit(text1, textRect1)

    text = font.render(str(f), True, black, white)
    textRect = text.get_rect()
    textRect.center = (145, 100)
    display_surface.blit(text, textRect)

    if f > 0:
        f = f-1

    # time.sleep(0.1)

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_BACKSPACE:
                gameOn = False

        elif event.type == QUIT:
            gameOn = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if 67 <= mouse[0] <= 67+65 and 365 <= mouse[1] <= 365 + 24:
                pygame.quit()

            if 170 <= mouse[0] <= 170+65 and 365 <= mouse[1] <= 365 + 24:
                f = 600

            if 270 <= mouse[0] <= 270+65 and 365 <= mouse[1] <= 365 + 24:
                pygame.quit()

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