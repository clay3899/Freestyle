import pygame, sys, random
from pygame import *
from os import path

width = 960
height = 720
FPS = 30



# initialize pygame and create window
pygame.init()

pygame.display.set_caption('Champions are Coming')

screen = pygame.display.set_mode((960, 720))

img_dir = path.join(path.dirname(__file__), 'images')

black = (0,0,0)
gold = (200,190,140)
darkgrey = (93,94,94)
white = (225,225,225)

#Code help to understand structure of Pygame from https://github.com/joshuawillman/The-Lonely-Shooter
def draw_text(surface, text, size, x, y, color):

    font = pygame.font.Font(pygame.font.match_font('cambria'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def start_screen():
    
    title = pygame.image.load(path.join(img_dir, "title_text.png")).convert_alpha()
    title = pygame.transform.scale(title, (width, 165))
    background = pygame.image.load('images\Home_Screen.jpg').convert()
    background_rect = background.get_rect()

    arrow_keys = pygame.image.load(path.join(img_dir, 'arrow_keys.png')).convert_alpha()
    arrow_keys = pygame.transform.scale(arrow_keys, (150, 85))
    
    screen.blit(background, background_rect)
    screen.blit(title, (0,110))
    screen.blit(arrow_keys, (720, 570))
    draw_text(screen, "Are You Ready for the Challenge?", 35, width/2, height/2, white)
    draw_text(screen, "If so, press [ENTER] to begin", 35, width/2, (height/2) + 50, white)
    draw_text(screen, "If not, press [Q] to quit", 35, width/2, (height/2) + 100, white)
    draw_text(screen, "MOVE:", 35, 630, 550, white)

    pygame.display.update()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                break
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        elif event.type == QUIT:
            pygame.quit()
            sys.exit() 

start_screen()