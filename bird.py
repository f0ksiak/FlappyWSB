import pygame, sys
from pygame.locals import *

def rys_podlog():
    screen.blit(podloga, (podloga_x_pos, 900))
    screen.blit(podloga, (podloga_x_pos + 500, 900))
pygame.init()
screen = pygame.display.set_mode((500,1000))
clock = pygame.time.Clock()

tlo = pygame.image.load('').convert()
tlo = pygame.transform.scale2x(tlo)

podloga = pygame.image.load('').convert()
podloga = pygame.transform.scale2x(podloga)
podloga_x_pos = 0

wsb_bird = pygame.image.load('/assets/wsb.png').convert()
wsb_bird = pygame.transform.scale2x(wsb_bird)
wsb_rect = wsb_bird.get_rect(center = (100, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(tlo, (0, 0))
    screen.blit(wsb_bird, wsb_rect)
    podloga_x_pos += 1
    rys_podlog()
    if podloga_x_pos <= -500:
        podloga_x_pos = 0


    pygame.display.update()
    clock.tick(120)