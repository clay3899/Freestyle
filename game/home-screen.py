import pygame
from pygame import *
from os import path

width = 960
height = 720

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

pygame.display.set_caption('Champions are Coming')

display_screen = pygame.display.set_mode((width, height))

img_dir = path.join(path.dirname(__file__), 'images')

WHITE = (225,225,225)

#Code help to understand structure of the start screen from https://github.com/joshuawillman/The-Lonely-Shooter
def draw_text(surface, text, size, x, y, color):

    font = pygame.font.Font(pygame.font.match_font('cambria'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def start_screen():
    
    title = pygame.image.load(path.join(img_dir, "title_text.png")).convert_alpha()
    title = pygame.transform.scale(title, (width, 165))
    background = pygame.image.load('game\images\Home_Screen.jpg').convert()
    background_rect = background.get_rect()

    arrow_keys = pygame.image.load(path.join(img_dir, 'arrow_keys.png')).convert_alpha()
    arrow_keys = pygame.transform.scale(arrow_keys, (150, 85))
    
    display_screen.blit(background, background_rect)
    display_screen.blit(title, (0,110))
    display_screen.blit(arrow_keys, (720, 570))
    draw_text(display_screen, "Are You Ready for the Challenge?", 35, width/2, height/2, WHITE)
    draw_text(display_screen, "If so, press [ENTER] to begin", 35, width/2, (height/2) + 50, WHTIE)
    draw_text(display_screen, "If not, press [Q] to quit", 35, width/2, (height/2) + 100, WHITE)
    draw_text(display_screen, "MOVE:", 35, 630, 550, WHITE)

    #code for playing sound from CrouchingPython on YouTube https://www.youtube.com/watch?v=YQ1mixa9RAw
    pygame.mixer.music.load('game\sounds\Destiny.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
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