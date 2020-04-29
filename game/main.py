import pygame as pg
import random
import math
from pygame.locals import *
from pygame import mixer
import os
from os import path
from settings import *
from sprites import *

pg.mixer.pre_init(44100,16,2,4096)
pg.init()

display_screen = pg.display.set_mode((WIDTH, HEIGHT))

class Game:
    def __init__(self):
        # initialiaze game window, etc.
        self.running = True
        pg.init()
        pg.mixer.init()
        #display_screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        
        pass
    
    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.arrows = pg.sprite.Group()
        self.player = Player(self, 'archer.png')
        self.all_sprites.add(self.player)
        self.enemy1 = Enemy(680, 655, 'wizard.png')
        self.enemy2 = Enemy(WIDTH - 100, HEIGHT - 420, 'wizard.png')
        self.enemy3 = Enemy(WIDTH - 155, HEIGHT - 600, 'wizard.png')
        self.all_sprites.add(self.enemy1, self.enemy2, self.enemy3) 
        self.enemies.add(self.enemy1, self.enemy2, self.enemy3)
        self.previous_time = pg.time.get_ticks()
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
      
        self.run()
        pass

    def run(self):
        # game loop
        
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

        pass
    
    def update(self):
        # game loop -- updates
        self.all_sprites.update()
        #check if player hits platform if falling
        
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False,)
        
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.acc.y = 0        
    
        hits = pg.sprite.groupcollide(self.enemies, self.arrows, False, True)
        for hit in hits:
            hit.health -= ARROW_DAMAGE

        hits = pg.sprite.groupcollide(self.platforms, self.arrows, False, True)
        for hit in hits:
            hit.acc = (0,0)
            hit.vel = (0,0)


    def events(self):
        # game loop -- events
        
        for event in pg.event.get():

            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                    self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()
                if event.key == pg.K_SPACE:
                    self.current_time = pg.time.get_ticks()
                    if self.current_time - self.previous_time > SHOT_TIME:   
                        self.previous_time = self.current_time
                        self.fire()


    
    def draw(self):
        # game loop -- draw
    
        
        
        
        self.background_image = pg.image.load("game\images\Forest.jpg").convert()
        self.screen.blit(self.background_image, [0, 0])
        self.all_sprites.draw(self.screen)
        
        
        
        
        # after drawing
        pg.display.flip()


    
    
    def fire(self):
        arrow = Arrow(int(self.player.rect.centerx),int(self.player.rect.centery), 'uber_tiny.png')
        self.all_sprites.add(arrow)
        self.arrows.add(arrow)
        

    #Code help to understand structure of the start screen from https://github.com/joshuawillman/The-Lonely-Shooter
    def start_screen(self):
        img_dir = path.join(path.dirname(__file__), 'images')
        title = pg.image.load(path.join(img_dir, "title_text.png")).convert_alpha()
        title = pg.transform.scale(title, (WIDTH, 165))
        background = pg.image.load('game\images\Home_Screen.jpg').convert()
        background_rect = background.get_rect()

        arrow_keys = pg.image.load(path.join(img_dir, 'arrow_keys.png')).convert_alpha()
        arrow_keys = pg.transform.scale(arrow_keys, (150, 85))

        display_screen.blit(background, background_rect)
        display_screen.blit(title, (0,110))
        display_screen.blit(arrow_keys, (720, 570))

        def draw_text(surface, text, size, x, y, color):

            font = pg.font.Font(pg.font.match_font('cambria'), size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surface.blit(text_surface, text_rect)

        draw_text(display_screen, "Are You Ready for the Challenge?", 35, WIDTH/2, HEIGHT/2, WHITE)
        draw_text(display_screen, "If so, press [ENTER] to begin", 35, WIDTH/2, (HEIGHT/2) + 50, WHITE)
        draw_text(display_screen, "If not, press [Q] to quit", 35, WIDTH/2, (HEIGHT/2) + 100, WHITE)
        draw_text(display_screen, "MOVE:", 35, 630, 550, WHITE)

        #code for playing sound from CrouchingPython on YouTube https://www.youtube.com/watch?v=YQ1mixa9RAw
        pg.mixer.music.load('game\sounds\Destiny.mp3')
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)
        pg.display.update()

        while True:
            event = pg.event.poll()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    break
                elif event.key == pg.K_q:
                    pg.quit()
                    self.running = False
            elif event.type == QUIT:
                pg.quit()
                sys.exit() 

    def end_screen(self):
        pass


g = Game()
g.start_screen()
while g.running:
    g.new()
    g.end_screen()

pg.quit()