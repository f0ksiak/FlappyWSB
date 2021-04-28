import pygame, sys
from pygame.locals import *


def rys_podlog():
    screen.blit(podloga, (podloga_x_pos, 900))
    screen.blit(podloga, (podloga_x_pos + 500, 900))


def stw_pipe():
    new_pipe = pipe.get_rect(midtop = (250, 500))
    return new_pipe


def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def rys_pipe(rury):
    for r in rury:
        screen.blit(pipe, r)

pygame.init()
screen = pygame.display.set_mode((500,1000))
clock = pygame.time.Clock()

# Zmienne
grav = 0.2
wsb_movement = 0

#Tło
tlo = pygame.image.load('./assets/wsbbg.png').convert()

#Podłoga
podloga = pygame.image.load('./assets/floor.png').convert_alpha()
podloga = pygame.transform.scale2x(podloga)
podloga_x_pos = 0
#Ptak
wsb_bird = pygame.image.load('./assets/wsb.png').convert_alpha()
wsb_rect = wsb_bird.get_rect(center = (100, 500))
#Rury
pipe = pygame.image.load('assets/pipe.png')
pipe = pygame.transform.scale2x(pipe)
pipe_list = []
GENPIPE = pygame.USEREVENT
pygame.time.set_timer(GENPIPE,1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wsb_movement = 0
                wsb_movement -= 10
        if event.type == GENPIPE:
            pipe_list.append(stw_pipe())

    screen.blit(tlo, (0, 0))

    #Wsb movement
    wsb_movement += grav
    wsb_rect.centery += wsb_movement
    screen.blit(wsb_bird, wsb_rect)
    #Rury
    pipe_list = move_pipe(pipe_list)
    rys_pipe(pipe_list)


    #Podłoga
    podloga_x_pos -= 1
    rys_podlog()
    if podloga_x_pos <= -500:
        podloga_x_pos = 0


    pygame.display.update()
    clock.tick(120)