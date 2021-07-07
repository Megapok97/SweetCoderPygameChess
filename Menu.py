import pygame, sys

mainCloack = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Menu')
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
fs = False
run = True
while run:
    screen.fill((0, 0, 50))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(screen.get_width()-50-(screen.get_width()/5), 50, screen.get_width()/5, 50))
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            if not fs:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
                pygame.quit()
                sys.exit()
            if event.key == K_f:
                fs = not fs
                print(fs)
                if fs:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
    pygame.display.update()
    mainCloack.tick(60)
