import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500,1000))
clock = pygame.time.Clock()

tlo = pygame.image.load('').convert()
tlo = pygame.transform.scale2x(tlo)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(tlo,(0,0))

    pygame.display.update()
    clock.tick(120)