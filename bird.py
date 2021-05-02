import pygame, sys, random
from pygame.locals import *


def rys_podlog():
    screen.blit(podloga, (podloga_x_pos, 900))
    screen.blit(podloga, (podloga_x_pos + 500, 900))


def stw_pipe():
    random_pipe_pos = random.choice(pipe_wys)
    bottom_pipe = pipe.get_rect(midtop = (700, random_pipe_pos))
    top_pipe = pipe.get_rect(midbottom = (700, random_pipe_pos - 350))
    return bottom_pipe, top_pipe


def move_pipe(pipes):
    for r in pipes:
        r.centerx -= 5
    return pipes

def rys_pipe(pipes):
    for r in pipes:
        if r.bottom >= 1000:
            screen.blit(pipe, r)
        else:
            flip_r = pygame.transform.flip(pipe, False, True)
            screen.blit(flip_r, r)

def spr_coll(pipes):
    for r in pipes:
        if wsb_rect.colliderect(r):
            game_over_sound.play()
            return False

    if wsb_rect.top <= -100 or wsb_rect.bottom >= 900:
        return False
    return True

def wynik_display(game_state):
    if game_state == 'main_game':
        wyn = gra_cz.render(str(int(wynik)), True, (255,255,255))
        wynik_rect = wyn.get_rect(center = (250, 100))
        screen.blit(wyn,wynik_rect)
    if game_state == 'game_over':
        wyn = gra_cz.render(f'Score: {int(wynik)}', True, (255, 255, 255))
        wynik_rect = wyn.get_rect(center=(250, 100))
        screen.blit(wyn, wynik_rect)

        naj_wyn = gra_cz.render(f'High Score: {int(naj_wynik)}', True, (255, 255, 255))
        naj_wynik_rect = naj_wyn.get_rect(center=(250, 850))
        screen.blit(naj_wyn, naj_wynik_rect)

def akt_wynik(wynik, naj_wynik):
    if wynik > naj_wynik:
        naj_wynik = wynik
    return naj_wynik



pygame.init()
screen = pygame.display.set_mode((500,1000))
clock = pygame.time.Clock()
gra_cz = pygame.font.Font('04B_19.ttf',40)

# Zmienne
grav = 0.2
wsb_movement = 0
gra_act = True
wynik = 0
naj_wynik = 0

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
pipe_wys = [400, 500, 600, 700]

#Game over
game_over = pygame.image.load('assets/gameover.png').convert_alpha()
game_over = pygame.transform.scale2x(game_over)
game_over_rect = game_over.get_rect(center = (250,450))

#Dźwięk
skok_sound = pygame.mixer.Sound('sounds/bruh.mp3')
game_over_sound = pygame.mixer.Sound('sounds/deathdiff.mp3')
punkt_sound = pygame.mixer.Sound('sounds/point.wav')
punkt_licz = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gra_act:
                wsb_movement = 0
                wsb_movement -= 10
                skok_sound.play()
            if event.key == pygame.K_SPACE and gra_act == False:
                gra_act = True
                pipe_list.clear()
                wsb_rect.center = (100,500)
                wsb_movement = 0
                wynik = 0
        if event.type == GENPIPE:
            pipe_list.extend(stw_pipe())

    screen.blit(tlo, (0, 0))

    if gra_act:

        #Wsb movement
        wsb_movement += grav
        wsb_rect.centery += wsb_movement
        screen.blit(wsb_bird, wsb_rect)
        gra_act = spr_coll(pipe_list)
        #Rury
        pipe_list = move_pipe(pipe_list)
        rys_pipe(pipe_list)
        #Wynik
        wynik += 0.01
        wynik_display('main_game')
        punkt_licz -= 1
        #if punkt_licz <= 0:
            #punkt_sound.play()
            #punkt_licz = 100
    else:
        screen.blit(game_over, game_over_rect)
        naj_wynik = akt_wynik(wynik, naj_wynik)
        wynik_display('game_over')



    #Podłoga
    podloga_x_pos -= 1
    rys_podlog()
    if podloga_x_pos <= -500:
        podloga_x_pos = 0


    pygame.display.update()
    clock.tick(120)