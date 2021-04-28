import pygame, sys
from pygame.locals import *

def rys_podlog():
    screen.blit(podloga, (podloga_x_pos, 900))
    screen.blit(podloga, (podloga_x_pos + 500, 900))


pygame.init()
screen = pygame.display.set_mode((500,1000))
clock = pygame.time.Clock()

# Zmienne
grav = 0.2
wsb_movement = 0


tlo = pygame.image.load('./assets/wsbbg.png').convert()


podloga = pygame.image.load('./assets/floor.png').convert_alpha()
podloga = pygame.transform.scale2x(podloga)
podloga_x_pos = 0

wsb_bird = pygame.image.load('./assets/wsb.png').convert_alpha()

wsb_rect = wsb_bird.get_rect(center = (100, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wsb_movement = 0
                wsb_movement -= 10

    screen.blit(tlo, (0, 0))

    wsb_movement += grav
    wsb_rect.centery += wsb_movement
    screen.blit(wsb_bird, wsb_rect)
    podloga_x_pos += 1
    rys_podlog()
    if podloga_x_pos <= -500:
        podloga_x_pos = 0


    pygame.display.update()
    clock.tick(120)